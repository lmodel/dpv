---
type: Dataset
id: https://w3id.org/lmodel/dpv/knowledge/datasets/neighbour-copies
genre: reference
title: The neighbours' copies
description: "`tests/neighbours/`: the adapt copies 27 other lmodel repositories release, each the release's schema asset, which tests use to hold this copy's names apart from theirs."
resource: tests/neighbours
references:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/adapt-copy
sources:
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: NEIGHBOURS and SHARED_WITH_NEIGHBOURS
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# The neighbours' copies

Each copy is pinned by its SHA-256, and each came from a release, checked against its `.sha256` and its attestation.[^test_schema_rules.py]

No class, enum or type is shared, since each carries the `Dpv` prefix. A few keys are, such as `subject` and `value`, under other IRIs, and a test lists them per neighbour, so a new overlap fails it.[^test_schema_rules.py]

[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and SHARED_WITH_NEIGHBOURS
