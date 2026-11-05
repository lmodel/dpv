---
type: Dataset
id: https://w3id.org/lmodel/dpv/knowledge/datasets/kinds-modules
genre: reference
title: The kinds' modules
description: "The modules the converter writes with one class per kind of term, 149 in all, under each kind's own IRI: `dpv_kinds` for the core, and `dpv_pd`, `dpv_tech`, `dpv_ai`, `dpv_risk`, `dpv_legal`, `dpv_sector` and `dpv_standards`."
resource: src/dpv/schema/dpv_kinds.yaml
isPartOf:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/dpv-linkml-schema
about:
  - https://w3id.org/lmodel/dpv/knowledge/glossary/kind
sources:
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: test_a_kinds_parent_sits_above_it_in_dpv
  - id: converter
    resource: scripts/dpv_to_linkml.py
    title: kind_class_names
  - resource: src/dpv/schema/dpv_ai.yaml
  - resource: src/dpv/schema/dpv_legal.yaml
  - resource: src/dpv/schema/dpv_pd.yaml
  - resource: src/dpv/schema/dpv_risk.yaml
  - resource: src/dpv/schema/dpv_sector.yaml
  - resource: src/dpv/schema/dpv_standards.yaml
  - resource: src/dpv/schema/dpv_tech.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# The kinds' modules

A class's title and description are the kind's own label and definition. Each class sits under the nearest kind above it along `skos:broader`, or under `DpvConcept` when no kind sits above it.[^test_coverage.py]

Where two namespaces define one kind, the core keeps the short name and any other takes its namespace too, such as `DpvRiskLevel` and `DpvEuAiactRiskLevel`.[^converter]

[^test_coverage.py]: tests/test_coverage.py, test_a_kinds_parent_sits_above_it_in_dpv
[^converter]: scripts/dpv_to_linkml.py, kind_class_names
