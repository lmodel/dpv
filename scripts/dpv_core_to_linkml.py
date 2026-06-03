#!/usr/bin/env python3
"""
Transform the DPV (Data Privacy Vocabulary) OWL/Turtle release into a set of
reproducible, 100%-compliant LinkML schema YAML files.

Inputs (default): ``upstream-releases/dpv/dpv/`` (vendored release)
  - ``dpv-owl.ttl``                      - aggregate OWL ontology    (identity)
  - ``dpv.ttl``                          - aggregate canonical/SKOS  (enrichment)
  - ``modules/<module>-owl.ttl``         - per-module OWL ontology   (identity)
  - ``modules/<module>.ttl``             - per-module canonical/SKOS (enrichment)

Outputs (default): ``src/dpv/schema/``
  - ``dpv.yaml``                  - top-level umbrella re-exporting the groups
  - ``dpv_<group>.yaml``          - 8 semantic-group schemas covering the
                                    aggregate ``dpv-owl.ttl`` (1:1 with upstream)
  - ``modules/<module>.yaml``            - one LinkML subset schema per upstream module

Reproducibility:
  - Deterministic: stable sort of subjects, deduplicated lists, no timestamps.
  - Idempotent: re-running with unchanged upstream produces byte-identical YAML.

Usage
-----
    uv run --with rdflib --with pyyaml python scripts/dpv_to_linkml.py \\
        [-i upstream-releases/dpv/dpv] [-o src/dpv/schema] [--version VERSION] [--report]

The DPV version is auto-detected from the upstream ``owl:versionInfo`` triple
in the aggregate ``dpv-owl.ttl`` (falling back to any per-module ontology).
Use ``--version`` only to override the detected value.
"""

from __future__ import annotations

import argparse
import re
import sys
import textwrap
import unicodedata
from pathlib import Path
from typing import Any

import rdflib
import rdflib.collection
import yaml
from rdflib import Graph, Literal, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SKOS, XSD

# ---------------------------------------------------------------------------
# Namespaces
# ---------------------------------------------------------------------------
DPV_OWL_NS = "https://w3id.org/dpv/owl#"           # upstream OWL flavour
DPV_CAN_NS = "https://w3id.org/dpv#"               # canonical SKOS flavour
DPV_LOCAL_NS = "https://w3id.org/lmodel/dpv/"     # this repo namespace
LMODEL_NS = "https://w3id.org/lmodel/dpv/"        # legacy alias for compatibility
LMODEL_BASE = "https://w3id.org/lmodel/dpv"

DPV_OWL = rdflib.Namespace(DPV_OWL_NS)
DPV_CAN = rdflib.Namespace(DPV_CAN_NS)
DCT = rdflib.Namespace("http://purl.org/dc/terms/")

# Ordered prefix table for uri_to_curie(); longest first to avoid ambiguity.
# Order matters: longest IRI prefix first so DPV_OWL_NS (which contains
# DPV_CAN_NS as a substring) wins.
_CURIE_PREFIXES: list[tuple[str, str]] = [
    (DPV_LOCAL_NS, "dpv"),
    (DPV_OWL_NS, "dpv_owl"),
    (DPV_CAN_NS, "dpv_upstream"),
    ("http://www.w3.org/ns/dx/prof/", "prof"),
    ("http://www.w3.org/2004/02/skos/core#", "skos"),
    ("http://purl.org/dc/terms/", "dcterms"),
    ("https://schema.org/", "schema"),
    ("http://schema.org/", "schema"),
    ("http://xmlns.com/foaf/0.1/", "foaf"),
    ("http://www.w3.org/ns/org#", "org"),
    ("http://www.w3.org/ns/dcat#", "dcat"),
    ("http://purl.org/dc/dcam/", "dcam"),
    ("http://purl.org/ontology/bibo/", "bibo"),
    ("http://purl.org/spar/scoro/", "scoro"),
    ("http://purl.org/vocab/vann/", "vann"),
    ("https://specialprivacy.ercim.eu/vocabs/data#", "svd"),
    ("https://specialprivacy.ercim.eu/vocabs/processing#", "svpr"),
    ("https://specialprivacy.ercim.eu/vocabs/purposes#", "svpu"),
    ("https://specialprivacy.ercim.eu/langs/usage-policy#", "usage_policy"),
    ("http://www.w3.org/2003/06/sw-vocab-status/ns#", "sw_vocab_status"),
]

# XSD -> LinkML type mapping (subset; DPV is mostly object-typed).
XSD_TO_LINKML: dict[str, str] = {
    str(XSD.string): "string",
    str(XSD.integer): "integer",
    str(XSD.int): "integer",
    str(XSD.float): "float",
    str(XSD.double): "float",
    str(XSD.decimal): "decimal",
    str(XSD.boolean): "boolean",
    str(XSD.dateTime): "datetime",
    str(XSD.date): "date",
    str(XSD.time): "time",
    str(XSD.anyURI): "uri",
}

# Local names that collide with LinkML metamodel reserved terms or are
# structural artefacts; never emit them as schema elements.
_RESERVED_LOCAL_NAMES = frozenset({"Class", "ObjectProperty", "DatatypeProperty",
                                   "AnnotationProperty", "Thing"})


# ---------------------------------------------------------------------------
# Cross-schema collision avoidance
# ---------------------------------------------------------------------------
# Note: every concrete DPV class inherits from the synthetic ``DpvThing``
# abstract base (see ``_inject_dpv_thing``), but this does NOT prevent
# *name* collisions when this schema is imported alongside another schema
# that declares the same local name. LinkML's element namespace is flat
# per merged schema: ``SchemaView.all_classes()`` keys on the bare local
# name, and on import-merge a duplicate name silently overwrites the
# earlier definition (with a ``from_schema`` rewrite). Inheritance only
# disambiguates structure *after* a name has been resolved; it does
# nothing for name resolution itself. The same applies to top-level
# ``slots`` (``id``, ``name``, ``status`` are looked up by their bare
# local name across the entire merged schema).
#
# Two complementary mitigations are therefore applied:
#
#   1. ``_COLLISION_PRONE_CLASSES`` (below) - local names that collide
#      with classes commonly declared by other LinkML / RDF schemas
#      (schema.org, FOAF, PROV, DCAT, OWL/RDFS primitives, Python
#      builtins shadowed in generated ``dpv.py``). These get a ``Dpv``
#      PascalCase prefix; the original local name is preserved in
#      ``aliases`` and the upstream CURIE in ``exact_mappings`` so
#      semantic identity is unchanged.
#
#      DPV's own *domain* terms (``Consent``, ``Notice``, ``Policy``,
#      ``Purpose``, ``Right``, ``Risk``, ``Rule``, ``Status``,
#      ``Contract``, ``Assessment``, ...) are deliberately NOT in this
#      list: those are the entities downstream users WANT to import
#      under their DPV names, and any third-party schema declaring its
#      own ``Consent`` is the schema that should be prefixing - not DPV.
#
#   2. ``_COLLISION_PRONE_SLOTS`` (further below) - slot names that
#      overlap with commonly used top-level slots (``id``, ``name``,
#      ``description``, ``status``, ``type``, ...). These are demoted
#      from top-level reusable ``slots`` to class-bound ``attributes``
#      via ``_split_collision_slots_to_attributes``. Attributes are
#      class-scoped and therefore cannot clash with an importer's own
#      top-level slot of the same name.
_COLLISION_PRONE_CLASSES: frozenset[str] = frozenset({
    # Generic ontology / RDF / OWL primitives
    "Agent", "Class", "Concept", "Container", "Element", "Entity",
    "Group", "Identifier", "Item", "Object", "Property", "Resource",
    "Statement", "Subject", "Term", "Thing", "Type",
    # Time / geo
    "Address", "Country", "Date", "Duration", "Jurisdiction", "Location",
    "Period", "Place", "Region", "Time",
    # Activity / process
    "Action", "Activity", "Decision", "Event", "Function", "Method",
    "Procedure", "Process", "Project", "Task",
    # Information / data
    "Asset", "Category", "Data", "Dataset", "Document", "Domain",
    "Information", "Knowledge", "Message", "Parameter", "Range",
    "Record", "Signal", "System", "Variable",
    # Org / role
    "Application", "Auditor", "Authority", "Component",
    "Consumer", "Controller", "Customer", "Operator", "Organisation",
    "Organization", "Person", "Processor", "Producer", "Product",
    "Provider", "Recipient", "Role", "Sender", "Service", "User",
    # Python typing / builtins - collide with imports in generated dpv.py
    # (e.g. `Optional` shadows `typing.Optional`, breaking `Optional[Union[...]]`
    # subscripts in generated Slot ranges). DPV currently defines `Optional`
    # under Necessity; the others are listed defensively.
    "Optional", "Union", "List", "Dict", "Tuple", "Set", "FrozenSet",
    "Any", "Callable", "Iterator", "Iterable", "Generator", "Awaitable",
    "ClassVar", "Final", "Literal", "None", "True", "False",
})

# Slot names that overlap with commonly used top-level slots in other LinkML
# schemas (e.g. ``name``, ``id``, ``description``). When a property
# would generate such a slot, it is emitted as a class-bound ``attribute``
# rather than a top-level reusable ``slot`` so that importing this schema
# does not redefine the importer's own top-level slots. Currently DPV
# generates none of these (all its properties are ``has_*`` / ``is_*``),
# but the guard is kept defensively.
_COLLISION_PRONE_SLOTS: frozenset[str] = frozenset({
    "id", "identifier", "name", "label", "title", "description",
    "type", "kind", "category", "status", "value", "code", "key",
    "uri", "url", "source", "target", "start", "end",
    "version", "comment", "comments", "created", "modified",
    "language", "text", "notes", "tags",
    "date", "time", "date_time", "quantity", "unit", "count",
})


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def ascii_safe_local(local: str) -> str:
    """Make a URI fragment safe for use as a CURIE local part or NCName.

    Strips Unicode diacritics via NFKD normalisation (so ``ä`` -> ``a``,
    ``ö`` -> ``o``, ``é`` -> ``e``) and replaces any remaining non-ASCII
    or non-``[A-Za-z0-9_-]`` character with ``_``. Idempotent for fragments
    that are already ASCII NCNames. Required because LinkML / CURIE syntax
    rejects characters outside the ASCII NCName set even though OWL/RDF
    URI fragments permit them (the upstream DPV legal extensions contain
    e.g. ``law-SN-SächsDSG``).
    """
    folded = unicodedata.normalize("NFKD", local)
    folded = "".join(c for c in folded if not unicodedata.combining(c))
    return re.sub(r"[^A-Za-z0-9_-]", "_", folded)


def camel_to_snake(name: str) -> str:
    """Convert camelCase/PascalCase to snake_case (hyphens become underscores)."""
    name = ascii_safe_local(name).replace("-", "_")
    s1 = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    return re.sub(r"([a-z\d])([A-Z])", r"\1_\2", s1).lower()


def sanitise_class_name(local: str) -> str:
    """Make a DPV local name a valid LinkML NCName and avoid collisions.

    Two transforms are applied (in order):

    1. **NCName / PascalCase** - hyphens are removed
       (``Authentication-ABC`` -> ``AuthenticationABC``) because LinkML
       element names must be NCNames and the ``standard_naming`` linter
       prefers PascalCase.
    2. **Collision avoidance** - local names that collide with classes
       commonly defined by other LinkML schemas (see
       ``_COLLISION_PRONE_CLASSES``) are prefixed with ``Dpv``
       (``Person`` -> ``DpvPerson``).

    Upstream identity is preserved in ``exact_mappings`` (as
    ``dpv_upstream:<original-local>`` and ``dpv_owl:<original-local>``) and in
    ``aliases``. ``class_uri`` uses the schema's own ``dpv:`` CURIE.
    The function is idempotent and reference-safe: because every callsite
    that resolves a parent / range / domain URI funnels through this
    helper, ``is_a``, ``mixins``, ``domain``, ``range`` and ``any_of``
    automatically use the renamed form.
    """
    base = ascii_safe_local(local).replace("-", "")
    if base in _COLLISION_PRONE_CLASSES:
        return f"Dpv{base}"
    return base


def dpv_owl_local(uri: URIRef) -> str | None:
    """Return local name if ``uri`` belongs to the dpv-owl: namespace."""
    s = str(uri)
    if not s.startswith(DPV_OWL_NS):
        return None
    local = s[len(DPV_OWL_NS):]
    if not local or "/" in local or local.startswith("serialisation-"):
        return None
    if local in _RESERVED_LOCAL_NAMES:
        return None
    return local


def dpv_can_local(uri: URIRef) -> str | None:
    """Return local name if ``uri`` belongs to the canonical dpv: namespace."""
    s = str(uri)
    if not s.startswith(DPV_CAN_NS):
        return None
    local = s[len(DPV_CAN_NS):]
    if not local or "/" in local or local.startswith("serialisation-"):
        return None
    return local


def uri_to_curie(uri: URIRef) -> str | None:
    s = str(uri)
    for ns, prefix in _CURIE_PREFIXES:
        if s.startswith(ns):
            return f"{prefix}:{ascii_safe_local(s[len(ns):])}"
    return None


def get_literals(g: Graph, subj, pred) -> list[str]:
    return [str(o) for o in g.objects(subj, pred) if isinstance(o, Literal)]


def first_literal(g: Graph, subj, pred) -> str | None:
    vals = get_literals(g, subj, pred)
    return vals[0] if vals else None


def get_ontology_iri(g: Graph) -> str | None:
    for s in g.subjects(RDF.type, OWL.Ontology):
        if isinstance(s, URIRef):
            return str(s)
    return None


def get_ontology_version(g: Graph) -> str | None:
    """Return ``owl:versionInfo`` of the first ``owl:Ontology`` in ``g``."""
    for s in g.subjects(RDF.type, OWL.Ontology):
        v = first_literal(g, s, OWL.versionInfo)
        if v:
            return v
    return None


# ---------------------------------------------------------------------------
# Extraction (OWL graph drives identity; canonical graph enriches metadata)
# ---------------------------------------------------------------------------

def _enrich_from_canonical(
    canonical_subj: URIRef | None,
    g_can: Graph | None,
    entry: dict[str, Any],
) -> None:
    """Merge richer SKOS/DCT metadata from the canonical graph into ``entry``.

    Only fields the OWL graph does not carry are added:
      - ``skos:inScheme``       -> ``annotations.skos_in_scheme`` (sorted list)
      - ``dct:source`` literal  -> ``annotations.dct_source``
      - extra ``skos:altLabel``  -> appended to ``aliases``
      - extra ``skos:scopeNote`` -> appended to ``comments`` if not duplicate
    """
    if g_can is None or canonical_subj is None:
        return

    schemes = sorted({
        dpv_can_local(o) for o in g_can.objects(canonical_subj, SKOS.inScheme)
        if isinstance(o, URIRef) and dpv_can_local(o)
    })
    if schemes:
        # LinkML annotation values must be scalar; join multiple schemes.
        entry.setdefault("annotations", {})["skos_in_scheme"] = ", ".join(schemes)

    src_literals = [str(o) for o in g_can.objects(canonical_subj, DCT.source)
                    if isinstance(o, Literal)]
    if src_literals:
        entry.setdefault("annotations", {})["dct_source"] = src_literals[0]

    extra_alts = [str(o) for o in g_can.objects(canonical_subj, SKOS.altLabel)
                  if isinstance(o, Literal)]
    if extra_alts:
        existing = entry.setdefault("aliases", [])
        for a in extra_alts:
            if a not in existing:
                existing.append(a)

    extra_scope = [str(o) for o in g_can.objects(canonical_subj, SKOS.scopeNote)
                   if isinstance(o, Literal)]
    if extra_scope:
        comments = entry.setdefault("comments", [])
        for c in extra_scope:
            if c not in comments and c != entry.get("description"):
                comments.append(c)


def extract_classes(
    g_owl: Graph,
    g_can: Graph | None = None,
) -> dict[str, dict]:
    """Extract every owl:Class in the ``dpv-owl:`` namespace as a LinkML class.

    The OWL graph drives identity (``class_uri``); the canonical graph (when
    provided) enriches each entry with concept-scheme membership and extra
    SKOS labels.
    """
    classes: dict[str, dict] = {}

    # DPV asserts both owl:Class and rdfs:Class on its classes; union both.
    subjects: set[URIRef] = set()
    for t in (OWL.Class, RDFS.Class):
        for s in g_owl.subjects(RDF.type, t):
            if isinstance(s, URIRef) and dpv_owl_local(s):
                subjects.add(s)

    structural = {OWL.Class, RDFS.Class, OWL.NamedIndividual,
                  OWL.ObjectProperty, OWL.DatatypeProperty,
                  OWL.AnnotationProperty, OWL.Ontology}

    for cls in sorted(subjects, key=str):
        cls_local = dpv_owl_local(cls)
        assert cls_local is not None
        cls_name = sanitise_class_name(cls_local)
        entry: dict[str, Any] = {}

        # ---- description ------------------------------------------------
        defn = first_literal(g_owl, cls, SKOS.definition) \
               or first_literal(g_owl, cls, SKOS.scopeNote)
        if defn:
            entry["description"] = defn

        # ---- is_a / mixins ---------------------------------------------
        named_parents = [
            o for o in g_owl.objects(cls, RDFS.subClassOf)
            if isinstance(o, URIRef) and dpv_owl_local(o)
        ]
        if named_parents:
            entry["is_a"] = sanitise_class_name(dpv_owl_local(named_parents[0]))

        # DPV's class-and-instance pattern: extra rdf:type pointing at another
        # dpv-owl: class records categorical membership -> capture as mixin.
        type_mixins = [
            sanitise_class_name(dpv_owl_local(t))
            for t in g_owl.objects(cls, RDF.type)
            if isinstance(t, URIRef) and dpv_owl_local(t) and t not in structural
        ]
        seen = {entry.get("is_a")}
        dedup_mixins: list[str] = []
        for m in type_mixins:
            if m and m != cls_name and m not in seen:
                dedup_mixins.append(m)
                seen.add(m)
        if len(named_parents) > 1:
            for p in named_parents[1:]:
                m = sanitise_class_name(dpv_owl_local(p))
                if m and m not in seen and m != cls_name:
                    dedup_mixins.append(m)
                    seen.add(m)
        if dedup_mixins:
            entry["mixins"] = dedup_mixins

        # ---- class_uri = our own (resolvable) identity ------------------
        # Upstream CURIEs go into exact_mappings below; emitting them as
        # class_uri would re-publish W3C IRIs under our name.
        entry["class_uri"] = f"dpv:{cls_local}"

        # ---- aliases (prefLabel + altLabel + rdfs:label + original local
        #               name when it was sanitised) --------------------
        aliases: list[str] = []
        if cls_name != cls_local:
            aliases.append(cls_local)  # preserve original hyphenated form
        pref = first_literal(g_owl, cls, SKOS.prefLabel)
        if pref and pref not in aliases:
            aliases.append(pref)
        for label in get_literals(g_owl, cls, SKOS.altLabel):
            if label not in aliases:
                aliases.append(label)
        for label in get_literals(g_owl, cls, RDFS.label):
            if label not in aliases:
                aliases.append(label)
        if aliases:
            entry["aliases"] = aliases

        # ---- comments (extra scopeNote + editorialNote) -----------------
        comments: list[str] = []
        for sn in get_literals(g_owl, cls, SKOS.scopeNote):
            if sn != entry.get("description") and sn not in comments:
                comments.append(sn)
        for note in get_literals(g_owl, cls, SKOS.editorialNote):
            if note not in comments:
                comments.append(note)
        if comments:
            entry["comments"] = comments

        # ---- ontology alignment (mappings) ------------------------------
        equivs: list[str] = []
        for o in g_owl.objects(cls, OWL.equivalentClass):
            if isinstance(o, URIRef):
                curie = uri_to_curie(o)
                equivs.append(curie if curie else str(o))
        for o in g_owl.objects(cls, SKOS.exactMatch):
            if isinstance(o, URIRef):
                curie = uri_to_curie(o)
                if curie and curie not in equivs:
                    equivs.append(curie)
        # The canonical dpv: counterpart is, by construction, an exact equivalent.
        # Both upstream flavours map exactly to this LinkML element.
        equivs.append(f"dpv_upstream:{cls_local}")
        equivs.append(f"dpv_owl:{cls_local}")
        seen_eq: set[str] = set()
        equivs = [e for e in equivs if not (e in seen_eq or seen_eq.add(e))]
        entry["exact_mappings"] = equivs

        for skos_pred, key in (
            (SKOS.closeMatch, "close_mappings"),
            (SKOS.broadMatch, "broad_mappings"),
            (SKOS.narrowMatch, "narrow_mappings"),
            (SKOS.relatedMatch, "related_mappings"),
            (SKOS.related, "related_mappings"),
        ):
            for o in g_owl.objects(cls, skos_pred):
                if isinstance(o, URIRef) and not dpv_owl_local(o):
                    curie = uri_to_curie(o)
                    if curie:
                        entry.setdefault(key, [])
                        if curie not in entry[key]:
                            entry[key].append(curie)

        # ---- deprecation ------------------------------------------------
        if first_literal(g_owl, cls, OWL.deprecated) == "true":
            entry["deprecated"] = "true"

        # ---- canonical enrichment --------------------------------------
        if g_can is not None:
            canonical_subj = URIRef(DPV_CAN_NS + cls_local)
            if (canonical_subj, None, None) in g_can:
                _enrich_from_canonical(canonical_subj, g_can, entry)

        classes[cls_name] = entry

    return classes


def extract_slots(
    g_owl: Graph,
    g_can: Graph | None = None,
) -> dict[str, dict]:
    """Extract every property in the ``dpv-owl:`` namespace as a LinkML slot."""
    slots: dict[str, dict] = {}

    prop_types = (OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)
    subjects: set[URIRef] = set()
    for t in prop_types:
        for s in g_owl.subjects(RDF.type, t):
            if isinstance(s, URIRef) and dpv_owl_local(s):
                subjects.add(s)

    for prop in sorted(subjects, key=str):
        prop_local = dpv_owl_local(prop)
        assert prop_local is not None
        sname = camel_to_snake(prop_local)
        # ``definition_uri`` (not ``slot_uri``) is the right field for the
        # slot's own native identity in this schema. ``slot_uri`` is reserved
        # for binding to a *different* RDF predicate (e.g. ``schema:name``,
        # ``dct:title``); using it for our own ``dpv:`` IRI would shadow that
        # reuse signal. See the linkml-schema skill ("URI wiring: identity vs.
        # mappings").
        entry: dict[str, Any] = {"definition_uri": f"dpv:{prop_local}"}

        defn = first_literal(g_owl, prop, SKOS.definition) \
               or first_literal(g_owl, prop, RDFS.comment)
        if defn:
            entry["description"] = defn

        sub_of = [
            o for o in g_owl.objects(prop, RDFS.subPropertyOf)
            if isinstance(o, URIRef) and dpv_owl_local(o)
        ]
        if sub_of:
            entry["is_a"] = camel_to_snake(dpv_owl_local(sub_of[0]))

        domains = [sanitise_class_name(dpv_owl_local(o))
                   for o in g_owl.objects(prop, RDFS.domain)
                   if isinstance(o, URIRef) and dpv_owl_local(o)]
        if domains:
            entry["domain"] = domains[0]

        all_types = set(g_owl.objects(prop, RDF.type))
        is_datatype = OWL.DatatypeProperty in all_types

        range_uris = [o for o in g_owl.objects(prop, RDFS.range)
                      if isinstance(o, URIRef)]
        if is_datatype:
            if range_uris:
                entry["range"] = XSD_TO_LINKML.get(str(range_uris[0]), "string")
        else:
            dpv_ranges = [sanitise_class_name(dpv_owl_local(o)) for o in range_uris
                          if dpv_owl_local(o)]
            if len(dpv_ranges) == 1:
                entry["range"] = dpv_ranges[0]
            elif len(dpv_ranges) > 1:
                entry["any_of"] = [{"range": r} for r in dpv_ranges]
            if OWL.ObjectProperty in all_types:
                entry["multivalued"] = True

        inverses = [dpv_owl_local(o) for o in g_owl.objects(prop, OWL.inverseOf)
                    if isinstance(o, URIRef) and dpv_owl_local(o)]
        if inverses:
            entry["inverse"] = camel_to_snake(inverses[0])

        aliases: list[str] = []
        pref = first_literal(g_owl, prop, SKOS.prefLabel)
        if pref and pref not in aliases:
            aliases.append(pref)
        for label in get_literals(g_owl, prop, SKOS.altLabel):
            if label not in aliases:
                aliases.append(label)
        for label in get_literals(g_owl, prop, RDFS.label):
            if label not in aliases:
                aliases.append(label)
        if aliases:
            entry["aliases"] = aliases

        equivs: list[str] = []
        for o in g_owl.objects(prop, OWL.equivalentProperty):
            if isinstance(o, URIRef):
                curie = uri_to_curie(o)
                equivs.append(curie if curie else str(o))
        equivs.append(f"dpv_upstream:{prop_local}")
        equivs.append(f"dpv_owl:{prop_local}")
        seen_eq: set[str] = set()
        equivs = [e for e in equivs if not (e in seen_eq or seen_eq.add(e))]
        entry["exact_mappings"] = equivs

        if OWL.TransitiveProperty in all_types:
            entry["transitive"] = True
        if OWL.SymmetricProperty in all_types:
            entry["symmetric"] = True
        if OWL.ReflexiveProperty in all_types:
            entry["reflexive"] = True

        if first_literal(g_owl, prop, OWL.deprecated) == "true":
            entry["deprecated"] = "true"

        if g_can is not None:
            canonical_subj = URIRef(DPV_CAN_NS + prop_local)
            if (canonical_subj, None, None) in g_can:
                _enrich_from_canonical(canonical_subj, g_can, entry)

        slots[sname] = entry

    return slots


def _split_collision_slots_to_attributes(
    classes: dict[str, dict],
    slots: dict[str, dict],
) -> tuple[dict[str, dict], int]:
    """Move slots whose name collides with common LinkML top-level slots
    into class-bound ``attributes`` of their declared ``domain`` class.

    Attributes are class-scoped, so they cannot clash with an importer's
    own top-level slots - this is the standard LinkML idiom for highly
    common names like ``name``, ``id``, ``status``. Slots without a
    resolvable ``domain`` (or whose domain class lives in another module
    not present in ``classes``) are left at the top level unchanged.

    Returns the filtered slot dict and the count of slots moved.
    """
    if not slots:
        return slots, 0
    remaining: dict[str, dict] = {}
    moved = 0
    for sname, sentry in slots.items():
        if sname in _COLLISION_PRONE_SLOTS:
            domain = sentry.get("domain")
            if domain and domain in classes:
                attr = {k: v for k, v in sentry.items() if k != "domain"}
                classes[domain].setdefault("attributes", {})[sname] = attr
                moved += 1
                continue
        remaining[sname] = sentry
    return remaining, moved


# ---------------------------------------------------------------------------
# YAML output
# ---------------------------------------------------------------------------

_SCHEMA_KEY_ORDER = [
    "id", "name", "title", "description", "license", "see_also",
    "source", "version", "annotations",
    "prefixes", "default_prefix", "default_range", "id_prefixes", "imports",
    "subsets", "types", "enums", "slots", "classes",
]

_ELEMENT_KEY_ORDER = [
    "is_a", "mixins", "abstract", "mixin", "tree_root",
    "class_uri", "slot_uri", "definition_uri",
    "description", "title", "aliases", "comments", "examples", "notes",
    "domain", "range", "multivalued", "required", "recommended", "identifier", "any_of",
    "inverse", "transitive", "symmetric", "antisymmetric", "reflexive", "disjoint_with",
    "deprecated", "deprecated_element_has_exact_replacement",
    "in_subset",
    "exact_mappings", "close_mappings", "narrow_mappings",
    "broad_mappings", "related_mappings", "see_also",
    "slots", "slot_usage", "attributes", "id_prefixes", "union_of", "unique_keys",
    "rules", "defining_slots",
    "ifabsent", "inlined", "inlined_as_list", "unit",
    "minimum_value", "maximum_value", "pattern", "string_serialization",
    "annotations",
]

_SECTION_KEYS = frozenset(["prefixes", "default_prefix", "imports",
                           "subsets", "types", "enums", "slots", "classes"])
_ELEMENT_SECTION_KEYS = frozenset(["classes", "slots", "enums", "subsets"])


def _order_keys(d: dict, key_order: list[str]) -> dict:
    result = {k: d[k] for k in key_order if k in d}
    result.update({k: v for k, v in d.items() if k not in result})
    return result


def _order_elements(
    elements: dict,
    subset_name: str | None = None,
    membership: dict[str, set[str]] | None = None,
) -> dict:
    """Order elements deterministically and assign ``in_subset``.

    If ``membership`` is provided, each element's ``in_subset`` is the
    sorted list of module subset names from ``membership[name]`` plus
    ``subset_name`` (if given). Otherwise ``in_subset`` defaults to
    ``[subset_name]``.
    """
    result = {}
    for name in sorted(elements):
        entry = dict(elements[name])
        subsets: list[str] = []
        if membership and name in membership:
            subsets.extend(sorted(membership[name]))
        if subset_name and subset_name not in subsets:
            subsets.append(subset_name)
        if subsets:
            entry.setdefault("in_subset", subsets)
        # Sort and key-order nested ``attributes`` so output is deterministic.
        attrs = entry.get("attributes")
        if isinstance(attrs, dict) and attrs:
            entry["attributes"] = {
                aname: _order_keys(dict(attrs[aname]), _ELEMENT_KEY_ORDER)
                for aname in sorted(attrs)
            }
        result[name] = _order_keys(entry, _ELEMENT_KEY_ORDER)
    return result


# Maximum allowed YAML line length (yamllint default rule line-length: 80,
# but we leave headroom and use 88 so 2-space indented strings still fit on
# a typical 88-char editor ruler). Strings longer than this are emitted as
# multi-line literal blocks (``|-``-folded by PyYAML's literal style).
_YAML_LINE_LIMIT = 88
# Trigger threshold on raw string length for switching to a block scalar.
# This is intentionally smaller than ``_YAML_LINE_LIMIT`` because the
# emitted physical line also contains the parent indent (up to ~10
# spaces in our schemas) plus the mapping key (e.g. ``description: ``,
# ``meaning: ``), which add ~15-20 characters of overhead. A 70-char
# raw string at indent 6 already produces an 88-char physical line.
_LONG_STRING_THRESHOLD = 70
# Width used by ``textwrap.fill`` for pre-wrapping long single-line strings.
# Conservatively narrower than ``_YAML_LINE_LIMIT`` to leave room for the
# YAML indent of deeply nested values (up to ~12 spaces in our schemas).
_TEXT_WRAP_WIDTH = 72


def _literal_representer(dumper, data):
    """String representer that picks a block scalar style for long strings.

    Rules:
      - Strings already containing ``\n`` -> literal ``|`` block
        (preserve newlines verbatim).
      - Strings whose physical YAML line would exceed
        ``_YAML_LINE_LIMIT`` -> pre-wrapped with ``textwrap.fill`` at
        ``_TEXT_WRAP_WIDTH`` and emitted as a literal ``|`` block so
        each line stays inside the yamllint ``line-length`` rule.
        We avoid PyYAML's folded ``>`` style because it can emit
        un-indented continuations when no wrap point fits the requested
        width, producing invalid YAML.
      - All other strings -> default plain / single-quoted scalar.
    """
    if "\n" in data:
        return dumper.represent_scalar(
            "tag:yaml.org,2002:str", data, style="|",
        )
    if len(data) > _LONG_STRING_THRESHOLD:
        wrapped = textwrap.fill(
            data,
            width=_TEXT_WRAP_WIDTH,
            break_long_words=False,
            break_on_hyphens=False,
        )
        return dumper.represent_scalar(
            "tag:yaml.org,2002:str", wrapped, style="|",
        )
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


def _setup_yaml():
    """Build a Dumper that produces yamllint-friendly indented sequences.

    PyYAML's default ``Dumper`` writes block sequences without indenting the
    ``-`` hyphen relative to its mapping key, which yamllint's
    ``indentation`` rule flags as ``wrong indentation: expected at least``.
    Overriding ``increase_indent(... indentless=False)`` forces hyphens to
    be indented by ``indent`` spaces under their parent key.
    """
    class _Dumper(yaml.Dumper):
        def increase_indent(self, flow=False, indentless=False):
            return super().increase_indent(flow, False)

    _Dumper.add_representer(str, _literal_representer)
    return _Dumper


def _add_blank_lines(text: str) -> str:
    lines = text.split("\n")
    output: list[str] = []
    in_elements = False
    for line in lines:
        if not line.strip():
            output.append(line)
            continue
        indent = len(line) - len(line.lstrip())
        if indent == 0 and ":" in line:
            key = line.split(":")[0].strip()
            if key in _SECTION_KEYS and output and output[-1] != "":
                output.append("")
            in_elements = key in _ELEMENT_SECTION_KEYS
        elif indent == 2 and in_elements and not line.lstrip().startswith("-"):
            if output and output[-1] != "":
                output.append("")
        output.append(line)
    result: list[str] = []
    prev_blank = False
    for line in output:
        is_blank = not line.strip()
        if is_blank and prev_blank:
            continue
        result.append(line)
        prev_blank = is_blank
    return "\n".join(result)


def dump_yaml(schema: dict) -> str:
    raw = yaml.dump(
        schema,
        Dumper=_setup_yaml(),
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        indent=2,
        width=_YAML_LINE_LIMIT,
    )
    return _add_blank_lines(raw)


# ---------------------------------------------------------------------------
# Schema assembly
# ---------------------------------------------------------------------------

def _base_prefixes() -> dict[str, str]:
    return {
        # The schema's own namespace (repo-local prefix).
        "dpv": DPV_LOCAL_NS,
        # Upstream DPV namespaces - mapping targets only, never identity.
        "dpv_upstream": DPV_CAN_NS,
        "dpv_owl": DPV_OWL_NS,
        # LinkML + core semantic-web prefixes.
        "linkml": "https://w3id.org/linkml/",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "owl": "http://www.w3.org/2002/07/owl#",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        # FAIR / standards backbone (canonical NCName aliases for lint cleanliness).
        "dcterms": "http://purl.org/dc/terms/",
        "dcat": "http://www.w3.org/ns/dcat#",
        "schema": "http://schema.org/",
        "foaf": "http://xmlns.com/foaf/0.1/",
        "org": "http://www.w3.org/ns/org#",
        "prof": "http://www.w3.org/ns/dx/prof/",
        # SPECIAL/ERCIM cross-references used in DPV mappings.
        "svd": "https://specialprivacy.ercim.eu/vocabs/data#",
        "svpr": "https://specialprivacy.ercim.eu/vocabs/processing#",
        "svpu": "https://specialprivacy.ercim.eu/vocabs/purposes#",
        "usage_policy": "https://specialprivacy.ercim.eu/langs/usage-policy#",
        # Shape Expressions namespace. Used by `linkml:types` itself
        # (e.g. `shex:iri`, `shex:nonLiteral`) but `SchemaLoader.merge`
        # does NOT propagate prefixes from imported schemas into the
        # merged top-level, so we declare it explicitly here. Without
        # this, downstream generators warn "Unrecognized prefix: shex".
        "shex": "http://www.w3.org/ns/shex#",
        # SSSOM mapping-overlay target namespaces. These are referenced
        # from `exact_mappings` / `close_mappings` etc. added by
        # `scripts/apply_sssom_overlay.py`. We pre-declare them in the
        # base prefix block because the SSSOM overlay only adds them to
        # the schema whose elements carry the mappings (the relevant
        # semantic-group schema), and `SchemaLoader.merge` does not carry
        # imported-schema prefixes into the merged top-level schema. So
        # without these, `gen-project` warns "Unrecognized prefix: iso..."
        # for every overlay prefix when consuming the merged YAML.
        "common_domain_model": "https://w3id.org/lmodel/common-domain-model/",
        "gists": "https://w3id.org/lmodel/gists/",
        "iso22989": "https://w3id.org/lmodel/iso22989/",
        "iso27001": "https://w3id.org/lmodel/iso27001/",
        "iso29100": "https://w3id.org/lmodel/iso29100/",
        "iso42001": "https://w3id.org/lmodel/iso42001/",
        "nist_ai_rmf": "https://w3id.org/lmodel/nist-ai-rmf/",
        "nist_csf_v2": "https://w3id.org/lmodel/nist-csf-v2/",
        "ocsf": "https://w3id.org/lmodel/ocsf/",
        "oscal": "https://w3id.org/lmodel/oscal/",
    }


def _module_subset_name(module: str) -> str:
    """Subset names use the ``_subset`` suffix so they cannot collide with the
    schema ``name`` (e.g. ``dpv_consent``), with class names (PascalCase), or
    with slot names (snake_case)."""
    return f"{module}_subset"


# Name of the synthetic abstract base class injected into the core schema so
# that every DPV class has a uniform identifier. DPV's upstream OWL declares
# zero ``rdfs:domain`` triples by design (open-world: any property can apply
# to any class), so ``DpvThing`` deliberately does NOT enumerate any slots -
# it only carries the ``id`` identifier. Listing every DPV slot on the base
# class would inflate ``class_induced_slots`` from O(1) to O(N) (973 classes
# × 145 slots = ~141k induced slot/class pairs), stalling every downstream
# generator that walks induced slots (gen-shacl, gen-sqlddl, gen-doc per-
# class pages, gen-pydantic) without adding semantic value: DPV does not
# constrain which properties apply to which classes.
_DPV_THING = "DpvThing"
_ID_SLOT = "id"


def _inject_dpv_thing(
    classes: dict[str, dict],
    slots: dict[str, dict],
) -> None:
    """Inject an abstract ``DpvThing`` base class with a single ``id`` slot.

    Every root class (no ``is_a``) is wired to ``is_a: DpvThing`` so every
    DPV entity has a uniform identifier. ``DpvThing`` intentionally does NOT
    list the full DPV slot inventory - DPV's upstream OWL has no
    ``rdfs:domain`` triples (open-world; any property can attach to any
    class), and inheriting all ~145 slots on every concrete class would blow
    up ``class_induced_slots`` and stall every downstream generator that
    walks it. Mutates ``classes`` and ``slots`` in place. Idempotent.

    Note: generators producing closed-world artifacts (e.g.
    ``gen-json-schema`` with ``additionalProperties: false``) will reject
    instance data carrying DPV properties unless the property is added to
    the specific class. That is the correct trade-off: closed-world
    validation is the wrong tool for DPV data - use SHACL or validate
    against the canonical W3C DPV OWL instead.
    """
    if _ID_SLOT not in slots:
        slots[_ID_SLOT] = {
            "description": (
                "Stable identifier for the instance. Typically a CURIE or IRI "
                "naming the RDF subject this LinkML instance corresponds to."
            ),
            "identifier": True,
            "range": "uriorcurie",
        }

    classes[_DPV_THING] = {
        "description": (
            "Abstract base class for every DPV entity. Provides a uniform "
            "``id`` identifier slot. Does NOT enumerate DPV properties: the "
            "upstream OWL declares no ``rdfs:domain`` triples, so any DPV "
            "property is semantically applicable to any DPV class "
            "(open-world). Generators that need a closed-world property "
            "list per class should consume the W3C DPV OWL release directly "
            "rather than this LinkML projection."
        ),
        "abstract": True,
        "slots": [_ID_SLOT],
    }

    _wire_dpv_thing_parent(classes)


def _wire_dpv_thing_parent(classes: dict[str, dict]) -> None:
    """Wire every root class (no ``is_a``) to ``is_a: DpvThing``.

    This is the sibling of :func:`_inject_dpv_thing` for the non-``common``
    semantic groups: ``DpvThing`` and its ``id`` slot are declared once in the
    ``common`` group, and every other group imports ``dpv_common`` (see each
    group's ``dependencies``), so the ``is_a`` reference resolves without
    re-declaring ``DpvThing`` (which would collide on ``from_schema`` when the
    umbrella merges all groups). Wiring all root classes — not just those in
    ``common`` — is what gives every concrete DPV class the required ``id``
    constraint after merge. Mutates ``classes`` in place. Idempotent.
    """
    for cls_name, entry in classes.items():
        if cls_name == _DPV_THING:
            continue
        if "is_a" not in entry:
            # Insert is_a as the first key so it renders at the top per
            # _ELEMENT_KEY_ORDER without disturbing the rest of the dict.
            new_entry = {"is_a": _DPV_THING}
            new_entry.update(entry)
            classes[cls_name] = new_entry


def build_module_schema(
    module_name: str,
    classes: dict,
    slots: dict,
    version: str,
    source: str | None,
    upstream_file: str,
) -> dict:
    subset_name = _module_subset_name(module_name)
    schema: dict[str, Any] = {
        "id": f"{LMODEL_BASE}/{module_name}",
        "name": f"dpv_{module_name}",
        "title": f"DPV - {module_name.replace('_', ' ').title()}",
        "description": (
            f"LinkML schema generated from the DPV {version} module "
            f"`{upstream_file}` (Data Privacy Vocabulary)."
        ),
        "license": "CC-BY-4.0",
        "see_also": [
            "https://w3id.org/dpv",
            "https://w3c.github.io/dpv/",
        ],
        "version": version,
    }
    if source:
        schema["source"] = source

    schema.update({
        "prefixes": _base_prefixes(),
        "default_prefix": "dpv",
        "default_range": "string",
        # Import the umbrella for the abstract parents (``DpvThing`` and any
        # cross-module ``is_a`` targets). The old aggregate ``dpv_core`` schema
        # was replaced by the 8 semantic groups; ``dpv:schema/dpv`` re-exports
        # all of them, so it is the 1:1 successor for resolution purposes.
        "imports": ["linkml:types", "dpv:schema/dpv"],
        "subsets": {
            subset_name: {
                "description": f"Entities from the DPV `{module_name}` module.",
            }
        },
    })
    if slots:
        schema["slots"] = _order_elements(slots, subset_name)
    if classes:
        schema["classes"] = _order_elements(classes, subset_name)
    return _order_keys(schema, _SCHEMA_KEY_ORDER)


def build_semantic_group_schema(
    group_name: str,
    classes: dict,
    slots: dict,
    version: str,
    source: str | None,
    group_info: dict,
    class_membership: dict[str, set[str]] | None = None,
    slot_membership: dict[str, set[str]] | None = None,
) -> dict:
    """Build a semantic group schema (e.g., dpv_legal_basis, dpv_entities).
    
    Each semantic group imports only its direct dependencies, not all 965 classes.
    """
    subset_name = _module_subset_name(group_name)
    
    # Build import list: linkml:types + dependencies
    imports: list[str] = ["linkml:types"]
    for dep in group_info.get("dependencies", []):
        imports.append(f"dpv:schema/dpv_{dep}")
    
    schema: dict[str, Any] = {
        "id": f"{LMODEL_BASE}/dpv_{group_name}",
        "name": f"dpv_{group_name}",
        "title": f"DPV - {group_name.replace('_', ' ').title()}",
        "description": (
            f"LinkML schema for DPV {version} semantic group: "
            f"{group_info.get('description', group_name)}. "
            f"This schema imports only its direct upstream module dependencies "
            f"({', '.join(group_info.get('modules', []))}) rather than all 965 DPV classes."
        ),
        "license": "CC-BY-4.0",
        "see_also": [
            "https://w3id.org/dpv",
            "https://w3c.github.io/dpv/",
        ],
        "version": version,
    }
    if source:
        schema["source"] = source

    subsets: dict[str, dict] = {
        subset_name: {
            "description": f"Entities from the DPV `{group_name}` semantic group.",
        }
    }

    schema.update({
        "prefixes": _base_prefixes(),
        "default_prefix": "dpv",
        "default_range": "string",
        "imports": imports,
        "subsets": subsets,
    })
    
    # NOTE: ``membership`` is intentionally NOT passed. The membership dicts
    # (``class_to_groups`` / ``slot_to_groups``) contain raw group names like
    # ``common``, but only ``common_subset`` (the proper subset name) is
    # declared in the ``subsets`` block. Passing membership would emit
    # ``in_subset: [common, common_subset]`` and LinkML's schema loader
    # would reject the undefined ``common`` subset.
    if slots:
        schema["slots"] = _order_elements(slots, subset_name)
    if classes:
        schema["classes"] = _order_elements(classes, subset_name)
    
    return _order_keys(schema, _SCHEMA_KEY_ORDER)


def build_top_schema_semantic(
    module_names: list[str], version: str,
    emitted_groups: list[str] | None = None,
) -> dict:
    """Build top-level dpv.yaml that imports semantic group schemas.

    Only groups for which a file was actually written are imported, so a
    group that ended up empty does not become a dangling import.
    """
    canonical_order = [
        "common",  # must come first (provides DpvThing)
        "legal_basis", "entities", "personal_data", "processing",
        "risk_notice", "rights", "consent",
    ]
    if emitted_groups is None:
        emitted = canonical_order
    else:
        emitted_set = set(emitted_groups)
        emitted = [g for g in canonical_order if g in emitted_set]
        for g in emitted_groups:
            if g not in emitted:
                emitted.append(g)
    semantic_imports = [f"dpv:schema/dpv_{g}" for g in emitted]
    
    schema: dict[str, Any] = {
        "id": LMODEL_BASE,
        "name": "dpv",
        "title": "Data Privacy Vocabulary (DPV)",
        "description": (
            "Top-level umbrella LinkML schema for the W3C Data Privacy "
            f"Vocabulary (DPV) version {version}. Re-exports the eight "
            f"semantic-group schemas ({', '.join(emitted)}), which together "
            "provide 1:1 coverage of every class and slot in the upstream "
            "DPV 2.3 OWL release.\n\n"
            "Each DPV semantic groups (i.e. `dpv_consent`) imports only its "
            "direct upstream module dependencies (i.e. `dpv_common`), avoiding "
            "the load cost of a single monolithic schema.\n\n"
            "DPV modules (under `./modules/`) remain usable as standalone scheama,"
            "and are intentionally NOT imported here to avoid duplicate class "
            "declarations during generation (each shared class would otherwise "
            "arrive with two conflicting `from_Schema` URIs).\n\n"
            "DPV extensions (under `./extensions/`, e.g. `ai`, `risk`, `pd`"
            "`tech`, `legal/*`, `sector/*`) also remain usable as standalone "
            "schema, and are intentially NOT imported. This design aims to "
            "help consumers import only what they needed, not everything."
        ),
        "license": "CC-BY-4.0",
        "see_also": [
            "https://w3id.org/dpv",
            "https://w3c.github.io/dpv/",
        ],
        "version": version,
        "prefixes": _base_prefixes(),
        "default_prefix": "dpv",
        "default_range": "string",
        "imports": ["linkml:types"] + semantic_imports,
    }
    
    # Document the semantic groups as annotations for discoverability
    schema["annotations"] = {
        "semantic_groups": ", ".join(emitted),
        "design_note": (
            "Decomposed into 8 semantic groups rather than a single "
            "monolithic schema. Each group imports only its direct upstream "
            "module dependencies, reducing downstream transitive import "
            "overhead."
        ),
    }
    
    return _order_keys(schema, _SCHEMA_KEY_ORDER)


# ---------------------------------------------------------------------------
# Generation
# ---------------------------------------------------------------------------

def _normalise_module_stem(path: Path) -> str:
    stem = path.stem
    if stem.endswith("-owl"):
        stem = stem[: -len("-owl")]
    return stem.lower()


def _parse_ttl(path: Path) -> Graph:
    g = Graph()
    g.parse(str(path), format="turtle")
    return g


def _write(schema: dict, path: Path) -> tuple[int, int]:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump_yaml(schema), encoding="utf-8")
    n_cls = len(schema.get("classes", {}))
    n_slt = len(schema.get("slots", {}))
    print(f"   -> {path}  (classes={n_cls}, slots={n_slt})", file=sys.stderr)
    return n_cls, n_slt


def _coverage(label: str, g_owl: Graph, classes: dict, slots: dict) -> str:
    n_owl_classes = sum(
        1 for s in g_owl.subjects(RDF.type, OWL.Class)
        if isinstance(s, URIRef) and dpv_owl_local(s)
    )
    n_obj = sum(1 for s in g_owl.subjects(RDF.type, OWL.ObjectProperty)
                if isinstance(s, URIRef) and dpv_owl_local(s))
    n_data = sum(1 for s in g_owl.subjects(RDF.type, OWL.DatatypeProperty)
                 if isinstance(s, URIRef) and dpv_owl_local(s))
    return (
        f"{label}: owl:Class={n_owl_classes} -> classes={len(classes)} | "
        f"obj_props={n_obj} data_props={n_data} -> slots={len(slots)}"
    )


# ---------------------------------------------------------------------------
# Semantic grouping (Option B: smart generation of 8 semantic groups)
# ---------------------------------------------------------------------------

# Mapping of semantic group name to upstream module stems that comprise it.
# Classes/slots are assigned to groups based on which modules contain them.
# Each group imports only its direct dependencies, not all 965 classes.
# Each upstream module must appear in exactly ONE group to guarantee a
# class/slot lands in exactly one group file (no duplicate class declarations
# when the umbrella ``dpv.yaml`` imports all groups).
SEMANTIC_GROUPS: dict[str, dict] = {
    "common": {
        "modules": ["status", "TOM", "rules", "context"],
        "dependencies": [],
        "description": "Shared metadata and administrative concepts (base layer)",
    },
    "legal_basis": {
        "modules": [
            "legal_basis", "legal_basis_status", "jurisdiction",
            "legal_measures",
            "contract", "contract_clause", "contract_control",
            "contract_status", "contract_types",
        ],
        "dependencies": ["common"],
        "description": "Legal basis, contracts, and lawfulness concepts",
    },
    "entities": {
        "modules": [
            "entities", "entities_authority", "entities_datasubject",
            "entities_legalrole", "entities_organisation",
        ],
        "dependencies": ["common"],
        "description": "Organisational and legal entities",
    },
    "personal_data": {
        "modules": [
            "personal_data", "physical_measures",
            "organisational_measures", "technical_measures",
        ],
        "dependencies": ["common"],
        "description": "Data classification, sensitivity, and mitigation measures",
    },
    "processing": {
        "modules": [
            "processing", "process", "processing_context",
            "processing_scale", "purposes",
        ],
        "dependencies": ["common", "personal_data"],
        "description": "Processing activities, purposes, and context",
    },
    "risk_notice": {
        "modules": ["risk", "notice"],
        "dependencies": ["common"],
        "description": "Risk, notice, and complaint concepts",
    },
    "rights": {
        "modules": ["rights"],
        "dependencies": ["common"],
        "description": "Rights, remedies, and requests",
    },
    "consent": {
        "modules": [
            "consent", "consent_controls", "consent_status", "consent_types",
        ],
        "dependencies": ["common"],
        "description": "Consent lifecycle and management",
    },
}

# Build reverse lookup and fail-fast if any module appears in >1 group.
# Keys are lowercased to match the normalised ``mod_name`` produced by
# ``_normalise_module_stem``.
_MODULE_TO_GROUP: dict[str, str] = {}
for _g, _info in SEMANTIC_GROUPS.items():
    for _m in _info["modules"]:
        _m_key = _m.lower()
        if _m_key in _MODULE_TO_GROUP:
            raise RuntimeError(
                f"Module '{_m}' appears in both "
                f"'{_MODULE_TO_GROUP[_m_key]}' and '{_g}' semantic groups; "
                f"groups must be mutually exclusive."
            )
        _MODULE_TO_GROUP[_m_key] = _g


def detect_version(input_dir: Path) -> str | None:
    """Detect DPV version from upstream ``owl:versionInfo``.

    Tries the aggregate ``dpv-owl.ttl`` first, then any per-module
    ``modules/*-owl.ttl`` until a value is found.
    """
    aggregate = input_dir / "dpv-owl.ttl"
    if aggregate.exists():
        v = get_ontology_version(_parse_ttl(aggregate))
        if v:
            return v
    for ttl in sorted(input_dir.glob("modules/*-owl.ttl")):
        v = get_ontology_version(_parse_ttl(ttl))
        if v:
            return v
    return None


def generate(
    input_dir: Path,
    output_dir: Path,
    version: str,
    report: bool,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    # ---- per-module schemas (with canonical enrichment) ----
    module_files = sorted(input_dir.glob("modules/*-owl.ttl"))
    if not module_files:
        sys.exit(f"No '*-owl.ttl' files found under {input_dir / 'modules'}")

    module_names: list[str] = []
    total_cls = total_slt = 0
    # class_name / slot_name -> set of module names containing it.
    # Populated during the per-module pass and surfaced as ``in_subset``
    # on semantic group schemas.
    class_to_modules: dict[str, set[str]] = {}
    slot_to_modules: dict[str, set[str]] = {}
    # class_name / slot_name -> set of semantic group names containing it.
    class_to_groups: dict[str, set[str]] = {}
    slot_to_groups: dict[str, set[str]] = {}

    for ttl_owl in module_files:
        mod_name = _normalise_module_stem(ttl_owl)
        print(f"\nParsing module {ttl_owl.name} ...", file=sys.stderr)
        g_owl = _parse_ttl(ttl_owl)

        ttl_can = ttl_owl.with_name(f"{mod_name}.ttl")
        g_can = _parse_ttl(ttl_can) if ttl_can.exists() else None
        if g_can is not None:
            print(f"   enriched from canonical {ttl_can.name}", file=sys.stderr)

        classes = extract_classes(g_owl, g_can)
        slots = extract_slots(g_owl, g_can)
        slots, moved = _split_collision_slots_to_attributes(classes, slots)
        if moved and report:
            print(f"   collision-prone slots moved to attributes: {moved}",
                  file=sys.stderr)

        if not classes and not slots:
            print("   (skipped - no DPV entities)", file=sys.stderr)
            continue

        mod_subset = _module_subset_name(mod_name)
        for cls_name in classes:
            class_to_modules.setdefault(cls_name, set()).add(mod_subset)
        for slot_name in slots:
            slot_to_modules.setdefault(slot_name, set()).add(mod_subset)
        
        # Classify classes/slots to their semantic group via _MODULE_TO_GROUP.
        # First-seen wins: a class declared in multiple upstream modules (e.g.,
        # ConsentNotice in both `notice` and `consent`) is assigned to the
        # FIRST module's group only, so it appears in exactly one group file.
        # This is essential — otherwise the umbrella ``dpv.yaml`` would import
        # the same class twice with conflicting ``from_schema`` URIs and
        # ``merge_linkml_schema.py`` would refuse to merge.
        group_name = _MODULE_TO_GROUP.get(mod_name)
        if group_name is None:
            print(f"   WARNING: module '{mod_name}' is not assigned to any "
                  f"semantic group; its classes/slots will be missing from "
                  f"the umbrella dpv.yaml. Add it to SEMANTIC_GROUPS.",
                  file=sys.stderr)
        else:
            for cls_name in classes:
                if cls_name not in class_to_groups:
                    class_to_groups[cls_name] = {group_name}
            for slot_name in slots:
                if slot_name not in slot_to_groups:
                    slot_to_groups[slot_name] = {group_name}

        schema = build_module_schema(
            mod_name, classes, slots, version,
            source=get_ontology_iri(g_owl),
            upstream_file=f"modules/{ttl_owl.name}",
        )
        n_cls, n_slt = _write(schema, output_dir / "modules" / f"{mod_name}.yaml")
        total_cls += n_cls
        total_slt += n_slt
        module_names.append(mod_name)

        if report:
            print(f"   {_coverage(mod_name, g_owl, classes, slots)}",
                  file=sys.stderr)

    # ---- semantic group schemas (NEW: replaces monolithic dpv_core) ----
    # Build in dependency order: common first, then others that depend on it.
    print("\n\nBuilding semantic group schemas...", file=sys.stderr)
    core_owl = input_dir / "dpv-owl.ttl"
    emitted_groups: list[str] = []
    if core_owl.exists():
        print(f"Parsing aggregate {core_owl.name} for semantic grouping...", 
              file=sys.stderr)
        g_owl_core = _parse_ttl(core_owl)
        core_can = input_dir / "dpv.ttl"
        g_can_core = _parse_ttl(core_can) if core_can.exists() else None

        all_core_classes = extract_classes(g_owl_core, g_can_core)
        all_core_slots = extract_slots(g_owl_core, g_can_core)

        # Process groups in dependency order (common first).
        group_order = ["common"] + [k for k in SEMANTIC_GROUPS
                                     if k != "common"]

        for group_name in group_order:
            group_info = SEMANTIC_GROUPS[group_name]
            print(f"\n  Generating semantic group: {group_name}", file=sys.stderr)
            
            # Filter classes/slots to this group only
            group_classes = {
                k: v for k, v in all_core_classes.items()
                if group_name in class_to_groups.get(k, set())
            }
            group_slots = {
                k: v for k, v in all_core_slots.items()
                if group_name in slot_to_groups.get(k, set())
            }
            
            if not group_classes and not group_slots:
                print(f"    (skipped - no classes/slots in group)", file=sys.stderr)
                continue
            
            # The ``common`` group declares ``DpvThing`` (+ its ``id`` slot) and
            # wires its own root classes to it. Every other group only wires its
            # root classes to ``is_a: DpvThing`` (resolved via the imported
            # ``dpv_common``), so all concrete classes inherit the required
            # ``id`` after the umbrella merges the groups.
            if group_name == "common":
                _inject_dpv_thing(group_classes, group_slots)
            else:
                _wire_dpv_thing_parent(group_classes)

            group_slots, moved = _split_collision_slots_to_attributes(
                group_classes, group_slots,
            )
            
            schema = build_semantic_group_schema(
                group_name,
                group_classes,
                group_slots,
                version,
                source=get_ontology_iri(g_owl_core),
                group_info=group_info,
                class_membership=class_to_groups,
                slot_membership=slot_to_groups,
            )
            # File is named ``dpv_<group>.yaml`` to match the schema ``name``
            # and the import URI ``dpv:schema/dpv_<group>`` used by the
            # umbrella ``dpv.yaml`` (LinkML resolves imports by filename).
            n_cls, n_slt = _write(schema, output_dir / f"dpv_{group_name}.yaml")
            emitted_groups.append(group_name)
            print(f"    dpv_{group_name}: {n_cls} classes, {n_slt} slots",
                  file=sys.stderr)

        if report:
            print(f"\n   {_coverage('ALL GROUPS', g_owl_core, all_core_classes, all_core_slots)}",
                  file=sys.stderr)

    # ---- top-level dpv.yaml (imports only emitted semantic groups) ----
    print("\nWriting top-level dpv.yaml ...", file=sys.stderr)
    _write(
        build_top_schema_semantic(module_names, version, emitted_groups),
        output_dir / "dpv.yaml",
    )

    # Compute total classes across all semantic groups
    total_semantic_classes = sum(len([c for c in class_to_groups.keys() 
                                       if g in class_to_groups[c]]) 
                                 for g in SEMANTIC_GROUPS)
    
    print(
        f"\nDone. Modules: {len(module_names)}, semantic groups: {len(SEMANTIC_GROUPS)}, "
        f"total classes: {total_semantic_classes}, total slots: {total_slt}.",
        file=sys.stderr,
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    linkml_root = Path(__file__).resolve().parent.parent
    default_input = linkml_root / "upstream-releases" / "dpv" / "dpv"
    default_output = linkml_root / "src" / "dpv" / "schema"

    parser = argparse.ArgumentParser(
        description="Generate LinkML schemas from the DPV OWL release.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--version", default=None,
        help="Override the DPV version string embedded in the schemas. "
             "By default the version is auto-detected from the upstream "
             "owl:versionInfo triple in dpv-owl.ttl.",
    )
    parser.add_argument(
        "-i", "--input-dir", type=Path, default=default_input,
        help="Directory containing dpv-owl.ttl, dpv.ttl and modules/ "
             "(default: upstream-releases/dpv/dpv relative to the linkml directory)",
    )
    parser.add_argument(
        "-o", "--output-dir", type=Path, default=default_output,
        help=f"Output directory for generated schemas (default: {default_output})",
    )
    parser.add_argument(
        "--report", action="store_true",
        help="Print a coverage summary to stderr.",
    )
    args = parser.parse_args()

    if not args.input_dir.exists():
        parser.error(f"Input directory does not exist: {args.input_dir}")

    version = args.version or detect_version(args.input_dir)
    if not version:
        parser.error(
            f"Could not detect DPV version from owl:versionInfo under "
            f"{args.input_dir}; pass --version explicitly."
        )
    print(f"DPV version: {version}", file=sys.stderr)

    generate(args.input_dir, args.output_dir, version, args.report)


if __name__ == "__main__":
    main()
