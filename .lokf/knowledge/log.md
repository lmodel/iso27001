# Change Log

## 2026-10-31

* **Changed**: the security properties follow the names ISO/IEC 27000 gives them, since ISO's record of the 2026 edition no longer calls it a vocabulary.
* **Prose**: reworded 22 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Added**: iso27001 LinkML schema, from `src/iso27001/schema/iso27001.yaml` and its adapt copy.
* **Added**: ISO Open Data records of ISO/IEC 27001, from `src/iso27001/schema/iso-open-data/`.
* **Added**: SSSOM mappings to released lmodel schemas, from `src/iso27001/mappings/`.
* **Added**: Generated artefacts, from the justfiles and `.linkml/generators.yaml`.
* **Added**: Test data and tests, from `tests/`.
* **Added**: Scope, influences and what is left out, from the README and `docs/about.md`.
* **Added**: How the schema names its elements and links records, from `docs/about.md` and the schema.
* **Added**: Information security management system (ISMS), a glossary term, from the schema.
* **Added**: Annex A control, a glossary term, from the schema.
* **Added**: Statement of Applicability, a glossary term, from the schema.
* **Added**: Documented information, a glossary term, from the schema.
* **Added**: Risk treatment, a glossary term, from the schema.
* **Added**: Nonconformity, a glossary term, from the schema.
* **Added**: Information security event and incident, a glossary term, from the schema.
* **Added**: ISO/IEC 27001:2022, the standard the schema models, from ISO Open Data's records.
* **Added**: ISO Open Data, the source of the pinned records, from its open data page.
* **Added**: Regenerate and test after a schema change, from CONTRIBUTING.md and the justfiles.
* **Added**: Validate ISMS data against the schema, from `docs/index.md`.
* **Added**: Update the upstream pins, from `scripts/check_upstream_release.py`.
* **Added**: Merge the standard's text into a private copy, from `src/iso27001/schema/OVERLAY.md`.
* **Added**: Cut a release, from `.releaserc.json` and CONTRIBUTING.md.
* **Added**: Licence and attribution, from NOTICE and the README.
* **Added**: Security policy, from SECURITY.md.
* **Added**: AI covenant, from AI_COVENANT.md.
* **Added**: Documentation site, from `website/`.
* **Added**: Build and test (main.yaml), from `.github/workflows/main.yaml`.
* **Added**: Lint & docs (lint-and-docs.yaml), from `.github/workflows/lint-and-docs.yaml`.
* **Added**: Upstream watch (upstream-watch.yaml), from `.github/workflows/upstream-watch.yaml`.
* **Added**: Semantic release (semantic-release.yml), from `.github/workflows/semantic-release.yml`.
* **Added**: Knowledge Librarian (knowledge-librarian.yaml), from `.github/workflows/knowledge-librarian.yaml`.
* **Added**: Knowledge Registrar (knowledge-registrar.yaml), from `.github/workflows/knowledge-registrar.yaml`.
* **Added**: Knowledge Release (knowledge-release.yaml), from `.github/workflows/knowledge-release.yaml`.
* **Added**: Knowledge sync (knowledge-sync.yaml), from `.github/workflows/knowledge-sync.yaml`.
* **Added**: Knowledge website (knowledge-website.yaml), from `.github/workflows/knowledge-website.yaml`.
* **Added**: Knowledge sources map, the librarian's scrape map of this repository.
* **Removal**: the sidecar's two example services, which the real concepts replace.
* **Initialization**: Scaffolded the LOKF bundle for iso27001 with placeholder
  services. Real concepts to follow.
