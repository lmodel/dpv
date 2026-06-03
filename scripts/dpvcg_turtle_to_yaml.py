#!/usr/bin/env python3
"""Transform DPV-CG Turtle fixtures into LinkML-validatable YAML.

Reads the wrapped Turtle fixtures produced by ``load_examples.py`` (under
``tests/data/dpvcg/valid/``) and emits one YAML document per typed root
subject under ``tests/data/dpvcg/valid/<ClassName>-<stem>-<n>.yaml`` so that
the standard ``tests/test_data.py`` runner (which keys class on filename
stem) can validate them against the generated ``dpv`` datamodel.

Mapping strategy (no guessing):

* A *class index* is built from every YAML file under
  ``src/dpv/schema/`` by recording each class's identity URI
  (``class_uri``) **and** its ``exact_mappings`` aliases. Both the canonical
  ``dpv:`` (W3C SKOS) and ``dpv_owl:`` upstream OWL CURIEs resolve via the
  exact-mappings path; the LinkML element name (PascalCase) is what we
  emit as the filename prefix.
* A *slot index* is built the same way over schema-level ``slots:`` and
  per-class ``attributes:``. The LinkML slot name (snake_case YAML key)
  is what we emit as the field name in the output YAML.

Subjects with no matching class (e.g. ``ex:CampaignA`` typed only as
``dpv:Purpose``) **are** emitted, anchored on the matched class.
Properties with no matching slot are preserved as a leading YAML
comment block (``# __unmapped__: ...``) so the file remains loadable
by the generated Pydantic / dataclass models while keeping the
triples visible for downstream curation.

Idempotent: re-running with unchanged inputs and schema produces
byte-identical YAML.

Usage::

    uv run python scripts/ttl_to_yaml.py \\
        [-s src/dpv/schema] \\
        [-i tests/data/dpvcg/valid] \\
        [-o tests/data/dpvcg/valid]
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import rdflib
import yaml
from rdflib import BNode, Graph, Literal, URIRef
from rdflib.namespace import RDF

# Same local/upstream/OWL DPV namespaces the generator uses.
DPV_LOCAL_NS = "https://w3id.org/lmodel/dpv/"
DPV_CAN_NS = "https://w3id.org/dpv#"
DPV_OWL_NS = "https://w3id.org/dpv/owl#"
LMODEL_DPV_NS = "https://w3id.org/lmodel/dpv/"


# ---------------------------------------------------------------------------
# Schema indexing
# ---------------------------------------------------------------------------

def _expand_curie(curie: str, prefixes: dict[str, str]) -> str | None:
    """Expand a CURIE using the schema's prefix table; return None on miss."""
    if ":" not in curie or curie.startswith(("http://", "https://")):
        return curie if curie.startswith(("http://", "https://")) else None
    prefix, _, local = curie.partition(":")
    base = prefixes.get(prefix)
    return base + local if base else None


def _collect_uris(
    element: dict, prefixes: dict[str, str], identity_key: str
) -> list[str]:
    """Return every full IRI that identifies this element (identity + maps)."""
    uris: list[str] = []
    if identity_key in element:
        expanded = _expand_curie(element[identity_key], prefixes)
        if expanded:
            uris.append(expanded)
    for mapping_key in ("exact_mappings", "close_mappings", "narrow_mappings"):
        for curie in element.get(mapping_key, []) or []:
            expanded = _expand_curie(curie, prefixes)
            if expanded:
                uris.append(expanded)
    return uris


def build_indexes(schema_dir: Path) -> tuple[dict[str, str], dict[str, str]]:
    """Walk every ``*.yaml`` in ``schema_dir`` and return:

    * ``classes``: full IRI -> LinkML class name (PascalCase)
    * ``slots``:   full IRI -> LinkML slot name (snake_case)

    A URI may map to multiple LinkML names across schemas. We keep the
    first occurrence in sort-stable schema order so the chosen name is
    deterministic across runs.
    """
    classes: dict[str, str] = {}
    slots: dict[str, str] = {}

    yaml_files = sorted(schema_dir.rglob("*.yaml"))
    for sf in yaml_files:
        try:
            doc = yaml.safe_load(sf.read_text()) or {}
        except yaml.YAMLError as exc:
            print(f"WARN: cannot parse {sf}: {exc}", file=sys.stderr)
            continue
        prefixes = doc.get("prefixes") or {}

        # Default identity (per the skill): class_uri / slot_uri default to
        # {default_prefix}:{ElementName} when not declared explicitly.
        default_prefix = doc.get("default_prefix")
        default_base = prefixes.get(default_prefix) if default_prefix else None

        for cname, cdef in (doc.get("classes") or {}).items():
            cdef = cdef or {}
            uris = _collect_uris(cdef, prefixes, "class_uri")
            if not uris and default_base:
                uris.append(default_base + cname)
            for uri in uris:
                classes.setdefault(uri, cname)
            # per-class attributes: act as slots scoped to that class
            for aname, adef in (cdef.get("attributes") or {}).items():
                adef = adef or {}
                a_uris = _collect_uris(adef, prefixes, "slot_uri")
                if not a_uris and default_base:
                    a_uris.append(default_base + aname)
                for uri in a_uris:
                    slots.setdefault(uri, aname)

        for sname, sdef in (doc.get("slots") or {}).items():
            sdef = sdef or {}
            uris = _collect_uris(sdef, prefixes, "slot_uri")
            if not uris and default_base:
                uris.append(default_base + sname)
            for uri in uris:
                slots.setdefault(uri, sname)

    return classes, slots


# ---------------------------------------------------------------------------
# CURIE compression for emitted YAML
# ---------------------------------------------------------------------------

# Compact, stable CURIE prefixes for *emitted* identifiers.
_EMIT_PREFIXES: list[tuple[str, str]] = [
    (DPV_LOCAL_NS, "dpv"),
    (DPV_CAN_NS, "dpv_upstream"),
    (DPV_OWL_NS, "dpv_owl"),
    ("https://w3id.org/dpv/legal/eu/gdpr#", "eu-gdpr"),
    ("https://w3id.org/dpv/legal/eu#", "legal-eu"),
    ("https://w3id.org/dpv/legal/ie#", "legal-ie"),
    ("https://w3id.org/dpv/loc#", "loc"),
    ("https://w3id.org/dpv/nace#", "nace"),
    ("https://w3id.org/dpv/pd#", "pd"),
    ("https://w3id.org/dpv/risk#", "risk"),
    ("https://w3id.org/dpv/tech#", "tech"),
    ("https://w3id.org/dpv/justifications#", "justifications"),
    ("https://w3id.org/dpv/extension#", "extension"),
    ("https://example.org/dpv/ex#", "ex"),
    ("https://example.org/dpv/exA#", "exA"),
    ("https://example.org/dpv/exB#", "exB"),
    ("https://example.org/dpv/default#", ""),
    ("http://www.w3.org/2004/02/skos/core#", "skos"),
    ("http://purl.org/dc/terms/", "dct"),
    ("http://schema.org/", "schema"),
    ("https://schema.org/", "schema"),
    ("http://www.w3.org/ns/odrl/2/", "odrl"),
    ("http://www.w3.org/2006/time#", "time"),
    ("http://www.w3.org/ns/org#", "org"),
    ("http://xmlns.com/foaf/0.1/", "foaf"),
    (LMODEL_DPV_NS, "dpv"),
]


def to_curie(uri: str) -> str:
    for ns, pfx in _EMIT_PREFIXES:
        if uri.startswith(ns):
            local = uri[len(ns):]
            return f"{pfx}:{local}" if pfx else local
    return uri


# ---------------------------------------------------------------------------
# TTL -> YAML conversion
# ---------------------------------------------------------------------------

def _term_to_json(
    term: Any, slot_index: dict[str, str], class_index: dict[str, str]
) -> Any:
    if isinstance(term, Literal):
        return str(term)
    if isinstance(term, URIRef):
        return to_curie(str(term))
    if isinstance(term, BNode):
        return f"_:{term}"
    return str(term)


def _subject_id(subj: Any) -> str:
    if isinstance(subj, BNode):
        return f"_:{subj}"
    return to_curie(str(subj))


def _root_class_for(
    subj: Any, graph: Graph, class_index: dict[str, str]
) -> str | None:
    """Pick the most specific LinkML class for ``subj`` from ``rdf:type``
    triples, falling back to alphabetical for determinism."""
    candidates: list[str] = []
    for o in graph.objects(subj, RDF.type):
        if isinstance(o, URIRef):
            name = class_index.get(str(o))
            if name:
                candidates.append(name)
    if not candidates:
        return None
    # Prefer the longest name (heuristic for specificity), tie-break alpha.
    candidates.sort(key=lambda n: (-len(n), n))
    return candidates[0]


def convert_ttl(
    src: Path,
    class_index: dict[str, str],
    slot_index: dict[str, str],
) -> list[tuple[str, dict, dict | None]]:
    """Return [(filename_stem_part, yaml_dict, unmapped_or_none), ...]
    for one TTL fixture."""
    graph = Graph()
    graph.parse(src, format="turtle")

    emitted: list[tuple[str, dict]] = []
    typed_subjects = sorted(
        {s for s in graph.subjects(RDF.type, None)
         if isinstance(s, URIRef) and _root_class_for(s, graph, class_index)},
        key=str,
    )
    for idx, subj in enumerate(typed_subjects, 1):
        cls_name = _root_class_for(subj, graph, class_index)
        if cls_name is None:
            continue
        obj: dict[str, Any] = {"id": _subject_id(subj)}
        unmapped: dict[str, list[str]] = defaultdict(list)

        # Collect predicates -> list of object renderings.
        bucket: dict[str, list[Any]] = defaultdict(list)
        unbucket: dict[str, list[Any]] = defaultdict(list)
        for p, o in graph.predicate_objects(subj):
            if p == RDF.type:
                continue
            slot_name = slot_index.get(str(p))
            value = _term_to_json(o, slot_index, class_index)
            if slot_name:
                bucket[slot_name].append(value)
            else:
                unbucket[to_curie(str(p))].append(value)

        for k, vs in bucket.items():
            obj[k] = vs[0] if len(vs) == 1 else sorted(vs, key=str)
        unmapped_out: dict[str, Any] | None = None
        if unbucket:
            unmapped_out = {
                k: (vs[0] if len(vs) == 1 else sorted(vs, key=str))
                for k, vs in unbucket.items()
            }

        emitted.append((f"{cls_name}-{src.stem}-{idx}", obj, unmapped_out))

    return emitted


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text() == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return True


def main() -> None:
    linkml_root = Path(__file__).resolve().parent.parent

    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "-s", "--schema-dir", type=Path,
        default=linkml_root / "src" / "dpv" / "schema",
        help="Directory containing generated LinkML schemas.",
    )
    parser.add_argument(
        "-i", "--input-dir", type=Path,
        default=linkml_root / "tests" / "data" / "dpvcg" / "valid",
        help="Directory of wrapped TTL fixtures from load_examples.py.",
    )
    parser.add_argument(
        "-o", "--output-dir", type=Path,
        default=linkml_root / "tests" / "data" / "dpvcg" / "valid",
        help="Directory to write per-subject YAML documents.",
    )
    args = parser.parse_args()

    if not args.schema_dir.exists():
        parser.error(
            f"Schema directory not found: {args.schema_dir}\n"
            "Run scripts/dpv_to_linkml.py first to generate the schema."
        )
    if not args.input_dir.exists():
        parser.error(
            f"Input directory not found: {args.input_dir}\n"
            "Run scripts/load_examples.py first to populate TTL fixtures."
        )

    print(f"indexing schema under {args.schema_dir} ...", file=sys.stderr)
    class_index, slot_index = build_indexes(args.schema_dir)
    print(
        f"  indexed {len(class_index)} class IRIs, "
        f"{len(slot_index)} slot IRIs",
        file=sys.stderr,
    )
    if not class_index:
        print(
            "ERROR: no classes indexed; the schema directory appears empty "
            "or is still the copier placeholder. Run dpv_to_linkml.py first.",
            file=sys.stderr,
        )
        sys.exit(1)

    args.output_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    skipped = 0
    untyped: list[str] = []
    written_paths: set[Path] = set()

    for src in sorted(args.input_dir.glob("E*.ttl")):
        try:
            docs = convert_ttl(src, class_index, slot_index)
        except Exception as exc:  # noqa: BLE001
            print(f"  ! {src.name}: parse failed: {exc}", file=sys.stderr)
            skipped += 1
            continue
        if not docs:
            untyped.append(src.name)
            continue
        for stem, doc, unmapped in docs:
            out = args.output_dir / f"{stem}.yaml"
            body = yaml.safe_dump(
                doc, sort_keys=True, allow_unicode=True, default_flow_style=False
            )
            # Unmapped predicates are preserved as a leading YAML comment
            # block (rather than an ``__unmapped__`` key) so the file is
            # loadable by the generated Pydantic / dataclass models while
            # still leaving the triples visible for downstream curation.
            if unmapped:
                lines = ["# __unmapped__:"]
                unmapped_yaml = yaml.safe_dump(
                    unmapped, sort_keys=True, allow_unicode=True,
                    default_flow_style=False,
                )
                for ln in unmapped_yaml.splitlines():
                    lines.append(f"#   {ln}" if ln else "#")
                content = "\n".join(lines) + "\n" + body
            else:
                content = body
            if write_if_changed(out, content):
                written += 1
            written_paths.add(out)

    # Prune stale converted YAMLs from previous runs (only those we own:
    # ``<ClassName>-E####-<n>.yaml`` pattern).
    stale_re = re.compile(r"^[A-Z][A-Za-z0-9_]+-E\d+-\d+\.yaml$")
    for existing in args.output_dir.glob("*.yaml"):
        if stale_re.match(existing.name) and existing not in written_paths:
            existing.unlink()

    print(
        f"ttl_to_yaml: wrote/updated {written} YAML documents; "
        f"skipped {skipped} TTL files; {len(untyped)} fixtures yielded "
        f"no typed root subject",
        file=sys.stderr,
    )
    if untyped:
        print("  fixtures with no typed root:", file=sys.stderr)
        for n in untyped[:20]:
            print(f"    - {n}", file=sys.stderr)
        if len(untyped) > 20:
            print(f"    ... ({len(untyped) - 20} more)", file=sys.stderr)


if __name__ == "__main__":
    main()
