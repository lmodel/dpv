---
type: Service
id: https://w3id.org/lmodel/dpv/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: The knowledge website in `website/`, a Hugo site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/dpv`, built from the README, `docs/`, the schema's pages and this bundle.
resource: website
dependsOn:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/generated-artefacts
references:
  - https://w3id.org/lmodel/dpv/knowledge/workflows/knowledge-website
sources:
  - id: site.toml
    resource: website/site.toml
    title: the site's address, title and redirects
  - id: website-readme.md
    resource: website/README.md
generated:
  by: process:ktl-librarian
  at: "2026-11-15T02:37:47Z"
status: draft
---

# Documentation site

The site replaces the mkdocs site. Its options redirect the old main pages, such as `/about` and `/extensions/ai`, to the new ones. The old pages of each class have no redirect, because the classes they described are gone.[^site.toml]

`website/README.md` says how to build it.[^website-readme.md]

[^site.toml]: website/site.toml, the site's address, title and redirects
[^website-readme.md]: website/README.md
