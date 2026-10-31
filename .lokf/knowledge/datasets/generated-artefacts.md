---
type: Dataset
id: https://w3id.org/lmodel/iso27001/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What `just gen-project`, `just gen-project-extended` and `just gen-doc` write from the schema: the Python dataclasses and Pydantic models in `src/iso27001/datamodel/`, the JSON Schema, OWL, SHACL, ShEx, SQL and other files in `project/`, the merged schema in `docs/schema/` and the element pages in `docs/elements/`, none of them edited by hand."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/iso27001/knowledge/datasets/iso27001-linkml-schema
sources:
  - id: justfile
    resource: justfile
    title: the gen-project, gen-doc and test recipes
  - id: project.justfile
    resource: project.justfile
    title: the gen-project-extended recipes
  - id: generators.yaml
    resource: .linkml/generators.yaml
    title: the excludes and generator arguments
  - id: gen_dbml_patched.py
    resource: scripts/gen_dbml_patched.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-10-31T00:21:57Z"
status: draft
---

# Generated artefacts

`just gen-project` merges the SSSOM mappings into the schema, then runs LinkML's `gen-project` with the settings in `.linkml/generators.yaml`, moves the Python dataclasses into `src/iso27001/datamodel/`, and writes the Pydantic models, the Java classes, the TypeScript types and the OWL ontology.[^justfile] `.linkml/generators.yaml` leaves out the Markdown generator and passes `mergeimports` to the others.[^generators.yaml] `just gen-doc` writes the merged schema to `docs/schema/iso27001.yaml` and the element pages to `docs/elements/`, which git ignores.

`just gen-project-extended` adds the other generators LinkML ships, each into its own folder under `project/`: among them a merged schema, RDF, SPARQL checks, a CSV and a Markdown data dictionary, diagrams, SQLAlchemy and DBML, Go, Rust, C++ and Pandera.[^project.justfile] Each runs the stock generator except DBML. `scripts/gen_dbml_patched.py` skips a reference to a class without an identifier, which linkml 1.12.1's generator stops on; LinkML fixed that after the 1.12.1 release, and the script is to go once a release carries the fix.[^gen_dbml_patched.py]

Nothing under `project/`, `src/iso27001/datamodel/` or `docs/schema/` is edited by hand: each is regenerated from the schema.

[^justfile]: justfile, gen-project and gen-doc
[^generators.yaml]: .linkml/generators.yaml, excludes and generator_args
[^project.justfile]: project.justfile, the supplemental generator recipes
[^gen_dbml_patched.py]: scripts/gen_dbml_patched.py, the docstring
