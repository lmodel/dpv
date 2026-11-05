---
type: Dataset
id: https://w3id.org/lmodel/dpv/knowledge/datasets/terms-module
genre: reference
title: The terms module
description: "`src/dpv/schema/dpv_terms.yaml`, which the converter writes: `DpvTerm` and its children `DpvConcept`, `DpvProperty` and `DpvResource`, `DpvExample`, `DpvStatement`, and one slot per DPV property under its own IRI."
resource: src/dpv/schema/dpv_terms.yaml
isPartOf:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/dpv-linkml-schema
derivedFrom:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/upstream-copy
sources:
  - id: dpv_terms.yaml
    resource: src/dpv/schema/dpv_terms.yaml
    title: classes
  - id: test_generated_json_schema.py
    resource: tests/test_generated_json_schema.py
    title: test_a_reference_must_look_like_one
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# The terms module

`DpvConcept` holds the metadata of a term and the DPV properties some term of the vocabularies states. `DpvProperty` adds the property's `subPropertyOf`, `domainIncludes` and `rangeIncludes`. `DpvResource` holds every DPV property, for a thing a use case describes.[^dpv_terms.yaml]

A slot takes DPV's own label and definition as its title and description. A slot whose value names a resource ranges over `DpvTerm` and carries a pattern, because LinkML renders such a reference as a string with no format.[^test_generated_json_schema.py]

[^dpv_terms.yaml]: src/dpv/schema/dpv_terms.yaml, classes
[^test_generated_json_schema.py]: tests/test_generated_json_schema.py, test_a_reference_must_look_like_one
