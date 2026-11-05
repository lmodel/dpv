---
type: Dataset
id: https://w3id.org/lmodel/dpv/knowledge/datasets/dpv-linkml-schema
genre: reference
title: The DPV LinkML schema
description: "`src/dpv/schema/`: the umbrella `dpv.yaml` over `dpv_core`, `dpv_terms` and one module of kinds per namespace family. It models DPV 2.3 under DPV's own IRIs, and `DpvCatalogue` is its tree root."
resource: src/dpv/schema/dpv.yaml
hasPart:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/core-module
  - https://w3id.org/lmodel/dpv/knowledge/datasets/terms-module
  - https://w3id.org/lmodel/dpv/knowledge/datasets/kinds-modules
derivedFrom:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/upstream-copy
sources:
  - id: dpv.yaml
    resource: src/dpv/schema/dpv.yaml
    title: prefixes and DpvCatalogue
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: What this project is
  - id: lint
    resource: .linkmllint.yaml
  - resource: src/dpv/schema
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# The DPV LinkML schema

The umbrella holds the tree root, `DpvCatalogue`, and binds every prefix the data's CURIEs use, because the JSON-LD context takes its prefixes from that file alone.[^dpv.yaml]

The converter writes `dpv_terms.yaml` and the kinds' modules. `dpv_core.yaml` and `dpv.yaml` are edited by hand.[^contributing.md]

`.linkmllint.yaml` relaxes the naming rule so that a slot keeps the local name of the property it renders, and turns `canonical_prefixes` off, because a DPV document's prefixes are DPV's own.[^lint]

[^dpv.yaml]: src/dpv/schema/dpv.yaml, prefixes and DpvCatalogue
[^contributing.md]: CONTRIBUTING.md, What this project is
[^lint]: .linkmllint.yaml
