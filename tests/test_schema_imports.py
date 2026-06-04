"""Regression tests for cross-schema class-name collisions.

Importing the DPV ``ai`` extension together with ``dpv_personal_data``
used to fail with ``ValueError: Conflicting URIs ... for item: DpvData``
because both schemas declared a LinkML class literally named ``DpvData``
with different ``class_uri`` values (``ai:Data`` vs. ``dpv:Data``).
The DPV-LinkML generators were updated so each extension prefixes its
collision-prone class names with its own PascalCase slug (``AiData``,
``PdCountry``, ``TechService``, ...) while core ``dpv_*`` schemas keep
the ``Dpv`` prefix.

These tests guard against re-introduction of such collisions and
verify that every generated schema under ``src/dpv/schema/**`` loads
cleanly via ``SchemaView``.
"""

from __future__ import annotations

import glob
import json
from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_ROOT = REPO_ROOT / "src" / "dpv" / "schema"
IMPORTMAP_PATH = REPO_ROOT / "importmap.json"

ALL_SCHEMAS = sorted(glob.glob(str(SCHEMA_ROOT / "**" / "*.yaml"), recursive=True))


@pytest.fixture(scope="session")
def importmap() -> dict[str, str]:
    """Absolute-path import map so SchemaView resolves ``dpv:schema/...``
    imports against the on-disk source tree rather than HTTP-fetching
    ``https://w3id.org/lmodel/dpv/...``.
    """
    raw = json.loads(IMPORTMAP_PATH.read_text())
    return {k: str((REPO_ROOT / v).resolve()) for k, v in raw.items()}


def _load(path: str, importmap: dict[str, str]) -> SchemaView:
    return SchemaView(path, importmap=importmap)


@pytest.mark.parametrize(
    "schema_path",
    ALL_SCHEMAS,
    ids=lambda p: Path(p).relative_to(SCHEMA_ROOT).as_posix(),
)
def test_schema_loads_without_collision(
    schema_path: str, importmap: dict[str, str]
) -> None:
    """Every schema (with its import closure) must load via SchemaView."""
    sv = _load(schema_path, importmap)
    # Force resolution of the full class set — this is what raises
    # ``ValueError: Conflicting URIs`` on collisions.
    classes = sv.all_classes()
    assert classes, f"no classes resolved for {schema_path}"


def test_dpv_data_collision_resolved(importmap: dict[str, str]) -> None:
    """``ai:Data`` (renamed ``AiData``) and ``dpv:Data`` (``DpvData``) coexist.

    Reproduces the originally reported failure: importing the AI extension
    (which transitively imports ``dpv_personal_data``) used to fail because
    both schemas declared ``DpvData``.
    """
    sv = _load(str(SCHEMA_ROOT / "extensions" / "ai.yaml"), importmap)
    classes = sv.all_classes()

    assert "AiData" in classes
    assert "DpvData" in classes
    assert sv.get_class("AiData").class_uri == "ai:Data"
    assert sv.get_class("DpvData").class_uri == "dpv:Data"


@pytest.mark.parametrize(
    "schema_rel,own_name,core_name,own_uri,core_uri",
    [
        ("extensions/pd.yaml", "PdCountry", "DpvCountry", "pd:Country", "dpv:Country"),
        ("extensions/pd.yaml", "PdLocation", "DpvLocation", "pd:Location", "dpv:Location"),
        ("extensions/pd.yaml", "PdRegion", "DpvRegion", "pd:Region", "dpv:Region"),
        ("extensions/tech.yaml", "TechService", "DpvService", "tech:Service", "dpv:Service"),
    ],
)
def test_extension_collision_pairs_coexist(
    schema_rel: str,
    own_name: str,
    core_name: str,
    own_uri: str,
    core_uri: str,
    importmap: dict[str, str],
) -> None:
    """Per-extension renames keep collision-prone classes distinct from core."""
    sv = _load(str(SCHEMA_ROOT / schema_rel), importmap)
    classes = sv.all_classes()
    assert own_name in classes
    assert core_name in classes
    assert sv.get_class(own_name).class_uri == own_uri
    assert sv.get_class(core_name).class_uri == core_uri


def test_merged_schema_loads_without_collision(
    importmap: dict[str, str]
) -> None:
    """Loading the pre-merged ``tmp/dpv.yaml`` (which flattens every core
    group AND every extension into a single self-contained schema) must
    not raise ``ValueError: Conflicting URIs``.

    This is the build artefact ``gen-project`` consumes — it's the only
    surface where two sibling trees (e.g. a core semantic group and an
    unrelated extension) end up in the same ``SchemaView``. The
    per-schema parametrized loads above don't surface cross-tree
    collisions because each extension's import closure may shadow the
    colliding core group locally.

    Example of the class this test catches: ``ai:RiskConcept`` vs.
    ``dpv:RiskConcept`` (both originally emitted as ``RiskConcept`` and
    only colliding in the merged build).
    """
    merged = REPO_ROOT / "tmp" / "dpv.yaml"
    if not merged.exists():
        pytest.skip(f"merged schema not built; run `just _merged-schema`: {merged}")
    sv = _load(str(merged), importmap)
    classes = sv.all_classes()
    assert classes, "merged schema resolved no classes"


def test_ai_risk_concept_collision_resolved(importmap: dict[str, str]) -> None:
    """``ai:RiskConcept`` (renamed ``AiRiskConcept``) coexists with core
    ``dpv:RiskConcept``.

    Reproduces the second collision discovered after the ``DpvData`` fix:
    AI redefined ``RiskConcept`` locally and ``extensions/ai.yaml`` imports
    ``dpv:schema/dpv_risk_notice``, so both arrive in the same
    ``SchemaView``. Pre-fix, this raised
    ``ValueError: Conflicting URIs ... for item: RiskConcept``. The
    generator now dynamically detects core class-name shadowing and
    auto-prefixes such extension classes with the extension's pascal slug.
    """
    sv = _load(str(SCHEMA_ROOT / "extensions" / "ai.yaml"), importmap)
    classes = sv.all_classes()
    assert "AiRiskConcept" in classes
    assert "RiskConcept" in classes
    assert sv.get_class("AiRiskConcept").class_uri == "ai:RiskConcept"
    assert sv.get_class("RiskConcept").class_uri == "dpv:RiskConcept"
