---
type: Dataset
id: https://w3id.org/lmodel/dpv/knowledge/datasets/upstream-copy
genre: reference
title: The copy of DPV's files
description: "`upstream/`: the Turtle of each vocabulary, the 88 examples, the ISO and ODRL mapping files and the licence, unchanged at the tag `dpv-2.3`. `scripts/upstream_pins.tsv` holds each of the 160 files' git object hashes."
resource: upstream
derivedFrom:
  - https://w3id.org/lmodel/dpv/knowledge/references/dpv-repository
sources:
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: test_copies_match_the_pinned_blobs
  - resource: scripts/upstream_pins.tsv
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# The copy of DPV's files

`upstream/` keeps the paths the tag gives them, so a file's path is its address in the repository. It leaves out the OWL serialisations and the module copies, which repeat the vocabularies.[^test_upstream.py]

A test holds each file to its pin, offline, and the watch holds the pins to the repository each week.[^test_upstream.py]

[^test_upstream.py]: tests/test_upstream.py, test_copies_match_the_pinned_blobs
