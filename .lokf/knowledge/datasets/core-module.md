---
type: Dataset
id: https://w3id.org/lmodel/dpv/knowledge/datasets/core-module
genre: reference
title: The core module
description: "`src/dpv/schema/dpv_core.yaml`, written by hand: the date and address types, the term status list, the classes for a vocabulary, a concept scheme, an agent, a web page and an interval, and the slots they share."
resource: src/dpv/schema/dpv_core.yaml
isPartOf:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/dpv-linkml-schema
sources:
  - id: core
    resource: src/dpv/schema/dpv_core.yaml
    title: types and enums
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# The core module

`dpv_date` and `dpv_uri` carry a pattern, because LinkML's own date and uri types ask a JSON Schema format checker, which many validators leave off.[^core]

`DpvTermStatus` holds the three values DPV states: `accepted`, `modified` and `sunset`.[^core]

[^core]: src/dpv/schema/dpv_core.yaml, types and enums
