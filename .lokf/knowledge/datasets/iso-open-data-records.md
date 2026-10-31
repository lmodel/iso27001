---
type: Dataset
id: https://w3id.org/lmodel/iso27001/knowledge/datasets/iso-open-data-records
genre: reference
title: ISO Open Data records of ISO/IEC 27001
description: "The pinned extract `src/iso27001/schema/iso-open-data/iso_deliverables_metadata.jsonl`: ISO Open Data's records of ISO/IEC 27001:2022, its Amendment 1:2024, ISO/IEC 27002:2022 and ISO/IEC 27000:2026 as of 2026-10-28, each without its scope, under the ODC Attribution License, which the upstream watch checks weekly."
resource: src/iso27001/schema/iso-open-data
derivedFrom:
  - https://w3id.org/lmodel/iso27001/knowledge/references/iso-open-data
license: https://opendatacommons.org/licenses/by/1-0/
sources:
  - id: iso-open-data
    resource: src/iso27001/schema/iso-open-data
    title: the four records
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring and the pins
  - id: notice
    resource: NOTICE
    title: the ISO Open Data section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# ISO Open Data records of ISO/IEC 27001

`src/iso27001/schema/iso-open-data/iso_deliverables_metadata.jsonl` holds four lines of ISO Open Data's `iso_deliverables_metadata` dataset, one record each:[^iso-open-data]

| Record | Reference | Stage | Published | Edition |
| --- | --- | --- | --- | --- |
| 82875 | ISO/IEC 27001:2022 | 6060 | 2022-10-25 | 3 |
| 88435 | ISO/IEC 27001:2022/Amd 1:2024 | 6060 | 2024-02-23 | 3 |
| 75652 | ISO/IEC 27002:2022 | 6060 | 2022-02-15 | 3 |
| 84257 | ISO/IEC 27000:2026 | 6060 | 2026-07-03 | 6 |

ISO/IEC 27002:2022 names project 94703 as what replaces it, a record the dataset does not yet hold. ISO's title for ISO/IEC 27000:2026 names it an overview.

Each line is ISO's record as published on 2026-10-28, without its `scope` field, which summarizes the standard in ISO's words. `scripts/check_upstream_release.py` pins each line by its SHA-256 hash.[^check_upstream_release.py] Every week it streams the live dataset, about 80 MB, line by line, and reports any of these:

- a new supplement of the edition;
- a changed record;
- a record that replaces a pinned one;
- the 27002 successor appearing;
- a dropped record;
- a changed licence.

 `NOTICE` gives ISO's attribution under the ODC Attribution License (ODC-By) v1.0.[^notice]

[^iso-open-data]: src/iso27001/schema/iso-open-data, the four records
[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring and PINNED_RECORDS
[^notice]: NOTICE, the ISO Open Data section
