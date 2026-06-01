# About iso27001

A LinkML schema for ISO/IEC 27001:2022 (Information Security Management Systems),
with a curated suite of SSSOM cross-framework mappings and an end-to-end
validation pipeline driven from real-world third-party content.

## Schema

- **35 classes** spanning the full ISMS lifecycle — governance, planning, risk
  assessment & treatment, Annex A controls, support, operations, performance
  evaluation, and continual improvement.
- **13 enumerations** including `AnnexAControlId` (93 permissible values for
  A.5.1–A.5.37, A.6.1–A.6.8, A.7.1–A.7.14, A.8.1–A.8.34), `ControlCategory`,
  `RiskTreatmentOption`, `RiskLevel`, `LikelihoodRating`, `ImpactRating`,
  `ImplementationStatus`, `DocumentType`, `AuditType`, `AuditFindingType`,
  `CIAProperty`, `SecurityIncidentCategory`, `RelatedManagementSystem`.
- **326 slots**, **6 subsets** (`isms_core`, `annex_a_controls`,
  `risk_management`, `performance_evaluation`, `continual_improvement`,
  `documented_information`).
- **3 custom types** (`positive integer type`, `unsigned short type`,
  `duration type`).
- **28 declared prefixes** wiring the schema to LinkML, OSCAL, NIST 800-series,
  CIS, ATT&CK, D3FEND, SLSA, STIX, OCSF, SPDX, CAPEC, CWE, CVE, NVD, KEV
  catalog, ISO 29100, ISO 42001, and SSSOM/SKOS/semapv.
- `control_id` is ranged on `AnnexAControlId`, making every Annex A control a
  first-class addressable concept and a valid SSSOM subject.

## Cross-framework mappings (SSSOM)

18 SSSOM/TSV mapping sets are published under `src/iso27001/mappings/`. All
files are validated with `sssom-py` and follow the 10-column SSSOM convention
with embedded YAML metadata. Subjects use the PV-based CURIE pattern
`iso27001:AnnexAControlId#a_X_Y` for the 93 Annex A controls; class-level
anchor rows precede per-control rows. Mapping justification is
`semapv:LLMBasedMatching` pending expert review.

Every row is also overlaid back into the LinkML schema as `exact_mappings` /
`close_mappings` / `narrow_mappings` / `broad_mappings` / `related_mappings`
on the relevant class, slot, enum, or permissible value via
[`scripts/apply_sssom_overlay.py`](../scripts/apply_sssom_overlay.py).
The overlay is schema-independent and idempotent, and uses `ruamel.yaml`
round-trip mode to preserve comments and folded scalars in the source schema.

### Tier 1 — Highest VALUE.md alignment

| File | Target | Rows |
|---|---|---|
| `iso27001-to-oscal.sssom.tsv` | NIST OSCAL (control/SSP/SAR/POA&M) | 21 |
| `iso27001-to-nist-sp-800-53.sssom.tsv` | NIST SP 800-53 Rev 5 | 95 |
| `iso27001-to-nist-csf-v2.sssom.tsv` | NIST CSF v2 subcategories | 72 |
| `iso27001-to-attack.sssom.tsv` | MITRE ATT&CK (tactics + mitigations) | 40 |
| `iso27001-to-d3fend.sssom.tsv` | MITRE D3FEND countermeasures | 21 |
| `iso27001-to-cis-controls.sssom.tsv` | CIS Controls v8 safeguards | 67 |
| `iso27001-to-slsa.sssom.tsv` | SLSA (supply-chain build integrity) | 15 |
| `iso27001-to-nist-sp-800-218.sssom.tsv` | NIST SSDF practices | 18 |

### Tier 2

| File | Target | Rows |
|---|---|---|
| `iso27001-to-stix.sssom.tsv` | STIX 2.1 | 15 |
| `iso27001-to-ocsf.sssom.tsv` | OCSF event classes | 14 |
| `iso27001-to-nist-sp-800-171.sssom.tsv` | NIST SP 800-171 Rev 3 CUI | 29 |
| `iso27001-to-spdx.sssom.tsv` | SPDX 3.0 SBOM | 9 |
| `iso27001-to-capec.sssom.tsv` | MITRE CAPEC | 15 |
| `iso27001-to-cwe.sssom.tsv` | MITRE CWE | 12 |
| `iso27001-to-cve__nist-nvd.sssom.tsv` | CVE + NIST NVD (merged) | 9 |
| `iso27001-to-kev-catalog.sssom.tsv` | CISA KEV catalog | 6 |
| `iso27001-to-iso29100.sssom.tsv` | ISO/IEC 29100 privacy framework | 15 |

### Sibling alignment

| File | Target | Rows |
|---|---|---|
| `iso27001-to-iso42001.sssom.tsv` | ISO/IEC 42001:2023 AI management system | 102 |

**Total: 575 mapping rows across 18 mapping sets.**

## Testing & examples

- **83 unit tests passing** (`uv run pytest tests/`) — class/slot coverage,
  fixture round-trips, enum integrity, mapping format checks.
- **First-party fixtures** under `tests/data/valid/` and counter-examples under
  `tests/data/invalid/` are exercised end-to-end via `linkml-run-examples`.
- **Third-party validation corpus** under `tests/data/third_party/probo/`:
  61 `SecurityControl` fixtures generated from the
  [Probo](https://github.com/getprobo/probo) open-source ISMS mitigation catalog
  (MIT-licensed). The converter (`convert.py`) maps Probo's
  `ISO27001:2022-A.X.Y` references onto the `AnnexAControlId` permissible
  values (`a_X_Y`) so every fixture validates against the schema's enum.
- `just test` runs the full pipeline: pytest → valid examples →
  third-party Probo examples. All green.

## Tooling

- **`scripts/apply_sssom_overlay.py`** — schema-independent SSSOM → LinkML
  overlay. Auto-discovers subject-side prefixes from each schema's
  `default_prefix` / `name`; promotes the first `exact_mappings` entry to
  `meaning` on permissible values (per the LinkML PermissibleValue model);
  idempotent; preserves comments via `ruamel.yaml`.
- **`justfile`** recipes: `test`, `gen-project` (standard LinkML generators —
  Python datamodel, JSON Schema, ShEx, SHACL, OWL, GraphQL, Markdown, JSON-LD,
  Protobuf, SQLDDL, Java, TypeScript, Excel), `gen-project-extended`
  (everything in `gen-project` plus C++ headers, a Pandera/Polars
  dataframe schema, a Markdown data dictionary, and GOLR views — driven by
  patched generators under `scripts/`), `lint`, `examples`, `test_probo`.

## Generated artifacts

`project/` contains generated representations refreshed from the LinkML source.

- **Standard targets** (`just gen-project`): JSON Schema, ShEx, SHACL, OWL/TTL,
  GraphQL, Protobuf, JSON-LD context, SQLDDL, Java POJOs, TypeScript, Excel.
- **Extended targets** (`just gen-project-extended`): all standard targets plus
  `project/cpp/iso27001.h`, `project/pandera/iso27001_pandera.py`
  (Pandera-on-Polars dataframe schema), `project/markdown-datadict/iso27001.md`
  (human-readable data dictionary), and `project/golr/` (GOLR views).

The extended targets use small patched wrappers under `scripts/` to work
around upstream generator quirks (panderagen `DependencySorter` cycle
handling, `map_type` fallbacks for non-builtin XSD types, etc.). The schema's
custom types now declare `typeof` so the panderagen TYPE_MAP fallback chain
resolves cleanly.

## Status

| Area | State |
|---|---|
| Schema structure (Clauses 4–10 + Annex A) | Stable |
| Annex A enum (93 PVs) | Stable |
| SSSOM mappings (18 files, 575 rows) | Curated, machine-validated, awaiting expert review |
| Schema↔mappings round-trip | Idempotent, validated |
| First-party tests | 83 passing |
| Third-party (Probo) corpus | 61 fixtures, all validate |
| Generator targets | All standard + extended LinkML generators succeed (`just gen-project-extended`) |
| Outstanding cosmetic lint warnings | `canonical_prefixes` for `iso` and `semapv` (deferred) |

## Reference

- [ISO/IEC 27001:2022(E)](https://www.iso.org/standard/27001)
- [SSSOM specification](https://mapping-commons.github.io/sssom/)
- [LinkML PermissibleValue `meaning` slot](https://linkml.io/linkml-model/latest/docs/meaning/)
- [Probo mitigations corpus](https://github.com/getprobo/probo)
