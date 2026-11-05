---
type: Playbook
id: https://w3id.org/lmodel/dpv/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Update the upstream pins
description: "What to do when the watch reports another DPV release: read what changed, replace `upstream/`, the pins and the headers together, regenerate, and look at each test that fails."
references:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/upstream-copy
  - https://w3id.org/lmodel/dpv/knowledge/workflows/upstream-watch
sources:
  - id: check
    resource: scripts/check_upstream_release.py
    title: the pins
  - id: about.md
    resource: docs/about.md
    title: The parts of a release
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# Update the upstream pins

The watch names the moved release, the moved tag or the changed file.[^check]

To move to another release:

1. Replace the files under `upstream/` from the tag, and rewrite `scripts/upstream_pins.tsv` with their git object hashes.
2. Move `PINNED_EDITION`, `PINNED_TAG`, `PINNED_DATE`, `PINNED_COMMIT` and `PINNED_SOURCE`, and the schema headers with them.[^check]
3. Run `just gen-schema`. The converter stops on a predicate no table names, so read what it reports.[^about.md]
4. Run the tests, and look at each count and list that fails, since a later edition may fix a fault this repository pins.[^about.md]

[^check]: scripts/check_upstream_release.py, the pins
[^about.md]: docs/about.md, The parts of a release
