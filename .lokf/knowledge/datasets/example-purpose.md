---
type: DpvPurpose
id: https://w3id.org/lmodel/dpv/knowledge/datasets/example-purpose
genre: reference
title: Marketing
description: The purpose `dpv:Marketing` of DPV 2.3, written as a concept of type `DpvPurpose` in the adapt copy's keys. It shows that the domain schema admits a term of a kind.
resource: src/dpv/data/dpv-2.3-core.yaml
prefLabel: Marketing
broader:
  - dpv:Purpose
term_status: accepted
derivedFrom:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/catalogue
sources:
  - id: readme.md
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_a_record_holds_what_the_turtle_says
generated:
  by: process:ktl-librarian
  at: "2026-11-06T21:19:27Z"
status: draft
---

# Marketing

This concept shows how a host writes a DPV term in its bundle: its `type` is a kind, and its relations name DPV's terms by their CURIEs. `lokf validate` checks it against `.lokf/schema/dpv.yaml`.[^readme.md]

The catalogue's own record of `dpv:Marketing` holds the same label and the same broader term.[^test_catalogue.py]

[^readme.md]: README.md, Knowledge Trust Ladder (KTL)
[^test_catalogue.py]: tests/test_catalogue.py, test_a_record_holds_what_the_turtle_says
