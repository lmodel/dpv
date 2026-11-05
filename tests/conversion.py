"""The Turtle and the catalogue, for the tests that read them.

scripts/dpv_to_linkml.py is not a package, so it is loaded by its path. Parsing the Turtle
takes about ten seconds and so does reading the catalogue, so each test module shares one
copy and must not change it.
"""

import importlib.util
import sys
from functools import cache
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "dpv_to_linkml.py"
SCHEMA_DIR = ROOT / "src" / "dpv" / "schema"
SCHEMA = SCHEMA_DIR / "dpv.yaml"
DATA_DIR = ROOT / "src" / "dpv" / "data"
FAMILIES = (
    "core",
    "pd",
    "tech",
    "ai",
    "risk",
    "justifications",
    "loc",
    "legal",
    "sector",
    "standards",
    "agents",
    "examples",
)


def _load():
    spec = importlib.util.spec_from_file_location("dpv_to_linkml", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


CONVERTER = _load()
# The C loader reads the catalogue in a fifth of the time, where the build has it.
LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def graph():
    """The Turtle, parsed once."""
    return CONVERTER.load()


@cache
def documents():
    """Each committed data file, by family, read once."""
    return {
        family: yaml.load(
            CONVERTER.data_path(family).read_text(encoding="utf-8"), Loader=LOADER
        )
        for family in FAMILIES
    }


@cache
def records(key):
    """Every record a key of the data files holds, by id, such as concepts or agents."""
    return {
        record["id"]: record
        for document in documents().values()
        for record in document.get(key, ())
    }


@cache
def terms():
    """Every concept and every property, by id."""
    return {**records("concepts"), **records("properties")}


@cache
def modules():
    """Each committed module of the schema, by file stem."""
    return {
        path.stem: yaml.load(path.read_text(encoding="utf-8"), Loader=LOADER)
        for path in sorted(SCHEMA_DIR.glob("dpv*.yaml"))
    }


@cache
def all_slots():
    """Each top-level slot of the schema, by name."""
    return {
        name: slot
        for module in modules().values()
        for name, slot in module.get("slots", {}).items()
    }


@cache
def all_classes():
    """Each class of the schema, by name."""
    return {
        name: cls
        for module in modules().values()
        for name, cls in module.get("classes", {}).items()
    }
