## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Rewrite the terms, the kinds, the catalogue and the mappings from upstream/.
[group('model development')]
gen-schema:
  uv run --quiet scripts/dpv_to_linkml.py --schema --catalogue --mappings

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/dpv.yaml` is the copy `lokf adapt` writes from the schema so that it can sit beside
# `.lokf/lokf.yaml` (`lokf adapt --help` lists the moves). The roots are the classes that
# carry the schema's identifier: DpvTerm, with every kind of concept under it, and the
# vocabulary, the concept scheme, the contributor and the example. A concept names one of
# them as its `type`. Each --keep names a key under one of LOKF's IRIs that takes another kind
# of value, a name or an address where LOKF's takes a concept. The recipes run the `lokf` the sidecar's floor pins (0.9.0 or later);
# LOKF_CMD runs another, such as a checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root DpvTerm --root DpvVocabulary --root DpvConceptScheme --root DpvAgent --root DpvExample --root DpvCatalogue --prefix dpv --keep source --keep source_page --keep isPartOf --keep isDefinedBy --keep DpvWebPage.page_name --keep url"

# Rewrite .lokf/dpv.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/dpv.yaml

# Fail when .lokf/dpv.yaml is stale against the schema or .lokf/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/dpv.yaml --check
