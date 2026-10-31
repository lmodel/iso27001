---
type: Service
id: https://w3id.org/lmodel/iso27001/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: "The Astro Starlight site in `website/`, for <https://lmodel.github.io/iso27001>: the README as its home page, the pages of `docs/`, the schema's element pages, a page per concept of this bundle with its trust label, and the bundle's exports, built and published by Knowledge website, with redirects from the retired mkdocs addresses."
resource: website
endpoint: https://lmodel.github.io/iso27001
documentation: website/README.md
sources:
  - id: site.config.mjs
    resource: website/site.config.mjs
    title: the values and options
  - id: website-readme.md
    resource: website/README.md
    title: what each page is built from
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Documentation site

`website/` holds an Astro Starlight site. `website/site.config.mjs` names the repository `lmodel/iso27001`, the site `https://lmodel.github.io` with the base path `/iso27001`, and the title `iso27001`.[^site.config.mjs] It shows the pages of `docs/` except `docs/templates-linkml/`. It redirects the addresses the retired mkdocs site gave its pages:

- `/elements` to `/schema/`;
- each class and enum page of the retired schema to its successor's page, such as `/elements/SecurityControl` to `/schema/IsmsControl/`;
- any other page under `/elements` whose name the schema still has to that page under `/schema/`;
- `/about` and `/rights` to their pages under `/docs/`.

The other options take the site's defaults: the Knowledge Trust Ladder logo, the README as the home page, the changelog once it holds a release, and the schema's pages that `just gen-doc` writes.

`website/README.md` says what each page is built from. It also says that `npm run build` syncs the bundle, the README, the docs and the schema's pages before it builds and checks every link.[^website-readme.md] [Knowledge website](../workflows/knowledge-website.md) builds the site on each change to its sources and publishes it once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.

[^site.config.mjs]: website/site.config.mjs, REPO, SITE, BASE, TITLE, DOCS and REDIRECTS
[^website-readme.md]: website/README.md, the build and its sources
