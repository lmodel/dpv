"""Checks DPV's own examples, the one instance data DPV publishes, against the catalogue.

Each example's Turtle file is in the data as records. These tests hold the records to the
file, say what the validator refuses, and read the one thing it cannot state: DPV's
rangeIncludes and domainIncludes say what a property usually joins, so a value outside them
is not wrong in RDF, but the examples are DPV's own account of how to use a property, so
tests/example_departures.yaml lists each place they leave those classes, and a new one fails.
"""

import collections
from functools import cache
from pathlib import Path

import pytest
import yaml
from rdflib import RDF, Graph, Literal, URIRef
from rdflib.compare import to_canonical_graph
from rdflib.term import BNode

from tests import conversion
from tests.dpv_rules import is_dpv, rule_errors

C = conversion.CONVERTER
DEPARTURES = Path(__file__).parent / "example_departures.yaml"


def _examples():
    return conversion.documents()["examples"]["examples"]


@cache
def _slot_table():
    """Each key a resource's record may hold, with its predicate and whether it is text."""
    table = {}
    for predicate, (name, text) in C._resource_slots(conversion.graph()).items():
        table[name] = (predicate, text)
    return table


def _node(value: str):
    return BNode(value[2:]) if value.startswith("_:") else C.expand(value)


def rebuilt(example: dict) -> Graph:
    """The triples an example's records state, read back from the records alone."""
    graph = Graph()
    table = _slot_table()
    for resource in example.get("resources", ()):
        subject = _node(resource["id"])
        for key, value in resource.items():
            if key == "id":
                continue
            if key == "rdf_type":
                for item in value:
                    graph.add((subject, RDF.type, _node(item)))
            elif key == "statements":
                for statement in value:
                    predicate = C.expand(statement["predicate"])
                    if "reference" in statement:
                        graph.add((subject, predicate, _node(statement["reference"])))
                        continue
                    datatype = statement.get("datatype")
                    literal = Literal(
                        statement["literal"],
                        lang=statement.get("language"),
                        datatype=C.expand(datatype) if datatype else None,
                    )
                    graph.add((subject, predicate, literal))
            else:
                predicate, text = table[key]
                for item in value if isinstance(value, list) else [value]:
                    graph.add(
                        (subject, predicate, Literal(item) if text else _node(item))
                    )
    return graph


def test_each_example_is_a_file():
    names = {path.stem for path in (C.UPSTREAM / "examples").glob("E*.ttl")}
    held = {example["id"].removeprefix("dex:") for example in _examples()}
    assert names == held
    assert len(names) == 88


def test_three_files_do_not_parse_and_the_rest_hold_their_statements():
    """Three files carry a Turtle fault, which issues/87 reports. The others hold resources."""
    faulty = {e["id"] for e in _examples() if "turtle_fault" in e}
    assert faulty == {"dex:E0030", "dex:E0059", "dex:E0061"}
    assert all("resources" not in e for e in _examples() if e["id"] in faulty)
    assert all("resources" in e for e in _examples() if e["id"] not in faulty)


@pytest.mark.parametrize(
    "example",
    [e for e in _examples() if "resources" in e],
    ids=lambda e: e["id"],
)
def test_the_records_state_what_the_file_states(example):
    """A blank node keeps its place by canonical labelling, so the two compare as sets."""
    upstream = C.example_graph(example["id"].removeprefix("dex:"))
    built = to_canonical_graph(rebuilt(example))
    assert set(built) == set(upstream)


def test_no_example_names_a_dpv_term_that_does_not_exist():
    """A value resolves to a term of the edition, or to a resource of its own example."""
    found = rule_errors({"examples": _examples()})
    assert not found, found[:10]


def test_every_dpv_predicate_is_a_slot_or_a_listed_departure():
    """A statement under a DPV predicate exists only where its value left the slot's form."""
    slots = {
        str(predicate)
        for predicate, (_, _text) in C._resource_slots(conversion.graph()).items()
    }
    for example in _examples():
        for resource in example.get("resources", ()):
            for statement in resource.get("statements", ()):
                if is_dpv(statement["predicate"]):
                    assert str(C.expand(statement["predicate"])) in slots


def _types_of(value, local):
    """What a value is an instance of: a resource's stated types, or a term's kinds."""
    if value in local:
        return set(local[value].get("rdf_type", ()))
    record = conversion.terms().get(value)
    return set(record.get("rdf_type", ())) if record else set()


@cache
def _above():
    """Each term with what skos:broader and rdfs:subClassOf place above it, and itself."""
    parents = {
        identifier: {*record.get("broader", ()), *record.get("subClassOf", ())}
        for identifier, record in conversion.terms().items()
    }
    closed = {}

    def walk(term):
        if term in closed:
            return closed[term]
        closed[term] = {term}
        for parent in parents.get(term, ()):
            closed[term] |= walk(parent)
        return closed[term]

    return {term: frozenset(walk(term)) for term in parents}


def _reaches(types, wanted):
    """Whether any of a value's types sits at or under one of the classes wanted."""
    above = _above()
    return any(wanted & above.get(kind, frozenset({kind})) for kind in types)


def _slot_properties():
    """Each reference slot with its property's record."""
    records = conversion.records("properties")
    return {
        name: records[C.curie(predicate)]
        for name, (predicate, text) in _slot_table().items()
        if not text and C.curie(predicate) in records
    }


def departures():
    """Where the examples leave a property's rangeIncludes or domainIncludes, or give a
    literal where its range names a class. A value or a subject with no stated type is left
    alone, since nothing says what it is."""
    found = collections.defaultdict(list)
    props = _slot_properties()
    for example in _examples():
        resources = example.get("resources", ())
        local = {r["id"]: r for r in resources}
        for resource in resources:
            subject = _types_of(resource["id"], local)
            for key, values in resource.items():
                record = props.get(key)
                if record is None:
                    continue
                wanted = set(record.get("rangeIncludes", ()))
                for value in values:
                    types = _types_of(value, local) | (
                        {value} if value in conversion.terms() else set()
                    )
                    if wanted and types and not _reaches(types, wanted):
                        found["range"].append(f"{example['id']} {key} {value}")
                domain = set(record.get("domainIncludes", ()))
                if domain and subject and not _reaches(subject, domain):
                    found["domain"].append(f"{example['id']} {key} {resource['id']}")
            for statement in resource.get("statements", ()):
                predicate = statement["predicate"]
                if not is_dpv(predicate) or "literal" not in statement:
                    continue
                if not C.is_text_property(conversion.graph(), C.expand(predicate)):
                    found["literal"].append(f"{example['id']} {predicate}")
    return {key: sorted(values) for key, values in sorted(found.items())}


def test_the_departures_are_the_listed_ones():
    """A new departure fails this test, and so does one DPV has fixed. Each is a place DPV's
    own examples use a property beyond what its rangeIncludes or domainIncludes say."""
    listed = yaml.safe_load(DEPARTURES.read_text(encoding="utf-8"))
    assert departures() == listed


def test_the_docs_give_the_departures_numbers():
    about = (Path(__file__).parent.parent / "docs" / "about.md").read_text(
        encoding="utf-8"
    )
    found = departures()
    assert (
        f"{len(found['range'])} values, {len(found['domain'])} subjects and "
        f"{len(found['literal'])} literals" in about
    )


def test_a_real_process_reads_as_dpv_says():
    """The first example's process names a purpose, and that purpose is DPV's."""
    example = next(e for e in _examples() if e["id"] == "dex:E0026")
    process = next(r for r in example["resources"] if r["id"] == "exd:PDH1")
    assert process["rdf_type"] == ["dpv:Process"]
    assert process["hasPurpose"] == ["dpv:CommunicationForCustomerCare"]
    assert "dpv:CommunicationForCustomerCare" in conversion.terms()
    assert URIRef("https://w3id.org/dpv#Process") == C.expand("dpv:Process")
