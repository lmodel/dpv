"""Checks that the adapt copy can sit beside LOKF and the neighbours' copies."""

import hashlib
import json
import keyword
from functools import cache
from pathlib import Path

import jsonschema
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator

from tests import conversion

ROOT = Path(__file__).parent.parent

# What a host may import beside this schema's adapt copy: LOKF's schema, pinned by the
# sidecar, and the adapt copies other lmodel repositories release. Each neighbour is the
# schema asset of a release, downloaded and checked against the release's .sha256 and its
# attestation, and pinned here by that checksum.
SOURCE_DIR = ROOT / "src" / "dpv" / "schema"
COPY = ROOT / ".lokf" / "dpv.yaml"
LOKF = ROOT / ".lokf" / "lokf.yaml"
NEIGHBOURS = {
    # lmodel/slsa v0.10.0
    "slsa.yaml": "9eeb68decc918565886794fe4eb6e32e1fee0620688cc699961c227242a2f4c2",
    # lmodel/github-actions v0.5.0
    "github-actions.yaml": "375794f7343936ae8c555e8c060c2790346661e7d81fa84d15a761fd5a329969",
    # lmodel/in-toto v0.3.0
    "in-toto.yaml": "b1d15be557adfbcd538ab75ec9d43f558027d4bcbd150d72d370e83c9602f25b",
    # lmodel/oscal v0.1.2
    "oscal.yaml": "4eb56d7d1106463ed0a2255a29af14b8d619741acc29863d1e86eb3f8923c710",
    # lmodel/spdx v0.1.1
    "spdx.yaml": "3411cf5d19b1955f0362988c542984e4c817417c7b7b7892647aba1adf1ddd4a",
    # lmodel/nist-sp-800-218 v0.1.1
    "nist-sp-800-218.yaml": "479824cdd95e52226a35ff3a471b7ce93239635ccd5db7ac72a8143cdd1d8495",
    # lmodel/nist-sp-800-53 v0.1.0
    "nist-sp-800-53.yaml": "d32a989b5b855281cb45d707bf59cf52b125f05a09c54930e2b4d45c174c0d99",
    # lmodel/nist-sp-800-171 v0.1.0
    "nist-sp-800-171.yaml": "d204efa6653692da665f8604a8fb8bf445f04b37f41460a5ce2853a014b2982f",
    # lmodel/nist-csf-v2 v0.2.0
    "nist-csf-v2.yaml": "f5819af21a3dbd4bd758987f166831df35aab9942a650156f6873d10d01a0dcc",
    # lmodel/cis-controls v0.2.1
    "cis-controls.yaml": "fbb325b4e55860381293b98f3be9c5b37e12903d3d88228d0e15a761dc80dc98",
    # lmodel/iso27001 v0.1.0
    "iso27001.yaml": "f5ca519043cd994c41f286f84ebc2ea510121bd2129d83c017f73a3d24ee2fe1",
    # lmodel/stix v0.1.0
    "stix.yaml": "3837d097c0cd48e0d2a98d118003c099d1290333f5b973aee85a7017bae344c9",
    # lmodel/attack v0.1.1
    "attack.yaml": "c2e436b0d8ab0e60a8d6557b3ba32894e0b0d23b866f1e0c0d608a97e9f5f08e",
    # lmodel/uco v0.3.0
    "uco.yaml": "78bc3a266fa463ba380da7290adcbdfb1b8e1b7cef1ceb992bf8b1bed9b7b758",
    # lmodel/datatype v0.1.0
    "datatype.yaml": "52fe21c1cd4675b851a26947b69ae9a3b5b68ead592711b23a6552866ec6f933",
    # lmodel/collections v0.2.0
    "collections.yaml": "d750bfbd5be7ddfe40ce26760c76fa7859cbff45cb960913427f0585639dfeb0",
    # lmodel/void v0.1.0
    "void.yaml": "8c21583f49b860e38cc2ee4312a9ef5242300989915bda6fa7a2dd1d0b252051",
    # lmodel/cve v0.1.0
    "cve.yaml": "33e6086a81ac8e4cdc1e6143598cfcc961cbc1864ad9268773da9e863c652a73",
    # lmodel/kev-catalog v0.1.0
    "kev-catalog.yaml": "76bdff7d02cc34ac6a14314692e316b005649a34f442eaf54c2846b1dac5396c",
    # lmodel/nist-nvd v0.1.0
    "nist-nvd.yaml": "69dc8a9b34cc6646cf44515c121c8924c4e07232a9699e31065fb8930ed8be40",
    # lmodel/cwe v0.1.0
    "cwe.yaml": "1b2bb4c1beb089f031adc8861572b98ddf0b42f0ed3c6e5c3bfbc0f767b032cd",
    # lmodel/capec v0.1.0
    "capec.yaml": "613164c0520384919de7d353ff87debb4e82938cec861158d151b41edd506d46",
    # lmodel/d3fend v0.1.0
    "d3fend.yaml": "517a5c8a35b916c1efe4e288151d241d2f350fef38aaec218c4ba7ebea986d08",
    # lmodel/ocsf v0.1.0
    "ocsf.yaml": "b4e033eff09dc3684142308dd70d98926f30a853eb8906f0ad79f6cf1839167d",
    # lmodel/nist-ai-100-1 v0.1.0
    "nist-ai-100-1.yaml": "a9498259b8ff781fa3c24e668f5258146fe1fc4cd6e08c2aac394cb63b76a3c9",
    # lmodel/nist-ai-600-1 v0.1.0
    "nist-ai-600-1.yaml": "4fffc03c0db437256b45ffa6814c54053ffeae06a933b4d4550f94c9ff0494f4",
    # lmodel/gist v0.7.1
    "gist.yaml": "f7283f1c1df4aa6b6e2803e0645c2b1cb2eab37815642a6616d8034feb26d94d",
}
NEIGHBOUR_DIR = ROOT / "tests" / "neighbours"
ELEMENT_KINDS = ("classes", "enums", "types", "subsets")

# Keys the copy shares with a neighbour, each under another IRI, since DPV's properties are
# ordinary words. LinkML merges a composite's imports into one namespace, so a host importing
# such a neighbour beside this copy projects these keys under one IRI, until lokf's adapt can
# rename what a neighbour copy defines (lokf #169). A new overlap fails this test. No class,
# enum or type is shared, since each carries the Dpv prefix.
SHARED_WITH_NEIGHBOURS = {name: set() for name in NEIGHBOURS}
SHARED_WITH_NEIGHBOURS |= {
    "attack.yaml": {"modified", "subject", "value"},
    "cve.yaml": {"format", "value"},
    "d3fend.yaml": {
        "broader",
        "contains",
        "contributor",
        "controls",
        "detects",
        "example",
        "identifier",
        "identifies",
        "issued",
        "modified",
        "modifies",
        "monitors",
        "related",
        "valid",
    },
    "datatype.yaml": {"value"},
    "in-toto.yaml": {"subject", "value"},
    "nist-nvd.yaml": {"format", "value"},
    "ocsf.yaml": {
        "creator",
        "edition",
        "format",
        "properties",
        "resources",
        "subject",
        "value",
    },
    "oscal.yaml": {
        "controls",
        "coverage",
        "identifier",
        "resources",
        "statements",
        "subject",
        "value",
    },
    "slsa.yaml": {"subject", "value"},
    "spdx.yaml": {"identifier", "subject", "value"},
    "stix.yaml": {"modified", "subject", "value"},
    "uco.yaml": {"creator", "format", "language", "properties", "subject", "value"},
    "void.yaml": {"properties"},
}

# The classes `just lokf-adapt` re-roots on Concept. DpvTerm is abstract, and every other
# class with a record's shape sits under it. The value classes stay inlined.
ROOTS = {
    "DpvTerm",
    "DpvVocabulary",
    "DpvConceptScheme",
    "DpvAgent",
    "DpvExample",
    "DpvCatalogue",
}
VALUE_CLASSES = {"DpvWebPage", "DpvInterval", "DpvStatement"}

# What the copy drops for LOKF's id and type, the keys it renames because LOKF has a slot of
# that name under another IRI, and the one it folds into LOKF's own. Each renamed key keeps
# its IRI.
DROPPED = {"id", "rdf_type"}
FOLDED = {"schema_version": "version"}
RENAMED = {
    name: f"dpv_{name}"
    for name in (
        "concepts",
        "created",
        "datatype",
        "definition",
        "description",
        "hasPart",
        "isPartOf",
        "license",
        "memberOf",
        "name",
        "publisher",
        "sameAs",
        "source",
        "title",
        "url",
    )
}


@cache
def _load(path):
    """A schema file, parsed once: the tests read the copy and the neighbours many times and
    change nothing in them."""
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _expander(doc):
    """A function that expands a CURIE by the prefixes a schema file binds."""
    prefixes = doc.get("prefixes") or {}

    def expand(curie):
        prefix, _, local = curie.partition(":")
        return prefixes[prefix] + local if prefix in prefixes else curie

    return expand


@cache
def _names(path):
    """Each kind of element a schema file declares, and every slot and attribute name with
    the IRI it expands to."""
    doc = _load(path)
    expand = _expander(doc)
    default = doc.get("default_prefix")
    elements = {kind: set(doc.get(kind) or {}) for kind in ELEMENT_KINDS}
    slots = {}
    owners = [doc.get("slots") or {}]
    owners += [
        (cls or {}).get("attributes") or {}
        for cls in (doc.get("classes") or {}).values()
    ]
    for owner in owners:
        for name, slot in owner.items():
            uri = (slot or {}).get("slot_uri") or f"{default}:{name}"
            slots.setdefault(name, set()).add(expand(uri))
    return elements, slots


def _source():
    """The modules of the source, merged by element kind."""
    merged = {"classes": {}, "slots": {}, "prefixes": {}, "enums": {}, "types": {}}
    for path in sorted(SOURCE_DIR.glob("*.yaml")):
        doc = _load(path)
        for kind, elements in merged.items():
            elements.update(doc.get(kind) or {})
    return merged


def test_neighbours_are_the_released_assets():
    """Each neighbour copy is byte for byte the file pinned above."""
    assert {p.name for p in NEIGHBOUR_DIR.iterdir()} == set(NEIGHBOURS)
    for name, sha256 in NEIGHBOURS.items():
        digest = hashlib.sha256((NEIGHBOUR_DIR / name).read_bytes()).hexdigest()
        assert digest == sha256, name


def test_names_apart_from_lokf():
    """No class, enum, type or subset name of the copy is LOKF's, and a slot name the two
    share carries LOKF's IRI."""
    elements, slots = _names(COPY)
    their_elements, their_slots = _names(LOKF)
    for kind in ELEMENT_KINDS:
        assert not elements[kind] & their_elements[kind], kind
    for name in slots.keys() & their_slots.keys():
        assert slots[name] == their_slots[name], name


def test_names_apart_from_neighbours():
    """A class, enum, type or subset name is the copy's alone, and the only keys it shares
    with a neighbour under another IRI are the listed ones."""
    elements, slots = _names(COPY)
    for name in NEIGHBOURS:
        their_elements, their_slots = _names(NEIGHBOUR_DIR / name)
        for kind in ELEMENT_KINDS:
            assert not elements[kind] & their_elements[kind], (name, kind)
        differ = {
            key
            for key in slots.keys() & their_slots.keys()
            if slots[key] != their_slots[key]
        }
        assert differ == SHARED_WITH_NEIGHBOURS[name], name


def test_the_copy_drops_and_renames_only_what_is_named():
    """The copy keeps each class and slot of the source, but for the keys it drops for
    LOKF's id and type and the keys it renames, and a renamed key keeps its IRI."""
    source, copy = _source(), _load(COPY)
    assert set(copy["classes"]) == set(source["classes"])
    expected = {RENAMED.get(name, name) for name in source["slots"]} - DROPPED - set(FOLDED)
    assert set(copy["slots"]) == expected
    expand_source = _expander({"prefixes": source["prefixes"]})
    expand_copy = _expander(copy)
    for old, new in RENAMED.items():
        uri = source["slots"][old].get("slot_uri", f"dpv_linkml:{old}")
        assert expand_copy(copy["slots"][new]["slot_uri"]) == expand_source(uri), old


def test_copy_roots_the_concept_classes():
    """The copy re-roots exactly the classes with an identifier on Concept, keeps every kind
    under DpvConcept, and imports nothing but the LinkML types and LOKF."""
    doc = _load(COPY)
    rooted = {
        name for name, cls in doc["classes"].items() if cls.get("is_a") == "Concept"
    }
    assert rooted == ROOTS
    assert doc["imports"] == ["linkml:types", "lokf"]
    assert not doc["classes"]["DpvCatalogue"].get("tree_root")
    for name, cls in doc["classes"].items():
        if name in ROOTS | VALUE_CLASSES:
            continue
        walk = name
        while doc["classes"][walk].get("is_a") != "Concept":
            walk = doc["classes"][walk]["is_a"]
        assert walk == "DpvTerm", name


def concept_types():
    """Every class a concept may name as its type."""
    return sorted(set(_load(COPY)["classes"]) - VALUE_CLASSES - {"DpvTerm"})


def test_the_readme_lists_the_concept_types():
    """The README's Known LOKF types block names each class a concept may use."""
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for name in concept_types():
        assert name in readme, name


def test_the_schema_states_no_mapping_of_its_own():
    """A term's class is its own IRI, and the only mappings are DPV's own, which sit in
    src/dpv/mappings/, so the copy holds none whose prefix a projection could lack."""
    def mappings(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key.endswith("_mappings") or key == "mappings":
                    yield value
                else:
                    yield from mappings(value)
        elif isinstance(node, list):
            for item in node:
                yield from mappings(item)

    assert not list(mappings(_load(COPY)))


def _page_names(source):
    """The name of each page gen-doc writes for an element of the source."""
    names = set(source["classes"]) | set(source["enums"]) | set(source["slots"])
    names |= {
        "".join(part.title() for part in name.split("_")) for name in source["types"]
    }
    for cls in source["classes"].values():
        names |= set(cls.get("attributes") or {})
    return names


def test_no_two_pages_differ_only_by_case():
    """gen-doc writes a page per element, and two names that differ only by case are one
    file on a case-insensitive disk. A slot is camelCase and every class, enum and type
    carries this schema's prefix, so no two can."""
    lowered = {}
    for name in _page_names(_source()):
        lowered.setdefault(name.lower(), set()).add(name)
    assert not {key: found for key, found in lowered.items() if len(found) > 1}


def test_no_page_collides_with_linkmls_types():
    linkml_types = {
        "Boolean", "Curie", "Date", "DateOrDatetime", "Datetime", "Decimal", "Double",
        "Float", "Integer", "Jsonpath", "Jsonpointer", "Ncname", "Nodeidentifier",
        "Objectidentifier", "Sparqlpath", "String", "Time", "Uri", "Uriorcurie",
        "boolean", "curie", "date", "datetime", "decimal", "double", "float", "integer",
        "ncname", "string", "time", "uri", "uriorcurie",
    }  # fmt: skip
    assert not _page_names(_source()) & linkml_types


def test_no_page_overwrites_the_index():
    assert "index" not in {name.lower() for name in _page_names(_source())}


def test_no_slot_is_a_python_keyword():
    """A slot named after a Python keyword breaks the generated dataclasses."""
    source = _source()
    slots = set(source["slots"])
    for cls in source["classes"].values():
        slots |= set(cls.get("attributes") or {})
    assert not {name for name in slots if keyword.iskeyword(name)}


@cache
def _concept_schema():
    """The JSON Schema of the adapt copy, as `lokf validate` reads it beside LOKF."""
    generator = JsonSchemaGenerator(str(COPY), mergeimports=True)
    return json.loads(generator.serialize())["$defs"]


def _concept_from(record, class_name):
    """A record of the catalogue in the copy's keys, with LOKF's id, type, title and
    description beside what it holds."""

    def renamed(value):
        if isinstance(value, dict):
            return {RENAMED.get(k, k): renamed(v) for k, v in value.items()}
        return [renamed(v) for v in value] if isinstance(value, list) else value

    concept = {}
    for key, value in record.items():
        if key not in DROPPED:
            concept[FOLDED.get(key, RENAMED.get(key, key))] = renamed(value)
    concept.update(
        type=class_name,
        id=f"https://example.org/knowledge/{class_name}",
        title="A title",
        description="A description.",
    )
    return concept


def test_a_concept_of_each_kind_validates_against_the_copy():
    """Each kind admits a real record of its kind, and refuses a key it does not hold."""
    definitions = _concept_schema()
    terms = conversion.terms()
    for name, cls in _load(COPY)["classes"].items():
        uri = cls.get("class_uri")
        record = next(
            (r for r in terms.values() if uri and uri in r.get("rdf_type", ())), None
        )
        if record is None:
            continue
        schema = {"$ref": f"#/$defs/{name}", "$defs": definitions}
        validator = jsonschema.validators.validator_for(schema)(schema)
        concept = _concept_from(record, name)
        errors = [e.message[:160] for e in validator.iter_errors(concept)]
        assert not errors, (name, errors)
        concept["hasPurposes"] = ["dpv:Marketing"]
        assert list(validator.iter_errors(concept)), (name, "is closed")


def test_a_resource_concept_holds_any_property():
    """A concept of DpvResource carries DPV's properties, under the keys DPV's terms name."""
    definitions = _concept_schema()
    schema = {"$ref": "#/$defs/DpvResource", "$defs": definitions}
    validator = jsonschema.validators.validator_for(schema)(schema)
    concept = _concept_from(
        {"hasPurpose": ["dpv:Marketing"], "hasPersonalData": ["pd:EmailAddress"]}, "DpvResource"
    )
    assert not list(validator.iter_errors(concept))
