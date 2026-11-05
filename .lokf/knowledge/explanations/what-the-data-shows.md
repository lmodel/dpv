---
type: Explanation
id: https://w3id.org/lmodel/dpv/knowledge/explanations/what-the-data-shows
genre: explanation
title: What the data shows
description: "What DPV's own files hold that a reader would not expect: names defined nowhere, predicates no vocabulary has, three example files that do not parse, and a term with two creation dates."
about:
  - https://w3id.org/lmodel/dpv/knowledge/references/dpv-vocabulary
sources:
  - id: about.md
    resource: docs/about.md
    title: What the data shows
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_what_the_data_shows_and_the_vocabulary_does_not_say
  - resource: tests/dpv_rules.py
    title: DANGLING
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# What the data shows

18 names under DPV's namespaces are used and defined nowhere, such as `dpv:System` and `tech:AI`. One is an IRI with a line break in it.[^about.md]

60 statements use `skos:sameAs`, and each vocabulary header uses `rdfs:Label`. Neither is a term of its vocabulary.[^about.md]

Three example files do not parse: `E0030`, `E0059` and `E0061`.[^about.md]

`dcat:Resource` states two creation dates, and five terms name two vocabularies under `rdfs:isDefinedBy`. 153 terms have no definition, nearly all laws and authorities.[^test_catalogue.py]

A test fails when a later edition fixes one of these, so each is looked at again then.[^test_catalogue.py]

[^about.md]: docs/about.md, What the data shows
[^test_catalogue.py]: tests/test_catalogue.py, test_what_the_data_shows_and_the_vocabulary_does_not_say
