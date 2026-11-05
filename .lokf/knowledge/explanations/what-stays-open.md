---
type: Explanation
id: https://w3id.org/lmodel/dpv/knowledge/explanations/what-stays-open
genre: explanation
title: What stays open
description: "Why no validator refuses a value for leaving a property's usual classes: DPV states `domainIncludes` and `rangeIncludes`, not `rdfs:domain` and `rdfs:range`, so `DpvResource` holds any property."
about:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/terms-module
relatedTo:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/example-departures
sources:
  - id: about.md
    resource: docs/about.md
    title: What stays open
  - id: test_generated_json_schema.py
    resource: tests/test_generated_json_schema.py
    title: test_a_concept_is_one_shape_whatever_its_kind
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# What stays open

DPV uses `dcam:domainIncludes` and `dcam:rangeIncludes`. They say what a property usually joins, not what it must. So `DpvResource` holds any property, and the validator refuses no value for leaving those classes.[^about.md]

What the validator does refuse is an unknown key and a value that does not look like a reference. `tests/dpv_rules.py` then holds a value to a term that exists.[^about.md]

A kind adds no slot of its own, so every kind's class has one shape, and a list of concepts does not try each kind in turn.[^test_generated_json_schema.py]

[^about.md]: docs/about.md, What stays open
[^test_generated_json_schema.py]: tests/test_generated_json_schema.py, test_a_concept_is_one_shape_whatever_its_kind
