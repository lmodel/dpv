---
type: Dataset
id: https://w3id.org/lmodel/dpv/knowledge/datasets/adapt-copy
genre: reference
title: The adapt copy
description: "`.lokf/schema/dpv.yaml`, which `just lokf-adapt` writes from the schema so that it can sit beside LOKF's: the file this bundle validates against, and the file a release attaches as `schema-<tag>-dpv.yaml`."
resource: .lokf/schema/dpv.yaml
derivedFrom:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/dpv-linkml-schema
about:
  - https://w3id.org/lmodel/dpv/knowledge/glossary/adapt-copy
sources:
  - id: readme.md
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: test_the_copy_drops_and_renames_only_what_is_named
  - resource: project.justfile
    title: lokf_adapt_roots
generated:
  by: process:ktl-librarian
  at: "2026-11-06T21:19:27Z"
status: draft
---

# The adapt copy

The copy roots `DpvTerm`, `DpvVocabulary`, `DpvConceptScheme`, `DpvAgent`, `DpvExample` and `DpvCatalogue` on `Concept`, and `just lokf-adapt-check` says when it is stale.[^readme.md]

It drops `id` and `rdf_type` for LOKF's `id` and `type`, folds `schema_version` into LOKF's `version`, and renames each key LOKF also has with a `dpv_` prefix, keeping its IRI.[^test_schema_rules.py]

[^readme.md]: README.md, Knowledge Trust Ladder (KTL)
[^test_schema_rules.py]: tests/test_schema_rules.py, test_the_copy_drops_and_renames_only_what_is_named
