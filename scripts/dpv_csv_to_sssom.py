#!/usr/bin/env python3
"""Convert DPV mapping CSVs to SSSOM TSVs.

Reads the CSV mapping tables vendored under
``upstream-releases/mappings/<source>/dpv-<source>.csv`` and emits
SSSOM-compliant TSV files under ``src/dpv/mappings/``:

* ``dpv-iso.sssom.tsv``  - DPV ↔ ISO/IEC 29100 mappings
* ``dpv-odrl.sssom.tsv`` - DPV ↔ ODRL mappings

Discovery is data-driven: each ``<source>/`` subdirectory containing a
``dpv-<source>.csv`` is processed if a converter is registered for it.
Unknown sources are skipped with a warning so adding a new vocabulary is a
matter of registering a converter in ``CONVERTERS``.

Each TSV starts with an SSSOM YAML metadata block (``#``-prefixed lines) and
the canonical SSSOM columns: ``subject_id``, ``subject_label``,
``predicate_id``, ``object_id``, ``object_label``, ``mapping_justification``,
``mapping_source``. See https://mapping-commons.github.io/sssom/.

Idempotent: rows are sorted on (subject_id, object_id) so re-running with the
same inputs produces byte-identical TSVs.

Usage::

    uv run python scripts/csv_to_sssom.py \\
        [-i upstream-releases/mappings] [-o src/dpv/mappings]
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Iterable

# Curie map embedded in the SSSOM header. The full IRI for each prefix lets
# downstream SSSOM tools resolve subject_id / object_id without ambiguity.
CURIE_MAP = {
    "dpv": "https://w3id.org/lmodel/dpv/",
    "dpv_upstream": "https://w3id.org/dpv#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "iso29100": "https://w3id.org/lmodel/iso29100/",
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "semapv": "https://w3id.org/semapv/vocab/",
}

# SKOS predicate inversion table. Applied when flipping a published mapping
# row so that DPV (the publisher of this mapping set) sits on the subject
# side, per SSSOM convention.
_SKOS_INVERSE = {
    "skos:exactMatch":   "skos:exactMatch",
    "skos:closeMatch":   "skos:closeMatch",
    "skos:relatedMatch": "skos:relatedMatch",
    "skos:broadMatch":   "skos:narrowMatch",
    "skos:narrowMatch":  "skos:broadMatch",
    "skos:broader":      "skos:narrower",
    "skos:narrower":     "skos:broader",
    "skos:related":      "skos:related",
}


def _invert_predicate(pred: str) -> str:
    """Return the SKOS-inverse of ``pred`` (identity for unknown predicates)."""
    return _SKOS_INVERSE.get(pred, pred)

SSSOM_COLUMNS = [
    "subject_id",
    "subject_label",
    "predicate_id",
    "object_id",
    "object_label",
    "mapping_justification",
    "mapping_source",
]


def render_header(meta: dict[str, str | dict[str, str]]) -> str:
    """Serialize the SSSOM YAML metadata block as ``#``-prefixed lines."""
    lines: list[str] = []
    for key, value in meta.items():
        if isinstance(value, dict):
            lines.append(f"# {key}:")
            for k, v in value.items():
                lines.append(f"#   {k}: {v}")
        else:
            lines.append(f"# {key}: {value}")
    return "\n".join(lines) + "\n"


def write_tsv(
    path: Path,
    meta: dict[str, str | dict[str, str]],
    rows: Iterable[dict[str, str]],
) -> bool:
    """Write TSV with deterministic ordering; return True if file changed."""
    rows_sorted = sorted(
        rows, key=lambda r: (r["subject_id"], r["object_id"])
    )
    buf: list[str] = [render_header(meta)]
    buf.append("\t".join(SSSOM_COLUMNS))
    for r in rows_sorted:
        buf.append("\t".join(r.get(col, "") for col in SSSOM_COLUMNS))
    content = "\n".join(buf) + "\n"

    if path.exists() and path.read_text() == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return True


# ---------------------------------------------------------------------------
# ISO 29100
# ---------------------------------------------------------------------------

def convert_iso(src: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with src.open(newline="") as fh:
        for r in csv.DictReader(fh):
            ext = r["ExternalConcept"].strip()
            ext_label = r["Label"].strip()
            pred = r["Mapping"].strip()
            dpv_obj = r["DPV"].strip()
            # Rewrite upstream canonical CURIEs to this repo's local prefix.
            if dpv_obj.startswith("dpv:"):
                dpv_obj = "dpv:" + dpv_obj[len("dpv:"):]
            rows.append({
                "subject_id": dpv_obj,
                "subject_label": "",
                "predicate_id": _invert_predicate(pred),
                "object_id": f"iso29100:{ext}",
                "object_label": ext_label,
                "mapping_justification": "semapv:ManualMappingCuration",
                "mapping_source": r["Source"].strip(),
            })
    return rows


# ---------------------------------------------------------------------------
# ODRL
# ---------------------------------------------------------------------------

def convert_odrl(src: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with src.open(newline="") as fh:
        for r in csv.DictReader(fh):
            ext = r["ExternalConcept"].strip()
            pred = r["MappingType"].strip()
            dpv_obj = r["DPVconcept"].strip()
            if dpv_obj.startswith("dpv:"):
                dpv_obj = "dpv:" + dpv_obj[len("dpv:"):]
            rows.append({
                "subject_id": dpv_obj,
                "subject_label": "",
                "predicate_id": _invert_predicate(pred),
                "object_id": ext,
                "object_label": "",
                "mapping_justification": "semapv:ManualMappingCuration",
                "mapping_source": "https://www.w3.org/TR/odrl-vocab/",
            })
    return rows


# Registry of supported mapping sources. To add a new vocabulary, drop the
# CSV into upstream-releases/mappings/<source>/dpv-<source>.csv and register
# a converter + description here.
CONVERTERS: dict[str, dict] = {
    "iso": {
        "convert": lambda p: convert_iso(p),
        "description": "DPV ↔ ISO/IEC 29100:2024 term alignments (curated upstream).",
    },
    "odrl": {
        "convert": lambda p: convert_odrl(p),
        "description": "DPV ↔ ODRL term alignments (curated upstream).",
    },
}


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "-i", "--input-dir", type=Path,
        default=repo_root / "upstream-releases" / "mappings",
        help="Directory containing <source>/dpv-<source>.csv files.",
    )
    parser.add_argument(
        "-o", "--output-dir", type=Path,
        default=repo_root / "src" / "dpv" / "mappings",
        help="Output directory for SSSOM TSVs.",
    )
    args = parser.parse_args()

    common_meta = {
        "mapping_set_version": "1.0",
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "curie_map": CURIE_MAP,
    }

    if not args.input_dir.is_dir():
        print(f"error: input dir not found: {args.input_dir}", file=sys.stderr)
        sys.exit(1)

    changed = 0
    total = 0
    skipped: list[str] = []

    # Discover candidate sources: any subdir with a dpv-<name>.csv file.
    for sub in sorted(p for p in args.input_dir.iterdir() if p.is_dir()):
        csv_path = sub / f"dpv-{sub.name}.csv"
        if not csv_path.exists():
            continue
        spec = CONVERTERS.get(sub.name)
        if spec is None:
            skipped.append(sub.name)
            continue
        total += 1
        meta = {
            "mapping_set_id": f"https://w3id.org/lmodel/dpv/mappings/dpv-{sub.name}",
            "mapping_set_description": spec["description"],
            **common_meta,
        }
        out = args.output_dir / f"dpv-{sub.name}.sssom.tsv"
        if write_tsv(out, meta, spec["convert"](csv_path)):
            changed += 1
            print(f"wrote: {out}", file=sys.stderr)
        else:
            print(f"unchanged: {out}", file=sys.stderr)

    if skipped:
        print(
            f"skip: no converter registered for {sorted(skipped)} "
            f"(add an entry to CONVERTERS in {Path(__file__).name})",
            file=sys.stderr,
        )

    print(
        f"csv_to_sssom: wrote/updated {changed}/{total} mapping set(s)",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
