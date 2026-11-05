---
type: Dataset
id: https://w3id.org/lmodel/dpv/knowledge/datasets/examples
genre: reference
title: The examples as data
description: "`src/dpv/data/dpv-2.3-examples.yaml`: DPV's 88 examples, each with its description, and the statements of 85 of them as `DpvResource` records. Three files do not parse."
resource: src/dpv/data/dpv-2.3-examples.yaml
derivedFrom:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/upstream-copy
references:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/example-departures
sources:
  - id: about.md
    resource: docs/about.md
    title: What the examples add
  - id: test_examples.py
    resource: tests/test_examples.py
    title: test_the_records_state_what_the_file_states
  - id: dpv_terms.yaml
    resource: src/dpv/schema/dpv_terms.yaml
    title: DpvStatement
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# The examples as data

Each example's file is at `upstream/examples/`. A file declares no prefixes, so the converter supplies them. A blank node takes a label from its canonical order.[^about.md]

The records of an example give back exactly the statements its file makes, compared with canonical blank nodes.[^test_examples.py]

A statement the slots cannot hold goes in the resource's `statements`: a predicate with no slot, or a value not in the form its slot takes.[^dpv_terms.yaml]

[^about.md]: docs/about.md, What the examples add
[^test_examples.py]: tests/test_examples.py, test_the_records_state_what_the_file_states
[^dpv_terms.yaml]: src/dpv/schema/dpv_terms.yaml, DpvStatement
