"""Checks that upstream/ holds the edition the schema renders.

upstream/ holds the release's whole-vocabulary Turtle files, its examples, the two mapping
folders with machine-readable files, and its licence, as the DPV Community Group publishes
them. scripts/check_upstream_release.py compares them with the repository. These tests make
the same comparison offline.
"""

import hashlib
import importlib.util
from functools import cache
from pathlib import Path

import pytest
import yaml
from rdflib import OWL, Graph, URIRef

from tests.conversion import ROOT, SCHEMA_DIR

UPSTREAM = ROOT / "upstream"
WATCH = ROOT / "scripts" / "check_upstream_release.py"


@cache
def _watch():
    spec = importlib.util.spec_from_file_location("watch_pins", WATCH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def test_upstream_holds_only_the_pinned_files():
    found = {
        str(path.relative_to(UPSTREAM))
        for path in UPSTREAM.rglob("*")
        if path.is_file()
    }
    assert found == set(_watch().pins())
    assert len(found) == 160


def test_copies_match_the_pinned_blobs():
    """Each file has the git object hash the watch pins."""
    wrong = [
        path
        for path, sha in _watch().pins().items()
        if _blob(UPSTREAM / path) != sha
    ]
    assert not wrong


def test_no_serialisation_or_module_copy_is_kept():
    """The whole-vocabulary Turtle is the one form kept, since the others repeat it."""
    paths = set(_watch().pins())
    assert not [p for p in paths if "-owl.ttl" in p or "/modules/" in p]


@pytest.mark.parametrize(
    "path",
    sorted(SCHEMA_DIR.glob("dpv*.yaml")),
    ids=lambda p: p.stem,
)
def test_each_module_names_the_pinned_edition(path):
    header = yaml.safe_load(path.read_text(encoding="utf-8"))
    watch = _watch()
    assert header["version"] == watch.PINNED_EDITION
    assert header["source"] == watch.PINNED_SOURCE
    assert header["license"] == "Apache-2.0"


def test_the_umbrella_names_the_pinned_release():
    header = yaml.safe_load((SCHEMA_DIR / "dpv.yaml").read_text(encoding="utf-8"))
    watch = _watch()
    annotations = header["annotations"]
    assert annotations["upstream_tag"] == watch.PINNED_TAG
    assert annotations["upstream_commit"] == watch.PINNED_COMMIT
    assert annotations["upstream_release_date"] == watch.PINNED_DATE


def test_the_core_vocabulary_states_the_pinned_edition():
    graph = Graph().parse(UPSTREAM / "2.3" / "dpv" / "dpv.ttl", format="turtle")
    version = graph.value(URIRef("https://w3id.org/dpv"), OWL.versionInfo)
    assert str(version) == _watch().PINNED_EDITION


def test_the_notice_carries_the_licence_the_upstream_requires():
    """DPV's LICENSE.md asks a copy for its notice, and a derivative for a statement of what
    changed, so NOTICE holds both."""
    notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
    assert "W3C Software and Document" in notice
    assert "https://www.w3.org/copyright/software-license-2023/" in notice
    assert "COPYRIGHT HOLDERS WILL NOT BE LIABLE" in notice
    assert "includes material copied from or derived from" in notice
