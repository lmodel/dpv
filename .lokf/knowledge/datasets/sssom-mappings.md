---
type: Dataset
id: https://w3id.org/lmodel/dpv/knowledge/datasets/sssom-mappings
genre: reference
title: DPV's own mappings as SSSOM
description: "`src/dpv/mappings/`: two SSSOM sets that render the mapping files DPV publishes, 5 rows for ISO/IEC 29100:2024 terms and 24 for ODRL, each row reading with DPV's term as its subject."
resource: src/dpv/mappings
derivedFrom:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/upstream-copy
about:
  - https://w3id.org/lmodel/dpv/knowledge/explanations/mappings
sources:
  - id: test_mappings.py
    resource: tests/test_mappings.py
    title: test_each_row_comes_from_the_csv_and_back
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# DPV's own mappings as SSSOM

The converter writes each set from DPV's CSV. A test holds each row to the CSV and to DPV's Turtle, both ways, and holds each set's header to the licence and the prefixes it needs.[^test_mappings.py]

[^test_mappings.py]: tests/test_mappings.py, test_each_row_comes_from_the_csv_and_back
