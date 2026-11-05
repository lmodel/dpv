---
type: DpvResource
id: https://w3id.org/lmodel/dpv/knowledge/datasets/example-process
genre: reference
title: A process with a purpose
description: The process `exd:PDH1` of DPV's example E0026, written as a concept of type `DpvResource`. It shows that the domain schema admits a thing a use case describes, with any DPV property.
resource: src/dpv/data/dpv-2.3-examples.yaml
hasPurpose:
  - dpv:CommunicationForCustomerCare
hasPersonalData:
  - pd:AccountIdentifier
  - pd:EmailAddressPersonal
derivedFrom:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/examples
sources:
  - id: test_examples.py
    resource: tests/test_examples.py
    title: test_a_real_process_reads_as_dpv_says
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# A process with a purpose

This concept shows how a host describes a thing in its own use case: its `type` is `DpvResource`, which holds any DPV property, and its values name DPV's terms by their CURIEs. It holds part of a record from DPV's example E0026.[^test_examples.py]

[^test_examples.py]: tests/test_examples.py, test_a_real_process_reads_as_dpv_says
