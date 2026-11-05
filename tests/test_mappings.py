"""Checks the two SSSOM sets against the files of DPV's they render.

src/dpv/mappings/ holds what DPV's editors publish as machine-readable mappings, for ISO/IEC
29100:2024 terms and for ODRL. Each row comes from the file's CSV, reads with DPV's term as
its subject, as the files' own statements do, and is held to both the CSV and the Turtle.
DPV's other mapping folders, for DCAT, Dublin Core, gist, PROV, schema.org and SEMIC, hold a
web page only, so nothing here renders them.
"""

import csv
import re
from pathlib import Path

import pytest
from rdflib import Graph, Namespace

from tests import conversion

C = conversion.CONVERTER
ROOT = Path(__file__).parent.parent
SETS = ROOT / "src" / "dpv" / "mappings"
UPSTREAM = ROOT / "upstream" / "mappings"
DPV_ISO = Namespace("https://w3id.org/dpv/mappings/iso#")
SKOS = "http://www.w3.org/2004/02/skos/core#"


def _rows(name):
    text = (SETS / f"dpv-{name}.sssom.tsv").read_text(encoding="utf-8")
    body = [line for line in text.splitlines() if not line.startswith("#")]
    return list(csv.DictReader(body, delimiter="\t"))


def _header(name):
    text = (SETS / f"dpv-{name}.sssom.tsv").read_text(encoding="utf-8")
    return "\n".join(line for line in text.splitlines() if line.startswith("#"))


def _csv(name):
    with (UPSTREAM / name / f"dpv-{name}.csv").open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


@pytest.mark.parametrize("name", ["iso", "odrl"])
def test_each_set_is_the_converters_output(name):
    written = C.mapping_text(conversion.graph(), name)
    assert (SETS / f"dpv-{name}.sssom.tsv").read_text(encoding="utf-8") == written


@pytest.mark.parametrize("name", ["iso", "odrl"])
def test_each_row_comes_from_the_csv_and_back(name):
    held = {(row["subject_id"], row["object_id"]) for row in _rows(name)}
    prefix = "dpv-iso:" if name == "iso" else ""
    source = {
        (row.get("DPV") or row["DPVconcept"], prefix + row["ExternalConcept"])
        for row in _csv(name)
    }
    assert held == source
    assert len(held) == {"iso": 5, "odrl": 24}[name]


@pytest.mark.parametrize("name", ["iso", "odrl"])
def test_each_subject_is_a_term_of_the_edition(name):
    """But for dpv:hasTechnology, which DPV's ODRL mapping names and 2.3 does not state, and
    which issues/87 reports."""
    terms = conversion.terms()
    missing = {row["subject_id"] for row in _rows(name)} - set(terms)
    assert missing == ({"dpv:hasTechnology"} if name == "odrl" else set())
    for row in _rows(name):
        if row["subject_id"] in terms:
            assert row["subject_label"] == terms[row["subject_id"]]["prefLabel"]


@pytest.mark.parametrize("name", ["iso", "odrl"])
def test_each_row_says_who_mapped_it(name):
    for row in _rows(name):
        assert row["mapping_justification"] == "semapv:ManualMappingCuration"
        assert row["author_label"] == C.MAPPING_AUTHOR


@pytest.mark.parametrize("name", ["iso", "odrl"])
def test_the_header_states_the_upstreams_licence_and_each_prefix(name):
    header = _header(name)
    assert C.MAPPING_LICENCE in header
    used = {
        value.split(":", 1)[0]
        for row in _rows(name)
        for value in (row["subject_id"], row["predicate_id"], row["object_id"])
    }
    for prefix in used | {"semapv"}:
        assert f"#   {prefix}: " in header, prefix


def test_the_iso_rows_read_as_dpvs_turtle_says():
    """DPV states dpv-iso:PII skos:narrower dpv:PersonalData, so dpv:PersonalData has the
    broader match dpv-iso:PII. The Turtle parses, so the two compare directly."""
    graph = Graph().parse(UPSTREAM / "iso" / "dpv-iso.ttl", format="turtle")
    stated = set()
    for subject, predicate, obj in graph:
        if predicate == graph.namespace_manager.expand_curie("skos:narrower"):
            stated.add((C.curie(obj), "skos:broadMatch", f"dpv-iso:{str(subject).split('#')[1]}"))
        elif predicate == graph.namespace_manager.expand_curie("skos:exactMatch"):
            stated.add((C.curie(obj), "skos:exactMatch", f"dpv-iso:{str(subject).split('#')[1]}"))
    held = {(r["subject_id"], r["predicate_id"], r["object_id"]) for r in _rows("iso")}
    assert held == stated


def test_the_odrl_rows_read_as_dpvs_turtle_says():
    """dpv-odrl.ttl does not parse, since its first prefix line has no full stop, so the
    statements of its comment lines are read as text. Each says which way a row reads."""
    text = (UPSTREAM / "odrl" / "dpv-odrl.ttl").read_text(encoding="utf-8")
    with pytest.raises(Exception, match="Bad syntax"):
        Graph().parse(data=text, format="turtle")
    pattern = re.compile(r"^# (dpv:\S+) (skos:broader|rdf:type) (odrl:\S+) \.$", re.M)
    predicates = {"skos:broader": "skos:broadMatch", "rdf:type": "rdf:type"}
    stated = {(s, predicates[p], o) for s, p, o in pattern.findall(text)}
    held = {(r["subject_id"], r["predicate_id"], r["object_id"]) for r in _rows("odrl")}
    assert held == stated
