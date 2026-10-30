#!/usr/bin/env python3
"""Run gen-dbml on this schema, skipping references to classes without an identifier.

gen-dbml in linkml 1.12.1 draws each reference between classes as a DBML
relationship to the referenced class's identifier, and raises ValueError when
the referenced class has none. This schema inlines three classes that have no
identifier of their own, because they live only inside the record that holds
them: IsmsApplicabilityEntry in the Statement of Applicability,
IsmsCommunication in the communication plan and IsmsMonitoringItem in the
monitoring programme. So the stock generator stops on the first of them.

This is linkml issue 3633 (https://github.com/linkml/linkml/issues/3633),
which pull request 3639 fixed on 2026-10-22, after the 1.12.1 release. The
wrapper below does what that fix does: it skips such a reference and keeps the
rest. Drop the wrapper, and call gen-dbml from project.justfile's
gen-dbml-artifact recipe, once the root lock holds a linkml release that
carries the fix.

Usage::

    uv run python scripts/gen_dbml_patched.py -s <schema> -o <output>
"""

from __future__ import annotations

import click
from linkml.generators.dbmlgen import DBMLGenerator
from linkml_runtime.utils.formatutils import camelcase, underscore


class PatchedDBMLGenerator(DBMLGenerator):
    """DBMLGenerator that skips a reference to a class without an identifier."""

    def _generate_relationships(self) -> str:
        view = self.schemaview
        classes = view.all_classes()
        relationships = []
        for class_name in classes:
            for slot in view.class_induced_slots(class_name):
                if slot.range not in classes:
                    continue
                identifier = next(
                    (
                        s.name
                        for s in view.class_induced_slots(slot.range)
                        if s.identifier
                    ),
                    None,
                )
                if identifier is None:
                    continue
                relationships.append(
                    f"Ref: {camelcase(class_name)}.{underscore(slot.name)} > "
                    f"{camelcase(slot.range)}.{underscore(identifier)}"
                )
        return "\n".join(relationships)


@click.command()
@click.option(
    "--schema",
    "-s",
    required=True,
    type=click.Path(exists=True, dir_okay=False, file_okay=True),
    help="Path to the LinkML schema YAML file",
)
@click.option(
    "--output",
    "-o",
    required=False,
    type=click.Path(dir_okay=False, writable=True),
    help="Output file (default: stdout)",
)
def cli(schema: str, output: str | None) -> None:
    """Write the schema as DBML."""
    dbml = PatchedDBMLGenerator(schema).serialize()
    if output:
        with open(output, "w", encoding="utf-8") as fh:
            fh.write(dbml)
    else:
        print(dbml)


if __name__ == "__main__":
    cli()
