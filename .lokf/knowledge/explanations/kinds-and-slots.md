---
type: Explanation
id: https://w3id.org/lmodel/dpv/knowledge/explanations/kinds-and-slots
genre: explanation
title: How kinds and slots get their names
description: "How the converter names what it writes: a kind's class takes a `Dpv` prefix and a slot keeps its property's local name, and where two namespaces define one name, the core keeps it and the other takes its namespace first."
about:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/terms-module
  - https://w3id.org/lmodel/dpv/knowledge/datasets/kinds-modules
sources:
  - id: about.md
    resource: docs/about.md
    title: Terms are records
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: test_a_shared_local_name_keeps_each_iri
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_german_stays_in_its_own_keys
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# How kinds and slots get their names

A slot keeps the local name of the DPV property it renders, so a record's keys are DPV's: `hasPurpose`, `prefLabel`. Where two namespaces define one name, the core keeps it and the other takes its namespace first: `hasRiskLevel` and `eu_aiact_hasRiskLevel`.[^about.md]

A kind's class takes the namespace the same way: `DpvRiskLevel` and `DpvEuAiactRiskLevel`. Each slot and each class keeps its own IRI.[^test_coverage.py]

German stays in keys of its own, `prefLabel_de` and `definition_de`, because only the German health data law states it.[^test_catalogue.py]

[^about.md]: docs/about.md, Terms are records
[^test_coverage.py]: tests/test_coverage.py, test_a_shared_local_name_keeps_each_iri
[^test_catalogue.py]: tests/test_catalogue.py, test_german_stays_in_its_own_keys
