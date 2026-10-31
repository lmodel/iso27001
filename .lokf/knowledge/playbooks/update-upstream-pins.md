---
type: Playbook
id: https://w3id.org/lmodel/iso27001/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Update the upstream pins
description: "What to do when the Upstream watch reports that ISO published a new amendment, corrigendum or edition of ISO/IEC 27001, changed a pinned record's stage, named a successor, or changed the dataset's licence: replace the ISO Open Data extract and move the pins in `scripts/check_upstream_release.py` and the schema header together."
resource: scripts/check_upstream_release.py
about:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso-open-data-records
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring and the pins
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the bullet on the ISO Open Data copy
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: test_header_pins_match_the_watch
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Update the upstream pins

[Upstream watch](../workflows/upstream-watch.md) opens an issue when ISO's records move. Then:

1. Read what changed. A new supplement of ISO/IEC 27001:2022, or a record that replaces it, may change what the schema models. A stage change may mean ISO confirmed, revised or withdrew a standard. A changed licence may change what the extract may hold.[^check_upstream_release.py]
2. Replace `src/iso27001/schema/iso-open-data/iso_deliverables_metadata.jsonl` whole from one day's dataset, each record without its `scope`, and never edit a line by hand.[^contributing.md]
3. Move the pins in `scripts/check_upstream_release.py` together: `PINNED_DATE`, `PINNED_RECORDS`, and `PINNED_VERSION` or `PINNED_SOURCE` when the edition or its amendments change.
4. Move the schema header's `version`, `source` and annotations to match, then run the schema's checks as [Regenerate and test after a schema change](regenerate-and-test.md) says.

`tests/test_upstream.py` fails until the header, the pins and the extract agree.[^test_upstream.py]

[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring and the pins
[^contributing.md]: CONTRIBUTING.md, the bullet on src/iso27001/schema/iso-open-data/
[^test_upstream.py]: tests/test_upstream.py, test_header_pins_match_the_watch
