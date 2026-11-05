---
type: GlossaryTerm
id: https://w3id.org/lmodel/dpv/knowledge/glossary/kind
title: Kind
description: "A kind: a type a DPV concept holds beyond `rdfs:Class` and `skos:Concept`, such as `dpv:Purpose`. Each of the 149 kinds is a class of this schema, and a record's `rdf_type` names its kinds."
relatedTo:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/kinds-modules
  - https://w3id.org/lmodel/dpv/knowledge/explanations/kinds-and-slots
sources:
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: test_every_kind_is_a_class_under_its_iri_and_back
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# Kind

A concept may be of several kinds or of none. Its `rdf_type` holds what DPV states, and a concept with no kind has none.[^test_coverage.py]

[^test_coverage.py]: tests/test_coverage.py, test_every_kind_is_a_class_under_its_iri_and_back
