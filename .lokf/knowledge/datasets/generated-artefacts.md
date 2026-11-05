---
type: Dataset
id: https://w3id.org/lmodel/dpv/knowledge/datasets/generated-artefacts
genre: reference
title: The generated artefacts
description: "What the generators write from the schema: `project/`, `src/dpv/datamodel/` and `docs/schema/dpv.yaml`. They are committed and never edited, and the SQL generator is off."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/dpv-linkml-schema
sources:
  - id: generators.yaml
    resource: .linkml/generators.yaml
    title: excludes and jsonschema
  - id: test_generated_json_schema.py
    resource: tests/test_generated_json_schema.py
    title: test_the_committed_file_is_the_generators_output
  - resource: src/dpv/datamodel
  - resource: docs/schema
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# The generated artefacts

`.linkml/generators.yaml` holds the generators' settings. It turns the SQL generator off, because it would write about 2,500 join tables for a vocabulary nobody queries through tables, and it names `DpvCatalogue` as the JSON Schema's top class.[^generators.yaml]

A test holds the committed JSON Schema to the generator's output.[^test_generated_json_schema.py]

[^generators.yaml]: .linkml/generators.yaml, excludes and jsonschema
[^test_generated_json_schema.py]: tests/test_generated_json_schema.py, test_the_committed_file_is_the_generators_output
