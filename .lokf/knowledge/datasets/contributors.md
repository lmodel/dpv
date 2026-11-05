---
type: Dataset
id: https://w3id.org/lmodel/dpv/knowledge/datasets/contributors
genre: reference
title: The contributors
description: "`src/dpv/data/dpv-2.3-agents.yaml`: the 70 people and organizations DPV's files name as contributors and creators, each with an id of the form `dpv_agent:person-<name>` or `dpv_agent:org-<name>`."
resource: src/dpv/data/dpv-2.3-agents.yaml
derivedFrom:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/upstream-copy
sources:
  - id: converter
    resource: scripts/dpv_to_linkml.py
    title: agent_id
  - id: dpv_rules.py
    resource: tests/dpv_rules.py
    title: _term_errors
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# The contributors

DPV's files hold each person on a blank node, labelled `person-<name>`. A parser drops the label, so the converter takes the same form from the name.[^converter]

A term's `contributor` names an agent by that id, and `tests/dpv_rules.py` holds it to a record here.[^dpv_rules.py]

[^converter]: scripts/dpv_to_linkml.py, agent_id
[^dpv_rules.py]: tests/dpv_rules.py, _term_errors
