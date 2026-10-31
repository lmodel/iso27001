---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/iso27001/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: iso27001 Knowledge Bundle
description: ISO/IEC 27001:2022 information security management system records (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/iso27001/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# iso27001 Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for iso27001. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The Astro Starlight site in `website/`, for <https://lmodel.github.io/iso27001>: the README as its home page, the pages of `docs/`, the schema's element pages, a page per concept of this bundle with its trust label, and the bundle's exports, built and published by Knowledge website, with redirects from the retired mkdocs addresses.

# Datasets

* [iso27001 LinkML schema](datasets/iso27001-linkml-schema.md) - The LinkML schema `src/iso27001/schema/iso27001.yaml`, version `2022/Amd 1:2024`: the records an organization keeps to run an information security management system (ISMS) to ISO/IEC 27001:2022, in 38 classes with the `Isms` prefix, 13 enums including the 93 Annex A controls by number, and its `lokf adapt` copy `.lokf/iso27001.yaml`, rooted on seven classes.
* [ISO Open Data records of ISO/IEC 27001](datasets/iso-open-data-records.md) - The pinned extract `src/iso27001/schema/iso-open-data/iso_deliverables_metadata.jsonl`: ISO Open Data's records of ISO/IEC 27001:2022, its Amendment 1:2024, ISO/IEC 27002:2022 and ISO/IEC 27000:2026 as of 2026-10-28, each without its scope, under the ODC Attribution License, which the upstream watch checks weekly.
* [SSSOM mappings to released lmodel schemas](datasets/sssom-mappings.md) - The three SSSOM mapping sets under `src/iso27001/mappings/`, 14 class-level rows from the schema's classes to classes of the released lmodel/oscal, lmodel/nist-sp-800-53 and lmodel/spdx schemas, which `just gen-project` merges into the schema, and the sets dropped until their targets are released.
* [Generated artefacts](datasets/generated-artefacts.md) - What `just gen-project`, `just gen-project-extended` and `just gen-doc` write from the schema: the Python dataclasses and Pydantic models in `src/iso27001/datamodel/`, the JSON Schema, OWL, SHACL, ShEx, SQL and other files in `project/`, the merged schema in `docs/schema/` and the element pages in `docs/elements/`, none of them edited by hand.
* [Test data and tests](datasets/test-data.md) - The schema's tests: 35 valid examples and 47 counter-examples under `tests/data/`, 61 controls derived from Probo's mitigations, and the tests that hold them to the validator, hold the header to ISO Open Data's records, check the upstream watch and the overlay, and keep the adapt copy apart from LOKF and nine released neighbours in `tests/neighbours/`.

# Explanations

* [Scope, influences and what is left out](explanations/scope-and-influences.md) - What the iso27001 schema models (the records an ISMS keeps under clauses 4 to 10 and Annex A of ISO/IEC 27001:2022), what shaped it (the standard, with names from ISO/IEC 27000, ISO/IEC 27005 and ISO 19011), what it maps to, and what it leaves out: the standard's text, certification itself and a fixed risk method.
* [How the schema names its elements and links records](explanations/names-and-references.md) - Why every class and enum carries the `Isms` prefix, how attributes and shared slots are named, how a record refers to another by `isms_id` through `IsmsRecordMixin`, why the record base is a mixin, and how the Statement of Applicability entries and security incidents are told apart by a type designator.

# Glossary

* [Information security management system (ISMS)](glossary/isms.md) - The organization's managed set of policies, processes, roles and records for information security that ISO/IEC 27001 sets requirements for; the schema's tree root `IsmsManagementSystem` holds one, with its scope and every record it keeps.
* [Annex A control](glossary/annex-a-control.md) - One of the 93 reference controls that Annex A of ISO/IEC 27001:2022 lists in four themes; the schema names each by number in the `IsmsAnnexAControl` enum, from `a_5_1` to `a_8_34`, without its title or text.
* [Statement of Applicability](glossary/statement-of-applicability.md) - The record that lists each control an organization needs, with why and whether it is in place, and each Annex A control it leaves out, with why; the schema models it as `IsmsStatementOfApplicability`, with `IsmsIncludedControl` and `IsmsExcludedControl` entries.
* [Documented information](glossary/documented-information.md) - Information an organization must keep under control, and the medium it is kept on, such as a policy, a procedure or a record; the schema gives such records `IsmsDocumentControlMixin`'s fields for reference, approval, review, classification, retention and change control.
* [Risk treatment](glossary/risk-treatment.md) - Choosing and carrying out how to deal with an information security risk: modify it with controls, retain it, avoid it or share it; the schema records the choice on `IsmsRisk` and the work in `IsmsRiskTreatmentPlan`.
* [Nonconformity](glossary/nonconformity.md) - A requirement not met, whether of ISO/IEC 27001, of the organization or of an interested party; the schema records one as `IsmsNonconformity`, and the action that removes its cause as `IsmsCorrectiveAction`.
* [Information security event and incident](glossary/security-incident.md) - An event is something reported that may bear on information security; an incident is an event assessed as harming it; the schema records an event as `IsmsSecurityEvent` and an incident as its kind `IsmsSecurityIncident`.

# References

* [ISO/IEC 27001:2022](references/iso-iec-27001-2022.md) - ISO/IEC 27001:2022, Information security, cybersecurity and privacy protection: Information security management systems: Requirements, third edition, published 2022-10-25, with Amendment 1:2024, Climate action changes; the standard the schema models, cited by number and never quoted.
* [ISO Open Data](references/iso-open-data.md) - ISO's open data page and its `iso_deliverables_metadata` dataset of every ISO deliverable's metadata, updated daily under the ODC Attribution License (ODC-By) v1.0, which the repository pins its records of ISO/IEC 27001 from and the upstream watch streams each week.

# Playbooks

* [Regenerate and test after a schema change](playbooks/regenerate-and-test.md) - How to change the schema and check it: `uv sync --group dev`, edit `src/iso27001/schema/iso27001.yaml`, then `just lint`, `just gen-project`, `just gen-doc`, `just create-empty-overlay`, `just lokf-adapt` and `just test`, and the pre-commit hooks before a pull request.
* [Validate ISMS data against the schema](playbooks/validate-data.md) - How to check a file of ISMS records with `linkml-validate -s src/iso27001/schema/iso27001.yaml -C <Class>`, why dates are written quoted, and what the generated dataclasses and Pydantic models leave unchecked.
* [Update the upstream pins](playbooks/update-upstream-pins.md) - What to do when the Upstream watch reports that ISO published a new amendment, corrigendum or edition of ISO/IEC 27001, changed a pinned record's stage, named a successor, or changed the dataset's licence: replace the ISO Open Data extract and move the pins in `scripts/check_upstream_release.py` and the schema header together.
* [Merge the standard's text into a private copy](playbooks/merge-licensed-text.md) - How a holder of a licence to ISO/IEC 27001 fills a private copy of the overlay scaffold `iso27001-overlay.template.yaml` with the standard's wording and merges it with `just overlay-licensed-text` into `tmp/iso27001-merged.yaml`, which git ignores and which is never distributed.
* [Cut a release](playbooks/release.md) - How a release is made: Conventional Commits on `main`, an `## [Unreleased]` changelog section, the `v0.0.0` baseline tag that keeps the first release at 0.1.0, and `semantic-release.yml`, which tags the release and dispatches Knowledge Release to attach `schema-<tag>-iso27001.yaml` once `KNOWLEDGE_RELEASE_ENABLED` is true.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external page this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose.

# Policies

* [Licence and attribution](policies/license-and-attribution.md) - The repository's licences and third-party terms: Apache-2.0 for the schema and code, CC BY 4.0 for the knowledge bundle and the mappings, no right to the text of ISO/IEC 27001 or 27002, ODC-By for ISO Open Data's records, MIT for Probo's mitigations and the copier template, and Apache-2.0 for the KTL copies.
* [Security policy](policies/security-policy.md) - How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, the ruleset on `main`, and the two repository settings that are not yet in force.
* [AI covenant](policies/ai-covenant.md) - The repository's rules for work done with artificial intelligence (AI): you own what you submit, an element under the schema names its clause and never quotes it, no text of ISO/IEC 27001 goes anywhere in the repository, ISO Open Data's records are never edited, and the scheduled librarian proposes changes only through reviewed pull requests.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow, `.github/workflows/main.yaml`: on a push to main and on every pull request, its test job runs `just test` on Python 3.10 to 3.14, and on 3.13 also `just lint` and `just lokf-adapt-check`, the check that `.lokf/iso27001.yaml` is current.
* [Lint & docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on a push to main, every pull request, a Monday 06:00 UTC schedule and by hand, four jobs run ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), and markdownlint, lychee and codespell over the Markdown.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its iso-records job runs `scripts/check_upstream_release.py` against ISO Open Data's live dataset and licence, and on a finding opens or updates the issue titled Upstream watch: ISO's records of ISO/IEC 27001 have changed.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request into main, its plan job checks that the commits, the changelog and the title would release and previews the release; on a push to main, its release job in the release Environment tags vX.Y.Z, publishes the GitHub release and dispatches Knowledge Release.
* [Knowledge Librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: every Monday at 05:00 UTC and by hand, once `KNOWLEDGE_LIBRARIAN_ENABLED` is true, it runs an agent with the ktl-librarian skill (pinned by `TRUST_LADDER_SKILLS_REF` at v0.59.0) in a read-only job and opens a review pull request from a separate job that runs no agent.
* [Knowledge Registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: the gate on the knowledge bundle, run on pull requests that touch `.lokf/` or `knowledge_bundle/`, every Monday at 06:00 UTC and by hand; it validates the bundle and its relation targets against the domain schema, runs the conventions script, and checks that each new confirmation by a person is backed by an approval or a signed commit.
* [Knowledge Release (knowledge-release.yaml)](workflows/knowledge-release.md) - The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: dispatched with a release's tag, or started by a published release once `KNOWLEDGE_RELEASE_ENABLED` is true, it attaches the bundle zip, the domain schema as `schema-<tag>-iso27001.yaml` with its checksum, and the Copilot skills to the release, when the bundle or the schema changed or `force` is set.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: every Monday at 04:10 UTC and by hand, it moves the sidecar's copies and the skills pin to the newest Knowledge Trust Ladder release through one pull request, opened with the `KNOWLEDGE_SYNC_TOKEN` secret, and holds the workflow changes for a person to approve.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds `website/` and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is true.
