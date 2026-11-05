---
type: GlossaryTerm
id: https://w3id.org/lmodel/dpv/knowledge/glossary/namespace-family
title: Namespace family
description: "A namespace family: the vocabularies this project keeps in one data file, such as `legal`, which holds the law vocabulary of each jurisdiction and each EU law."
relatedTo:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/catalogue
sources:
  - id: converter
    resource: scripts/dpv_to_linkml.py
    title: FAMILIES
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# Namespace family

The converter's table of families says which namespaces each holds. A term belongs to the family of its IRI, and any other term DPV adopts, such as the Dublin Core properties, belongs to the core.[^converter]

[^converter]: scripts/dpv_to_linkml.py, FAMILIES
