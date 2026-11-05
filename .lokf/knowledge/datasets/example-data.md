---
type: Dataset
id: https://w3id.org/lmodel/dpv/knowledge/datasets/example-data
genre: reference
title: The example data
description: "`tests/data/`: a valid example per class, each kind's a real record of the catalogue, a counter-example per constraint the validator can state, and one per rule it cannot, under `problem/invalid/`."
resource: tests/data
sources:
  - id: test_data.py
    resource: tests/test_data.py
    title: test_counter_examples_fail_where_they_say and test_each_kinds_example_is_a_real_record
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# The example data

A counter-example's first comment names the JSON pointer where it fails, and the test holds it to that place.[^test_data.py]

A kind's example is a copy of a term of that kind, so nothing in it is made up.[^test_data.py]

[^test_data.py]: tests/test_data.py, test_counter_examples_fail_where_they_say and test_each_kinds_example_is_a_real_record
