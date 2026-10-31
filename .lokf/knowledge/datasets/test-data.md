---
type: Dataset
id: https://w3id.org/lmodel/iso27001/knowledge/datasets/test-data
genre: reference
title: Test data and tests
description: "The schema's tests: 35 valid examples and 47 counter-examples under `tests/data/`, 61 controls derived from Probo's mitigations, and the tests that hold them to the validator, hold the header to ISO Open Data's records, check the upstream watch and the overlay, and keep the adapt copy apart from LOKF and nine released neighbours in `tests/neighbours/`."
resource: tests
about:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
sources:
  - id: data
    resource: tests/data
    title: the valid and invalid examples
  - id: probo
    resource: tests/data/third_party/probo
    title: convert.py and the examples
  - id: test_data.py
    resource: tests/test_data.py
    title: the data tests
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the header and Annex A tests
  - id: test_watch.py
    resource: tests/test_watch.py
    title: the stubbed watch tests
  - id: test_overlay.py
    resource: tests/test_overlay.py
    title: the overlay tests
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: NEIGHBOURS and the tests
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Test data and tests

`tests/data/valid/` holds 35 examples, one or more for each class that data can be written in, about a fictional company, Acme Widgets Ltd. `tests/data/invalid/` holds 47 counter-examples, each breaking one constraint. Each counter-example's first line names where the validator must fail, as `# Fails at: <pointer>`.[^data] A file's class is the part of its name before the first hyphen. `tests/data/third_party/probo/` holds Probo's mitigations, under the MIT License, and 61 `IsmsControl` examples that its `convert.py` derives from them, one for each mitigation that names an Annex A control.[^probo]

- `tests/test_data.py` loads each valid example into the dataclasses, holds it and each Probo example to the validator, holds each counter-example to its named failure, and checks that every class has an example.[^test_data.py]
- `tests/test_upstream.py` holds the extract to its pinned hashes, the schema header to the watch's pins and the extract's dates, and the Annex A enum to 93 values in four themes.[^test_upstream.py]
- `tests/test_watch.py` runs the upstream watch against stubbed answers.[^test_watch.py]
- `tests/test_overlay.py` checks the overlay scaffold and the merge script.[^test_overlay.py]
- `tests/test_schema_rules.py` checks the adapt copy against `lokf.yaml`, the schema of the Linked Open Knowledge Format (LOKF), and nine released neighbours, each pinned by its SHA-256 checksum. The neighbours are slsa v0.7.0, github-actions v0.3.0, oscal v0.1.2, spdx v0.1.0, nist-sp-800-218 v0.1.1, nist-sp-800-53 v0.1.0, nist-sp-800-171 v0.1.0, nist-csf-v2 v0.1.0 and in-toto v0.1.0.[^test_schema_rules.py] No class, enum, type or subset may share a name with them, and the copy shares no key with a neighbour.

`just test` generates the project into `tmp/`, runs the tests, and runs the examples and Probo's through `linkml-run-examples`.

[^data]: tests/data, valid/ and invalid/
[^probo]: tests/data/third_party/probo, convert.py and the examples
[^test_data.py]: tests/test_data.py, the tests
[^test_upstream.py]: tests/test_upstream.py, the tests
[^test_watch.py]: tests/test_watch.py, the tests
[^test_overlay.py]: tests/test_overlay.py, the tests
[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and the tests
