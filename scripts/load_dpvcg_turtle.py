#!/usr/bin/env python3
"""Load DPV example snippets into LinkML test fixtures.

Reads the curated ``examples/E*.ttl`` files at the repository root, wraps each
fragment in a self-contained Turtle document (prepending the standard DPV
prefix preamble), and writes them to ``linkml/tests/data/dpvcg/``:

* ``valid/<stem>.ttl``    - clean, round-trippable RDF
* ``problem/<stem>-problem-<n>.ttl`` - chunks tagged ``# problem:`` upstream
* ``invalid/``            - reserved for SHACL-failing fixtures (placeholder)

Idempotent: same inputs produce byte-identical outputs. Each emitted file is
parsed with rdflib as a sanity check; failures are reported on stderr.

Usage::

    uv run python scripts/load_examples.py [-i ../examples] [-o tests/data/dpvcg]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import rdflib

PREAMBLE = """\
@prefix : <https://example.org/dpv/default#> .
@prefix bibo: <http://purl.org/ontology/bibo/> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix dex: <https://w3id.org/dpv/examples#> .
@prefix dpv: <https://w3id.org/lmodel/dpv> .
@prefix dpv_upstream: <https://w3id.org/dpv#> .
@prefix eu-gdpr: <https://w3id.org/dpv/legal/eu/gdpr#> .
@prefix ex: <https://example.org/dpv/ex#> .
@prefix exA: <https://example.org/dpv/exA#> .
@prefix exB: <https://example.org/dpv/exB#> .
@prefix extension: <https://w3id.org/dpv/extension#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix justifications: <https://w3id.org/dpv/justifications#> .
@prefix legal-eu: <https://w3id.org/dpv/legal/eu#> .
@prefix legal-ie: <https://w3id.org/dpv/legal/ie#> .
@prefix loc: <https://w3id.org/dpv/loc#> .
@prefix nace: <https://w3id.org/dpv/nace#> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix org: <http://www.w3.org/ns/org#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix pd: <https://w3id.org/dpv/pd#> .
@prefix profile: <http://www.w3.org/ns/dx/prof/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix risk: <https://w3id.org/dpv/risk#> .
@prefix schema: <https://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix tech: <https://w3id.org/dpv/tech#> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
"""

PROBLEM_RE = re.compile(r"^\s*#\s*problem\b", re.IGNORECASE)
SOLUTION_RE = re.compile(r"^\s*#\s*(solution|valid|fix)\b", re.IGNORECASE)


def split_chunks(text: str) -> tuple[str, list[str]]:
    """Return (valid_text, [problem_chunks]).

    Chunks beginning with a ``# problem`` comment line and ending at the
    next ``# solution`` / ``# valid`` / ``# problem`` marker (or EOF) are
    pulled into the problem list. Everything else stays in valid.
    """
    lines = text.splitlines(keepends=True)
    valid: list[str] = []
    problems: list[list[str]] = []
    current: list[str] | None = None

    for line in lines:
        if PROBLEM_RE.match(line):
            if current is not None:
                problems.append(current)
            current = [line]
        elif current is not None and SOLUTION_RE.match(line):
            problems.append(current)
            current = None
            valid.append(line)
        elif current is not None:
            current.append(line)
        else:
            valid.append(line)

    if current is not None:
        problems.append(current)

    return "".join(valid), ["".join(c) for c in problems]


def wrap(body: str) -> str:
    """Prepend the prefix preamble and ensure a single trailing newline."""
    body = body.rstrip() + "\n"
    return PREAMBLE + "\n" + body


def write_if_changed(path: Path, content: str) -> bool:
    """Write only when content differs; return True if changed."""
    if path.exists() and path.read_text() == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return True


def parses(content: str) -> bool:
    try:
        rdflib.Graph().parse(data=content, format="turtle")
    except Exception:  # noqa: BLE001
        return False
    return True


def main() -> None:
    linkml_root = Path(__file__).resolve().parent.parent
    dpv_repo_root = linkml_root.parent

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "-i", "--input-dir", type=Path,
        default=dpv_repo_root / "examples",
        help="Directory containing E*.ttl fragments.",
    )
    parser.add_argument(
        "-o", "--output-dir", type=Path,
        default=linkml_root / "tests" / "data" / "dpvcg",
        help="Output root with valid/, invalid/, problem/ subdirs.",
    )
    args = parser.parse_args()

    if not args.input_dir.exists():
        parser.error(f"Input directory does not exist: {args.input_dir}")

    valid_dir = args.output_dir / "valid"
    invalid_dir = args.output_dir / "invalid"
    problem_dir = args.output_dir / "problem"
    for d in (valid_dir, invalid_dir, problem_dir):
        d.mkdir(parents=True, exist_ok=True)

    # Placeholder so the invalid/ folder is tracked even when empty.
    placeholder = invalid_dir / ".gitkeep"
    if not placeholder.exists():
        placeholder.write_text("")

    n_valid = n_problem = n_skipped = 0
    written: set[Path] = set()

    for src in sorted(args.input_dir.glob("E*.ttl")):
        text = src.read_text()
        valid_body, problem_chunks = split_chunks(text)

        if valid_body.strip():
            content = wrap(valid_body)
            # Route to valid/ when the wrapped snippet round-trips through
            # rdflib; otherwise the snippet is intentionally fragmentary or
            # malformed and belongs in problem/ for downstream review.
            target_dir = valid_dir if parses(content) else problem_dir
            out = target_dir / f"{src.stem}.ttl"
            if write_if_changed(out, content):
                if target_dir is valid_dir:
                    n_valid += 1
                else:
                    n_problem += 1
            written.add(out)
        else:
            n_skipped += 1

        for i, chunk in enumerate(problem_chunks, 1):
            content = wrap(chunk)
            out = problem_dir / f"{src.stem}-problem-{i}.ttl"
            if write_if_changed(out, content):
                n_problem += 1
            written.add(out)

    # Prune stale fixtures from earlier runs to keep the tree deterministic.
    for d in (valid_dir, problem_dir):
        for existing in d.glob("E*.ttl"):
            if existing not in written:
                existing.unlink()

    print(
        f"load_examples: valid={n_valid} problem={n_problem} skipped={n_skipped}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
