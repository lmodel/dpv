"""Checks the whole catalogue against the Turtle it comes from.

src/dpv/data/ holds every term of the edition as a record. These tests hold it to the
converter's output, to the validator the docs tell a user to run, to the rules JSON Schema
cannot state and, through the generated JSON-LD context, to the triples of the Turtle.
"""

import hashlib
import json
from functools import cache
from pathlib import Path

import jsonschema
import pytest
import rdflib
import yaml
from linkml.validator import validate
from rdflib import RDF, RDFS, SKOS, BNode, Literal, URIRef

from tests import conversion
from tests.conversion import ROOT
from tests.dpv_rules import DANGLING, rule_errors

JSON_SCHEMA = ROOT / "project" / "jsonschema" / "dpv.schema.json"
CONTEXT = ROOT / "project" / "jsonld" / "dpv.context.jsonld"
OWN = "https://w3id.org/lmodel/dpv/"
C = conversion.CONVERTER


def _digest(document) -> str:
    return hashlib.sha256(json.dumps(document, sort_keys=True).encode()).hexdigest()


@cache
def _converted():
    return C.catalogues(conversion.graph())


def test_the_catalogue_is_the_converters_output():
    """Each committed data file is what the converter writes from the Turtle, so nothing was
    edited by hand and a change to the converter shows here. The files compare by digest,
    since a diff of files this size does not finish."""
    wrong = [
        family
        for family, document in conversion.documents().items()
        if _digest(document) != _digest(_converted()[family])
    ]
    assert not wrong


def test_the_modules_are_the_converters_output():
    """The committed slots and kinds are what the converter writes from the Turtle."""
    graph = conversion.graph()
    written = {"dpv_terms": C.terms_module(graph), **C.kind_modules(graph)}
    wrong = [
        stem
        for stem, module in written.items()
        if _digest(module) != _digest(conversion.modules()[stem])
    ]
    assert not wrong


@pytest.mark.parametrize("family", conversion.FAMILIES)
def test_each_file_passes_the_committed_json_schema(family):
    """Every record passes project/jsonschema/dpv.schema.json, the file a consumer without
    LinkML validates with."""
    schema = json.loads(JSON_SCHEMA.read_text(encoding="utf-8"))
    validator = jsonschema.validators.validator_for(schema)(schema)
    errors = [
        (list(e.absolute_path)[:3], e.message[:120])
        for e in validator.iter_errors(conversion.documents()[family])
    ]
    assert not errors, errors[:5]


@pytest.mark.parametrize("family", conversion.FAMILIES)
def test_each_file_passes_the_validator_the_docs_name(family):
    """linkml-validate runs a format checker the test above does not, so each file goes
    through it too. This is the call behind the command in docs/index.md."""
    report = validate(conversion.documents()[family], conversion.SCHEMA, "DpvCatalogue")
    assert not report.results, [r.message[:200] for r in report.results[:5]]


@pytest.mark.parametrize("family", conversion.FAMILIES)
def test_each_file_keeps_the_rules(family):
    """Every value names a term that exists, and each IRI is one record."""
    found = rule_errors(conversion.documents()[family])
    assert not found, found[:10]


def test_a_record_holds_what_the_turtle_says():
    """The walk docs/about.md describes."""
    terms = conversion.terms()
    marketing = terms["dpv:Marketing"]
    assert marketing["rdf_type"] == ["dpv:Purpose"]
    assert marketing["broader"] == ["dpv:Purpose"]
    assert marketing["prefLabel"] == "Marketing"
    has_purpose = terms["dpv:hasPurpose"]
    assert has_purpose["rangeIncludes"] == ["dpv:Purpose"]
    assert "domainIncludes" not in has_purpose
    level = terms["risk:RM5x5S3L2"]
    assert level["hasLikelihood"] == ["risk:LowLikelihood"]
    germany = terms["loc:DE"]
    assert germany["iso_alpha2"] == ["DE"]
    assert "dpv:Country" in germany["rdf_type"]


def test_german_stays_in_its_own_keys():
    """Only de-gdng states German, and only there do the _de keys appear. The projection
    below compares text by its lexical form, so this keeps the language honest."""
    graph = conversion.graph()
    for predicate, key in (
        (SKOS.prefLabel, "prefLabel_de"),
        (SKOS.definition, "definition_de"),
    ):
        stated = {
            (C.curie(s), str(o))
            for s, o in graph.subject_objects(predicate)
            if o.language == "de"
        }
        held = {
            (identifier, record[key])
            for identifier, record in conversion.terms().items()
            if key in record
        }
        assert held == stated
        assert stated


@cache
def _projected():
    """The catalogue's triples, through the committed JSON-LD context."""
    context = json.loads(CONTEXT.read_text(encoding="utf-8"))["@context"]
    graph = rdflib.Graph()
    for family, document in conversion.documents().items():
        if family == "examples":
            document = {k: v for k, v in document.items() if k != "examples"}
        graph.parse(data=json.dumps(dict(document, **{"@context": context})), format="json-ld")
    return graph


def _agent_name(graph, node):
    """A contributor by name: a blank node in the Turtle, an IRI in the projection."""
    return str(graph.value(node, C.FOAF.name))


def _interval_of(graph, node):
    """A period by its dates. The Turtle holds each date on a node of its own, and a record
    holds it directly."""
    dates = []
    for predicate in (C.TIME.hasBeginning, C.TIME.hasEnd):
        value = graph.value(node, predicate)
        if isinstance(value, BNode):
            value = graph.value(value, C.TIME.inXSDDate)
        dates.append(None if value is None else str(value))
    return tuple(dates)


def _normal(graph, subject):
    """A subject's triples, each object by its lexical form, and what the Turtle holds on a
    blank node by the facts on it."""
    found = set()
    for predicate, obj in graph.predicate_objects(subject):
        if str(predicate).startswith(OWN):
            continue
        if predicate == RDF.value:
            found.add((subject, predicate, float(str(obj))))
        elif predicate in (C.DCTERMS.contributor, C.DCTERMS.creator):
            found.add((subject, predicate, _agent_name(graph, obj)))
        elif predicate == C.DCTERMS.temporal:
            found.add((subject, predicate, _interval_of(graph, obj)))
        elif predicate == C.DCTERMS.source and isinstance(obj, BNode):
            name = str(graph.value(obj, C.SCHEMA_ORG.name))
            found.add((subject, predicate, (name, str(graph.value(obj, C.SCHEMA_ORG.url)))))
        else:
            found.add((subject, predicate, str(obj)))
    return found


def _with_agents(graph):
    """The projection, with each agent's name from the agents' file."""
    return graph


def _term_triples(graph, subjects, leave_out):
    found = set()
    for subject in subjects:
        for triple in _normal(graph, subject):
            if triple[1] not in leave_out:
                found.add(triple)
    return found


def test_the_json_ld_projection_reproduces_the_turtle_for_every_term():
    """Each triple of the Turtle about a term comes back from the catalogue, and nothing
    else does, but for what a record's class says and what a test proves derived. Objects
    compare by their lexical form, and what the Turtle holds on a blank node by its facts.
    The comparison is by set, since a graph isomorphism check on this size does not finish."""
    graph = conversion.graph()
    terms = C.term_subjects(graph)
    leave_out = {C.SKOS.narrower, C.SCHEMA_ORG.domainIncludes, C.SCHEMA_ORG.rangeIncludes}
    upstream = _term_triples(graph, terms, leave_out)
    fixed = C.CONCEPT_TYPES | C.PROPERTY_TYPES
    upstream = {t for t in upstream if not (t[1] == RDF.type and URIRef(t[2]) in fixed)}
    projected = _term_triples(_projected(), terms, leave_out)
    assert not upstream - projected, sorted(upstream - projected, key=str)[:10]
    assert not projected - upstream, sorted(projected - upstream, key=str)[:10]
    assert len(upstream) > 100000


def test_the_json_ld_projection_reproduces_each_vocabulary_header():
    """Each vocabulary's own facts come back, but for its types and the site furniture."""
    graph = conversion.graph()
    vocabularies = C.vocabulary_subjects(graph)
    leave_out = {RDF.type, *C.VOCABULARY_LEFT_OUT, C.DCTERMS["format"]}
    upstream = _term_triples(graph, vocabularies, leave_out)
    projected = _term_triples(_projected(), vocabularies, leave_out)
    assert not upstream - projected, sorted(upstream - projected, key=str)[:10]
    assert not projected - upstream, sorted(projected - upstream, key=str)[:10]


def test_a_relation_projects_as_an_iri():
    """A relation's target is a node of the graph, not a piece of text."""
    triple = (C.DPV.Marketing, SKOS.broader, C.DPV.Purpose)
    assert triple in conversion.graph()
    assert triple in _projected()
    assert (C.DPV.Marketing, RDF.type, C.DPV.Purpose) in _projected()


def test_a_term_with_a_date_projects_it_typed():
    """A date keeps its datatype, which the lexical comparison above leaves aside."""
    created = _projected().value(C.DPV.Marketing, C.DCTERMS.created)
    assert isinstance(created, Literal)
    assert created.datatype == C.XSD.date
    assert str(created) == "2020-11-04"


def test_the_docs_give_the_catalogues_numbers():
    """docs/index.md's table and docs/about.md's counts follow the files."""
    index = (ROOT / "docs" / "index.md").read_text(encoding="utf-8")
    for family, document in conversion.documents().items():
        concepts = len(document.get("concepts", ()))
        properties = len(document.get("properties", ()))
        if family == "agents":
            continue
        row = f"| `dpv-2.3-{family}.yaml` | {concepts:,} | {properties} |"
        assert row in index, row
    assert f"{len(conversion.records('agents'))} contributors" in index
    assert f"the {len(conversion.records('examples'))} examples" in index
    about = (ROOT / "docs" / "about.md").read_text(encoding="utf-8")
    assert "68,032 times" in about
    assert "4,959 are the inverse" in about
    assert "The other 63,073" in about
    assert f"{len(DANGLING)} names under DPV's namespaces" in about


def test_the_docs_example_validates():
    """The record docs/index.md shows is a resource whose values are real terms."""
    index = (ROOT / "docs" / "index.md").read_text(encoding="utf-8")
    block = index.split("```yaml")[1].split("```")[0]
    record = yaml.safe_load(block)
    report = validate(record, conversion.SCHEMA, "DpvResource")
    assert not report.results, [r.message for r in report.results]
    assert not rule_errors({"examples": [{"id": "dex:E0", "title": "x", "resources": [record]}]})


def test_what_the_data_shows_and_the_vocabulary_does_not_say():
    """What the files hold that a reader would not expect. docs/about.md names these, and a
    later edition that fixes one fails here."""
    terms = conversion.terms()
    assert terms["dcat:Resource"]["created"] == ["2022-11-02", "2022-11-09"]
    two_homes = {i for i, r in terms.items() if len(r.get("isDefinedBy", ())) > 1}
    assert two_homes == {
        "dcat:Resource",
        "dcterms:hasPart",
        "dcterms:isPartOf",
        "dcterms:valid",
        "dpv:hasStatus",
    }
    assert sum(len(r.get("sameAs", ())) for r in terms.values()) == 60
    no_definition = [r for r in terms.values() if "definition" not in r and "definition_de" not in r]
    assert len(no_definition) == 153
    assert Path(C.UPSTREAM).is_dir()
    assert RDFS.Class in C.CONCEPT_TYPES
