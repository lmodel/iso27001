# iso27001

This project is a LinkML model of the records an organization keeps to run an
information security management system (ISMS) to ISO/IEC 27001:2022 with
Amendment 1:2024. It covers the ISMS's context and scope, its policies, roles
and objectives, its risks and their treatment, its controls and Statement of
Applicability, the support and operation it needs, its audits and management
reviews, and its nonconformities, corrective actions and improvements. It
holds no text of the standard.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the elements are named and what the model leaves out
- [Use cases](value.md): what the model is for
- [Rights](rights.md): what may be reproduced, and what may not
- [`iso27001.yaml`](schema/iso27001.yaml): the schema

## Validating data

`linkml-validate -s src/iso27001/schema/iso27001.yaml -C IsmsRisk risk.yaml`
checks a file against the JSON Schema generated from the schema, and
`tests/test_data.py` holds every example to it. Write dates as quoted
strings, as JSON carries them: the validator reads a date as text.

Validate a file before loading it into either model in
`src/iso27001/datamodel/`. LinkML 1.12.1 generates models that check less:

- The dataclasses check required fields and enum values, but no pattern and
  no minimum.
- The Pydantic models also check a pattern or a minimum that a field carries
  itself, such as a blank title or justification, or an employee count of
  zero. They do not check the patterns of the two types, so a retention
  period that is not an ISO 8601 duration, or a requirement that is not a
  clause or Annex A number, goes unchecked.
- Neither checks that an included control names an Annex A control or one
  of the organization's controls.

No check covers these rules:

- that a reference names a record the ISMS holds, of the class the
  reference ranges over;
- that a list never repeats an identifier;
- that an audit ends after it begins, or that a control's theme is the theme
  of the Annex A controls it answers to;
- that the Statement of Applicability has one entry for each Annex A control.
