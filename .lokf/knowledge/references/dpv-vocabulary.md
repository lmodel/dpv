---
type: Reference
id: https://w3id.org/lmodel/dpv/knowledge/references/dpv-vocabulary
genre: reference
title: Data Privacy Vocabulary (DPV)
description: "The upstream authority: DPV 2.3 of 2026-02-28, the vocabulary of the W3C Data Privacy Vocabularies and Controls Community Group for describing the processing of personal data, at `https://w3id.org/dpv/2.3`."
resource: https://w3id.org/dpv/2.3
references:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/upstream-copy
  - https://w3id.org/lmodel/dpv/knowledge/references/dpv-repository
sources:
  - id: dpv.yaml
    resource: src/dpv/schema/dpv.yaml
    title: annotations
  - id: index.md
    resource: docs/index.md
    title: What the catalogue holds
  - id: notice
    resource: NOTICE
    title: Data Privacy Vocabulary (DPV)
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# Data Privacy Vocabulary (DPV)

The schema renders DPV at the release the umbrella's annotations name: the tag `dpv-2.3`, released on 2026-02-28.[^dpv.yaml]

DPV is a set of vocabularies, each with its own namespace: the core at `https://w3id.org/dpv#`, and extensions for personal data, technology, artificial intelligence, risk, justifications, locations, laws, sectors and standards.[^index.md]

This project is not endorsed by the Community Group or by W3C.[^notice]

[^dpv.yaml]: src/dpv/schema/dpv.yaml, annotations
[^index.md]: docs/index.md, What the catalogue holds
[^notice]: NOTICE, Data Privacy Vocabulary (DPV)
