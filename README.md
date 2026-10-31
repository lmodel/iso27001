<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# iso27001

ISO/IEC 27001:2022 information security management system records (LinkML)

> **Two ways in.** This README is one; the other is a docent, a museum's name
> for a guide. Install
> [`ktl-docent`](https://github.com/noelmcloughlin/knowledge-trust-ladder) into
> whatever agent you already use, by a route from
> [the install page](https://w3id.org/ktl/docs/install/), and ask it anything
> about this project. It answers from `.lokf/knowledge/`,
> the checked part of what the project knows, and says how far each answer has
> been trusted (still a draft, checked by automation only, or confirmed by a
> named person). It opens the source for exact values, and records what it
> could not answer so the gap gets filled. The same docent serves a person at a
> prompt, an agent reading this file, or a chatbot that can load a skill.
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt`
> says how to weigh it.

## Documentation Website

[https://lmodel.github.io/iso27001](https://lmodel.github.io/iso27001)

## What it models

The schema models the records an organization keeps to run an information security management system (ISMS) to [ISO/IEC 27001:2022](https://www.iso.org/standard/82875.html), third edition, with [Amendment 1:2024](https://www.iso.org/standard/88435.html), Climate action changes. The schema holds no text of the standard, which is ISO's copyright. Each element cites the clause or Annex A control it models by number.

* **The ISMS** (`IsmsManagementSystem`): its scope, context and certification, and a list of each kind of record it keeps (clause 4).
* **Context and leadership**: the organization (`IsmsOrganization`), its interested parties (`IsmsInterestedParty`), the information security policy (`IsmsPolicy`), topic-specific policies (`IsmsTopicSpecificPolicy`) and roles (`IsmsRole`) (clauses 4 and 5).
* **Planning and risk**: objectives (`IsmsObjective`), the risk assessment and treatment processes, risk assessments, the risk register (`IsmsRisk`) and risk treatment plans (clauses 6 and 8).
* **Controls**: the organization's controls (`IsmsControl`), each answering to Annex A controls by number, and the Statement of Applicability (`IsmsStatementOfApplicability`) with its included and excluded entries.
* **Support and operation**: resources, competence records, the awareness programme, the communication plan, other documented information (`IsmsDocumentedInformation`), operational procedures and the asset inventory (`IsmsAsset`) (clauses 7 and 8, Annex A 5.9).
* **Performance evaluation**: the monitoring programme, audit programmes, audits and their findings, and management reviews (clause 9).
* **Improvement**: nonconformities, corrective actions and opportunities for improvement (clause 10), and information security events and incidents (Annex A 5.24 to 5.28).
* **Annex A** (`IsmsAnnexAControl`, `IsmsControlTheme`): the 93 reference controls by number, from `a_5_1` to `a_8_34`, in their four themes.

The schema header's `version` is the edition with its amendment, `2022/Amd 1:2024`, and its `source` is ISO's page for the edition. ISO sells the standard's text, so the repository pins ISO's own metadata instead. [src/iso27001/schema/iso-open-data/](src/iso27001/schema/iso-open-data) holds ISO Open Data's records of the edition, its amendment, ISO/IEC 27002:2022 and ISO/IEC 27000:2026, as published on 2026-10-28 and matched by hash. A weekly workflow opens an issue when ISO publishes another amendment, corrigendum or edition, changes a record's stage, or names a successor.

A licence holder can merge the standard's wording into a private copy of the schema with the overlay that [OVERLAY.md](src/iso27001/schema/OVERLAY.md) describes. The private copy is never committed.

Release tags number the schema's versions.

## Influences

The schema renders one publication, ISO/IEC 27001:2022 with its amendment. Its enums follow the names ISO/IEC 27000 gives the three security properties, ISO/IEC 27005 the four risk treatment options, and ISO 19011 the three kinds of audit. Its release asset and governance files follow [lmodel/nist-csf-v2](https://github.com/lmodel/nist-csf-v2).

## Mappings

The schema maps to three vocabularies and borrows from none. Each mapping names a class of a released lmodel schema, by the IRI that release gives it, and comes from an SSSOM file in [src/iso27001/mappings/](src/iso27001/mappings).

* **OSCAL**, the Open Security Controls Assessment Language ([lmodel/oscal](https://github.com/lmodel/oscal)): the included control is close to OSCAL's implemented requirement, the role to OSCAL's role, and OSCAL's party is broader than the organization. The ISMS, the control, the Statement of Applicability, the risk treatment plan, the corrective action, the audit, the audit programme and the asset are related to their nearest OSCAL classes.
* **SP 800-53** ([lmodel/nist-sp-800-53](https://github.com/lmodel/nist-sp-800-53)): the organization's control is related to SP 800-53's control.
* **SPDX**, the Software Package Data Exchange ([lmodel/spdx](https://github.com/lmodel/spdx)): the organization is close to SPDX's organization, and an asset is related to SPDX's package.

Mappings to schemas that have no release yet, and to terms the released schemas do not hold, such as one SP 800-53 control, are left out until those exist. [docs/value.md](docs/value.md#implementation-status) lists what was dropped.

## Not modelled here

* The text of ISO/IEC 27001 and ISO/IEC 27002: clauses, control titles and guidance.
* Certification itself: the certification body's audit programme, its grading and its certificates, beyond the ISMS's own record of an audit and its certification status.
* A fixed method of risk assessment. The likelihood, impact and risk-level scales and the incident categories are offered for an organization that adopts them. ISO/IEC 27001 leaves both to the organization.
* The rules no validator checks, which [docs/index.md](docs/index.md) lists.

## Repository Structure

* [docs/](docs/): the website's pages, with the generated schema pages in [elements/](docs/elements/)
* [examples/](examples/): usage examples
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch, the overlay scripts, the SSSOM merge and the DBML wrapper
* [src/iso27001/schema/](src/iso27001/schema): the LinkML schema, `iso27001.yaml` (edit this), ISO Open Data's records and the overlay scaffold
* [src/iso27001/mappings/](src/iso27001/mappings): the SSSOM mappings
* [src/iso27001/datamodel/](src/iso27001/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data), Probo's mitigations in [data/third_party/probo/](tests/data/third_party/probo), and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle, in the Linked Open Knowledge Format (LOKF). Its domain schema is `.lokf/iso27001.yaml`, which `lokf adapt` writes from `src/iso27001/schema/iso27001.yaml`. Edit the source, never the copy. A release carries the copy as `schema-<tag>-iso27001.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

`just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` says when it is stale. `project.justfile` names the classes the copy roots on `Concept`, and a concept may name any of them as its `type`: the records that describe how an organization runs its ISMS and stay true for a while. Records of events and of work done, such as audits, findings, reviews and incidents, stay plain classes. In Obsidian, add these classes to the KTL Registrar and KTL Curator plugins' *Known LOKF types* setting:

```text
IsmsPolicy, IsmsTopicSpecificPolicy, IsmsRole, IsmsControl, IsmsAsset, IsmsDocumentedInformation, IsmsOperationalProcedure
```

In the copy, LOKF's `id` takes the place of `isms_id`, so a concept's own `id` identifies the record, and a reference names the other concept's `id`. A name and a description are the concept's own `title` and `description`.

A host imports the copy beside LOKF's schema, `lokf.yaml`, and beside other adapt copies. LinkML merges them into one namespace, where the last definition of a name wins silently. So no class, enum or type shares a name with LOKF's or with the copies of slsa, github-actions, oscal, spdx, nist-sp-800-218, nist-sp-800-53, nist-sp-800-171, nist-csf-v2 and in-toto.

A slot shares a name only where it carries LOKF's meaning and Internationalized Resource Identifier (IRI), as `title` and `description` do, so `lokf adapt` folds the two into LOKF's and renames nothing. The copy shares no other key with the nine neighbours, and `tests/test_schema_rules.py` fails on a new shared name.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)).

The knowledge bundle in `.lokf/knowledge/` is under the Creative Commons Attribution 4.0 International licence (CC BY 4.0), as its `index.md` declares.

ISO/IEC 27001 and ISO/IEC 27002 are copyright ISO and IEC, and this repository's licence grants no right to reproduce their text. The schema's descriptions are this project's own words. ISO Open Data's records are under the ODC Attribution License (ODC-By) v1.0, and Probo's mitigations under the MIT License: see [NOTICE](NOTICE) and [docs/rights.md](docs/rights.md).

This is not an official ISO project, and its use implies no endorsement by ISO or IEC.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
