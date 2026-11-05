"""Walks the Turtle beside the schema and the catalogue, both ways.

Every term, kind, property, vocabulary, concept scheme, example and contributor the Turtle
states has its one home here, and nothing here lacks one in the Turtle. Every predicate on a
term is a slot, or is one DERIVED names with its reason.
"""

import collections

from rdflib import RDF, RDFS, SKOS, BNode, URIRef

from tests import conversion
from tests.dpv_rules import DANGLING

C = conversion.CONVERTER

# What this edition holds. A change here is a change of edition, and should be looked at.
COUNTS = {
    "concepts": 8856,
    "properties": 307,
    "vocabularies": 67,
    "concept_schemes": 219,
    "examples": 88,
    "agents": 70,
}
KINDS = 149

# Each fact of a term no record holds, and why.
DERIVED = {
    "http://www.w3.org/2004/02/skos/core#narrower": "derived_narrower gives every pair",
    "https://schema.org/domainIncludes": "it repeats dcam:domainIncludes on every property",
    "https://schema.org/rangeIncludes": "it repeats dcam:rangeIncludes on every property",
}


def _iris(key):
    return {C.expand(identifier) for identifier in conversion.records(key)}


def test_each_part_of_the_edition_holds_what_it_should():
    found = {key: len(conversion.records(key)) for key in COUNTS}
    assert found == COUNTS


def test_every_concept_is_one_record_and_back():
    assert _iris("concepts") == C.concept_subjects(conversion.graph())


def test_every_property_is_one_record_and_back():
    assert _iris("properties") == C.property_subjects(conversion.graph())


def test_every_vocabulary_is_one_record_and_back():
    assert _iris("vocabularies") == C.vocabulary_subjects(conversion.graph())


def test_every_scheme_is_one_record_and_back():
    assert _iris("concept_schemes") == C.scheme_subjects(conversion.graph())


def test_every_example_is_one_record_and_back():
    assert _iris("examples") == C.example_subjects(conversion.graph())


def test_no_two_files_hold_one_record():
    """Each record sits in the file of its namespace family."""
    seen = collections.Counter(
        record["id"]
        for document in conversion.documents().values()
        for key in ("concepts", "properties", "vocabularies", "concept_schemes")
        for record in document.get(key, ())
    )
    assert [identifier for identifier, count in seen.items() if count > 1] == []
    for family, document in conversion.documents().items():
        for key in ("concepts", "properties"):
            for record in document.get(key, ()):
                assert C.family_of(C.expand(record["id"])) == family, record["id"]


def test_every_kind_is_a_class_under_its_iri_and_back():
    """A kind is a type a concept holds beyond rdfs:Class and skos:Concept."""
    graph = conversion.graph()
    kinds = {
        kind
        for term in C.concept_subjects(graph)
        for kind in graph.objects(term, RDF.type)
        if kind not in C.CONCEPT_TYPES
    }
    assert len(kinds) == KINDS
    classes = {
        C.expand(cls["class_uri"]): name
        for name, cls in conversion.all_classes().items()
        if name not in FIXED_CLASSES
    }
    assert set(classes) == kinds


FIXED_CLASSES = {
    "DpvAgent",
    "DpvCatalogue",
    "DpvConcept",
    "DpvConceptScheme",
    "DpvExample",
    "DpvInterval",
    "DpvProperty",
    "DpvResource",
    "DpvStatement",
    "DpvTerm",
    "DpvVocabulary",
    "DpvWebPage",
}


def test_a_kinds_parent_sits_above_it_in_dpv():
    """A kind's class descends from the nearest kind above it along skos:broader."""
    graph = conversion.graph()
    classes = conversion.all_classes()
    by_uri = {cls.get("class_uri"): name for name, cls in classes.items()}
    for name, cls in classes.items():
        if name in FIXED_CLASSES:
            continue
        parent = cls["is_a"]
        if parent == "DpvConcept":
            assert C.kind_parent(graph, C.expand(cls["class_uri"])) is None, name
        else:
            found = C.kind_parent(graph, C.expand(cls["class_uri"]))
            assert by_uri[C.curie(found)] == parent, name


def test_every_property_is_a_slot_under_its_iri_and_back():
    graph = conversion.graph()
    slots = conversion.all_slots()
    declared = {
        C.expand(slot["slot_uri"]) for slot in slots.values() if "slot_uri" in slot
    }
    assert C.property_subjects(graph) <= declared
    resource = conversion.all_classes()["DpvResource"]["slots"]
    term = conversion.all_classes()["DpvTerm"]["slots"]
    for prop in C.property_subjects(graph):
        name = C.slot_name(prop)
        assert name in resource or name in term, name
        assert C.expand(slots[name]["slot_uri"]) == prop


def test_a_shared_local_name_keeps_each_iri():
    """Where two namespaces define one name, the core keeps it, and each slot keeps its IRI."""
    slots = conversion.all_slots()
    assert slots["hasRiskLevel"]["slot_uri"] == "dpv:hasRiskLevel"
    assert slots["eu_aiact_hasRiskLevel"]["slot_uri"] == "eu-aiact:hasRiskLevel"
    assert slots["ai_hasCapability"]["slot_uri"] == "ai:hasCapability"
    assert slots["tech_hasCapability"]["slot_uri"] == "tech:hasCapability"


def test_every_predicate_on_a_term_is_a_slot_or_named_as_derived():
    graph = conversion.graph()
    slots = {
        str(C.expand(slot["slot_uri"]))
        for slot in conversion.all_slots().values()
        if "slot_uri" in slot
    }
    stated = {
        str(predicate)
        for term in C.term_subjects(graph)
        for predicate in graph.predicates(term, None)
    }
    assert stated - slots - {str(RDF.type)} == set(DERIVED)


def test_skos_narrower_is_exactly_what_the_records_regenerate():
    """Of 68,032 pairs only loc states, 4,959 are the inverse of skos:broader, and 63,073
    list what each loc:non-X holds. The rule gives every pair, and no other."""
    graph = conversion.graph()
    derived = C.derived_narrower(graph)
    stated = C.stated_narrower(graph)
    assert derived == stated
    assert len(stated) == 68032
    inverse = {(p, c) for c, p in graph.subject_objects(SKOS.broader)}
    assert len(stated & inverse) == 4959
    assert {str(p) for p, _ in stated - inverse} <= {
        str(s) for s in graph.subjects(RDF.type, C.DPV.InverseJurisdiction)
    }


def test_schema_org_repeats_dcam():
    graph = conversion.graph()
    for dcam, schema_org in (
        (C.DCAM.domainIncludes, C.SCHEMA_ORG.domainIncludes),
        (C.DCAM.rangeIncludes, C.SCHEMA_ORG.rangeIncludes),
    ):
        assert set(graph.subject_objects(dcam)) == set(graph.subject_objects(schema_org))


def test_a_term_holds_the_types_its_class_says():
    """Each concept is an rdfs:Class and a skos:Concept, and each property an rdf:Property
    and a skos:Concept, so a record's rdf_type leaves them out. dex:Example, the type of an
    example, is the one concept DPV does not call a class."""
    graph = conversion.graph()
    for term in C.concept_subjects(graph) - {C.DEX.Example}:
        assert {RDFS.Class, SKOS.Concept} <= set(graph.objects(term, RDF.type)), term
    for term in C.property_subjects(graph):
        assert {RDF.Property, SKOS.Concept} <= set(graph.objects(term, RDF.type)), term


def test_every_contributor_is_one_agent_and_back():
    graph = conversion.graph()
    named = {
        C.agent_id(graph, node)
        for predicate in (C.DCTERMS.contributor, C.DCTERMS.creator)
        for node in graph.objects(None, predicate)
    }
    members = {
        C.agent_id(graph, node) for node in graph.objects(None, C.ORG.memberOf)
    }
    assert named | members == set(conversion.records("agents"))


def test_what_stays_out_is_only_the_site_furniture():
    """The serialisation descriptors say how DPV's site publishes a file. They are the one
    kind of statement the catalogue leaves out, and nothing else names them."""
    graph = conversion.graph()
    descriptors = set(graph.subjects(RDF.type, C.DESCRIPTOR_TYPE))
    vocabularies = C.vocabulary_subjects(graph)
    assert len(descriptors - vocabularies) == 337
    subjects = {s for s in graph.subjects() if not isinstance(s, BNode)}
    known = (
        C.term_subjects(graph)
        | vocabularies
        | C.scheme_subjects(graph)
        | C.example_subjects(graph)
        | descriptors
    )
    assert subjects == known


def test_dangling_is_as_listed():
    """Every DPV name the data leaves undefined is listed, and every listed name is still
    named: the check on the list in tests/dpv_rules.py."""
    terms = conversion.terms()
    keys = {
        name
        for name, slot in conversion.all_slots().items()
        if slot.get("range") == "DpvTerm"
    }
    named = set()
    for record in terms.values():
        for key in keys & record.keys():
            named.update(record[key])
    assert DANGLING == {
        value
        for value in named
        if value.split(":", 1)[0] in _dpv_prefixes() and value not in terms
    }


def _dpv_prefixes():
    return {
        name
        for name, namespace in C.prefixes().items()
        if namespace.startswith("https://w3id.org/dpv")
    }


def test_the_umbrella_binds_every_prefix_the_data_uses():
    """The JSON-LD context takes its prefixes from the umbrella alone."""
    assert conversion.modules()["dpv"]["prefixes"] == C.prefixes()


def test_the_prefixes_are_dpvs_own():
    """Each DPV namespace keeps the prefix DPV's files bind."""
    graph = conversion.graph()
    bound = {name: str(namespace) for name, namespace in graph.namespaces()}
    for name, namespace in C.prefixes().items():
        if namespace.startswith("https://w3id.org/dpv"):
            assert bound[name] == namespace, name
    assert URIRef("https://w3id.org/dpv#Marketing") == C.expand("dpv:Marketing")
