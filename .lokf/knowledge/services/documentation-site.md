---
type: Service
id: https://w3id.org/lmodel/dpv/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/dpv`, built from the README, `docs/`, the schema's pages and this bundle.
resource: website
dependsOn:
  - https://w3id.org/lmodel/dpv/knowledge/datasets/generated-artefacts
references:
  - https://w3id.org/lmodel/dpv/knowledge/workflows/knowledge-website
sources:
  - id: site.config.mjs
    resource: website/site.config.mjs
    title: REPO, SITE, BASE and REDIRECTS
  - id: website-readme.md
    resource: website/README.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T14:57:48Z"
status: draft
---

# Documentation site

The site replaces the mkdocs site. Its options send the old landing pages, such as `/about` and `/extensions/ai`, to the new ones. The old pages of each class do not move, because the classes they described are gone.[^site.config.mjs]

`website/README.md` says how to build it.[^website-readme.md]

[^site.config.mjs]: website/site.config.mjs, REPO, SITE, BASE and REDIRECTS
[^website-readme.md]: website/README.md
