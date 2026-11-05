---
type: Playbook
id: https://w3id.org/lmodel/dpv/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test
description: "How to change the schema: edit the converter or a hand-written module, run `just gen-schema`, `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write."
references:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/dpv-linkml-schema
  - https://w3id.org/lmodel/dpv/knowledge/datasets/generated-artefacts
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - id: project.justfile
    resource: project.justfile
    title: gen-schema
  - id: justfile
    resource: justfile
    title: the test recipe
  - id: main.yaml
    resource: .github/workflows/main.yaml
    title: the lint step
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# Regenerate and test

1. Edit `scripts/dpv_to_linkml.py`, `src/dpv/schema/dpv_core.yaml` or `src/dpv/schema/dpv.yaml`.[^contributing.md]
2. Run `just gen-schema`, which writes the terms, the kinds, the catalogue and the mappings from `upstream/`.[^project.justfile]
3. Run `just lint`, `just gen-project`, `just gen-doc` and `just lokf-adapt`.[^contributing.md]
4. Run `just test`, which generates the schema into `tmp/`, runs `pytest`, and runs the example runner.[^justfile]
5. Commit the output. CI runs `just lint` and `just lokf-adapt-check` on Python 3.13, and `just test` on each version.[^main.yaml]

[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
[^project.justfile]: project.justfile, gen-schema
[^justfile]: justfile, the test recipe
[^main.yaml]: .github/workflows/main.yaml, the lint step
