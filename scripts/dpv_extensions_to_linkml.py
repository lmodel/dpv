#!/usr/bin/env python3
"""
Transform every DPV 2.3 extension (the non-core modules vendored alongside
``upstream-releases/dpv/dpv/``) into per-extension LinkML schemas under
``src/dpv/schema/extensions/``.

This is the complement to ``dpv_core_to_linkml.py`` (which only handles the
``dpv/`` core release). It produces one LinkML schema per extension, each
with its own ``id``, ``name`` and ``default_prefix``, importing only
``linkml:types`` + ``dpv:schema/dpv`` (the umbrella that re-exports the 8
semantic-group schemas, for the abstract parents) plus any sibling
extensions whose classes it specialises.

Layout produced (mirrors the upstream ``2.3/<ext>/`` tree):

    src/dpv/schema/extensions/
      ai.yaml                  # aggregate of ai/ai-owl.ttl
      ai/
        capabilities.yaml      # ai/modules/capabilities-owl.ttl
        core.yaml
        data.yaml
        development.yaml
        lifecycle.yaml
        measures.yaml
        risks.yaml
        systems.yaml
        techniques.yaml
      pd.yaml                  # …/pd
      pd/{core,extended}.yaml
      loc.yaml
      tech.yaml
      risk.yaml
      risk/{incident,incident_status,risk_controls,risk_levels,
            risk_management,risk_matrix,risk_taxonomy}.yaml
      justifications.yaml
      justifications/{delay,exercise,nonfulfilment,notrequired}.yaml
      legal.yaml
      legal/<cc>.yaml          # one per upstream jurisdiction (eu, de, …)
      legal/eu/{gdpr,dga,ehds,nis2,aiact,rights}.yaml
      legal/eu/gdpr/{compliance,data_breach,…}.yaml
      sector.yaml
      sector/<industry>.yaml
      standards.yaml
      standards/ieee/7012.yaml

Key design choices
==================

* Identity (LinkML) - every extension declares its own
  ``default_prefix: <slug>`` and ``id: https://w3id.org/lmodel/dpv/<path>``;
  classes carry ``class_uri: <slug>:<Name>`` rather than ``dpv:<Name>`` so
  the LinkML identity URI matches the schema's namespace.
* Identity (RDF) - the upstream W3C DPV CURIEs are recorded as
  ``exact_mappings: [dpv_<ext>:<Name>, dpv_<ext>_owl:<Name>]`` so generated
  RDF/OWL never shadows the W3C IRI.
* Cross-extension parents - classes whose ``rdfs:subClassOf`` points at a
  *different* DPV-family namespace (e.g. ``ai-owl:Foo`` ⊑ ``dpv-owl:Bar``,
  or ``eu-gdpr-owl:Foo`` ⊑ ``pd-owl:Baz``) resolve their parent local-name
  unchanged. LinkML name resolution is flat across the merged schema, so as
  long as ``Bar``/``Baz`` is declared in any imported sibling schema the
  ``is_a`` link is valid. Auto-imports are computed from observed foreign
  namespaces.
* Per-module schemas inside an extension reuse the per-module pattern
  already established in ``dpv_core_to_linkml.py``: each module schema imports
  the extension aggregate and emits the *same* classes with an
  ``in_subset: <module>_subset`` tag for downstream slicing.

Reproducibility
===============

Deterministic (stable sort of subjects, no timestamps). Re-running with
unchanged ``upstream-releases/dpv/`` produces byte-identical YAML.

Usage
-----

    uv run --with rdflib --with pyyaml \
      python scripts/dpv_extensions_to_linkml.py \
        [-i upstream-releases/dpv] \
        [-o src/dpv/schema/extensions] \
        [--report]

The DPV version is auto-detected (same logic as ``dpv_core_to_linkml.py``).
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

import rdflib
from rdflib import Graph, Literal, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SKOS, XSD

# ---------------------------------------------------------------------------
# Share helpers with the core generator (keeps formatting / sanitisation
# identical between core and extensions; do not duplicate).
# ---------------------------------------------------------------------------
_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

import dpv_core_to_linkml as core  # noqa: E402

DPV_CORE_OWL_NS = core.DPV_OWL_NS              # https://w3id.org/dpv/owl#
DPV_CORE_CAN_NS = core.DPV_CAN_NS              # https://w3id.org/dpv#
DPV_FAMILY_BASE = "https://w3id.org/dpv/"
LMODEL_BASE = core.LMODEL_BASE                 # https://w3id.org/lmodel/dpv
LMODEL_EXT_BASE = f"{LMODEL_BASE}/"            # https://w3id.org/lmodel/dpv/
DCT = core.DCT

# Match every DPV-family OWL namespace, e.g.
#   https://w3id.org/dpv/owl#                 -> (slug="dpv", flavour="owl")
#   https://w3id.org/dpv/ai/owl#              -> (slug="ai", flavour="owl")
#   https://w3id.org/dpv/legal/eu/gdpr/owl#   -> (slug="legal/eu/gdpr", flavour="owl")
#   https://w3id.org/dpv/ai#                  -> (slug="ai", flavour="can")
_FAMILY_RE = re.compile(
    r"^https://w3id\.org/dpv/(?:(?P<slug>[^#]+?)/)?(?P<tail>owl#|#)"
)

# Local names we never emit as elements (LinkML metamodel / structural).
_RESERVED = core._RESERVED_LOCAL_NAMES


# ---------------------------------------------------------------------------
# Extension model
# ---------------------------------------------------------------------------

@dataclass
class ExtensionSpec:
    """A single DPV extension (aggregate file + optional submodules)."""

    slug: str                        # path under /dpv/, e.g. "ai", "legal/eu/gdpr"
    rel_path: Path                   # dir relative to input_dir, e.g. Path("ai")
    owl_ns: str                      # https://w3id.org/dpv/<slug>/owl#
    can_ns: str                      # https://w3id.org/dpv/<slug>#
    aggregate_owl: Path              # ai/ai-owl.ttl
    aggregate_can: Path | None       # ai/ai.ttl (canonical SKOS)
    submodules: list["SubmoduleSpec"] = field(default_factory=list)
    # Sibling extensions referenced from this extension's TTL (computed
    # post-hoc by scanning subClassOf / domain / range URIs).
    foreign_refs: set[str] = field(default_factory=set)
    # When the ontology IRI namespace differs from the filesystem path
    # (namespace-fallback case), this stores the slug derived from the IRI.
    # E.g., legal/eu/rights has ontology_iri_slug="rights/eu". Used to filter
    # self-referential foreign imports so the extension doesn't try to import
    # a non-existent sibling that is actually itself.
    ontology_iri_slug: str | None = None

    @property
    def name(self) -> str:
        """LinkML schema ``name`` - snake_case underscored path."""
        return "dpv_" + self.slug.replace("/", "_").replace("-", "_")

    @property
    def prefix(self) -> str:
        """Default prefix for this extension (NCName)."""
        return self.slug.replace("/", "_").replace("-", "_")

    @property
    def pascal_prefix(self) -> str:
        """PascalCase owner prefix for collision-prone class renaming.

        Derived from the slug by splitting on ``/`` and ``-`` and capitalising
        each segment. Examples:

        >>> ExtensionSpec("ai", ...).pascal_prefix          # "Ai"
        >>> ExtensionSpec("pd", ...).pascal_prefix          # "Pd"
        >>> ExtensionSpec("legal/eu/gdpr", ...).pascal_prefix  # "LegalEuGdpr"
        >>> ExtensionSpec("standards/ieee/7012", ...).pascal_prefix
        ... # "StandardsIeee7012"

        Used so that e.g. ``ai:Data`` becomes the LinkML class ``AiData`` and
        does not collide with core ``DpvData`` (``dpv:Data``) when both
        schemas are imported into the same SchemaView.
        """
        parts = re.split(r"[/_-]+", self.slug)
        return "".join(p[:1].upper() + p[1:] for p in parts if p)

    @property
    def lmodel_id(self) -> str:
        """Stable LinkML schema id under the lmodel/dpv/ w3id redirect."""
        return f"{LMODEL_BASE}/{self.slug}"

    @property
    def lmodel_ns(self) -> str:
        """Namespace IRI that ``prefix`` binds to in the generated schema."""
        return f"{LMODEL_EXT_BASE}{self.slug}/"

    @property
    def out_aggregate(self) -> Path:
        """Output path for the aggregate schema, relative to output_dir."""
        return Path(self.slug + ".yaml")

    @property
    def out_dir(self) -> Path:
        """Output directory for submodule schemas, relative to output_dir."""
        return Path(self.slug)


@dataclass
class SubmoduleSpec:
    """A per-extension module file (e.g. ai/modules/risks-owl.ttl)."""

    name: str                        # snake_case module name (e.g. "risks")
    owl_path: Path                   # ai/modules/risks-owl.ttl
    can_path: Path | None            # ai/modules/risks.ttl


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def _slug_from_owl_iri(iri: str) -> str | None:
    """Extract the DPV path slug from an OWL ontology IRI.

    >>> _slug_from_owl_iri("https://w3id.org/dpv/ai/owl#")
    'ai'
    >>> _slug_from_owl_iri("https://w3id.org/dpv/legal/eu/gdpr/owl#")
    'legal/eu/gdpr'
    >>> _slug_from_owl_iri("https://w3id.org/dpv/owl#")  # core, never an extension
    """
    m = _FAMILY_RE.match(iri)
    if not m or not m.group("slug") or m.group("tail") != "owl#":
        return None
    return m.group("slug")


def _ontology_namespace(g: Graph) -> str | None:
    """Return the ``owl:Ontology`` IRI's namespace (with trailing ``#``).

    Upstream DPV files always declare ``<ns>: a owl:Ontology`` where the IRI
    is the namespace itself (e.g. ``https://w3id.org/dpv/ai/owl#`` minus the
    ``#``). The serialiser writes it with the ``#`` stripped; we re-add it.
    """
    for s in g.subjects(RDF.type, OWL.Ontology):
        if isinstance(s, URIRef):
            iri = str(s)
            if not iri.endswith("#"):
                iri += "#"
            return iri
    return None


def discover_extensions(input_dir: Path) -> list[ExtensionSpec]:
    """Walk ``input_dir`` and return one ExtensionSpec per aggregate file.

    The aggregate file for an extension is any ``<basename>-owl.ttl`` that
    is NOT under a ``modules/`` directory AND whose declared
    ``owl:Ontology`` IRI lives below ``https://w3id.org/dpv/`` with at
    least one path segment (i.e. not the bare core ``dpv/owl#``). Each
    sibling under ``<dir>/modules/`` becomes a SubmoduleSpec sharing the
    same OWL namespace.
    """
    extensions: list[ExtensionSpec] = []

    # Find every potential aggregate file. We deliberately walk the whole
    # tree so deeply nested extensions (legal/eu/gdpr, standards/ieee/7012,
    # sector/health) are picked up uniformly.
    candidate_owls = sorted(input_dir.rglob("*-owl.ttl"))
    aggregates: list[Path] = [
        p for p in candidate_owls
        # exclude modules/ files (those become SubmoduleSpec instances)
        if p.parent.name != "modules"
        # exclude the dpv/ core (handled by dpv_core_to_linkml.py)
        and "dpv" not in {p.parent.name}
    ]

    for owl_path in aggregates:
        # Derive the slug from the path under input_dir. Upstream DPV uses
        # the path layout as the canonical namespace mirror: a file at
        # `<input>/legal/eu/gdpr/eu-gdpr-owl.ttl` corresponds to the
        # ontology IRI `https://w3id.org/dpv/legal/eu/gdpr/owl#`.
        rel_dir = owl_path.parent.relative_to(input_dir)
        slug = rel_dir.as_posix()
        if slug in {"", "."}:
            continue
        ns = f"https://w3id.org/dpv/{slug}/owl#"
        can_ns = f"https://w3id.org/dpv/{slug}#"

        # Sanity-check: the file should actually contain triples in `ns`.
        # Upstream is mostly path-consistent, but a few extensions (notably
        # `legal/eu/rights/`) declare an ontology IRI that does NOT mirror
        # the filesystem path (`https://w3id.org/dpv/rights/eu/owl#`). When
        # that happens, fall back to the actual `owl:Ontology` IRI so
        # extraction still finds the file's classes/properties.
        g = _parse_ttl(owl_path)
        ontology_iri_slug = None
        if not any(str(s).startswith(ns) for s in g.subjects() if isinstance(s, URIRef)):
            actual_ns = _ontology_namespace(g)
            if actual_ns and any(
                str(s).startswith(actual_ns)
                for s in g.subjects() if isinstance(s, URIRef)
            ):
                ns = actual_ns
                can_ns = actual_ns.replace("/owl#", "#")
                # Record the actual ontology IRI slug so we can filter it from
                # foreign imports later (it's really an alias for this extension,
                # not a foreign one).
                ontology_iri_slug = _slug_from_owl_iri(ns)
                print(
                    f"   [namespace-fallback] {owl_path.relative_to(input_dir)}: "
                    f"path-ns mismatched, using ontology IRI {ns}",
                    file=sys.stderr,
                )
            elif not (owl_path.parent / "modules").is_dir():
                # Truly empty shell with no submodules - skip silently.
                continue
        canonical_path = owl_path.with_name(owl_path.name.replace("-owl.ttl", ".ttl"))
        if not canonical_path.exists():
            canonical_path = None  # type: ignore[assignment]

        ext = ExtensionSpec(
            slug=slug,
            rel_path=owl_path.parent.relative_to(input_dir),
            owl_ns=ns,
            can_ns=can_ns,
            aggregate_owl=owl_path,
            aggregate_can=canonical_path,
            ontology_iri_slug=ontology_iri_slug,
        )

        modules_dir = owl_path.parent / "modules"
        if modules_dir.is_dir():
            for mod_owl in sorted(modules_dir.glob("*-owl.ttl")):
                mod_name = mod_owl.stem[:-len("-owl")]
                mod_can = mod_owl.with_name(f"{mod_name}.ttl")
                ext.submodules.append(SubmoduleSpec(
                    name=mod_name,
                    owl_path=mod_owl,
                    can_path=mod_can if mod_can.exists() else None,
                ))
        extensions.append(ext)

    # Stable ordering: shallowest path first, then alphabetical.
    extensions.sort(key=lambda e: (e.slug.count("/"), e.slug))
    return extensions


# ---------------------------------------------------------------------------
# Namespace-aware extraction (mirrors dpv_to_linkml.extract_*, generalised)
# ---------------------------------------------------------------------------

def _local_of(uri: URIRef, ns: str) -> str | None:
    s = str(uri)
    if not s.startswith(ns):
        return None
    local = s[len(ns):]
    if not local or "/" in local or local.startswith("serialisation-"):
        return None
    if local in _RESERVED:
        return None
    return local


def _family_local(uri: URIRef) -> tuple[str, str] | None:
    """Return (slug, local) if ``uri`` is in ANY DPV-family OWL namespace.

    ``slug`` is the empty string for the core ``dpv-owl:`` namespace, and
    a path slug otherwise. ``local`` is the post-``#`` fragment, with the
    same reserved-name / hyphen filtering as ``_local_of``.
    """
    s = str(uri)
    if not s.startswith(DPV_FAMILY_BASE):
        return None
    # Core dpv-owl:
    if s.startswith(DPV_CORE_OWL_NS):
        local = s[len(DPV_CORE_OWL_NS):]
    else:
        m = _FAMILY_RE.match(s)
        if not m or m.group("tail") != "owl#":
            return None
        local = s[m.end():]
    if not local or "/" in local or local.startswith("serialisation-"):
        return None
    if local in _RESERVED:
        return None
    slug = ""
    if s.startswith(DPV_CORE_OWL_NS):
        slug = ""
    else:
        m = _FAMILY_RE.match(s)
        assert m is not None
        slug = m.group("slug") or ""
    return slug, local


def _uri_to_curie_for(ext: ExtensionSpec, uri: URIRef) -> str | None:
    """Like ``core.uri_to_curie`` but also recognises the extension's own
    ``dpv_<slug>`` / ``dpv_<slug>_owl`` namespaces. URI fragments are
    ASCII-folded (see ``core.ascii_safe_local``) so the resulting CURIE
    is a valid LinkML element reference even when the upstream fragment
    contains diacritics."""
    s = str(uri)
    if s.startswith(ext.owl_ns):
        return f"dpv_{ext.prefix}_owl:{core.ascii_safe_local(s[len(ext.owl_ns):])}"
    if s.startswith(ext.can_ns):
        return f"dpv_{ext.prefix}:{core.ascii_safe_local(s[len(ext.can_ns):])}"
    return core.uri_to_curie(uri)


def _slug_to_pascal(slug: str) -> str:
    """Convert a DPV slug ('ai', 'legal/eu/gdpr') to PascalCase owner prefix.

    Mirrors ``ExtensionSpec.pascal_prefix`` for the foreign-slug case where
    we only have the slug string (no ExtensionSpec in scope).
    """
    parts = re.split(r"[/_-]+", slug)
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


def _owner_prefix_for(slug: str, ext: ExtensionSpec) -> str:
    """Return the PascalCase ``owner_prefix`` for a class owned by ``slug``.

    ``slug == ext.slug`` -> this extension's own pascal prefix.
    ``slug == ""``       -> core ``dpv`` namespace, owner prefix ``Dpv``.
    Any other slug       -> the sibling extension's pascal prefix derived
                            mechanically from the slug.
    """
    if slug == ext.slug:
        return ext.pascal_prefix
    if not slug:
        return "Dpv"
    return _slug_to_pascal(slug)


def _class_name_for(slug: str, local: str, ext: ExtensionSpec,
                    core_class_names: frozenset[str] = frozenset()) -> str:
    """Resolve a (slug, local) reference to its LinkML class name.

    Encapsulates the collision-prone rename: e.g. (``"ai"``, ``"Data"``) ->
    ``AiData`` when ``ext.slug == "ai"``; (``""``, ``"Data"``) -> ``DpvData``.

    ``core_class_names`` enables *dynamic* collision detection: when the
    reference points at *this* extension's own namespace (``slug == ext.slug``)
    and the resulting unprefixed name would shadow a core class name
    (e.g. AI redefines ``RiskConcept`` already declared by
    ``dpv_risk_notice``), the name is force-prefixed with this extension's
    pascal prefix (``AiRiskConcept``). This catches DPV-domain collisions
    that are not in the static ``_COLLISION_PRONE_CLASSES`` list. Names
    already prefixed by the static rename are left alone.
    """
    owner_prefix = _owner_prefix_for(slug, ext)
    name = core.sanitise_class_name(local, owner_prefix=owner_prefix)
    if slug == ext.slug and core_class_names:
        unprefixed = core.ascii_safe_local(local).replace("-", "")
        # Only fire dynamic rename if the static collision list did NOT already
        # prefix the name (otherwise we'd double-prefix).
        if name == unprefixed and unprefixed in core_class_names:
            return f"{ext.pascal_prefix}{unprefixed}"
    return name


def _extract_classes_ns(
    g_owl: Graph,
    g_can: Graph | None,
    ext: ExtensionSpec,
    foreign_log: set[str],
    core_class_names: frozenset[str] = frozenset(),
) -> dict[str, dict]:
    """Extract every owl:Class in ``ext.owl_ns`` as a LinkML class.

    ``foreign_log`` is mutated to record every external DPV-family slug
    seen on subClassOf / mixin / type triples (used to compute imports).
    """
    classes: dict[str, dict] = {}

    subjects: set[URIRef] = set()
    for t in (OWL.Class, RDFS.Class):
        for s in g_owl.subjects(RDF.type, t):
            if isinstance(s, URIRef) and _local_of(s, ext.owl_ns):
                subjects.add(s)

    structural = {OWL.Class, RDFS.Class, OWL.NamedIndividual,
                  OWL.ObjectProperty, OWL.DatatypeProperty,
                  OWL.AnnotationProperty, OWL.Ontology}

    for cls in sorted(subjects, key=str):
        cls_local = _local_of(cls, ext.owl_ns)
        assert cls_local is not None
        # ASCII-safe form for use in CURIEs / element names; the raw
        # ``cls_local`` is retained for canonical-NS URI reconstruction
        # (RDF graph lookup) and for traceability via ``aliases``.
        cls_local_safe = core.ascii_safe_local(cls_local)
        cls_name = _class_name_for(ext.slug, cls_local, ext, core_class_names)
        entry: dict[str, Any] = {}

        # ---- description -----------------------------------------------
        defn = core.first_literal(g_owl, cls, SKOS.definition) \
               or core.first_literal(g_owl, cls, SKOS.scopeNote)
        if defn:
            entry["description"] = defn

        # ---- named parents (own ns + foreign DPV-family ns) ------------
        named_parents: list[tuple[str, str]] = []
        for o in g_owl.objects(cls, RDFS.subClassOf):
            if not isinstance(o, URIRef):
                continue
            fl = _family_local(o)
            if fl is None:
                continue
            slug, local = fl
            named_parents.append((slug, local))
            if slug != ext.slug:
                foreign_log.add(slug)

        if named_parents:
            parent_slug, parent_local = named_parents[0]
            parent_name = _class_name_for(parent_slug, parent_local, ext, core_class_names)
            # Guard: a class can never be its own parent.
            if parent_name and parent_name != cls_name:
                entry["is_a"] = parent_name

        # ---- rdf:type secondary classes -> mixins ----------------------
        type_mixins: list[str] = []
        for t in g_owl.objects(cls, RDF.type):
            if not isinstance(t, URIRef) or t in structural:
                continue
            fl = _family_local(t)
            if fl is None:
                continue
            slug, local = fl
            type_mixins.append(_class_name_for(slug, local, ext, core_class_names))
            if slug != ext.slug:
                foreign_log.add(slug)

        seen = {entry.get("is_a")}
        dedup_mixins: list[str] = []
        for m in type_mixins:
            if m and m != cls_name and m not in seen:
                dedup_mixins.append(m)
                seen.add(m)
        if len(named_parents) > 1:
            for parent_slug2, local in named_parents[1:]:
                m = _class_name_for(parent_slug2, local, ext, core_class_names)
                if m and m not in seen and m != cls_name:
                    dedup_mixins.append(m)
                    seen.add(m)
        if dedup_mixins:
            entry["mixins"] = dedup_mixins

        # ---- identity --------------------------------------------------
        entry["class_uri"] = f"{ext.prefix}:{cls_local_safe}"

        # ---- aliases ---------------------------------------------------
        aliases: list[str] = []
        if cls_name != cls_local:
            aliases.append(cls_local)
        pref = core.first_literal(g_owl, cls, SKOS.prefLabel)
        if pref and pref not in aliases:
            aliases.append(pref)
        for label in core.get_literals(g_owl, cls, SKOS.altLabel):
            if label not in aliases:
                aliases.append(label)
        for label in core.get_literals(g_owl, cls, RDFS.label):
            if label not in aliases:
                aliases.append(label)
        if aliases:
            entry["aliases"] = aliases

        # ---- comments --------------------------------------------------
        comments: list[str] = []
        for sn in core.get_literals(g_owl, cls, SKOS.scopeNote):
            if sn != entry.get("description") and sn not in comments:
                comments.append(sn)
        for note in core.get_literals(g_owl, cls, SKOS.editorialNote):
            if note not in comments:
                comments.append(note)
        if comments:
            entry["comments"] = comments

        # ---- exact / close / broad / narrow / related mappings ---------
        equivs: list[str] = []
        for o in g_owl.objects(cls, OWL.equivalentClass):
            if isinstance(o, URIRef):
                curie = _uri_to_curie_for(ext, o)
                equivs.append(curie if curie else str(o))
        for o in g_owl.objects(cls, SKOS.exactMatch):
            if isinstance(o, URIRef):
                curie = _uri_to_curie_for(ext, o)
                if curie and curie not in equivs:
                    equivs.append(curie)
        # Canonical upstream identity, both flavours, under ext-specific prefixes.
        equivs.append(f"dpv_{ext.prefix}:{cls_local_safe}")
        equivs.append(f"dpv_{ext.prefix}_owl:{cls_local_safe}")
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
                if isinstance(o, URIRef) and not _local_of(o, ext.owl_ns):
                    curie = _uri_to_curie_for(ext, o)
                    if curie:
                        entry.setdefault(key, [])
                        if curie not in entry[key]:
                            entry[key].append(curie)

        # ---- deprecation -----------------------------------------------
        if core.first_literal(g_owl, cls, OWL.deprecated) == "true":
            entry["deprecated"] = "true"

        # ---- canonical SKOS enrichment ---------------------------------
        if g_can is not None:
            canonical_subj = URIRef(ext.can_ns + cls_local)
            if (canonical_subj, None, None) in g_can:
                core._enrich_from_canonical(canonical_subj, g_can, entry)
        # Canonical enrichment may have re-introduced a self-referential
        # parent (e.g. SKOS broader pointing to the same SKOS concept);
        # strip it so generated LinkML stays acyclic.
        if entry.get("is_a") == cls_name:
            entry.pop("is_a", None)

        # ---- provenance annotations (skill enrichment) -----------------
        entry.setdefault("annotations", {}).update({
            "upstream_iri": str(cls),
            "dpv_extension_slug": ext.slug,
        })

        classes[cls_name] = entry

    return classes


def _extract_slots_ns(
    g_owl: Graph,
    g_can: Graph | None,
    ext: ExtensionSpec,
    foreign_log: set[str],
    core_class_names: frozenset[str] = frozenset(),
) -> dict[str, dict]:
    slots: dict[str, dict] = {}

    prop_types = (OWL.ObjectProperty, OWL.DatatypeProperty, OWL.AnnotationProperty)
    subjects: set[URIRef] = set()
    for t in prop_types:
        for s in g_owl.subjects(RDF.type, t):
            if isinstance(s, URIRef) and _local_of(s, ext.owl_ns):
                subjects.add(s)

    for prop in sorted(subjects, key=str):
        prop_local = _local_of(prop, ext.owl_ns)
        assert prop_local is not None
        prop_local_safe = core.ascii_safe_local(prop_local)
        sname = core.camel_to_snake(prop_local)
        entry: dict[str, Any] = {
            "definition_uri": f"{ext.prefix}:{prop_local_safe}",
        }

        defn = core.first_literal(g_owl, prop, SKOS.definition) \
               or core.first_literal(g_owl, prop, RDFS.comment)
        if defn:
            entry["description"] = defn

        sub_of: list[tuple[str, str]] = []
        for o in g_owl.objects(prop, RDFS.subPropertyOf):
            if isinstance(o, URIRef):
                fl = _family_local(o)
                if fl:
                    sub_of.append(fl)
                    if fl[0] != ext.slug:
                        foreign_log.add(fl[0])
        if sub_of:
            parent_name = core.camel_to_snake(sub_of[0][1])
            # Guard: a slot can never be its own parent.
            if parent_name and parent_name != sname:
                entry["is_a"] = parent_name

        domains: list[str] = []
        for o in g_owl.objects(prop, RDFS.domain):
            if isinstance(o, URIRef):
                fl = _family_local(o)
                if fl:
                    domains.append(_class_name_for(fl[0], fl[1], ext, core_class_names))
                    if fl[0] != ext.slug:
                        foreign_log.add(fl[0])
        if domains:
            entry["domain"] = domains[0]

        all_types = set(g_owl.objects(prop, RDF.type))
        is_datatype = OWL.DatatypeProperty in all_types

        range_uris = [o for o in g_owl.objects(prop, RDFS.range)
                      if isinstance(o, URIRef)]
        if is_datatype:
            if range_uris:
                entry["range"] = core.XSD_TO_LINKML.get(str(range_uris[0]), "string")
        else:
            dpv_ranges: list[str] = []
            for o in range_uris:
                fl = _family_local(o)
                if fl:
                    dpv_ranges.append(_class_name_for(fl[0], fl[1], ext, core_class_names))
                    if fl[0] != ext.slug:
                        foreign_log.add(fl[0])
            if len(dpv_ranges) == 1:
                entry["range"] = dpv_ranges[0]
            elif len(dpv_ranges) > 1:
                entry["any_of"] = [{"range": r} for r in dpv_ranges]
            if OWL.ObjectProperty in all_types:
                entry["multivalued"] = True

        inverses: list[str] = []
        for o in g_owl.objects(prop, OWL.inverseOf):
            if isinstance(o, URIRef):
                fl = _family_local(o)
                if fl:
                    inverses.append(core.camel_to_snake(fl[1]))
        if inverses:
            entry["inverse"] = inverses[0]

        aliases: list[str] = []
        pref = core.first_literal(g_owl, prop, SKOS.prefLabel)
        if pref and pref not in aliases:
            aliases.append(pref)
        for label in core.get_literals(g_owl, prop, SKOS.altLabel):
            if label not in aliases:
                aliases.append(label)
        for label in core.get_literals(g_owl, prop, RDFS.label):
            if label not in aliases:
                aliases.append(label)
        if aliases:
            entry["aliases"] = aliases

        equivs: list[str] = []
        for o in g_owl.objects(prop, OWL.equivalentProperty):
            if isinstance(o, URIRef):
                curie = _uri_to_curie_for(ext, o)
                equivs.append(curie if curie else str(o))
        equivs.append(f"dpv_{ext.prefix}:{prop_local_safe}")
        equivs.append(f"dpv_{ext.prefix}_owl:{prop_local_safe}")
        seen_eq: set[str] = set()
        equivs = [e for e in equivs if not (e in seen_eq or seen_eq.add(e))]
        entry["exact_mappings"] = equivs

        if OWL.TransitiveProperty in all_types:
            entry["transitive"] = True
        if OWL.SymmetricProperty in all_types:
            entry["symmetric"] = True
        if OWL.ReflexiveProperty in all_types:
            entry["reflexive"] = True
        if core.first_literal(g_owl, prop, OWL.deprecated) == "true":
            entry["deprecated"] = "true"

        if g_can is not None:
            canonical_subj = URIRef(ext.can_ns + prop_local)
            if (canonical_subj, None, None) in g_can:
                core._enrich_from_canonical(canonical_subj, g_can, entry)
        # Strip any self-referential parent that canonical enrichment
        # might have re-introduced.
        if entry.get("is_a") == sname:
            entry.pop("is_a", None)

        # ---- provenance annotations (skill enrichment) -----------------
        entry.setdefault("annotations", {}).update({
            "upstream_iri": str(prop),
            "dpv_extension_slug": ext.slug,
        })

        slots[sname] = entry

    return slots


# ---------------------------------------------------------------------------
# Schema assembly
# ---------------------------------------------------------------------------

def _ext_prefixes(ext: ExtensionSpec, foreign: set[str]) -> dict[str, str]:
    """Prefix map for an extension schema.

    Combines the base ``_base_prefixes()`` from the core generator (so
    every standard mapping target is pre-declared and lint-clean) with
    this extension's own LinkML namespace plus its upstream OWL +
    canonical SKOS namespaces. Foreign extensions referenced from this
    schema's TTL also get their LinkML / OWL / canonical prefixes pre-
    declared so cross-extension ``is_a`` / ``range`` references resolve.
    """
    prefixes = dict(core._base_prefixes())
    # Own ext
    prefixes[ext.prefix] = ext.lmodel_ns
    prefixes[f"dpv_{ext.prefix}"] = ext.can_ns
    prefixes[f"dpv_{ext.prefix}_owl"] = ext.owl_ns
    # Each foreign extension we touched
    for slug in sorted(foreign):
        pref = slug.replace("/", "_").replace("-", "_")
        prefixes.setdefault(pref, f"{LMODEL_EXT_BASE}{slug}/")
        prefixes.setdefault(f"dpv_{pref}", f"https://w3id.org/dpv/{slug}#")
        prefixes.setdefault(f"dpv_{pref}_owl", f"https://w3id.org/dpv/{slug}/owl#")
    return prefixes


# Canonical group order (common first) for deterministic import blocks.
_GROUP_ORDER: list[str] = (
    ["common"] + [g for g in core.SEMANTIC_GROUPS if g != "common"]
)


def _build_core_group_index(schema_dir: Path) -> dict[str, str]:
    """Map each core element name (class or slot) -> its semantic-group slug.

    Read from the generated ``dpv_<group>.yaml`` files (which exist because the
    extension build runs after ``dpv_core_to_linkml.py``). Lets each extension
    import only the groups it actually specialises instead of the full umbrella
    ``dpv:schema/dpv``. First-seen wins; groups are disjoint by construction so
    there is no real contention.
    """
    index: dict[str, str] = {}
    for group in core.SEMANTIC_GROUPS:
        f = schema_dir / f"dpv_{group}.yaml"
        if not f.exists():
            continue
        doc = core.yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        for name in list(doc.get("classes") or {}) + list(doc.get("slots") or {}):
            index.setdefault(name, group)
    return index


def _build_core_class_names(schema_dir: Path) -> frozenset[str]:
    """Return the set of all class names defined by any core ``dpv_<group>.yaml``.

    Used for dynamic collision detection so an extension class that shadows a
    core class name (e.g. AI redefines ``RiskConcept`` already declared by
    ``dpv_risk_notice``) is auto-prefixed with the extension's pascal prefix
    (``AiRiskConcept``). Without this, the umbrella merge built by
    ``gen-project`` triggers ``ValueError: Conflicting URIs ... for item: X``.
    Slot names are intentionally excluded: LinkML slot/class namespaces are
    independent for ``definition_uri`` purposes.
    """
    names: set[str] = set()
    for group in core.SEMANTIC_GROUPS:
        f = schema_dir / f"dpv_{group}.yaml"
        if not f.exists():
            continue
        doc = core.yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        names.update((doc.get("classes") or {}).keys())
    return frozenset(names)


def _referenced_core_groups(
    classes: dict, slots: dict, core_index: dict[str, str],
) -> list[str]:
    """Semantic groups (canonical order) declaring the core elements referenced
    by these extension classes/slots.

    Scans every reference field that LinkML must resolve to a schema element:
    class ``is_a``/``mixins`` and slot ``is_a``/``domain``/``range``/``any_of``/
    ``inverse``. Locally-defined names win, so an extension class that shadows a
    core name does not drag in that core group. Mapping targets (``*_mappings``)
    are plain CURIEs, not schema references, so they are deliberately ignored.
    """
    local = set(classes) | set(slots)
    needed: set[str] = set()

    def consider(name: Any) -> None:
        if not isinstance(name, str) or name in local:
            return
        group = core_index.get(name)
        if group:
            needed.add(group)

    for entry in classes.values():
        consider(entry.get("is_a"))
        for m in entry.get("mixins") or []:
            consider(m)
    for entry in slots.values():
        consider(entry.get("is_a"))
        consider(entry.get("domain"))
        consider(entry.get("range"))
        consider(entry.get("inverse"))
        for branch in entry.get("any_of") or []:
            consider(branch.get("range") if isinstance(branch, dict) else None)
    return [g for g in _GROUP_ORDER if g in needed]


def _core_imports(groups: list[str] | None) -> list[str]:
    """Core-schema imports for an extension. ``groups`` is the list of semantic
    groups it specialises; ``None`` falls back to the full umbrella (used only
    when the group schemas are not present yet)."""
    if groups is None:
        return ["dpv:schema/dpv"]
    return [f"dpv:schema/dpv_{g}" for g in groups]


def _ext_imports(
    ext: ExtensionSpec, foreign: set[str], groups: list[str] | None,
) -> list[str]:
    imports = ["linkml:types"] + _core_imports(groups)
    for slug in sorted(foreign):
        imports.append(f"dpv:schema/extensions/{slug}")
    return imports


def _humanise(slug: str) -> str:
    return slug.replace("/", " - ").replace("_", " ").title()


def build_aggregate_schema(
    ext: ExtensionSpec,
    classes: dict,
    slots: dict,
    submodule_names: list[str],
    version: str,
    foreign: set[str],
    groups: list[str],
    source: str | None,
) -> dict:
    subset_name = core._module_subset_name(ext.prefix)
    subsets: dict[str, dict] = {
        subset_name: {
            "description": (
                f"All entities from the DPV `{ext.slug}` extension."
            ),
        }
    }
    for sub in sorted(submodule_names):
        subsets[core._module_subset_name(f"{ext.prefix}_{sub}")] = {
            "description": (
                f"Entities from the DPV `{ext.slug}/modules/{sub}` submodule."
            ),
        }

    schema: dict[str, Any] = {
        "id": ext.lmodel_id,
        "name": ext.name,
        "title": f"DPV - {_humanise(ext.slug)}",
        "description": (
            f"LinkML schema generated from the DPV {version} extension "
            f"`{ext.slug}` (`{ext.aggregate_owl.name}`), enriched with "
            "canonical SKOS metadata. " + (
                "Imports the semantic-group schema(s) "
                + ", ".join(f"`dpv:schema/dpv_{g}`" for g in groups)
                + " for the abstract parent classes this extension "
                "specialises (instead of the full umbrella `dpv:schema/dpv`)."
                if groups else
                "Imports the full umbrella `dpv:schema/dpv` for the abstract "
                "parent classes this extension specialises."
                if groups is None else
                "References no core DPV classes, so it imports only "
                "`linkml:types` (and any sibling extensions it specialises)."
            )
        ),
        "license": "CC-BY-4.0",
        "see_also": [
            f"https://w3id.org/dpv/{ext.slug}",
            f"https://w3c.github.io/dpv/2.3/{ext.slug}/",
        ],
        "version": version,
    }
    if source:
        schema["source"] = source

    schema.update({
        "prefixes": _ext_prefixes(ext, foreign),
        "default_prefix": ext.prefix,
        "default_range": "string",
        "id_prefixes": [
            ext.prefix,
            f"dpv_{ext.prefix}",
            f"dpv_{ext.prefix}_owl",
        ],
        "imports": _ext_imports(ext, foreign, groups),
        "subsets": subsets,
    })
    schema["annotations"] = {
        "dpv_version": version,
        "dpv_extension_slug": ext.slug,
        "source_ttl": _repo_rel(ext.aggregate_owl),
        **({"source_canonical_ttl": _repo_rel(ext.aggregate_can)}
           if ext.aggregate_can else {}),
        "upstream_owl_namespace": ext.owl_ns,
        "upstream_canonical_namespace": ext.can_ns,
    }
    if slots:
        schema["slots"] = core._order_elements(slots, subset_name)
    if classes:
        schema["classes"] = core._order_elements(classes, subset_name)
    return core._order_keys(schema, core._SCHEMA_KEY_ORDER)


def build_submodule_schema(
    ext: ExtensionSpec,
    sub: SubmoduleSpec,
    classes: dict,
    slots: dict,
    version: str,
    foreign: set[str],
    groups: list[str],
    source: str | None,
) -> dict:
    subset_name = core._module_subset_name(f"{ext.prefix}_{sub.name}")
    schema: dict[str, Any] = {
        "id": f"{ext.lmodel_id}/{sub.name}",
        "name": f"{ext.name}_{sub.name}",
        "title": f"DPV - {_humanise(ext.slug)} / {sub.name.replace('_', ' ').title()}",
        "description": (
            f"LinkML schema generated from the DPV {version} extension "
            f"module `{ext.slug}/modules/{sub.owl_path.name}`."
        ),
        "license": "CC-BY-4.0",
        "see_also": [
            f"https://w3id.org/dpv/{ext.slug}",
            f"https://w3c.github.io/dpv/2.3/{ext.slug}/",
        ],
        "version": version,
    }
    if source:
        schema["source"] = source

    # Submodule imports the aggregate so we can reference its slots/classes
    # by local name (LinkML resolves names across the merged tree), plus only
    # the semantic groups its own elements specialise (not the full umbrella).
    sub_imports = ["linkml:types"] + _core_imports(groups)
    sub_imports.append(f"dpv:schema/extensions/{ext.slug}")
    for slug in sorted(foreign):
        if slug != ext.slug:
            entry = f"dpv:schema/extensions/{slug}"
            if entry not in sub_imports:
                sub_imports.append(entry)

    schema.update({
        "prefixes": _ext_prefixes(ext, foreign),
        "default_prefix": ext.prefix,
        "default_range": "string",
        "id_prefixes": [
            ext.prefix,
            f"dpv_{ext.prefix}",
            f"dpv_{ext.prefix}_owl",
        ],
        "imports": sub_imports,
        "subsets": {
            subset_name: {
                "description": (
                    f"Entities from the DPV `{ext.slug}/modules/{sub.name}` "
                    "submodule."
                ),
            },
        },
    })
    schema["annotations"] = {
        "dpv_version": version,
        "dpv_extension_slug": ext.slug,
        "dpv_submodule": sub.name,
        "source_ttl": _repo_rel(sub.owl_path),
        **({"source_canonical_ttl": _repo_rel(sub.can_path)}
           if sub.can_path else {}),
        "upstream_owl_namespace": ext.owl_ns,
        "upstream_canonical_namespace": ext.can_ns,
    }
    if slots:
        schema["slots"] = core._order_elements(slots, subset_name)
    if classes:
        schema["classes"] = core._order_elements(classes, subset_name)
    return core._order_keys(schema, core._SCHEMA_KEY_ORDER)


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def _parse_ttl(path: Path) -> Graph:
    g = Graph()
    g.parse(str(path), format="turtle")
    return g


_REPO_ROOT = Path(__file__).resolve().parent.parent


def _repo_rel(path: Path) -> str:
    """Return ``path`` as a repo-root-relative POSIX string when possible."""
    try:
        return path.resolve().relative_to(_REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def _write(schema: dict, path: Path) -> tuple[int, int]:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(core.dump_yaml(schema), encoding="utf-8")
    n_cls = len(schema.get("classes", {}))
    n_slt = len(schema.get("slots", {}))
    print(f"   -> {path.relative_to(path.parents[len(path.parents) - 1])}  "
          f"(classes={n_cls}, slots={n_slt})", file=sys.stderr)
    return n_cls, n_slt

# ---------------------------------------------------------------------------
# Generation
# ---------------------------------------------------------------------------

def generate(
    input_dir: Path,
    output_dir: Path,
    version: str,
    report: bool,
) -> tuple[int, int, int]:
    """Generate every extension schema. Returns (n_ext, n_cls, n_slt)."""
    extensions = discover_extensions(input_dir)
    if not extensions:
        sys.exit(f"No DPV extensions found under {input_dir}")

    # Map every core class/slot name to its semantic group so each extension
    # imports only the groups it specialises. Built from the group schemas the
    # core generator emits into the parent of ``output_dir`` (src/dpv/schema).
    core_index = _build_core_group_index(output_dir.parent)
    core_class_names = _build_core_class_names(output_dir.parent)
    if not core_index:
        print("   WARNING: no dpv_<group>.yaml schemas found next to "
              f"{output_dir}; run dpv_core_to_linkml.py first. Extensions will "
              "fall back to importing the full umbrella.", file=sys.stderr)

    total_ext = total_cls = total_slt = 0

    for ext in extensions:
        print(f"\n=== Extension: {ext.slug} ({ext.aggregate_owl.name}) ===",
              file=sys.stderr)

        # --- aggregate -----------------------------------------------------
        g_owl = _parse_ttl(ext.aggregate_owl)
        g_can = _parse_ttl(ext.aggregate_can) if ext.aggregate_can else None
        if g_can is not None:
            print(f"   enriched from canonical {ext.aggregate_can.name}",
                  file=sys.stderr)

        foreign: set[str] = set()
        classes = _extract_classes_ns(g_owl, g_can, ext, foreign, core_class_names)
        slots = _extract_slots_ns(g_owl, g_can, ext, foreign, core_class_names)
        slots, moved = core._split_collision_slots_to_attributes(classes, slots)
        if moved and report:
            print(f"   collision-prone slots moved to attributes: {moved}",
                  file=sys.stderr)
        # Strip the slug for the *own* extension; only foreign refs matter.
        foreign.discard(ext.slug)
        if ext.ontology_iri_slug:
            # Also discard the ontology IRI slug alias (it's really self-referential)
            foreign.discard(ext.ontology_iri_slug)
        foreign.discard("")  # core "dpv" slug is implicit via the dpv umbrella import

        if not classes and not slots:
            print("   (skipped - aggregate empty)", file=sys.stderr)
            continue

        groups = (_referenced_core_groups(classes, slots, core_index)
                  if core_index else None)
        agg_schema = build_aggregate_schema(
            ext,
            classes,
            slots,
            submodule_names=[s.name for s in ext.submodules],
            version=version,
            foreign=foreign,
            groups=groups,
            source=core.get_ontology_iri(g_owl),
        )
        agg_path = output_dir / ext.out_aggregate
        _write(agg_schema, agg_path)
        total_ext += 1
        total_cls += len(classes)
        total_slt += len(slots)

        if report:
            n_owl = sum(1 for s in g_owl.subjects(RDF.type, OWL.Class)
                        if isinstance(s, URIRef) and _local_of(s, ext.owl_ns))
            print(f"   coverage: owl:Class={n_owl} -> classes={len(classes)} | "
                  f"slots={len(slots)} | core-groups="
                  f"{groups if groups is not None else 'umbrella'} | "
                  f"foreign-imports={sorted(foreign)}",
                  file=sys.stderr)

        # --- submodules ---------------------------------------------------
        for sub in ext.submodules:
            g_owl_s = _parse_ttl(sub.owl_path)
            g_can_s = _parse_ttl(sub.can_path) if sub.can_path else None
            sub_foreign: set[str] = set()
            sub_classes = _extract_classes_ns(g_owl_s, g_can_s, ext, sub_foreign, core_class_names)
            sub_slots = _extract_slots_ns(g_owl_s, g_can_s, ext, sub_foreign, core_class_names)
            sub_slots, _ = core._split_collision_slots_to_attributes(
                sub_classes, sub_slots,
            )
            sub_foreign.discard(ext.slug)
            if ext.ontology_iri_slug:
                # Also discard the ontology IRI slug alias for submodules
                sub_foreign.discard(ext.ontology_iri_slug)
            sub_foreign.discard("")
            if not sub_classes and not sub_slots:
                continue
            sub_groups = (_referenced_core_groups(sub_classes, sub_slots, core_index)
                          if core_index else None)
            sub_schema = build_submodule_schema(
                ext, sub, sub_classes, sub_slots, version,
                foreign=sub_foreign,
                groups=sub_groups,
                source=core.get_ontology_iri(g_owl_s),
            )
            # Collect submodule subsets too.
            sub_path = output_dir / ext.out_dir / f"{sub.name}.yaml"
            _write(sub_schema, sub_path)

    return total_ext, total_cls, total_slt


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    default_input = repo_root / "upstream-releases" / "dpv"
    default_output = repo_root / "src" / "dpv" / "schema" / "extensions"

    parser = argparse.ArgumentParser(
        description=("Generate LinkML schemas for every DPV 2.3 extension "
                     "vendored under upstream-releases/dpv/."),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--version", default=None,
        help="Override the DPV version (default: auto-detect from core).",
    )
    parser.add_argument(
        "-i", "--input-dir", type=Path, default=default_input,
        help=("Directory containing the vendored DPV upstream tree "
              "(default: upstream-releases/dpv/)."),
    )
    parser.add_argument(
        "-o", "--output-dir", type=Path, default=default_output,
        help=f"Output directory for extension schemas "
             f"(default: {default_output.relative_to(repo_root)}).",
    )
    parser.add_argument(
        "--report", action="store_true",
        help="Print per-extension coverage summary to stderr.",
    )
    args = parser.parse_args()

    if not args.input_dir.exists():
        parser.error(f"Input directory does not exist: {args.input_dir}")

    version = args.version
    if not version:
        # Re-use the core detection logic against the core dpv/ subdir.
        core_dir = args.input_dir / "dpv"
        if core_dir.exists():
            version = core.detect_version(core_dir)
    if not version:
        parser.error(
            "Could not detect DPV version; pass --version explicitly."
        )
    print(f"DPV version: {version}", file=sys.stderr)
    print(f"Input:  {args.input_dir}", file=sys.stderr)
    print(f"Output: {args.output_dir}", file=sys.stderr)

    n_ext, n_cls, n_slt = generate(
        args.input_dir, args.output_dir, version, args.report,
    )
    print(
        f"\nDone. Extensions: {n_ext}, "
        f"classes (sum): {n_cls}, slots (sum): {n_slt}.",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
