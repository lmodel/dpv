---
type: Dataset
id: https://w3id.org/lmodel/dpv/knowledge/datasets/catalogue
genre: reference
title: The catalogue
description: "`src/dpv/data/`: one YAML file per namespace family, with every vocabulary, concept scheme, concept and property of DPV 2.3 as a record under its own IRI: 8,856 concepts and 307 properties."
resource: src/dpv/data
derivedFrom:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/upstream-copy
references:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/dpv-linkml-schema
  - https://w3id.org/lmodel/dpv/knowledge/services/converter
sources:
  - id: about.md
    resource: docs/about.md
    title: The parts of a release
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: the module's tests
  - resource: docs/index.md
    title: What the catalogue holds
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# The catalogue

The converter writes each file from `upstream/`. Each file is a `DpvCatalogue`, and the file's family says which part of the release it holds.[^about.md]

| File | Concepts | Properties |
| --- | --- | --- |
| `dpv-2.3-core.yaml` | 973 | 162 |
| `dpv-2.3-pd.yaml` | 231 | 0 |
| `dpv-2.3-tech.yaml` | 130 | 52 |
| `dpv-2.3-ai.yaml` | 231 | 10 |
| `dpv-2.3-risk.yaml` | 507 | 43 |
| `dpv-2.3-justifications.yaml` | 66 | 0 |
| `dpv-2.3-loc.yaml` | 5,270 | 4 |
| `dpv-2.3-legal.yaml` | 896 | 15 |
| `dpv-2.3-sector.yaml` | 415 | 0 |
| `dpv-2.3-standards.yaml` | 136 | 21 |
| `dpv-2.3-examples.yaml` | 1 | 0 |

Every file passes the committed JSON Schema, `linkml-validate` and the rules in `tests/dpv_rules.py`, and its JSON-LD projection gives back every triple the Turtle states about a term, except what `explanations/what-the-records-leave-out` lists.[^test_catalogue.py]

[^about.md]: docs/about.md, The parts of a release
[^test_catalogue.py]: tests/test_catalogue.py, the module's tests
