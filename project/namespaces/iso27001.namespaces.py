# Auto generated from iso27001.yaml by namespacegen.py version: 0.0.1
# Generation date: 2026-06-01T19:41:20
# Schema: iso27001
#
# id: https://w3id.org/lmodel/iso27001
# description: A comprehensive LinkML schema modeling ISMS entities, workflows, and traceability links aligned to
#              ISO/IEC 27001:2022 clause and Annex references. Designed for open data publication, automated
#              validation, and integration with governance, risk, and compliance (GRC) systems. This schema
#              captures: - ISMS lifecycle (establish, implement, maintain, improve) - Risk assessment and
#              treatment processes (Clause 6.1) - Annex A control catalog structures organized by domain - Audit,
#              measurement, and continual improvement artifacts
# license: https://www.apache.org/licenses/LICENSE-2.0

from collections import defaultdict
from typing import Iterable, Dict, Tuple

from linkml_runtime.utils.curienamespace import CurieNamespace

GENE = 'gene'
DISEASE = 'disease'
CHEMICAL_SUBSTANCE = 'chemical substance'

SYMBOL = 'Approved_Symbol'


class IdentifierResolverException(RuntimeError):
    pass


class BiolinkNameSpace:
    """
    Map of BioLink Model registered URI Namespaces
    """

    _namespaces = [
        CurieNamespace('attack', 'https://w3id.org/lmodel/attack/'),
        CurieNamespace('capec', 'https://w3id.org/lmodel/capec/'),
        CurieNamespace('cis_controls', 'https://w3id.org/lmodel/cis-controls/'),
        CurieNamespace('cve', 'https://w3id.org/lmodel/cve/'),
        CurieNamespace('cwe', 'https://w3id.org/lmodel/cwe/'),
        CurieNamespace('d3f', 'https://d3fend.mitre.org/ontologies/d3fend.owl#'),
        CurieNamespace('dcterms', 'http://purl.org/dc/terms/'),
        CurieNamespace('iso', 'https://www.iso.org/standard/'),
        CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/'),
        CurieNamespace('iso27002', 'https://w3id.org/lmodel/iso27002/'),
        CurieNamespace('iso29100', 'https://w3id.org/lmodel/iso29100/'),
        CurieNamespace('iso42001', 'https://w3id.org/lmodel/iso42001/'),
        CurieNamespace('kev_catalog', 'https://w3id.org/lmodel/kev-catalog/'),
        CurieNamespace('linkml', 'https://w3id.org/linkml/'),
        CurieNamespace('nist_csf_v2', 'https://w3id.org/lmodel/nist-csf-v2/'),
        CurieNamespace('nist_sp_800_171', 'https://w3id.org/lmodel/nist-sp-800-171/'),
        CurieNamespace('nist_sp_800_218', 'https://w3id.org/lmodel/nist-sp-800-218/'),
        CurieNamespace('nist_sp_800_53', 'https://w3id.org/lmodel/nist-sp-800-53/'),
        CurieNamespace('nvd', 'https://w3id.org/lmodel/nist-nvd/'),
        CurieNamespace('ocsf', 'https://w3id.org/lmodel/ocsf/'),
        CurieNamespace('oscal', 'https://w3id.org/lmodel/oscal/'),
        CurieNamespace('prov', 'http://www.w3.org/ns/prov#'),
        CurieNamespace('schema', 'http://schema.org/'),
        CurieNamespace('semapv', 'https://w3id.org/semapv/vocab/'),
        CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#'),
        CurieNamespace('slsa', 'https://w3id.org/lmodel/slsa/'),
        CurieNamespace('spdx', 'https://w3id.org/lmodel/spdx/'),
        CurieNamespace('stix', 'https://w3id.org/lmodel/stix/'),
        CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#'),
    ]

    # class level dictionaries

    _prefix_map: Dict[str, CurieNamespace] = {}

    @classmethod
    def _get_prefix_map(cls):
        if not cls._prefix_map:
            for ns in cls._namespaces:
                # index by upper case for uniformity of search
                cls._prefix_map[ns.prefix.upper()] = ns
        return cls._prefix_map

    @classmethod
    def parse_curie(cls, curie: str) -> Tuple[CurieNamespace, str]:
        """
        Parse a candidate CURIE
        :param curie: candidate curie string
        :return: CURIE namespace and object_id
        """
        found = CurieNamespace("", ""), curie  # default value if not a CURIE or unknown XMLNS prefix
        if ':' in curie:
            part = curie.split(":")
            # Normalize retrieval with upper case of prefix for lookup
            prefix = part[0].upper()
            if prefix in cls._get_prefix_map():
                found = cls._prefix_map[prefix], part[1]
        return found

    @classmethod
    def parse_uri(cls, uri: str) -> Tuple[CurieNamespace,  str]:
        """
        Parse a candidate URI
        :param uri: candidate URI string
        :return: namespace and object_id
        """
        found = CurieNamespace("", ""), uri   # default value returned if unknown URI namespace

        # TODO: is there a more efficient lookup scheme here than a linear search of namespaces?
        for ns in cls._namespaces:
            base_uri = str(ns)
            if uri.startswith(base_uri):
                # simple minded deletion of base_uri to give the object_id
                object_id = uri.replace(base_uri, "")
                found = ns, object_id
                break
        return found

    @classmethod
    def parse_identifier(cls,  identifier: str) -> Tuple[CurieNamespace,  str]:

        # trivial case of a null identifier?
        if not identifier:
            return CurieNamespace("", ""), ""

        # check if this is a candidate URI...
        if identifier.lower().startswith("http"):
            # guess that perhaps it is, so try to parse it
            return cls.parse_uri(identifier)

        else:  # attempt to parse as a CURIE
            return cls.parse_curie(identifier)


def object_id(identifier, keep_version=False) -> str:
    """
    Returns the core object_id of a CURIE, with or without the version suffix.
    Note:  not designed to be used with a URI (will give an invalid outcome)
    :param identifier: candidate CURIE identifier for processing
    :param keep_version: True if the version string suffix is to be retained in the identifier
    :return:
    """
    # trivial case: null input value?
    if not identifier:
        return identifier

    if ':' in identifier:
        identifier = identifier.split(":")[1]

    if not keep_version and '.' in identifier:
        identifier = identifier.split(".")[0]

    return identifier


def fix_curies(identifiers, prefix=''):
    """
    Applies the specified XMLNS prefix to (an) identifier(s) known
    to be "raw" IDs as keys in a dictionary or elements in a list (or a simple string)
    :param identifiers:
    :param prefix:
    :return:
    """
    if not prefix:
        # return identifiers without modification
        # Caller may already consider them in curie format
        return identifiers

    if isinstance(identifiers, dict):
        curie_dict = defaultdict(dict)
        for key in identifiers.keys():
            curie_dict[prefix + ':' + object_id(key, keep_version=True)] = identifiers[key]
        return curie_dict

    # identifiers assumed to be just a single object identifier
    elif isinstance(identifiers, str):
        # single string to convert
        return prefix + ':' + object_id(identifiers, keep_version=True)

    elif isinstance(identifiers, Iterable):
        return [prefix + ':' + object_id(x, keep_version=True) for x in identifiers]

    else:
        raise RuntimeError("fix_curie() is not sure how to fix an instance of data type '", type(identifiers))


def curie(identifier) -> str:
    # Ignore enpty strings
    if not identifier:
        return ""
    else:
        namespace: CurieNamespace
        identifier_object_id: str
        namespace, identifier_object_id = BiolinkNameSpace.parse_identifier(identifier)
        return namespace.curie(identifier_object_id)

