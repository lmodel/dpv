"""Checks the JSON Schema this project commits, as a user of it would read it.

project/jsonschema/dpv.schema.json is what a consumer without LinkML validates with. It is
read here under the draft it declares, and held to the generator's settings in
.linkml/generators.yaml.
"""

import json
from functools import cache
from pathlib import Path

import jsonschema
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator

ROOT = Path(__file__).parent.parent
COMMITTED = ROOT / "project" / "jsonschema" / "dpv.schema.json"
SCHEMA = ROOT / "src" / "dpv" / "schema" / "dpv.yaml"


@cache
def schema():
    return json.loads(COMMITTED.read_text(encoding="utf-8"))


def _validator():
    return jsonschema.validators.validator_for(schema())(schema())


def test_the_schema_is_valid_under_the_draft_it_declares():
    jsonschema.validators.validator_for(schema()).check_schema(schema())


def test_the_committed_file_is_the_generators_output():
    """A schema edit without `just gen-project` fails here."""
    settings = yaml.safe_load((ROOT / ".linkml" / "generators.yaml").read_text())
    args = settings["generator_args"]["jsonschema"]
    generated = JsonSchemaGenerator(str(SCHEMA), **args).serialize()
    assert json.loads(generated) == schema()


def test_the_top_of_the_schema_is_the_catalogue():
    """The file's root takes one part of a release, and refuses any other key."""
    assert schema()["title"] == "dpv"
    assert schema()["version"] == "2.3"
    assert not _validator().is_valid({"edition": "2.3"})
    assert not _validator().is_valid({"edition": "2.3", "family": "core", "x": 1})
    assert _validator().is_valid({"edition": "2.3", "family": "core"})


def test_a_concept_is_one_shape_whatever_its_kind():
    """A kind adds no slot, so the list of concepts does not try each kind in turn, which
    would make a validator take minutes over the locations."""
    concepts = schema()["$defs"]["DpvCatalogue"]["properties"]["concepts"]
    assert concepts["items"] == {"$ref": "#/$defs/DpvConcept"}
    concept = schema()["$defs"]["DpvConcept"]["properties"]
    purpose = schema()["$defs"]["DpvPurpose"]["properties"]
    assert concept == purpose


def test_a_reference_must_look_like_one():
    """LinkML renders a reference as a string with no format, so each slot carries a pattern
    of its own, and free text in one fails."""
    props = schema()["$defs"]["DpvResource"]["properties"]
    assert "pattern" in props["hasPurpose"]["items"]
    assert "pattern" in props["broader"]["items"]
    assert "pattern" not in props["hasName"]["items"]
