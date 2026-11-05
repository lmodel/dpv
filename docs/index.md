# dpv

This project is a LinkML model of the Data Privacy Vocabulary (DPV) 2.3 of the W3C Data Privacy Vocabularies and Controls Community Group. It holds every term of DPV's vocabularies as a record, and DPV's examples as data.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the schema reads DPV, where each part comes from and what it leaves out
- [`dpv.yaml`](schema/dpv.yaml): the schema, with its modules merged

## Validating a file of the catalogue

```bash
uv run linkml-validate -s src/dpv/schema/dpv.yaml -C DpvCatalogue src/dpv/data/dpv-2.3-core.yaml
```

`project/jsonschema/dpv.schema.json` is the same schema for anyone without LinkML. `tests/dpv_rules.py` adds what a validator cannot state, such as that a value names a term that exists.

## Describing a use case

A thing a use case describes is a `DpvResource`, which holds any DPV property:

```yaml
id: ex:Newsletter
rdf_type:
  - dpv:Process
hasPurpose:
  - dpv:DirectMarketing
hasPersonalData:
  - pd:EmailAddress
```

```bash
uv run linkml-validate -s src/dpv/schema/dpv.yaml -C DpvResource newsletter.yaml
```

## What the catalogue holds

| File | Concepts | Properties |
| --- | --- | --- |
| `dpv-2.3-core.yaml` | 973 | 162 |
| `dpv-2.3-pd.yaml` | 231 | 0 |
| `dpv-2.3-tech.yaml` | 130 | 52 |
| `dpv-2.3-ai.yaml` | 231 | 10 |
| `dpv-2.3-risk.yaml` | 507 | 43 |
| `dpv-2.3-justifications.yaml` | 66 | 0 |
| `dpv-2.3-loc.yaml` | 5,270 | 4 |
| `dpv-2.3-legal.yaml` | 896 | 15 |
| `dpv-2.3-sector.yaml` | 415 | 0 |
| `dpv-2.3-standards.yaml` | 136 | 21 |
| `dpv-2.3-examples.yaml` | 1 | 0 |

`dpv-2.3-agents.yaml` holds 70 contributors and organizations, and `dpv-2.3-examples.yaml` also holds the 88 examples.

## What the validator cannot check

- That a value names a term that exists. `tests/dpv_rules.py` checks it.
- That a value is of a class a property's `rangeIncludes` names, which DPV does not require. `tests/test_examples.py` lists where DPV's own examples leave those classes.
