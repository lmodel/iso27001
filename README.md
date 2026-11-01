<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# iso27001

ISO/IEC 27001:2022 information security management system records (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/iso27001](https://lmodel.github.io/iso27001)

## What it models

The schema models the records an organization keeps to run an information security management system (ISMS) to [ISO/IEC 27001:2022](https://www.iso.org/standard/82875.html), third edition, with [Amendment 1:2024](https://www.iso.org/standard/88435.html), Climate action changes. It covers clauses 4 to 10, from the ISMS's scope and policies to risks, controls, the Statement of Applicability, audits and improvement, and the 93 Annex A controls by number. Each element cites the clause or Annex A control it models by number, and the schema holds no text of the standard.

ISO sells the standard's text, so [src/iso27001/schema/iso-open-data/](src/iso27001/schema/iso-open-data) pins ISO Open Data's records of the edition and its neighbours instead. A weekly workflow opens an issue when ISO publishes another amendment, corrigendum or edition, changes a record's stage, or names a successor. A licence holder can merge the standard's wording into a private copy of the schema with the overlay that [OVERLAY.md](src/iso27001/schema/OVERLAY.md) describes. The private copy is never committed.

## Influences

The enums follow the names ISO/IEC 27000 gives the three security properties, ISO/IEC 27005 the four risk treatment options, and ISO 19011 the three kinds of audit. The release asset and governance files follow [lmodel/nist-csf-v2](https://github.com/lmodel/nist-csf-v2).

## Mappings

Each mapping names a class of a released lmodel schema and comes from an SSSOM file in [src/iso27001/mappings/](src/iso27001/mappings).

* **OSCAL** ([lmodel/oscal](https://github.com/lmodel/oscal)): the included control is close to OSCAL's implemented requirement and the role to OSCAL's role, and the other record classes are related to their nearest OSCAL classes.
* **SP 800-53** ([lmodel/nist-sp-800-53](https://github.com/lmodel/nist-sp-800-53)): the organization's control is related to SP 800-53's control.
* **SPDX** ([lmodel/spdx](https://github.com/lmodel/spdx)): the organization is close to SPDX's organization, and an asset is related to SPDX's package.

[docs/value.md](docs/value.md#implementation-status) lists the mappings left out until their targets are released.

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

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/iso27001.yaml`, is the copy `just lokf-adapt` writes from `src/iso27001/schema/iso27001.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-iso27001.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots on `Concept` the records that describe how an organization runs its ISMS and stay true for a while, so a concept may name any of them as its `type`. Records of events and of work done, such as audits, findings, reviews and incidents, stay plain classes. In Obsidian, add these classes to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
IsmsPolicy, IsmsTopicSpecificPolicy, IsmsRole, IsmsControl, IsmsAsset, IsmsDocumentedInformation, IsmsOperationalProcedure
```

In the copy, LOKF's `id` takes the place of `isms_id`, so a concept's own `id` identifies the record, and a reference names the other concept's `id`.

No class, enum or type of the copy shares a name with LOKF's schema or with another lmodel copy, and `tests/test_schema_rules.py` fails on a new shared name.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in `.lokf/knowledge/` is under CC BY 4.0.

ISO/IEC 27001 and ISO/IEC 27002 are copyright ISO and IEC, and this repository's licence grants no right to reproduce their text. The schema's descriptions are this project's own words. ISO Open Data's records are under ODC-By v1.0, and Probo's mitigations under the MIT License: see [NOTICE](NOTICE) and [docs/rights.md](docs/rights.md). This is not an official ISO project, and its use implies no endorsement by ISO or IEC.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
