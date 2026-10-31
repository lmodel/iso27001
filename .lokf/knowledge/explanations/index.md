# Explanations

* [Scope, influences and what is left out](scope-and-influences.md) - What the iso27001 schema models (the records an ISMS keeps under clauses 4 to 10 and Annex A of ISO/IEC 27001:2022), what shaped it (the standard, with names from ISO/IEC 27000, ISO/IEC 27005 and ISO 19011), what it maps to, and what it leaves out: the standard's text, certification itself and a fixed risk method.
* [How the schema names its elements and links records](names-and-references.md) - Why every class and enum carries the `Isms` prefix, how attributes and shared slots are named, how a record refers to another by `isms_id` through `IsmsRecordMixin`, why the record base is a mixin, and how the Statement of Applicability entries and security incidents are told apart by a type designator.
