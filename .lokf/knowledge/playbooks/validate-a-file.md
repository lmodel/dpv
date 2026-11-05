---
type: Playbook
id: https://w3id.org/lmodel/dpv/knowledge/playbooks/validate-a-file
genre: how-to
title: Validate a file of the catalogue
description: "How to validate a file: `uv run linkml-validate -s src/dpv/schema/dpv.yaml -C DpvCatalogue <file>`, or the committed JSON Schema without LinkML, and `tests/dpv_rules.py` for what a validator cannot state."
references:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/catalogue
sources:
  - id: index.md
    resource: docs/index.md
    title: Validating a file of the catalogue
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# Validate a file of the catalogue

Run the validator over one file of the catalogue:

```bash
uv run linkml-validate -s src/dpv/schema/dpv.yaml -C DpvCatalogue src/dpv/data/dpv-2.3-core.yaml
```

`project/jsonschema/dpv.schema.json` is the same schema for anyone without LinkML. `tests/dpv_rules.py` adds what a validator cannot state, such as that a value names a term that exists.[^index.md]

[^index.md]: docs/index.md, Validating a file of the catalogue
