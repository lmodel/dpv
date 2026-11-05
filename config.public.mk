# config.public.mk

# This file is public in git. No sensitive info allowed.

###### schema definition variables, used by justfile

# Note:
# - just works fine with quoted variables of dot-env files like this one
LINKML_SCHEMA_NAME="dpv"
LINKML_SCHEMA_AUTHOR="Noel McLoughlin <noel.mcloughlin@gmail.com>"
LINKML_SCHEMA_DESCRIPTION="Data Privacy Vocabularies (DPV) - LinkML Schema"
LINKML_SCHEMA_SOURCE_DIR="src/dpv/schema"

###### linkml generator variables, used by justfile

## gen-project configuration file
LINKML_GENERATORS_CONFIG_YAML=.linkml/generators.yaml

## LinkML import map (relative to repo root). Maps canonical URI prefixes
## (e.g. `dpv:`) to local source directories so that URI-style imports such
## as `dpv:schema/dpv_core` resolve to files in this repo during build.
## The committed `importmap.json` is the source of truth (relative paths);
## the justfile materialises an absolute-path copy at `tmp/importmap.json`
## because SchemaLoader joins importmap values with the importing schema's
## directory. Build tooling must consume the absolutised copy.
## Set to an empty string to disable and fall back to HTTP resolution.
LINKML_IMPORT_MAP=tmp/importmap.json

## pass args if gendoc ignores config.yaml (i.e. --no-mergeimports)
LINKML_GENERATORS_DOC_ARGS=

## pass args to workaround genowl rdfs config bug (linkml#1453)
##   (i.e. --no-type-objects --no-metaclasses --metadata-profile=rdfs)
# LINKML_GENERATORS_OWL_ARGS="--no-type-objects --no-metaclasses --metadata-profile=rdfs"
LINKML_GENERATORS_OWL_ARGS=

## pass args to pydantic generator which isn't supported by gen-project
## https://github.com/linkml/linkml/issues/2537
LINKML_GENERATORS_PYDANTIC_ARGS=
