---
type: Reference
id: https://w3id.org/lmodel/dpv/knowledge/references/dpv-repository
genre: reference
title: The DPV repository
description: The Community Group's repository, `w3c-cg/dpv`, whose tag `dpv-2.3` names commit `cbcd215`. It keeps each edition in a folder, and the examples and the mappings at its root.
resource: https://github.com/w3c-cg/dpv
references:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/upstream-copy
sources:
  - id: check
    resource: scripts/check_upstream_release.py
    title: PINNED_COMMIT and FOLDERS
  - id: test_mappings.py
    resource: tests/test_mappings.py
    title: the module's description
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# The DPV repository

The watch lists this repository through GitHub's API and compares git object hashes against the pins.[^check]

The tag names commit `cbcd21567808812677eeb3bb0f05b2ff2c2211a5`. A release's folder is `2.3/`, and the examples and the mapping files sit at the repository's root.[^check]

Only two mapping folders hold machine-readable files, `iso` and `odrl`. The folders for DCAT, Dublin Core, gist, PROV, schema.org and SEMIC hold a web page only.[^test_mappings.py]

[^check]: scripts/check_upstream_release.py, PINNED_COMMIT and FOLDERS
[^test_mappings.py]: tests/test_mappings.py, the module's description
