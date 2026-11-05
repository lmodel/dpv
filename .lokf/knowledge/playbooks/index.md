# Playbooks

* [Regenerate and test](regenerate-and-test.md) - How to change the schema: edit the converter or a hand-written module, run `just gen-schema`, `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write.
* [Validate a file of the catalogue](validate-a-file.md) - How to validate a file: `uv run linkml-validate -s src/dpv/schema/dpv.yaml -C DpvCatalogue <file>`, or the committed JSON Schema without LinkML, and `tests/dpv_rules.py` for what a validator cannot state.
* [Describe a use case](describe-a-use-case.md) - How to describe a thing in a use case with DPV: write a `DpvResource` with an `id`, the term it is an instance of in `rdf_type`, and DPV's properties as keys, then validate it with `-C DpvResource`.
* [Update the upstream pins](update-upstream-pins.md) - What to do when the watch reports another DPV release: read what changed, replace `upstream/`, the pins and the headers together, regenerate, and look at each test that fails.
* [Cut a release](release.md) - How a release happens: write `## [Unreleased]`, merge with a releasing commit type, and `semantic-release.yml` tags, writes the changelog and dispatches the knowledge release, which attaches the assets.
* [Knowledge sources map](knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.
