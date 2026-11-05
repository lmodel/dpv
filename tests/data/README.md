# Test data

`valid/<Class>-<anything>.yaml` must validate against `<Class>`. Each kind's example is a real record of the catalogue. `tests/test_data.py` holds each file to the JSON Schema.

`invalid/<Class>-<anything>.yaml` must fail, and its first line names the JSON pointer where.

`problem/invalid/` holds what passes the JSON Schema and breaks a rule of `tests/dpv_rules.py`, which a validator cannot state.
