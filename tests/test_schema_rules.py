"""Checks that the adapt copy can sit beside LOKF and the neighbours' copies."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent

# What a host may import beside this schema's adapt copy: LOKF's schema, pinned
# by the sidecar, and the adapt copies other lmodel repositories release. Each
# neighbour is the schema asset of a release, downloaded and checked against
# the release's .sha256 and its build-provenance attestation, and pinned here
# by that checksum.
COPY = ROOT / ".lokf" / "iso27001.yaml"
LOKF = ROOT / ".lokf" / "lokf.yaml"
NEIGHBOURS = {
    # lmodel/slsa v0.7.0, schema-v0.7.0-slsa.yaml
    "slsa.yaml": "b25407db9480751e521edf36a1ef75ab0ef2d6652d7e153e66afdbfc37aa19ce",
    # lmodel/github-actions v0.3.0, schema-v0.3.0-github-actions.yaml
    "github-actions.yaml": "52224e53939325f56d3470ed6ddd2041cdd53ae7cdb0ac72773829100798452e",
    # lmodel/oscal v0.1.2, schema-v0.1.2-oscal.yaml
    "oscal.yaml": "4eb56d7d1106463ed0a2255a29af14b8d619741acc29863d1e86eb3f8923c710",
    # lmodel/spdx v0.1.0, schema-v0.1.0-spdx.yaml
    "spdx.yaml": "3411cf5d19b1955f0362988c542984e4c817417c7b7b7892647aba1adf1ddd4a",
    # lmodel/nist-sp-800-218 v0.1.1, schema-v0.1.1-nist-sp-800-218.yaml
    "nist-sp-800-218.yaml": "479824cdd95e52226a35ff3a471b7ce93239635ccd5db7ac72a8143cdd1d8495",
    # lmodel/nist-sp-800-53 v0.1.0, schema-v0.1.0-nist-sp-800-53.yaml
    "nist-sp-800-53.yaml": "d32a989b5b855281cb45d707bf59cf52b125f05a09c54930e2b4d45c174c0d99",
    # lmodel/nist-sp-800-171 v0.1.0, schema-v0.1.0-nist-sp-800-171.yaml
    "nist-sp-800-171.yaml": "d204efa6653692da665f8604a8fb8bf445f04b37f41460a5ce2853a014b2982f",
    # lmodel/nist-csf-v2 v0.1.0, schema-v0.1.0-nist-csf-v2.yaml
    "nist-csf-v2.yaml": "5f6bba4c4721f65665c3a0a702ca6b15df5b488048fed454acfe4cc69f7ca9c7",
    # lmodel/in-toto v0.1.0, schema-v0.1.0-in-toto.yaml
    "in-toto.yaml": "ab56ad846e8115b7908bc51dae80e2d6031fa8633068c65cf0f315d76a2a7aca",
}
NEIGHBOUR_DIR = ROOT / "tests" / "neighbours"
ELEMENT_KINDS = ("classes", "enums", "types", "subsets")

# Keys the copy shares with a neighbour. LinkML keeps one namespace, and the
# JSON-LD context gives each key one IRI across a composite, whether it is a
# slot or an attribute on either side, so a shared key projects under one
# vocabulary's IRI. The copy shares none, so a new overlap fails the test.
SHARED_WITH_NEIGHBOURS = {name: set() for name in NEIGHBOURS}

# The classes `just lokf-adapt` re-roots on Concept, which the README lists
# for the plugins' Known LOKF types setting.
ROOTS = {
    "IsmsPolicy",
    "IsmsTopicSpecificPolicy",
    "IsmsRole",
    "IsmsControl",
    "IsmsAsset",
    "IsmsDocumentedInformation",
    "IsmsOperationalProcedure",
}

MAPPING_KEYS = (
    "mappings",
    "exact_mappings",
    "close_mappings",
    "related_mappings",
    "narrow_mappings",
    "broad_mappings",
)

# Prefixes the neighbours bind for vocabularies of their own that are no
# neighbour's: a mapping into one of these is not a mapping into a neighbour.
SHARED_VOCABULARIES = {
    "http://www.w3.org/2001/XMLSchema#",
    "http://schema.org/",
    "https://w3id.org/linkml/",
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
}


def _load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _expander(doc):
    prefixes = doc.get("prefixes") or {}

    def expand(curie):
        prefix, _, local = curie.partition(":")
        return prefixes[prefix] + local if prefix in prefixes else curie

    return expand


def _names(path):
    """Each kind of element a schema file declares, and every slot and
    attribute name with the IRI it expands to."""
    doc = _load(path)
    expand = _expander(doc)
    default = doc.get("default_prefix")
    elements = {kind: set(doc.get(kind) or {}) for kind in ELEMENT_KINDS}
    slots = {}
    owners = [doc.get("slots") or {}]
    owners += [
        (cls or {}).get("attributes") or {}
        for cls in (doc.get("classes") or {}).values()
    ]
    for owner in owners:
        for name, slot in owner.items():
            uri = (slot or {}).get("slot_uri") or f"{default}:{name}"
            slots.setdefault(name, set()).add(expand(uri))
    return elements, slots


def _terms(path):
    """The IRI of every class, enum, type and slot a schema file declares."""
    doc = _load(path)
    expand = _expander(doc)
    default = doc.get("default_prefix")
    uri_keys = {
        "classes": "class_uri",
        "enums": "enum_uri",
        "types": "uri",
        "slots": "slot_uri",
    }
    terms = set()
    for kind, key in uri_keys.items():
        for name, element in (doc.get(kind) or {}).items():
            terms.add(expand((element or {}).get(key) or f"{default}:{name}"))
    return terms


def _namespaces(path):
    """The namespaces a neighbour names its own terms in."""
    prefixes = (_load(path).get("prefixes") or {}).values()
    return {iri for iri in prefixes if iri not in SHARED_VOCABULARIES}


def _mappings(node):
    """Every mapping value anywhere in a parsed schema file."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in MAPPING_KEYS:
                yield from value if isinstance(value, list) else [value]
            else:
                yield from _mappings(value)
    elif isinstance(node, list):
        for item in node:
            yield from _mappings(item)


def test_neighbours_are_the_released_assets():
    """Each neighbour copy is byte for byte the asset its release published."""
    assert {p.name for p in NEIGHBOUR_DIR.iterdir()} == set(NEIGHBOURS)
    for name, sha256 in NEIGHBOURS.items():
        digest = hashlib.sha256((NEIGHBOUR_DIR / name).read_bytes()).hexdigest()
        assert digest == sha256, name


def test_names_apart_from_lokf():
    """No class, enum, type or subset name of the copy is LOKF's, and a slot
    name the two share carries LOKF's IRI."""
    elements, slots = _names(COPY)
    their_elements, their_slots = _names(LOKF)
    for kind in ELEMENT_KINDS:
        assert not elements[kind] & their_elements[kind], kind
    for name in slots.keys() & their_slots.keys():
        assert slots[name] == their_slots[name], name


def test_names_apart_from_neighbours():
    """A class, enum, type or subset name is the copy's alone, and the only
    keys it shares with a neighbour are the listed ones."""
    elements, slots = _names(COPY)
    for name in NEIGHBOURS:
        their_elements, their_slots = _names(NEIGHBOUR_DIR / name)
        for kind in ELEMENT_KINDS:
            assert not elements[kind] & their_elements[kind], (name, kind)
        assert slots.keys() & their_slots.keys() == SHARED_WITH_NEIGHBOURS[name], name


def test_copy_roots_the_concept_classes():
    """The copy re-roots exactly the seven concept classes on Concept and
    imports nothing but the LinkML types and LOKF."""
    doc = _load(COPY)
    rooted = {
        name for name, cls in doc["classes"].items() if cls.get("is_a") == "Concept"
    }
    assert rooted == ROOTS
    assert doc["imports"] == ["linkml:types", "lokf"]


def test_mappings_use_a_bound_prefix():
    """Every mapping in the copy is a CURIE whose prefix the copy binds. A full
    address that no prefix covers makes every `lokf convert --schema` over the
    copy warn that it has no namespace."""
    doc = _load(COPY)
    prefixes = doc.get("prefixes") or {}
    mappings = list(_mappings(doc))
    assert mappings
    for mapping in mappings:
        prefix, sep, _ = mapping.partition(":")
        assert sep and prefix in prefixes, mapping


def test_mappings_name_a_released_term():
    """Every mapping names a term of a released neighbour copy: an address in
    a neighbour's namespace that one of its classes, enums, types or slots
    has. A mapping into a schema with no release, or to a term the release
    does not have, fails."""
    doc = _load(COPY)
    expand = _expander(doc)
    namespaces = {}
    for name in NEIGHBOURS:
        for namespace in _namespaces(NEIGHBOUR_DIR / name):
            namespaces.setdefault(namespace, set()).add(name)
    for mapping in _mappings(doc):
        iri = expand(mapping)
        owners = {
            owner
            for namespace, names in namespaces.items()
            if iri.startswith(namespace)
            for owner in names
        }
        assert owners, f"{mapping} is in no released neighbour's namespace"
        assert any(iri in _terms(NEIGHBOUR_DIR / owner) for owner in owners), mapping


def test_sssom_rows_are_the_schema_mappings():
    """The SSSOM files and the schema's mappings say the same: every row is a
    mapping of the schema, and every mapping of the schema is a row."""
    source = _load(ROOT / "src" / "iso27001" / "schema" / "iso27001.yaml")
    predicates = {
        "skos:exactMatch": "exact_mappings",
        "skos:closeMatch": "close_mappings",
        "skos:broadMatch": "broad_mappings",
        "skos:narrowMatch": "narrow_mappings",
        "skos:relatedMatch": "related_mappings",
    }
    rows = set()
    for path in (ROOT / "src" / "iso27001" / "mappings").glob("*.sssom.tsv"):
        lines = [
            line
            for line in path.read_text(encoding="utf-8").splitlines()
            if line and not line.startswith("#")
        ]
        header = lines[0].split("\t")
        for line in lines[1:]:
            row = dict(zip(header, line.split("\t")))
            subject = row["subject_id"].removeprefix("iso27001:")
            rows.add((subject, predicates[row["predicate_id"]], row["object_id"]))
    in_schema = set()
    for kind in ("classes", "slots", "enums", "types"):
        for name, element in (source.get(kind) or {}).items():
            for key in MAPPING_KEYS:
                for target in (element or {}).get(key) or []:
                    in_schema.add((name, key, target))
    assert rows == in_schema
