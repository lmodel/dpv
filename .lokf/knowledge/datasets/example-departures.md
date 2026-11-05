---
type: Dataset
id: https://w3id.org/lmodel/dpv/knowledge/datasets/example-departures
genre: reference
title: Where DPV's examples leave a property's usual classes
description: "`tests/example_departures.yaml`: each place DPV's own examples use a property beyond its `rangeIncludes` or `domainIncludes`, or give a literal where the range names a class: 58 values, 65 subjects and 30 literals."
resource: tests/example_departures.yaml
about:
  - https://w3id.org/lmodel/dpv/knowledge/glossary/departure
derivedFrom:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/examples
sources:
  - id: test_examples.py
    resource: tests/test_examples.py
    title: departures
  - id: about.md
    resource: docs/about.md
    title: What stays open
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# Where DPV's examples leave a property's usual classes

A test compares this list with what the examples hold, so a new departure fails it, and so does one DPV has fixed.[^test_examples.py]

A value or a subject with no stated type is left alone, since nothing says what it is.[^test_examples.py]

None of these is a fault in RDF. `domainIncludes` and `rangeIncludes` say what a property usually joins, not what it must.[^about.md]

[^test_examples.py]: tests/test_examples.py, departures
[^about.md]: docs/about.md, What stays open
