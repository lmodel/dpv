---
type: Explanation
id: https://w3id.org/lmodel/dpv/knowledge/explanations/what-the-records-leave-out
genre: explanation
title: What the records leave out
description: "The facts of DPV's files no record holds, each with its reason: `skos:narrower`, which the records regenerate, the repeated `schema:` domain and range, what says how the site publishes a file, and `dpv-27560`."
about:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/catalogue
sources:
  - id: test_coverage.py
    resource: tests/test_coverage.py
    title: test_skos_narrower_is_exactly_what_the_records_regenerate
  - id: about.md
    resource: docs/about.md
    title: What the records leave out
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# What the records leave out

Only the locations state `skos:narrower`, 68,032 times. 4,959 of them are the inverse of `skos:broader`. The other 63,073 list what each `loc:non-X` holds: every country but X, and but X's member countries when X is a union. A test regenerates every pair.[^test_coverage.py]

`schema:domainIncludes` and `schema:rangeIncludes` repeat the `dcam:` pair on every property.[^test_coverage.py]

`prof:hasResource` and the 337 resource descriptors say how DPV's site publishes a file, so they stay out.[^about.md]

`dpv-27560`, DPV's schema for consent records, stays out because its Turtle file names four classes and states nothing about them.[^about.md]

[^test_coverage.py]: tests/test_coverage.py, test_skos_narrower_is_exactly_what_the_records_regenerate
[^about.md]: docs/about.md, What the records leave out
