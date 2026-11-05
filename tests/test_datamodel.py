"""Checks what the generated models do with real data.

The Pydantic models and the dataclasses load each file of the catalogue, and a concept as
the class of each kind. RDF goes through JSON-LD with the generated context, which is how
tests/test_catalogue.py compares the catalogue with the Turtle.
"""

import json

import pytest
import yaml
from linkml_runtime.loaders import json_loader

from dpv.datamodel import dpv as dataclasses_module
from dpv.datamodel import dpv_pydantic
from tests import conversion


@pytest.mark.parametrize("family", conversion.FAMILIES)
def test_each_file_loads_into_the_pydantic_models(family):
    document = conversion.documents()[family]
    model = dpv_pydantic.DpvCatalogue(**document)
    for key in ("concepts", "properties", "vocabularies", "agents", "examples"):
        assert len(getattr(model, key) or []) == len(document.get(key, []))


@pytest.mark.parametrize("family", ["core", "standards", "agents", "examples"])
def test_each_file_loads_into_the_dataclasses(family):
    """The locations and the laws load the same way and take a minute, so these four stand
    for them, and between them hold every slot's form."""
    document = conversion.documents()[family]
    model = json_loader.loads(json.dumps(document), target_class=dataclasses_module.DpvCatalogue)
    assert len(model.concepts or []) == len(document.get("concepts", []))
    assert len(model.examples or []) == len(document.get("examples", []))


def test_a_kinds_class_takes_a_real_record():
    """A class of each kind is DPV's: the Pydantic class of dpv:Purpose takes its instances."""
    record = conversion.terms()["dpv:Marketing"]
    assert dpv_pydantic.DpvPurpose(**record).broader == ["dpv:Purpose"]
    assert issubclass(dpv_pydantic.DpvSpecialCategoryPersonalData, dpv_pydantic.DpvPersonalData)
    assert dpv_pydantic.DpvPurpose.linkml_meta["class_uri"] == "dpv:Purpose"


def test_a_resource_takes_any_property():
    """DPV states no property as limited to a class, so a resource holds any of them."""
    resource = dpv_pydantic.DpvResource(
        id="ex:P", hasPurpose=["dpv:Marketing"], hasName=["Acme"], tech_hasCapability=["ex:C"]
    )
    assert resource.hasPurpose == ["dpv:Marketing"]
    with pytest.raises(ValueError):
        dpv_pydantic.DpvResource(id="ex:P", hasPurposes=["dpv:Marketing"])


def test_the_example_data_parses_as_yaml_everywhere():
    """A record's text keeps its line breaks through the writer's block style."""
    described = next(
        e for e in conversion.documents()["examples"]["examples"] if e["id"] == "dex:E0001"
    )
    assert yaml.safe_load(yaml.safe_dump(described)) == described
    assert "\n" in described["description"]
