---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/dpv/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: dpv Knowledge Bundle
description: Data Privacy Vocabulary (DPV) 2.3 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/dpv/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# dpv Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for dpv. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [The converter](services/converter.md) - `scripts/dpv_to_linkml.py`: reads the Turtle under `upstream/` and writes the terms module, the kinds' modules, the catalogue, the examples and the SSSOM sets. `just gen-schema` runs it, and it stops on a predicate no table names.
* [Documentation site](services/documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/dpv`, built from the README, `docs/`, the schema's pages and this bundle.

# References

* [Data Privacy Vocabulary (DPV)](references/dpv-vocabulary.md) - The upstream authority: DPV 2.3 of 2026-02-28, the vocabulary of the W3C Data Privacy Vocabularies and Controls Community Group for describing the processing of personal data, at `https://w3id.org/dpv/2.3`.
* [The DPV repository](references/dpv-repository.md) - The Community Group's repository, `w3c-cg/dpv`, whose tag `dpv-2.3` names commit `cbcd215`. It keeps each edition in a folder, and the examples and the mappings at its root.

# Datasets

* [The DPV LinkML schema](datasets/dpv-linkml-schema.md) - `src/dpv/schema/`: the umbrella `dpv.yaml` over `dpv_core`, `dpv_terms` and one module of kinds per namespace family. It models DPV 2.3 under DPV's own IRIs, and `DpvCatalogue` is its tree root.
* [The core module](datasets/core-module.md) - `src/dpv/schema/dpv_core.yaml`, written by hand: the date and address types, the term status list, the classes for a vocabulary, a concept scheme, an agent, a web page and an interval, and the slots they share.
* [The terms module](datasets/terms-module.md) - `src/dpv/schema/dpv_terms.yaml`, which the converter writes: `DpvTerm` and its children `DpvConcept`, `DpvProperty` and `DpvResource`, `DpvExample`, `DpvStatement`, and one slot per DPV property under its own IRI.
* [The kinds' modules](datasets/kinds-modules.md) - The modules the converter writes with one class per kind of term, 149 in all, under each kind's own IRI: `dpv_kinds` for the core, and `dpv_pd`, `dpv_tech`, `dpv_ai`, `dpv_risk`, `dpv_legal`, `dpv_sector` and `dpv_standards`.
* [The catalogue](datasets/catalogue.md) - `src/dpv/data/`: one YAML file per namespace family, with every vocabulary, concept scheme, concept and property of DPV 2.3 as a record under its own IRI: 8,856 concepts and 307 properties.
* [The examples as data](datasets/examples.md) - `src/dpv/data/dpv-2.3-examples.yaml`: DPV's 88 examples, each with its description, and the statements of 85 of them as `DpvResource` records. Three files do not parse.
* [Where DPV's examples leave a property's usual classes](datasets/example-departures.md) - `tests/example_departures.yaml`: each place DPV's own examples use a property beyond its `rangeIncludes` or `domainIncludes`, or give a literal where the range names a class: 58 values, 65 subjects and 30 literals.
* [The contributors](datasets/contributors.md) - `src/dpv/data/dpv-2.3-agents.yaml`: the 70 people and organizations DPV's files name as contributors and creators, each with an id of the form `dpv_agent:person-<name>` or `dpv_agent:org-<name>`.
* [DPV's own mappings as SSSOM](datasets/sssom-mappings.md) - `src/dpv/mappings/`: two SSSOM sets that render the mapping files DPV publishes, 5 rows for ISO/IEC 29100:2024 terms and 24 for ODRL, each row reading with DPV's term as its subject.
* [The copy of DPV's files](datasets/upstream-copy.md) - `upstream/`: the Turtle of each vocabulary, the 88 examples, the ISO and ODRL mapping files and the licence, unchanged at the tag `dpv-2.3`. `scripts/upstream_pins.tsv` holds each of the 160 files' git object hashes.
* [The adapt copy](datasets/adapt-copy.md) - `.lokf/schema/dpv.yaml`, which `just lokf-adapt` writes from the schema so that it can sit beside LOKF's: the file this bundle validates against, and the file a release attaches as `schema-<tag>-dpv.yaml`.
* [The neighbours' copies](datasets/neighbour-copies.md) - `tests/neighbours/`: the adapt copies 27 other lmodel repositories release, each the release's schema asset, which tests use to hold this copy's names apart from theirs.
* [The example data](datasets/example-data.md) - `tests/data/`: a valid example per class, each kind's a real record of the catalogue, a counter-example per constraint the validator can state, and one per rule it cannot, under `problem/invalid/`.
* [The generated artefacts](datasets/generated-artefacts.md) - What the generators write from the schema: `project/`, `src/dpv/datamodel/` and `docs/schema/dpv.yaml`. They are committed and never edited, and the SQL generator is off.
* [Marketing](datasets/example-purpose.md) - The purpose `dpv:Marketing` of DPV 2.3, written as a concept of type `DpvPurpose` in the adapt copy's keys. It shows that the domain schema admits a term of a kind.
* [A process with a purpose](datasets/example-process.md) - The process `exd:PDH1` of DPV's example E0026, written as a concept of type `DpvResource`. It shows that the domain schema admits a thing a use case describes, with any DPV property.

# Explanations

* [Why terms are records](explanations/terms-as-records.md) - Why the schema holds DPV's terms as records and not as classes: DPV states each concept as a class and as an instance, so one class per term could not say that a process's `hasPurpose` is `dpv:Marketing`.
* [How kinds and slots get their names](explanations/kinds-and-slots.md) - How the converter names what it writes: a kind's class takes a `Dpv` prefix and a slot keeps its property's local name, and where two namespaces define one name, the core keeps it and the other takes its namespace first.
* [What stays open](explanations/what-stays-open.md) - Why no validator refuses a value for leaving a property's usual classes: DPV states `domainIncludes` and `rangeIncludes`, not `rdfs:domain` and `rdfs:range`, so `DpvResource` holds any property.
* [What the records leave out](explanations/what-the-records-leave-out.md) - The facts of DPV's files no record holds, each with its reason: `skos:narrower`, which the records regenerate, the repeated `schema:` domain and range, what says how the site publishes a file, and `dpv-27560`.
* [What the data shows](explanations/what-the-data-shows.md) - What DPV's own files hold that a reader would not expect: names defined nowhere, predicates no vocabulary has, three example files that do not parse, and a term with two creation dates.
* [The mappings](explanations/mappings.md) - Which mappings this repository holds and why: only what DPV's editors publish in machine-readable form, for ISO/IEC 29100:2024 terms and for ODRL. The other 24 sets, which a matching tool wrote, are gone.

# Glossary

* [Term](glossary/term.md) - A term: one thing DPV's vocabularies state as a concept or a property, under its own IRI. Each is one record here, a `DpvConcept` or a `DpvProperty`.
* [Kind](glossary/kind.md) - A kind: a type a DPV concept holds beyond `rdfs:Class` and `skos:Concept`, such as `dpv:Purpose`. Each of the 149 kinds is a class of this schema, and a record's `rdf_type` names its kinds.
* [Resource](glossary/resource.md) - A resource: a thing a use case describes with DPV, such as a process. `DpvResource` holds any DPV property, because DPV states none as limited to a class.
* [Namespace family](glossary/namespace-family.md) - A namespace family: the vocabularies this project keeps in one data file, such as `legal`, which holds the law vocabulary of each jurisdiction and each EU law.
* [Departure](glossary/departure.md) - A departure: a place DPV's own examples use a property beyond what its `rangeIncludes` or `domainIncludes` name, or give a literal where the range names a class. It breaks no rule of RDF.
* [Adapt copy](glossary/adapt-copy.md) - An adapt copy: the form of a schema `lokf adapt` writes so that it can sit beside LOKF's, in which concept classes descend from `Concept` and keys LOKF also has are renamed. Here it is `.lokf/schema/dpv.yaml`.

# Playbooks

* [Regenerate and test](playbooks/regenerate-and-test.md) - How to change the schema: edit the converter or a hand-written module, run `just gen-schema`, `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write.
* [Validate a file of the catalogue](playbooks/validate-a-file.md) - How to validate a file: `uv run linkml-validate -s src/dpv/schema/dpv.yaml -C DpvCatalogue <file>`, or the committed JSON Schema without LinkML, and `tests/dpv_rules.py` for what a validator cannot state.
* [Describe a use case](playbooks/describe-a-use-case.md) - How to describe a thing in a use case with DPV: write a `DpvResource` with an `id`, the term it is an instance of in `rdf_type`, and DPV's properties as keys, then validate it with `-C DpvResource`.
* [Update the upstream pins](playbooks/update-upstream-pins.md) - What to do when the watch reports another DPV release: read what changed, replace `upstream/`, the pins and the headers together, regenerate, and look at each test that fails.
* [Cut a release](playbooks/release.md) - How a release happens: write `## [Unreleased]`, merge with a releasing commit type, and `semantic-release.yml` tags, writes the changelog and dispatches the knowledge release, which attaches the assets.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.

# Policies

* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work here: a person owns every contribution, an element says what DPV says, a rule states only what DPV states, and a mapping is DPV's own or it is absent.
* [Licence and attribution](policies/license-and-attribution.md) - Whose work each part is: the code and the schema under Apache-2.0, the bundle under CC BY 4.0, and DPV's files and the text taken from them under the W3C Software and Document License, which NOTICE reproduces.
* [Security policy](policies/security-policy.md) - How to report a vulnerability, what this repository releases, what executes here and what holds each surface. A report goes through GitHub's private vulnerability reporting, and only the latest release receives fixes.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow: on every pull request and push to `main`, it runs `just test` on Python 3.10 to 3.14, and lints the schema and checks the adapt copy on 3.13.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The static checks on pull requests and on `main`: ShellCheck, actionlint, the governance files' word budgets, markdownlint, lychee and codespell.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The workflow that computes the next version from Conventional Commits on `main`, promotes the changelog, tags and publishes the GitHub Release, and dispatches the knowledge release.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The weekly check that `scripts/check_upstream_release.py` runs: another release of DPV, a moved tag, a changed or missing pinned file, or a changed licence opens or updates an issue.
* [Knowledge registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The gate on the bundle: it validates the bundle on each pull request that touches it, and checks who vouched for what.
* [Knowledge librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The sidecar's scheduled agent run that keeps the bundle in step with the repository. It stays inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`, and a person merges what it proposes.
* [Knowledge release (knowledge-release.yaml)](workflows/knowledge-release.md) - The workflow that attaches the bundle, a Copilot skill and the schema's adapt copy to a GitHub release, each with its `.sha256` and an attestation, when the bundle or the schema changed.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The weekly workflow that keeps the sidecar's copies and the skills pin at the newest release of Knowledge Trust Ladder, by a pull request a person merges.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The workflow that builds `website/` on each pull request that touches its inputs, and deploys it from `main` once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
