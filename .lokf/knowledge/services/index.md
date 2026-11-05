# Services

* [The converter](converter.md) - `scripts/dpv_to_linkml.py`: reads the Turtle under `upstream/` and writes the terms module, the kinds' modules, the catalogue, the examples and the SSSOM sets. `just gen-schema` runs it, and it stops on a predicate no table names.
* [Documentation site](documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/dpv`, built from the README, `docs/`, the schema's pages and this bundle.
