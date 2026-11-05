---
type: GlossaryTerm
id: https://w3id.org/lmodel/dpv/knowledge/glossary/term
title: Term
description: "A term: one thing DPV's vocabularies state as a concept or a property, under its own IRI. Each is one record here, a `DpvConcept` or a `DpvProperty`."
relatedTo:
  - https://w3id.org/lmodel/dpv/knowledge/explanations/terms-as-records
sources:
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: COUNTS
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# Term

Every term of the vocabularies is a record in `src/dpv/data/`. There are 8,856 concepts and 307 properties.[^test_coverage.py]

[^test_coverage.py]: tests/test_coverage.py, COUNTS
