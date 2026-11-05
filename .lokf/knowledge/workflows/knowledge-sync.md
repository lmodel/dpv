---
type: Service
id: https://w3id.org/lmodel/dpv/knowledge/workflows/knowledge-sync
genre: reference
title: Knowledge sync (knowledge-sync.yaml)
description: The weekly workflow that keeps the sidecar's copies and the skills pin at the newest release of Knowledge Trust Ladder, by a pull request a person merges.
resource: .github/workflows/knowledge-sync.yaml
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:59:07Z"
status: draft
references:
  - https://w3id.org/lmodel/dpv/knowledge/workflows/knowledge-librarian
---

# Knowledge sync (knowledge-sync.yaml)

`CONTRIBUTING.md` says the skills pin moves with the sidecar copies. The workflow runs on a schedule and moves them together.[^contributing.md]

[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
