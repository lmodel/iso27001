---
type: Reference
id: https://w3id.org/lmodel/iso27001/knowledge/references/iso-open-data
genre: reference
title: ISO Open Data
description: ISO's open data page and its `iso_deliverables_metadata` dataset of every ISO deliverable's metadata, updated daily under the ODC Attribution License (ODC-By) v1.0, which the repository pins its records of ISO/IEC 27001 from and the upstream watch streams each week.
resource: https://www.iso.org/open-data.html
sources:
  - id: open-data-page
    resource: https://www.iso.org/open-data.html
    title: the ISO Deliverables Metadata section, read through the Internet Archive's capture of 2026-10-17 on 2026-10-30
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: DATASET, LICENCE_PAGE and LICENCE_MIRROR
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# ISO Open Data

ISO's open data page publishes machine-readable datasets about ISO's work. One, `iso_deliverables_metadata`, holds metadata describing each deliverable that is published or being developed, and ISO updates it daily, in Parquet, JSON Lines and CSV.[^open-data-page] Its licence is the ODC Attribution License (ODC-By) v1.0, and the page gives the attribution text to cite it with.

iso.org refuses a script, so `scripts/check_upstream_release.py` reads the page through the Internet Archive's latest capture, and streams the dataset's JSON Lines file from ISO's blob storage.[^check_upstream_release.py] [ISO Open Data records of ISO/IEC 27001](../datasets/iso-open-data-records.md) describes the four records the repository pins.

[^open-data-page]: <https://www.iso.org/open-data.html>, the ISO Deliverables Metadata section
[^check_upstream_release.py]: scripts/check_upstream_release.py, DATASET and LICENCE_MIRROR
