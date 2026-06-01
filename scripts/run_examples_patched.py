#!/usr/bin/env python3
"""Wrapper around ``linkml-run-examples`` that applies the same
post-processing as ``scripts/patch_pythongen.py`` to the generated
python source *before* it is compiled in-process for example
validation.

``linkml-run-examples`` invokes ``PythonGenerator.compile_module()``
to load a fresh python module per example. That code path bypasses
our on-disk patched module entirely, so it trips over upstream
``pythongen`` defects (notably linkml/linkml#3572 - wrapper classes
emitted before the referenced enum bodies). This wrapper monkey-
patches ``compile_module`` so the in-process compile path goes
through the same fix-ups documented in ``ISSUE.md`` (Issues C, D, E
and #3572).
"""
from __future__ import annotations

import sys
from pathlib import Path

# Make sibling ``patch_pythongen`` importable without installing.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from patch_pythongen import (  # noqa: E402
    alias_enum_wrappers,
    inject_enum_hash_patch,
    reorder,
)

from linkml.generators.pythongen import PythonGenerator  # noqa: E402
from linkml_runtime.utils.compile_python import compile_python  # noqa: E402


def _patched_compile_module(self, **kwargs):
    pycode = self.serialize(**kwargs)
    pycode = inject_enum_hash_patch(alias_enum_wrappers(reorder(pycode)))
    try:
        return compile_python(pycode)
    except NameError as e:
        # Keep the upstream diagnostic but route through stderr so it
        # does not pollute the markdown summary on stdout.
        print(f"Error compiling generated python code: {e}", file=sys.stderr)
        raise


PythonGenerator.compile_module = _patched_compile_module

from linkml.workspaces.example_runner import cli  # noqa: E402

if __name__ == "__main__":
    sys.exit(cli())
