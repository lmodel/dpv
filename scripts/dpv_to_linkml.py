#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["rdflib>=7", "pyyaml>=6"]
# ///
"""Turn the DPV 2.3 Turtle files under upstream/ into this project's schema and catalogue.

DPV states each concept as a class, as a SKOS concept and as an instance of a broader
concept: ``dpv:Marketing a rdfs:Class, skos:Concept, dpv:Purpose``. So a DPV term reads as
a record, and the concepts its terms are instances of read as kinds. This script writes the
files that say so:

- ``--schema`` writes ``src/dpv/schema/dpv_terms.yaml``, with one slot per DPV property and
  the classes that hold them, and one module of kinds per namespace family.
- ``--catalogue`` writes ``src/dpv/data/``, with one file per namespace family, every term
  a record under its own IRI, and the examples as data.
- ``--mappings`` writes ``src/dpv/mappings/`` from DPV's own two mapping files.

The script makes no judgement beyond the tables below, and it stops on a predicate it does
not know, so a new edition cannot lose a fact silently.
"""

from __future__ import annotations

import argparse
import collections
import csv
import logging
import re
import sys
import unicodedata
from functools import cache
from pathlib import Path

import rdflib
import yaml
from rdflib import OWL, RDF, RDFS, SKOS, BNode, Graph, Literal, Namespace, URIRef
from rdflib.compare import to_canonical_graph

# Keep each literal's lexical form as DPV writes it. The examples hold a few that are not
# valid for their datatype, such as a duration of "10" and a date with one dash, and rdflib
# would otherwise rewrite each. It still logs a traceback for each when it parses them, which
# is noise about DPV's files and not about this script, so those messages are kept down.
rdflib.NORMALIZE_LITERALS = False
logging.getLogger("rdflib.term").setLevel(logging.ERROR)

ROOT = Path(__file__).resolve().parent.parent
UPSTREAM = ROOT / "upstream"
SCHEMA_DIR = ROOT / "src" / "dpv" / "schema"
DATA_DIR = ROOT / "src" / "dpv" / "data"
MAPPINGS_DIR = ROOT / "src" / "dpv" / "mappings"
EDITION = "2.3"
VOCABULARIES = UPSTREAM / EDITION

BIBO = Namespace("http://purl.org/ontology/bibo/")
DCAM = Namespace("http://purl.org/dc/dcam/")
DCTERMS = Namespace("http://purl.org/dc/terms/")
DEX = Namespace("https://w3id.org/dpv/examples#")
DPV = Namespace("https://w3id.org/dpv#")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
ORG = Namespace("http://www.w3.org/ns/org#")
PROF = Namespace("http://www.w3.org/ns/dx/prof/")
SCHEMA_ORG = Namespace("https://schema.org/")
SCORO = Namespace("http://purl.org/spar/scoro/")
SW = Namespace("http://www.w3.org/2003/06/sw-vocab-status/ns#")
TIME = Namespace("http://www.w3.org/2006/time#")
VANN = Namespace("http://purl.org/vocab/vann/")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")

OWN = "https://w3id.org/lmodel/dpv/"
AGENT = OWN + "agents/"

# Prefixes this project binds beside the ones DPV's files bind. DPV's example files use
# ex:, exA:, exB: and a bare colon but declare none of them. DPV's page says ex: stands for
# http://example.com#, and this project takes the other three from it.
EXAMPLE_PREFIXES = {
    "ex": "http://example.com#",
    "exA": "http://example.com/exA#",
    "exB": "http://example.com/exB#",
    "exd": "http://example.com/default#",
}
OWN_PREFIXES = {
    "dpv_linkml": OWN,
    "dpv_agent": AGENT,
    "linkml": "https://w3id.org/linkml/",
    **EXAMPLE_PREFIXES,
    # Named in the examples beside the terms, and bound by no vocabulary file.
    "nace": "http://data.europa.eu/ux2/nace2.1/",
}
# DPV's dct: is the family's dcterms:. DPV's schema: names https://schema.org/, and LinkML's
# types bind schema: to the http address, which a schema may not bind otherwise.
RENAMED_PREFIXES = {"dct": "dcterms", "schema": "sdo"}
# rdflib binds these itself. No value of the catalogue or the examples uses them.
UNUSED_PREFIXES = frozenset(
    {
        "brick",
        "csvw",
        "dc",
        "dcat2",
        "dcmitype",
        "doap",
        "geo",
        "qb",
        "sh",
        "sosa",
        "ssn",
        "void",
        "wgs",
        "xml",
    }
)

# Namespace families, in the order the data files and modules list them. A term belongs to
# the first family whose namespace start its IRI matches, and everything else, such as the
# Dublin Core properties DPV adopts, to the core.
FAMILIES = (
    ("examples", ("https://w3id.org/dpv/examples",)),
    ("pd", ("https://w3id.org/dpv/pd",)),
    ("tech", ("https://w3id.org/dpv/tech",)),
    ("ai", ("https://w3id.org/dpv/ai",)),
    ("risk", ("https://w3id.org/dpv/risk",)),
    ("justifications", ("https://w3id.org/dpv/justifications",)),
    ("loc", ("https://w3id.org/dpv/loc",)),
    ("legal", ("https://w3id.org/dpv/legal", "https://w3id.org/dpv/rights")),
    ("sector", ("https://w3id.org/dpv/sector",)),
    ("standards", ("https://w3id.org/dpv/standards",)),
)
FAMILY_TITLES = {
    "agents": "the contributors",
    "examples": "the examples",
    "core": "the core",
    "pd": "personal data",
    "tech": "technology",
    "ai": "artificial intelligence",
    "risk": "risk",
    "justifications": "justifications",
    "loc": "locations",
    "legal": "laws and authorities",
    "sector": "sectors",
    "standards": "standards",
}

# Types every concept and every property holds, which a record's class already says.
CONCEPT_TYPES = frozenset({RDFS.Class, SKOS.Concept})
PROPERTY_TYPES = frozenset({RDF.Property, SKOS.Concept})

# A property with no rangeIncludes, or one naming a literal type, whose value is text. DPV's
# examples write each of those without a range as a literal, and the Dublin Core ones are
# literals in DCMI's own definitions. Every other property's value names a resource.
TEXT_PROPERTIES = frozenset(
    {
        DPV.hasAddress,
        DPV.hasContact,
        DPV.hasIdentifier,
        DPV.hasName,
        DPV.isIndicatedAtTime,
        URIRef("https://w3id.org/dpv/standards/ieee/7012#hasHumanDescription"),
        DCTERMS.created,
        DCTERMS.dateAccepted,
        DCTERMS.dateSubmitted,
        DCTERMS.description,
        DCTERMS["format"],
        DCTERMS.identifier,
        DCTERMS.modified,
        DCTERMS["title"],
        DCTERMS.valid,
    }
)
LITERAL_RANGES = frozenset({XSD.string, XSD.anyURI})

# skos:sameAs is no SKOS term. It is what DPV states, so the slot keeps it.
SAME_AS = URIRef("http://www.w3.org/2004/02/skos/core#sameAs")

# Predicates that are not DPV properties and that a term states, by slot. Their slots are
# declared in the term classes below, or in dpv_core.yaml for those several classes share.
TERM_REFERENCES = {
    SKOS.broader: "broader",
    SKOS.related: "related",
    SKOS.inScheme: "inScheme",
    SAME_AS: "sameAs",
    RDFS.isDefinedBy: "isDefinedBy",
    RDFS.subClassOf: "subClassOf",
    VANN.example: "example",
}
PROPERTY_REFERENCES = {
    RDFS.subPropertyOf: "subPropertyOf",
    DCAM.domainIncludes: "domainIncludes",
    DCAM.rangeIncludes: "rangeIncludes",
}
# A term's facts a record does not hold, because something else states them.
# schema:domainIncludes and schema:rangeIncludes repeat the dcam: pair on every property,
# and skos:narrower is what derived_narrower() gives. load_terms() stops if either stops
# being true.
DERIVED_PREDICATES = frozenset(
    {SCHEMA_ORG.domainIncludes, SCHEMA_ORG.rangeIncludes, SKOS.narrower}
)

# The vocabularies' own facts, by slot. A vocabulary's prof:hasResource lists the
# serialisations DPV's site publishes, not the vocabulary, so neither it nor the descriptors
# it names reach the catalogue.
VOCABULARY_TEXT = {
    DCTERMS.bibliographicCitation: "bibliographicCitation",
    DCTERMS.description: "description",
    DCTERMS.identifier: "identifier",
    DCTERMS["title"]: "title",
    BIBO.doi: "doi",
    BIBO.status: "bibo_status",
    VANN.preferredNamespacePrefix: "preferredNamespacePrefix",
    VANN.preferredNamespaceUri: "preferredNamespaceUri",
    URIRef(str(RDFS) + "Label"): "rdfs_Label",
    OWL.versionInfo: "versionInfo",
    SCHEMA_ORG.version: "schema_version",
    DCTERMS.created: "created",
    DCTERMS.issued: "issued",
    DCTERMS.modified: "modified",
    DCTERMS.conformsTo: "conformsTo",
    DCTERMS.source: "source",
}
VOCABULARY_REFERENCES = {
    DCTERMS.license: "license",
    DCTERMS.publisher: "publisher",
    OWL.versionIRI: "versionIRI",
    PROF.isProfileOf: "isProfileOf",
    FOAF.logo: "logo",
}
VOCABULARY_LEFT_OUT = frozenset({PROF.hasResource, PROF.hasArtifact, PROF.hasRole})
DESCRIPTOR_TYPE = PROF.ResourceDescriptor

# What the rest of an example's record, its description in dex.ttl, states.
EXAMPLE_TEXT = {
    DCTERMS["title"]: "title",
    DCTERMS.description: "description",
    DCTERMS["format"]: "format",
    DCTERMS.source: "source",
}

# Upstream example files whose Turtle does not parse, whatever the prefixes. A record names
# the fault, and it holds no resources. issues/87 reports them to the Community Group.
TURTLE_FAULTS = {
    "E0030": "A semicolon is missing after `odrl:profile ex:`.",
    "E0059": "A semicolon is missing after a nested personal data block.",
    "E0061": "A closing bracket follows the last statement without its opening one.",
}


def local(iri) -> str:
    """The part of an IRI after its namespace."""
    text = str(iri)
    return re.split(r"[#/]", text)[-1]


def family_of(iri) -> str:
    """The namespace family of a term or a vocabulary."""
    text = str(iri)
    for name, starts in FAMILIES:
        if text.startswith(starts):
            return name
    return "core"


@cache
def load() -> Graph:
    """Every vocabulary's Turtle, and dex.ttl, as one graph. A vocabulary such as
    legal/legal.ttl repeats triples of others, and the union holds each once."""
    graph = Graph()
    for path in sorted(VOCABULARIES.rglob("*.ttl")):
        graph.parse(path, format="turtle")
    return graph


@cache
def prefixes() -> dict[str, str]:
    """The prefix map the schema and the data use: DPV's, as its files bind them, with
    dct: as dcterms:, and this project's own."""
    graph = load()
    found = {}
    for name, namespace in graph.namespaces():
        if name and name not in UNUSED_PREFIXES:
            found[RENAMED_PREFIXES.get(name, name)] = str(namespace)
    found.update(OWN_PREFIXES)
    return dict(sorted(found.items()))


@cache
def _namespaces() -> tuple[tuple[str, str], ...]:
    pairs = sorted(prefixes().items(), key=lambda item: -len(item[1]))
    return tuple((namespace, name) for name, namespace in pairs)


def curie(iri) -> str:
    """An IRI as a CURIE under the longest namespace that holds it, or whole when none
    does. A bare namespace, such as https://w3id.org/dpv#, keeps its empty local part."""
    text = str(iri)
    for namespace, name in _namespaces():
        if text.startswith(namespace):
            return f"{name}:{text[len(namespace) :]}"
    return text


def expand(value: str) -> URIRef:
    """A CURIE, or a whole IRI, as the IRI it stands for."""
    head, _, tail = value.partition(":")
    namespace = prefixes().get(head)
    return URIRef(namespace + tail) if namespace else URIRef(value)


def concept_subjects(graph: Graph) -> set[URIRef]:
    """Every term the vocabularies state as a concept and not as a property."""
    concepts = set(graph.subjects(RDF.type, SKOS.Concept))
    return {term for term in concepts if (term, RDF.type, RDF.Property) not in graph}


def property_subjects(graph: Graph) -> set[URIRef]:
    """Every property the vocabularies state."""
    return set(graph.subjects(RDF.type, RDF.Property))


def term_subjects(graph: Graph) -> set[URIRef]:
    return concept_subjects(graph) | property_subjects(graph)


def vocabulary_subjects(graph: Graph) -> set[URIRef]:
    return set(graph.subjects(RDF.type, OWL.Ontology))


def scheme_subjects(graph: Graph) -> set[URIRef]:
    return set(graph.subjects(RDF.type, SKOS.ConceptScheme))


def example_subjects(graph: Graph) -> set[URIRef]:
    return set(graph.subjects(RDF.type, DEX.Example))


@cache
def _property_slot_names() -> dict[URIRef, str]:
    """Each property's slot name. A slot keeps the property's local name, so a record's
    keys are DPV's. Where two namespaces define one name, the core keeps it, and any other
    takes its namespace's prefix before an underscore."""
    graph = load()
    props = sorted(property_subjects(graph), key=str)
    by_local = collections.defaultdict(list)
    for prop in props:
        by_local[local(prop)].append(prop)
    names = {}
    for name, sharing in by_local.items():
        for prop in sharing:
            if len(sharing) == 1 or str(prop).startswith(str(DPV)):
                names[prop] = name
            else:
                prefix = curie(prop).split(":", 1)[0]
                names[prop] = f"{prefix.replace('-', '_')}_{name}"
    return names


def slot_name(prop) -> str:
    return _property_slot_names()[prop]


def is_text_property(graph: Graph, prop) -> bool:
    """Whether a property's value is text, by its rangeIncludes or the table above."""
    if prop in TEXT_PROPERTIES:
        return True
    ranges = set(graph.objects(prop, DCAM.rangeIncludes))
    return bool(ranges) and ranges <= LITERAL_RANGES


def _kind_terms(graph: Graph, term) -> list[URIRef]:
    fixed = PROPERTY_TYPES if (term, RDF.type, RDF.Property) in graph else CONCEPT_TYPES
    return sorted((o for o in graph.objects(term, RDF.type) if o not in fixed), key=str)


@cache
def kind_counts() -> dict[URIRef, int]:
    """Each kind, and how many concepts are instances of it. A kind is a type a concept
    holds beyond rdfs:Class and skos:Concept."""
    graph = load()
    counts = collections.Counter()
    for term in concept_subjects(graph):
        counts.update(_kind_terms(graph, term))
    return dict(counts)


@cache
def kind_class_names() -> dict[URIRef, str]:
    """Each kind's class name. It takes a Dpv prefix, and where two namespaces define one
    kind, the core keeps the short name and any other takes its namespace too."""
    by_local = collections.defaultdict(list)
    for kind in kind_counts():
        by_local[local(kind)].append(kind)
    names = {}
    for name, sharing in by_local.items():
        for kind in sharing:
            if len(sharing) == 1 or str(kind).startswith(str(DPV)):
                names[kind] = f"Dpv{name}"
            else:
                prefix = curie(kind).split(":", 1)[0]
                camel = "".join(part.capitalize() for part in prefix.split("-"))
                names[kind] = f"Dpv{camel}{name}"
    return names


def kind_parent(graph: Graph, kind: URIRef) -> URIRef | None:
    """The nearest kind above a kind along skos:broader, breadth first, or None. The IRI's
    order settles a tie between two at one distance."""
    kinds = kind_counts()
    seen = {kind}
    frontier = [kind]
    while frontier:
        above = sorted(
            {p for node in frontier for p in graph.objects(node, SKOS.broader)} - seen,
            key=str,
        )
        for parent in above:
            if parent in kinds:
                return parent
        seen.update(above)
        frontier = above
    return None


def _sorted_refs(graph: Graph, subject, predicate) -> list[str]:
    return sorted(curie(o) for o in graph.objects(subject, predicate))


def _split_by_language(graph: Graph, subject, predicate, name, record) -> None:
    """Text in English, or with no language, under the slot's name, and German beside it.
    Only de-gdng states German. A slot holding two values per language stops the script."""
    values = collections.defaultdict(list)
    for node in graph.objects(subject, predicate):
        values[node.language or "en"].append(str(node))
    unknown = set(values) - {"en", "de"}
    if unknown or any(len(found) > 1 for found in values.values()):
        raise ValueError(f"{subject} holds {predicate} in {dict(values)}")
    if "en" in values:
        record[name] = values["en"][0]
    if "de" in values:
        record[f"{name}_de"] = values["de"][0]


def agent_id(graph: Graph, node: BNode) -> str:
    """A contributor as a CURIE. DPV's blank node labels read person-<name> and org-<name>,
    and a parser drops them, so the id takes the same form from the node's name."""
    name = graph.value(node, FOAF.name)
    if name is None:
        raise ValueError(f"an agent has no name: {node}")
    ascii_name = (
        unicodedata.normalize("NFKD", str(name)).encode("ascii", "ignore").decode()
    )
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_name.lower()).strip("-")
    role = "org" if (node, RDF.type, FOAF.Organization) in graph else "person"
    return f"dpv_agent:{role}-{slug}"


def _agents(graph: Graph, subject, predicate) -> list[str]:
    return sorted(agent_id(graph, node) for node in graph.objects(subject, predicate))


def _web_page(graph: Graph, node: BNode) -> dict:
    types = set(graph.objects(node, RDF.type))
    if types != {SCHEMA_ORG.WebPage}:
        raise ValueError(f"a source of another type: {types}")
    page = {"page_name": str(graph.value(node, SCHEMA_ORG.name))}
    url = graph.value(node, SCHEMA_ORG.url)
    if url is not None:
        page["url"] = str(url)
    return page


def _interval(graph: Graph, node: BNode) -> dict:
    types = set(graph.objects(node, RDF.type))
    if types != {TIME.ProperInterval}:
        raise ValueError(f"a period of another type: {types}")
    interval = {}
    for slot, predicate in (
        ("hasBeginning", TIME.hasBeginning),
        ("hasEnd", TIME.hasEnd),
    ):
        instant = graph.value(node, predicate)
        if instant is not None:
            interval[slot] = str(graph.value(instant, TIME.inXSDDate))
    return interval


def _sources(graph: Graph, term, record) -> None:
    text = []
    pages = []
    for node in graph.objects(term, DCTERMS.source):
        if isinstance(node, BNode):
            pages.append(_web_page(graph, node))
        else:
            text.append(str(node))
    if text:
        record["source"] = sorted(text)
    if pages:
        record["source_page"] = sorted(
            pages, key=lambda p: (p["page_name"], p.get("url", ""))
        )


def term_properties(graph: Graph) -> set[URIRef]:
    """The properties at least one term states as a fact of its own."""
    props = property_subjects(graph)
    return {
        predicate
        for term in term_subjects(graph)
        for predicate in graph.predicates(term, None)
        if predicate in props and predicate not in _HANDLED
    }


# Predicates whose slot a term's record names apart from DPV's own properties. A few of
# them, such as dct:created, DPV also lists as properties.
_HANDLED = frozenset(
    {
        RDF.type,
        SKOS.prefLabel,
        SKOS.definition,
        SKOS.scopeNote,
        SKOS.exactMatch,
        RDF.value,
        DCTERMS.contributor,
        DCTERMS.created,
        DCTERMS.modified,
        DCTERMS.source,
        DCTERMS.temporal,
        FOAF.homepage,
        SW.term_status,
    }
    | set(TERM_REFERENCES)
    | set(PROPERTY_REFERENCES)
    | DERIVED_PREDICATES
)


def _record(graph: Graph, term, is_property: bool, used: set[URIRef]) -> dict:
    """One term as a record, its keys in a fixed order."""
    record = {"id": curie(term)}
    kinds = _kind_terms(graph, term)
    if kinds:
        record["rdf_type"] = [curie(k) for k in kinds]
    _split_by_language(graph, term, SKOS.prefLabel, "prefLabel", record)
    _split_by_language(graph, term, SKOS.definition, "definition", record)
    notes = sorted(str(n) for n in graph.objects(term, SKOS.scopeNote))
    if notes:
        record["scopeNote"] = notes
    for predicate, name in TERM_REFERENCES.items():
        found = _sorted_refs(graph, term, predicate)
        if found:
            record[name] = found
    if is_property:
        for predicate, name in PROPERTY_REFERENCES.items():
            found = _sorted_refs(graph, term, predicate)
            if found:
                record[name] = found
    matches = sorted(str(n) for n in graph.objects(term, SKOS.exactMatch))
    if matches:
        record["exactMatch"] = matches
    status = graph.value(term, SW.term_status)
    if status is not None:
        record["term_status"] = str(status)
    created = sorted(str(n) for n in graph.objects(term, DCTERMS.created))
    if created:
        record["created"] = created
    modified = graph.value(term, DCTERMS.modified)
    if modified is not None:
        record["modified"] = str(modified)
    contributors = _agents(graph, term, DCTERMS.contributor)
    if contributors:
        record["contributor"] = contributors
    _sources(graph, term, record)
    homepage = graph.value(term, FOAF.homepage)
    if homepage is not None:
        record["homepage"] = str(homepage)
    value = graph.value(term, RDF.value)
    if value is not None:
        record["value"] = float(str(value))
    temporal = graph.value(term, DCTERMS.temporal)
    if temporal is not None:
        record["temporal"] = _interval(graph, temporal)
    for prop in sorted(used, key=slot_name):
        found = list(graph.objects(term, prop))
        if not found:
            continue
        if is_text_property(graph, prop):
            record[slot_name(prop)] = sorted(str(n) for n in found)
        else:
            record[slot_name(prop)] = sorted(curie(n) for n in found)
    return record


def _check_term_predicates(graph: Graph) -> None:
    """Stop on a predicate no table names, so a new edition cannot lose a fact."""
    props = property_subjects(graph)
    known = _HANDLED | props
    for term in term_subjects(graph):
        for predicate in graph.predicates(term, None):
            if predicate not in known:
                raise ValueError(f"{term} states {predicate}, which no table names")


def derived_narrower(graph: Graph) -> set[tuple[URIRef, URIRef]]:
    """The skos:narrower pairs the location vocabulary states, from what its records hold.

    Only loc states skos:narrower, in two ways. Each loc:non-X is every country but X, and
    but X's own member countries when X is no country itself. Every other pair is the
    inverse of a skos:broader, but for the editions of a union below it.
    """
    loc = "https://w3id.org/dpv/loc#"
    countries = set(graph.subjects(RDF.type, DPV.Country))
    found = set()
    for child, parent in graph.subject_objects(SKOS.broader):
        if str(parent).startswith(loc) and (child, parent) not in _UNION_EDITIONS:
            found.add((parent, child))
    for region, inverse in graph.subject_objects(DPV.hasInverseJurisdiction):
        left_out = {region}
        if region not in countries:
            left_out = {c for p, c in found if p == region and c in countries}
        found.update((inverse, country) for country in countries - left_out)
    return found


_LOC = Namespace("https://w3id.org/dpv/loc#")
# Each union's editions say skos:broader the union with no skos:narrower to match.
_UNION_EDITIONS = frozenset(
    {
        (_LOC.EU27, _LOC.EU),
        (_LOC.EU28, _LOC.EU),
        (_LOC.EEA30, _LOC.EEA),
        (_LOC.EEA31, _LOC.EEA),
    }
)


def stated_narrower(graph: Graph) -> set[tuple[URIRef, URIRef]]:
    return set(graph.subject_objects(SKOS.narrower))


def _check_derived(graph: Graph) -> None:
    if derived_narrower(graph) != stated_narrower(graph):
        raise ValueError("skos:narrower no longer follows what the records hold")
    for dcam, schema_org in (
        (DCAM.domainIncludes, SCHEMA_ORG.domainIncludes),
        (DCAM.rangeIncludes, SCHEMA_ORG.rangeIncludes),
    ):
        if set(graph.subject_objects(dcam)) != set(graph.subject_objects(schema_org)):
            raise ValueError(f"{schema_org} no longer repeats {dcam}")


def _vocabulary(graph: Graph, subject) -> dict:
    """One vocabulary's own facts."""
    record = {"id": str(subject)}
    known = (
        set(VOCABULARY_TEXT)
        | set(VOCABULARY_REFERENCES)
        | VOCABULARY_LEFT_OUT
        | {RDF.type, DCTERMS.contributor, DCTERMS.creator, DCTERMS["format"]}
    )
    for predicate in graph.predicates(subject, None):
        if predicate not in known:
            raise ValueError(f"{subject} states {predicate}, which no table names")
    for predicate, name in VOCABULARY_TEXT.items():
        found = sorted(str(n) for n in graph.objects(subject, predicate))
        if not found:
            continue
        record[name] = (
            found if name in ("conformsTo", "created", "source") else found[0]
        )
    for predicate, name in VOCABULARY_REFERENCES.items():
        found = sorted(str(n) for n in graph.objects(subject, predicate))
        if not found:
            continue
        record[name] = found if name == "isProfileOf" else found[0]
    for predicate, name in (
        (DCTERMS.contributor, "contributor"),
        (DCTERMS.creator, "creator"),
    ):
        found = _agents(graph, subject, predicate)
        if found:
            record[name] = found
    return record


def _agent_records(graph: Graph) -> list[dict]:
    """Every contributor and each organization, once, whichever files state them."""
    records = {}
    nodes = list(graph.subjects(RDF.type, FOAF.Person)) + list(
        graph.subjects(RDF.type, FOAF.Organization)
    )
    for node in nodes:
        identifier = agent_id(graph, node)
        record = {"id": identifier, "name": str(graph.value(node, FOAF.name))}
        orcid = graph.value(node, SCORO.hasORCID)
        if orcid is not None:
            record["hasORCID"] = str(orcid)
        homepage = graph.value(node, FOAF.homepage)
        if homepage is not None:
            record["homepage"] = str(homepage)
        member = sorted(agent_id(graph, o) for o in graph.objects(node, ORG.memberOf))
        if member:
            record["memberOf"] = member
        if identifier in records and records[identifier] != record:
            merged = dict(records[identifier])
            for key, value in record.items():
                if key == "memberOf":
                    merged[key] = sorted({*merged.get(key, []), *value})
                elif merged.setdefault(key, value) != value:
                    raise ValueError(f"{identifier} differs in {key} across files")
            record = merged
        records[identifier] = record
    return [records[key] for key in sorted(records)]


def _example_preamble() -> str:
    """The prefixes an example file needs, since DPV's files declare none. A bare colon
    takes the namespace EXAMPLE_PREFIXES calls exd:."""
    lines = [f"@prefix {name}: <{ns}> ." for name, ns in prefixes().items()]
    lines.append("@prefix dct: <http://purl.org/dc/terms/> .")
    lines.append("@prefix schema: <https://schema.org/> .")
    lines.append(f"@prefix : <{EXAMPLE_PREFIXES['exd']}> .")
    return "\n".join(lines) + "\n"


def example_graph(name: str) -> Graph | None:
    """An example's statements, with canonical blank nodes, or None when the file holds a
    fault TURTLE_FAULTS names. A file that fails unnamed stops the script."""
    text = (UPSTREAM / "examples" / f"{name}.ttl").read_text(encoding="utf-8")
    graph = Graph()
    try:
        graph.parse(data=_example_preamble() + text, format="turtle")
    except Exception as err:
        if name in TURTLE_FAULTS:
            return None
        raise ValueError(f"{name} does not parse: {err}") from err
    if name in TURTLE_FAULTS:
        raise ValueError(f"{name} now parses, so TURTLE_FAULTS is out of date")
    return to_canonical_graph(graph)


def _resource_slots(vocabulary: Graph) -> dict[URIRef, tuple[str, bool]]:
    """What a resource's record holds directly: each property by slot and whether its value
    is text, and the few other predicates DPV's examples state."""
    slots = {
        prop: (slot_name(prop), is_text_property(vocabulary, prop))
        for prop in property_subjects(vocabulary)
        # A period is an inlined value of its own, which a reference cannot name.
        if prop != DCTERMS.temporal
    }
    for predicate, name in (
        (SKOS.broader, "broader"),
        (RDFS.subClassOf, "subClassOf"),
    ):
        slots[predicate] = (name, False)
    for predicate, name in (
        (SKOS.prefLabel, "prefLabel"),
        (SKOS.definition, "definition"),
        (SKOS.scopeNote, "scopeNote"),
    ):
        slots[predicate] = (name, True)
    return slots


# The single-valued slots of the term classes, which a resource cannot repeat, by predicate.
_SINGLE = {
    "prefLabel": SKOS.prefLabel,
    "definition": SKOS.definition,
    "title": DCTERMS["title"],
    "description": DCTERMS.description,
    "identifier": DCTERMS.identifier,
    "modified": DCTERMS.modified,
}


def _literal_statement(predicate, node: Literal) -> dict:
    statement = {"predicate": curie(predicate), "literal": str(node)}
    if node.datatype is not None:
        statement["datatype"] = curie(node.datatype)
    if node.language:
        statement["language"] = node.language
    return statement


def resource_records(name: str, graph: Graph, vocabulary: Graph) -> list[dict]:
    """An example's statements, as one record per subject. A blank node takes a label by
    its canonical order, and a value that does not fit its slot's form, or a predicate with
    no slot, becomes one of the record's `statements`."""
    labels = {}
    nodes = {n for t in graph for n in (t[0], t[2]) if isinstance(n, BNode)}
    for index, node in enumerate(sorted(nodes, key=str), start=1):
        labels[node] = f"_:{name}-{index}"

    def ref(node) -> str:
        return labels[node] if isinstance(node, BNode) else curie(node)

    slots = _resource_slots(vocabulary)
    records = []
    subjects = sorted(set(graph.subjects()), key=ref)
    for subject in subjects:
        record = {"id": ref(subject)}
        rows = collections.defaultdict(list)
        statements = []
        for predicate, node in graph.predicate_objects(subject):
            if predicate == RDF.type:
                rows["rdf_type"].append(ref(node))
                continue
            slot = slots.get(predicate)
            literal = isinstance(node, Literal)
            plain = (
                literal
                and node.language is None
                and (node.datatype is None or node.datatype == XSD.string)
            )
            if slot is None or (slot[1] and not plain) or (not slot[1] and literal):
                if literal:
                    statements.append(_literal_statement(predicate, node))
                else:
                    statements.append(
                        {"predicate": curie(predicate), "reference": ref(node)}
                    )
                continue
            rows[slot[0]].append(str(node) if literal else ref(node))
        for key in sorted(rows):
            values = sorted(rows[key])
            if key in _SINGLE:
                statements += [
                    {"predicate": curie(_SINGLE[key]), "literal": extra}
                    for extra in values[1:]
                ]
                record[key] = values[0]
            else:
                record[key] = values
        if statements:
            record["statements"] = sorted(
                statements,
                key=lambda s: (
                    s["predicate"],
                    s.get("reference", ""),
                    s.get("literal", ""),
                ),
            )
        records.append(record)
    return records


def _example_record(graph: Graph, subject) -> dict:
    record = {"id": curie(subject)}
    known = set(EXAMPLE_TEXT) | {
        RDF.type,
        DCTERMS.contributor,
        DCTERMS.created,
        DCTERMS.modified,
        DCTERMS.subject,
        DCTERMS.temporal,
        SW.term_status,
    }
    for predicate in graph.predicates(subject, None):
        if predicate not in known:
            raise ValueError(f"{subject} states {predicate}, which no table names")
    for predicate, name in EXAMPLE_TEXT.items():
        value = graph.value(subject, predicate)
        if value is not None:
            record[name] = [str(value)] if name in ("format", "source") else str(value)
    subjects = _sorted_refs(graph, subject, DCTERMS.subject)
    if subjects:
        record["subject"] = subjects
    created = sorted(str(n) for n in graph.objects(subject, DCTERMS.created))
    if created:
        record["created"] = created
    modified = graph.value(subject, DCTERMS.modified)
    if modified is not None:
        record["modified"] = str(modified)
    temporal = graph.value(subject, DCTERMS.temporal)
    if temporal is not None:
        record["temporal"] = _interval(graph, temporal)
    contributors = _agents(graph, subject, DCTERMS.contributor)
    if contributors:
        record["contributor"] = contributors
    status = graph.value(subject, SW.term_status)
    if status is not None:
        record["term_status"] = str(status)
    name = local(subject)
    if name in TURTLE_FAULTS:
        record["turtle_fault"] = TURTLE_FAULTS[name]
    else:
        statements = example_graph(name)
        if statements is not None and len(statements):
            record["resources"] = resource_records(name, statements, graph)
    return record


def catalogues(graph: Graph) -> dict[str, dict]:
    """Every data file's content, by family: each vocabulary, concept scheme, concept and
    property under its namespace family, then one file each of agents and of examples."""
    _check_term_predicates(graph)
    _check_derived(graph)
    used = term_properties(graph)
    documents = {
        name: {"edition": EDITION, "family": name}
        for name in ("core", *(family for family, _ in FAMILIES))
    }
    documents["agents"] = {
        "edition": EDITION,
        "family": "agents",
        "agents": _agent_records(graph),
    }
    for subject in sorted(vocabulary_subjects(graph), key=str):
        documents[family_of(subject)].setdefault("vocabularies", []).append(
            _vocabulary(graph, subject)
        )
    for subject in sorted(scheme_subjects(graph), key=str):
        documents[family_of(subject)].setdefault("concept_schemes", []).append(
            {"id": curie(subject)}
        )
    for subject in sorted(concept_subjects(graph), key=curie):
        documents[family_of(subject)].setdefault("concepts", []).append(
            _record(graph, subject, False, used)
        )
    for subject in sorted(property_subjects(graph), key=curie):
        documents[family_of(subject)].setdefault("properties", []).append(
            _record(graph, subject, True, used)
        )
    documents["examples"]["examples"] = [
        _example_record(graph, subject)
        for subject in sorted(example_subjects(graph), key=curie)
    ]
    return documents


def _property_slot(graph: Graph, prop) -> dict:
    """One DPV property as a slot, under its own IRI, in DPV's own label and definition."""
    slot: dict = {"title": str(graph.value(prop, SKOS.prefLabel))}
    definition = graph.value(prop, SKOS.definition)
    slot["description"] = (
        str(definition) if definition is not None else f"The property {curie(prop)}."
    )
    slot["slot_uri"] = curie(prop)
    if is_text_property(graph, prop):
        slot["range"] = "string"
    else:
        slot["range"] = "DpvTerm"
        slot["pattern"] = REFERENCE_PATTERN
        slot["inlined"] = False
    slot["multivalued"] = True
    notes = sorted(str(n) for n in graph.objects(prop, SKOS.scopeNote))
    if notes:
        slot["comments"] = notes
    # A slot's parent must take the same form of value, or generators find two ranges for
    # one slot. DPV's subPropertyOf stays whole in the property's record either way.
    parents = sorted(
        slot_name(p)
        for p in graph.objects(prop, RDFS.subPropertyOf)
        if p in _property_slot_names()
        and is_text_property(graph, p) == is_text_property(graph, prop)
    )
    if parents:
        slot["is_a"] = parents[0]
        if parents[1:]:
            slot["mixins"] = parents[1:]
    return slot


# What a value naming a resource looks like: a CURIE, a whole IRI or a labelled blank node.
REFERENCE_PATTERN = r"^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$"


def _core_slots() -> set[str]:
    """The slots dpv_core.yaml declares, which the generated module must not repeat."""
    module = yaml.safe_load((SCHEMA_DIR / "dpv_core.yaml").read_text(encoding="utf-8"))
    return set(module.get("slots", {}))


def terms_module(graph: Graph) -> dict:
    """dpv_terms.yaml: the classes that hold a term, and a slot per property."""
    slots = {}
    for prop in sorted(property_subjects(graph), key=slot_name):
        slots[slot_name(prop)] = _property_slot(graph, prop)
    core = _core_slots()
    used_names = sorted(slot_name(p) for p in term_properties(graph))
    all_names = sorted(slots)
    for name in core:
        slots.pop(name, None)
    slots.update(_structural_slots())
    term_slots = [
        "id",
        "rdf_type",
        "prefLabel",
        "prefLabel_de",
        "definition",
        "definition_de",
        "scopeNote",
        "broader",
        "related",
        "inScheme",
        "sameAs",
        "isDefinedBy",
        "subClassOf",
        "example",
        "exactMatch",
        "term_status",
        "created",
        "modified",
        "contributor",
        "source",
        "source_page",
        "homepage",
        "value",
        "temporal",
    ]
    classes = {
        "DpvTerm": {
            "title": "Term",
            "abstract": True,
            "description": "One thing DPV's vocabularies state, or a thing a use case describes "
            "with them, as a record under its own IRI.",
            "slots": term_slots,
        },
        "DpvConcept": {
            "title": "Concept",
            "is_a": "DpvTerm",
            "class_uri": "skos:Concept",
            "description": "A term DPV states as a concept and a class. Its rdf_type names the "
            "concepts it is an instance of, each a class of this schema, where DPV states one.",
            "comments": [
                "It holds the DPV properties some term of the vocabularies states. A thing a "
                "use case describes takes DpvResource, which holds them all.",
            ],
            "slots": used_names,
        },
        "DpvProperty": {
            "title": "Property",
            "is_a": "DpvTerm",
            "class_uri": "rdf:Property",
            "description": "A property DPV states, with the classes it names as its usual "
            "subjects and values. Every property is also a slot of DpvResource.",
            "slots": ["subPropertyOf", "domainIncludes", "rangeIncludes"],
        },
        "DpvResource": {
            "title": "Resource",
            "is_a": "DpvTerm",
            "class_uri": "rdfs:Resource",
            "description": "A thing a use case describes with DPV, such as a process, holding "
            "any DPV property, because DPV states none as limited to a class.",
            "comments": [
                "DPV's domainIncludes and rangeIncludes say what a property usually joins, not "
                "what it must, so a validator cannot refuse a value on them. tests/dpv_rules.py "
                "reports a value that names nothing, and tests/test_examples.py lists where "
                "DPV's own examples leave those classes.",
            ],
            "slots": [name for name in all_names if name not in term_slots]
            + ["statements"],
        },
        "DpvExample": {
            "title": "Example",
            "class_uri": "dex:Example",
            "description": "One of DPV's examples: what it shows, and the statements its Turtle "
            "file makes, as one resource per subject.",
            "comments": [
                "Every file leaves its prefixes out, so a parser reads it with the prefixes of "
                "the vocabularies beside it. An example may show two ways of saying one thing, "
                "so its resources are what the file states, not one consistent account.",
            ],
            "slots": [
                "id",
                "title",
                "description",
                "format",
                "source",
                "subject",
                "created",
                "modified",
                "temporal",
                "contributor",
                "term_status",
            ],
            "attributes": {
                "turtle_fault": {
                    "title": "Turtle Fault",
                    "description": "What stops a parser reading the example's file, where the "
                    "file does not parse.",
                },
                "resources": {
                    "title": "Resources",
                    "description": "Each subject the example's file states, with what it says "
                    "about it.",
                    "range": "DpvResource",
                    "multivalued": True,
                    "inlined_as_list": True,
                },
            },
            "slot_usage": {"title": {"required": True}},
        },
        "DpvStatement": {
            "title": "Statement",
            "description": "One statement of a resource that its keys cannot hold: a predicate "
            "with no slot, or a value not in the form its slot takes.",
            "slots": ["datatype"],
            "attributes": {
                "predicate": {
                    "title": "Predicate",
                    "description": "The predicate, as a CURIE or an IRI.",
                    "range": "uriorcurie",
                    "pattern": REFERENCE_PATTERN,
                    "required": True,
                    "slot_uri": "rdf:predicate",
                },
                "reference": {
                    "title": "Reference",
                    "description": "The object, when it names a resource.",
                    "range": "uriorcurie",
                    "pattern": REFERENCE_PATTERN,
                    "slot_uri": "rdf:object",
                },
                "literal": {
                    "title": "Literal",
                    "description": "The object, when it is a literal, in its lexical form.",
                    "slot_uri": "rdf:value",
                },
                "language": {
                    "title": "Language",
                    "description": "The literal's language tag.",
                },
            },
        },
    }
    return {
        "id": f"{OWN}dpv_terms",
        "name": "dpv_terms",
        "title": "DPV terms",
        "description": "The classes that hold a DPV term, and one slot per DPV property under "
        "its own IRI.",
        **_header(),
        "prefixes": prefixes(),
        "default_prefix": "dpv_linkml",
        "default_range": "string",
        "imports": ["linkml:types", "./dpv_core"],
        "classes": classes,
        "slots": slots,
    }


def _header() -> dict:
    return {
        "version": EDITION,
        "source": "https://w3id.org/dpv/2.3",
        "license": "Apache-2.0",
        "see_also": ["https://lmodel.github.io/dpv", "https://w3id.org/dpv"],
    }


def _reference(title, description, uri, many=True, **extra) -> dict:
    slot = {
        "title": title,
        "description": description,
        "slot_uri": uri,
        "range": "DpvTerm",
        "pattern": REFERENCE_PATTERN,
        "inlined": False,
    }
    if many:
        slot["multivalued"] = True
    slot.update(extra)
    return slot


def _structural_slots() -> dict:
    """The slots of a term's record that are no DPV property."""
    return {
        "rdf_type": _reference(
            "RDF Type",
            "The concepts DPV states the term is an instance of. A concept is also an "
            "rdfs:Class and a skos:Concept, and a property an rdf:Property and a skos:Concept.",
            "rdf:type",
        ),
        "prefLabel": {
            "title": "Preferred Label",
            "description": "The term's label, in English where DPV states a language.",
            "slot_uri": "skos:prefLabel",
        },
        "prefLabel_de": {
            "title": "Preferred Label in German",
            "description": "The term's German label, which the German health data law states.",
            "slot_uri": "skos:prefLabel",
        },
        "definition": {
            "title": "Definition",
            "description": "The term's definition, in English where DPV states a language.",
            "slot_uri": "skos:definition",
        },
        "definition_de": {
            "title": "Definition in German",
            "description": "The term's German definition, which the German health data law "
            "states.",
            "slot_uri": "skos:definition",
        },
        "scopeNote": {
            "title": "Scope Note",
            "description": "What DPV says about the term's scope.",
            "slot_uri": "skos:scopeNote",
            "multivalued": True,
        },
        "broader": _reference(
            "Broader", "The terms directly above this one.", "skos:broader"
        ),
        "related": _reference(
            "Related",
            "Other vocabularies' terms DPV relates to this one.",
            "skos:related",
        ),
        "inScheme": {
            "title": "In Scheme",
            "description": "The concept schemes that list the term.",
            "slot_uri": "skos:inScheme",
            "range": "DpvConceptScheme",
            "multivalued": True,
            "inlined": False,
            "pattern": REFERENCE_PATTERN,
        },
        "sameAs": _reference(
            "Same As",
            "A term DPV states as the same as this one, under skos:sameAs, which is not a "
            "SKOS term.",
            "skos:sameAs",
        ),
        "isDefinedBy": {
            "title": "Is Defined By",
            "description": "The namespace of the vocabulary that defines the term.",
            "slot_uri": "rdfs:isDefinedBy",
            "range": "DpvVocabulary",
            "multivalued": True,
            "inlined": False,
            "pattern": REFERENCE_PATTERN,
        },
        "subClassOf": _reference(
            "Subclass Of", "The classes directly above the term.", "rdfs:subClassOf"
        ),
        "subPropertyOf": _reference(
            "Subproperty Of",
            "The properties directly above this one.",
            "rdfs:subPropertyOf",
        ),
        "domainIncludes": _reference(
            "Domain Includes",
            "Classes DPV names as usual subjects of the property, not as the only ones.",
            "dcam:domainIncludes",
        ),
        "rangeIncludes": _reference(
            "Range Includes",
            "Classes DPV names as usual values of the property, not as the only ones.",
            "dcam:rangeIncludes",
        ),
        "example": {
            "title": "Example",
            "description": "The DPV examples that show the term in use.",
            "slot_uri": "vann:example",
            "range": "DpvExample",
            "multivalued": True,
            "inlined": False,
            "pattern": REFERENCE_PATTERN,
        },
        "exactMatch": {
            "title": "Exact Match",
            "description": "The address of the same thing elsewhere, as DPV writes it, typed "
            "xsd:anyURI.",
            "slot_uri": "skos:exactMatch",
            "range": "dpv_uri",
            "multivalued": True,
        },
        "term_status": {
            "title": "Term Status",
            "description": "How DPV's editors mark the term's standing.",
            "slot_uri": "sw:term_status",
            "range": "DpvTermStatus",
        },
        "value": {
            "title": "Value",
            "description": "The number DPV gives a level on a risk scale.",
            "slot_uri": "rdf:value",
            "range": "decimal",
        },
        "temporal": {
            "title": "Temporal",
            "description": "The period the term applies over, such as an adequacy decision's.",
            "slot_uri": "dcterms:temporal",
            "range": "DpvInterval",
            "inlined": True,
        },
        "source_page": {
            "title": "Source Page",
            "description": "The web pages DPV names as sources of the term.",
            "slot_uri": "dcterms:source",
            "range": "DpvWebPage",
            "multivalued": True,
            "inlined_as_list": True,
        },
        "datatype": {
            "title": "Datatype",
            "description": "The literal's datatype, as a CURIE.",
            "range": "uriorcurie",
            "pattern": REFERENCE_PATTERN,
        },
        "statements": {
            "title": "Statements",
            "description": "What the record's keys cannot hold.",
            "range": "DpvStatement",
            "multivalued": True,
            "inlined_as_list": True,
        },
    }


def kind_modules(graph: Graph) -> dict[str, dict]:
    """One module of kinds per namespace family that has any, by file stem."""
    names = kind_class_names()
    classes = collections.defaultdict(dict)
    parents = {}
    for kind in sorted(names, key=lambda k: names[k]):
        family = family_of(kind)
        parent = kind_parent(graph, kind)
        parents[kind] = parent
        label = graph.value(kind, SKOS.prefLabel)
        definition = graph.value(kind, SKOS.definition)
        entry: dict = {"title": str(label) if label is not None else local(kind)}
        entry["is_a"] = names[parent] if parent is not None else "DpvConcept"
        entry["description"] = (
            str(definition)
            if definition is not None
            else f"A kind of term DPV names as {curie(kind)} and does not define."
        )
        entry["class_uri"] = curie(kind)
        classes[family][names[kind]] = entry
    imports = collections.defaultdict(set)
    for kind, parent in parents.items():
        if parent is not None and family_of(parent) != family_of(kind):
            imports[family_of(kind)].add(family_of(parent))
    modules = {}
    for family, entries in classes.items():
        stem = "dpv_kinds" if family == "core" else f"dpv_{family}"
        needed = [
            "dpv_kinds" if other == "core" else f"dpv_{other}"
            for other in sorted(imports[family])
        ]
        modules[stem] = {
            "id": f"{OWN}{stem}",
            "name": stem,
            "title": f"DPV kinds: {FAMILY_TITLES[family]}",
            "description": f"The kinds of term DPV's vocabularies of {FAMILY_TITLES[family]} "
            "state: each a concept that terms are instances of, under its own IRI.",
            **_header(),
            "prefixes": _prefixes_for(entries),
            "default_prefix": "dpv_linkml",
            "default_range": "string",
            "imports": ["./dpv_terms", *(f"./{name}" for name in needed)],
            "classes": dict(sorted(entries.items())),
        }
    _check_module_order(modules)
    return modules


def _prefixes_for(entries: dict) -> dict[str, str]:
    """The prefixes a module of kinds names."""
    every = prefixes()
    wanted = {entry["class_uri"].split(":", 1)[0] for entry in entries.values()}
    wanted |= {"dpv_linkml", "linkml"}
    return {name: every[name] for name in sorted(wanted)}


def _check_module_order(modules: dict) -> None:
    """Stop on an import cycle between the kinds' modules."""
    seen = set()

    def visit(stem, path):
        if stem in path:
            raise ValueError(f"the kinds' modules import in a cycle: {path}")
        if stem in seen or stem not in modules:
            return
        for name in modules[stem]["imports"]:
            visit(name.removeprefix("./"), (*path, stem))
        seen.add(stem)

    for stem in modules:
        visit(stem, ())


# SKOS's mapping properties for the two kinds of statement DPV's mapping files make. A row
# reads with DPV's term as its subject, as the files' own statements do.
ISO_PREDICATES = {
    "skos:narrower": "skos:broadMatch",
    "skos:exactMatch": "skos:exactMatch",
}
ODRL_PREDICATES = {"skos:narrower": "skos:broadMatch", "rdf:type": "rdf:type"}
MAPPING_PREFIXES = {
    "dpv": "https://w3id.org/dpv#",
    "dpv-iso": "https://w3id.org/dpv/mappings/iso#",
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "semapv": "https://w3id.org/semapv/vocab/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
}
MAPPING_LICENCE = "https://www.w3.org/copyright/software-license-2023/"
MAPPING_COLUMNS = (
    "subject_id",
    "subject_label",
    "predicate_id",
    "object_id",
    "object_label",
    "mapping_justification",
    "author_label",
    "comment",
)
MAPPING_AUTHOR = "W3C Data Privacy Vocabularies and Controls Community Group"


def _mapping_rows(graph: Graph, name: str) -> list[dict]:
    """A mapping file's rows. DPV's CSV gives the other vocabulary's term first, and its
    Turtle says the statement reads the other way: dpv:Entity skos:broader odrl:Party."""
    path = UPSTREAM / "mappings" / name / f"dpv-{name}.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    out = []
    for row in rows:
        target = row.get("DPV") or row["DPVconcept"]
        kind = row.get("Mapping") or row["MappingType"]
        label = graph.value(expand(target), SKOS.prefLabel)
        if name == "iso":
            external = f"dpv-iso:{row['ExternalConcept']}"
            predicate = ISO_PREDICATES[kind]
            source = f"DPV names the source as {row['Source']}."
            external_label = row["Label"]
        else:
            external = row["ExternalConcept"]
            predicate = ODRL_PREDICATES[kind]
            source = ""
            external_label = ""
        out.append(
            {
                "subject_id": target,
                "subject_label": str(label) if label is not None else "",
                "predicate_id": predicate,
                "object_id": external,
                "object_label": external_label,
                "mapping_justification": "semapv:ManualMappingCuration",
                "author_label": MAPPING_AUTHOR,
                "comment": source,
            }
        )
    return sorted(out, key=lambda r: (r["subject_id"], r["object_id"]))


def mapping_text(graph: Graph, name: str) -> str:
    """A mapping file's rows as SSSOM's TSV, with its metadata as a comment."""
    description = {
        "iso": "ISO/IEC 29100:2024 terms DPV's editors align with DPV 2.3.",
        "odrl": "ODRL terms DPV's editors align with DPV 2.3.",
    }[name]
    wanted = {
        "iso": ("dpv", "dpv-iso", "semapv", "skos"),
        "odrl": ("dpv", "odrl", "rdf", "semapv", "skos"),
    }[name]
    lines = [
        f"# mapping_set_id: https://w3id.org/lmodel/dpv/mappings/dpv-{name}",
        f"# mapping_set_title: DPV's own {name.upper()} mappings",
        f"# mapping_set_description: {description}",
        f'# mapping_set_version: "{EDITION}"',
        f"# mapping_set_source: https://w3id.org/dpv/mappings/{name}",
        f"# license: {MAPPING_LICENCE}",
        "# curie_map:",
        *(f"#   {key}: {MAPPING_PREFIXES[key]}" for key in wanted),
        "\t".join(MAPPING_COLUMNS),
    ]
    for row in _mapping_rows(graph, name):
        lines.append("\t".join(row[column] for column in MAPPING_COLUMNS))
    return "\n".join(lines) + "\n"


class _Dumper(yaml.SafeDumper):
    """Writes block lists indented, and text with line breaks as a block."""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def _text_representer(dumper, value):
    style = "|" if "\n" in value else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


_Dumper.add_representer(str, _text_representer)


def dump(document, handle) -> None:
    """Write YAML in the project's style."""
    yaml.dump(
        document, handle, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=100
    )


SCHEMA_HEADER = """\
---
# Written by scripts/dpv_to_linkml.py from upstream/. Edit the script, not this file. A title
# and a description are DPV's own label and definition. NOTICE gives the licence they carry.
"""

CATALOGUE_HEADER = """\
---
# DPV 2.3: {what}. scripts/dpv_to_linkml.py writes this file from upstream/, so regenerate it,
# never edit it.
#
# Copyright (c) the Contributors to the Data Privacy Vocabulary (DPV), under the W3C Software
# and Document License (https://www.w3.org/copyright/software-license-2023/). This file
# includes material copied from and derived from https://w3id.org/dpv/2.3. It restates the
# material as records, and NOTICE says what else changed.
"""


def write_schema(graph: Graph) -> None:
    SCHEMA_DIR.mkdir(parents=True, exist_ok=True)
    modules = {"dpv_terms": terms_module(graph), **kind_modules(graph)}
    for stem, module in modules.items():
        with (SCHEMA_DIR / f"{stem}.yaml").open("w", encoding="utf-8") as handle:
            handle.write(SCHEMA_HEADER)
            dump(module, handle)


def data_path(family: str) -> Path:
    return DATA_DIR / f"dpv-{EDITION}-{family}.yaml"


def write_catalogue(graph: Graph) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for family, document in catalogues(graph).items():
        what = FAMILY_TITLES.get(family, family)
        with data_path(family).open("w", encoding="utf-8") as handle:
            handle.write(CATALOGUE_HEADER.format(what=what))
            dump(document, handle)


def write_mappings(graph: Graph) -> None:
    MAPPINGS_DIR.mkdir(parents=True, exist_ok=True)
    for name in ("iso", "odrl"):
        path = MAPPINGS_DIR / f"dpv-{name}.sssom.tsv"
        path.write_text(mapping_text(graph, name), encoding="utf-8")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--schema", action="store_true")
    parser.add_argument("--catalogue", action="store_true")
    parser.add_argument("--mappings", action="store_true")
    args = parser.parse_args(argv)
    if not (args.schema or args.catalogue or args.mappings):
        parser.error("name --schema, --catalogue, --mappings or several")
    graph = load()
    if args.schema:
        write_schema(graph)
    if args.catalogue:
        write_catalogue(graph)
    if args.mappings:
        write_mappings(graph)
    return 0


if __name__ == "__main__":
    sys.exit(main())
