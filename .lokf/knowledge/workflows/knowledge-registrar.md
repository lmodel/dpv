---
type: Service
id: https://w3id.org/lmodel/dpv/knowledge/workflows/knowledge-registrar
genre: reference
title: Knowledge registrar (knowledge-registrar.yaml)
description: "The gate on the bundle: it validates the bundle on each pull request that touches it, and checks who vouched for what."
resource: .github/workflows/knowledge-registrar.yaml
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# Knowledge registrar (knowledge-registrar.yaml)

It runs on any pull request that touches `.lokf/`.[^contributing.md]

[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
