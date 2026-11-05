---
type: Explanation
id: https://w3id.org/lmodel/dpv/knowledge/explanations/mappings
genre: explanation
title: The mappings
description: "Which mappings this repository holds and why: only what DPV's editors publish in machine-readable form, for ISO/IEC 29100:2024 terms and for ODRL. The other 24 sets, which a matching tool wrote, are gone."
about:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/sssom-mappings
sources:
  - id: about.md
    resource: docs/about.md
    title: Mappings
  - id: readme.md
    resource: README.md
    title: Mappings
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: test_the_schema_states_no_mapping_of_its_own
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# The mappings

`src/dpv/mappings/` renders the two mapping files DPV publishes in machine-readable form. A row reads with DPV's term as its subject, as DPV's own statements do, and `skos:broadMatch` stands for DPV's `skos:broader`.[^about.md]

`dpv-odrl.ttl` does not parse, so the test reads its comment lines, and one row names `dpv:hasTechnology`, which 2.3 does not state.[^about.md]

The other 24 SSSOM sets are gone. A matching tool wrote their rows, and many named terms that do not exist.[^readme.md]

A class here is DPV's own term, so the schema states no mapping of its own.[^test_schema_rules.py]

[^about.md]: docs/about.md, Mappings
[^readme.md]: README.md, Mappings
[^test_schema_rules.py]: tests/test_schema_rules.py, test_the_schema_states_no_mapping_of_its_own
