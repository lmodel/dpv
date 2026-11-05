---
type: Service
id: https://w3id.org/lmodel/dpv/knowledge/services/converter
genre: reference
title: The converter
description: "`scripts/dpv_to_linkml.py`: reads the Turtle under `upstream/` and writes the terms module, the kinds' modules, the catalogue, the examples and the SSSOM sets. `just gen-schema` runs it, and it stops on a predicate no table names."
resource: scripts/dpv_to_linkml.py
references:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/catalogue
  - https://w3id.org/lmodel/dpv/knowledge/datasets/terms-module
  - https://w3id.org/lmodel/dpv/knowledge/datasets/kinds-modules
  - https://w3id.org/lmodel/dpv/knowledge/datasets/sssom-mappings
sources:
  - id: converter
    resource: scripts/dpv_to_linkml.py
    title: the module's description and _check_derived
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_the_catalogue_is_the_converters_output
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# The converter

The script makes no judgement beyond its tables, and it stops on a predicate no table names, so a new edition cannot lose a fact unnoticed.[^converter]

It also stops when `skos:narrower` no longer follows what the records hold, or when `schema:domainIncludes` no longer repeats the `dcam:` pair.[^converter]

Tests hold the committed files to its output by digest, since a diff of files this size does not finish.[^test_catalogue.py]

[^converter]: scripts/dpv_to_linkml.py, the module's description and _check_derived
[^test_catalogue.py]: tests/test_catalogue.py, test_the_catalogue_is_the_converters_output
