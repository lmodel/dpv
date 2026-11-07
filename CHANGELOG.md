# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change is a minor release.

## [Unreleased]

### Added

- **The schema as RDF Turtle and the merged schema**, in `project/rdf/` and `project/linkml/`, from `just gen-rdf` and `just gen-merged-schema`.

### Changed

- **The bundle's schema files sit in `.lokf/schema/`**: `lokf.yaml` and the `lokf adapt` copy `dpv.yaml`, as KTL v0.62.0 lays them out.

## [0.1.0] - 2026-11-05

### Added

- **Every DPV 2.3 term as a record** in `src/dpv/data/`, one file per namespace family, with the contributors and DPV's 88 examples. `scripts/dpv_to_linkml.py` writes them from `upstream/`.
- **`upstream/`**, holding DPV's Turtle, examples, machine-readable mapping files and licence at the tag `dpv-2.3`, pinned by git object hash, with a weekly watch.
- **Rules a validator cannot state** in `tests/dpv_rules.py`, and a list of where DPV's own examples leave what a property's `rangeIncludes` and `domainIncludes` name.
- **Tests** that walk the Turtle both ways, compare the catalogue's JSON-LD projection with it triple by triple, and hold an example per class and a counter-example per constraint.
- **`.lokf/dpv.yaml`, the schema's `lokf adapt` copy.** The knowledge release attaches it as `schema-<tag>-dpv.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **The governance files**: SECURITY.md, AI_COVENANT.md, NOTICE and the CONTRIBUTING checklist.

### Changed

- **Terms are records, not classes.** DPV states each concept as a class and as an instance, and 973 classes with no slots could not hold `hasPurpose: dpv:Marketing`. Each kind of concept is a class, 149 of them, and each property a slot.
- **Each element keeps DPV's IRI.** `dpv:` now means `https://w3id.org/dpv#`, where it meant this repository's namespace, and `dpv_linkml:` is this repository's.
- **The two mapping sets DPV publishes read with DPV's term as their subject**, and are written from DPV's files with its licence.
- **The template settings** turn PyPI publishing and the docs preview off, linkml and linkml-runtime are locked at 1.12.1, and the Python project is named `dpv-linkml`.

### Removed

- **The 24 SSSOM sets a matching tool wrote**, with the scripts that overlaid them on the schema.
- **The per-module and per-extension schema trees**, the `dpv_<group>` modules and the import map. An address such as `dpv:schema/dpv_common` no longer answers.
- **`dpv-27560`**, whose Turtle file names four classes and states nothing about them.
- **`upstream-releases/`**, which `upstream/` replaces, with the OWL serialisations and the module copies.
- **The mkdocs site**, with redirects from its main pages to the new site.
