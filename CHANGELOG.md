# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Added

- **A pinned copy of ISO Open Data's records of ISO/IEC 27001:2022, its Amendment 1:2024, ISO/IEC 27002:2022 and ISO/IEC 27000:2026, and a weekly upstream watch.** The watch reports a new amendment or corrigendum, a stage change, a successor edition, a changed licence or a drifted copy. The copy leaves out each record's scope, which summarizes the standard in ISO's words.
- **`.lokf/iso27001.yaml`, the schema's `lokf adapt` copy, rooted on the policy, the topic-specific policy, the role, the control, the asset, documented information and the operational procedure.** The knowledge release attaches it as `schema-<tag>-iso27001.yaml`. Tests hold its names apart from those of the Linked Open Knowledge Format (LOKF) and of nine released lmodel copies, and hold every mapping to a term one of them has.
- **An example of each class and a counter-example for each constraint**, held to the validator by `just test`, and 61 controls derived from Probo's mitigations.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.59.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **`.github/release/package-lock.json`, which pins semantic-release and every package it pulls in.** The release job installs from it with `npm ci`, and Dependabot keeps it current.

### Changed

- **The schema is rewritten, and every class and enum carries the `Isms` prefix**, so none shares a name with LOKF or a neighbour.
- **Every record has an `isms_id`, a `title` and a `description`** in place of `id`, `name` and `description`, and a reference holds the `isms_id` of the record it names. A field one class uses is that class's attribute.
- **The Statement of Applicability holds included and excluded entries, and an incident is a kind of event**, each told apart by a type designator. The ISMS lists every kind of record it keeps.
- **The schema's header names the edition, `2022/Amd 1:2024`, ISO's page for it, and the Apache-2.0 licence.**
- **The overlay that merges a licence holder's text into a private copy covers class attributes, and writes only under `tmp/`.** `.gitignore` now keeps the private overlay out of git, as `OVERLAY.md` always said it did.
- **The Python project's name is `iso27001-linkml`.** PyPI publishing stays off.

### Removed

- **Mappings whose target has no release.** The SSSOM files for ATT&CK, CAPEC, CIS Controls, CVE and NVD, CWE, D3FEND, ISO/IEC 29100, ISO/IEC 42001, the KEV catalog, OCSF and STIX are gone. So are the rows for NIST CSF 2.0, SP 800-171, SP 800-218 and SLSA whose objects the released copies do not hold. Fourteen class-level rows to OSCAL, SP 800-53 and SPDX remain.
- **The copied generator wrappers that linkml 1.12.1 makes unnecessary**, and the PyPI publishing workflow, the mkdocs site and its preview.
