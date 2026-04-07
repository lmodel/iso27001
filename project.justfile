## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Validate Probo-sourced SecurityControl fixtures against the iso27001 schema
[group('model development')]
test_probo: _ensure_probo_output
    uv run linkml-run-examples \
        --input-formats yaml \
        --output-formats yaml \
        --input-directory tests/data/third_party/probo \
        --output-directory examples/output/third_party/probo \
        --schema {{source_schema_path}} > examples/output/third_party/probo/README.md

[private]
_ensure_probo_output:
    -mkdir -p examples/output/third_party/probo
    -rm -rf examples/output/third_party/probo/*.*
