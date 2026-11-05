---
type: Explanation
id: https://w3id.org/lmodel/dpv/knowledge/explanations/terms-as-records
genre: explanation
title: Why terms are records
description: "Why the schema holds DPV's terms as records and not as classes: DPV states each concept as a class and as an instance, so one class per term could not say that a process's `hasPurpose` is `dpv:Marketing`."
about:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/dpv-linkml-schema
relatedTo:
  - https://w3id.org/lmodel/dpv/knowledge/glossary/kind
  - https://w3id.org/lmodel/dpv/knowledge/glossary/term
sources:
  - id: about.md
    resource: docs/about.md
    title: Terms are records
  - id: readme.md
    resource: README.md
    title: What it models
  - id: changelog
    resource: CHANGELOG.md
    title: Changed
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# Why terms are records

DPV states `dpv:Marketing a rdfs:Class, skos:Concept, dpv:Purpose`. A LinkML class cannot also be a value, so a schema with one class per term could not hold `hasPurpose: dpv:Marketing`.[^about.md]

So the concepts that terms are instances of are classes, and every term is a record. A term and its kind's class can be the same thing seen two ways: `dpv:Purpose` is a record, and `DpvPurpose` is the class a host names as a concept's `type`.[^about.md]

It follows that `project/owl/` describes this schema, and `upstream/2.3/` is DPV's ontology.[^readme.md]

The schema it replaced held 973 classes with no slots of their own, and enforced only `id`.[^changelog]

[^about.md]: docs/about.md, Terms are records
[^readme.md]: README.md, What it models
[^changelog]: CHANGELOG.md, Changed
