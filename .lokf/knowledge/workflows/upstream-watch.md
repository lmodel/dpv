---
type: Service
id: https://w3id.org/lmodel/dpv/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The weekly check that `scripts/check_upstream_release.py` runs: another release of DPV, a moved tag, a changed or missing pinned file, or a changed licence opens or updates an issue."
resource: .github/workflows/upstream-watch.yaml
references:
  - https://w3id.org/lmodel/dpv/knowledge/playbooks/update-upstream-pins
  - https://w3id.org/lmodel/dpv/knowledge/references/dpv-repository
sources:
  - id: check
    resource: scripts/check_upstream_release.py
    title: the module's description
  - id: watch
    resource: .github/workflows/upstream-watch.yaml
    title: the header
  - resource: .github/scripts/report-issue.sh
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

The script lists the repository through GitHub's API, compares git object hashes and downloads no file.[^check]

A failing check fails the run and opens an issue, or comments on the one already open.[^watch]

[^check]: scripts/check_upstream_release.py, the module's description
[^watch]: .github/workflows/upstream-watch.yaml, the header
