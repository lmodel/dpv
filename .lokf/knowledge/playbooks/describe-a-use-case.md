---
type: Playbook
id: https://w3id.org/lmodel/dpv/knowledge/playbooks/describe-a-use-case
genre: how-to
title: Describe a use case
description: "How to describe a thing in a use case with DPV: write a `DpvResource` with an `id`, the term it is an instance of in `rdf_type`, and DPV's properties as keys, then validate it with `-C DpvResource`."
about:
  - https://w3id.org/lmodel/dpv/knowledge/glossary/resource
sources:
  - id: index.md
    resource: docs/index.md
    title: Describing a use case
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# Describe a use case

Write the record, naming DPV's terms by their CURIEs:

```yaml
id: ex:Newsletter
rdf_type:
  - dpv:Process
hasPurpose:
  - dpv:DirectMarketing
hasPersonalData:
  - pd:EmailAddress
```

Validate it with `-C DpvResource`. An unknown key fails, and so does a value that does not look like a reference.[^index.md]

[^index.md]: docs/index.md, Describing a use case
