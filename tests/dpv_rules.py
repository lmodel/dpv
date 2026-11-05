"""The rules on DPV's data that the generated JSON Schema cannot state.

JSON Schema looks at one value at a time, and DPV's domainIncludes and rangeIncludes say what
a property usually joins, not what it must. So JSON Schema cannot say that a value names a
term that exists, that an rdf_type names a kind, or that no two records share an IRI. A
consumer that wants every rule runs these too. They say nothing about a value outside DPV's
namespaces, which DPV's own files name freely.
"""

from functools import cache

from tests import conversion

C = conversion.CONVERTER

# What DPV's files name under a DPV namespace and define nowhere. issues/87 reports these to
# the Community Group, and a later edition that fixes one fails test_dangling_is_as_listed.
DANGLING = frozenset(
    {
        "dpv:AggregatedData",
        "dpv:Incident",
        "dpv:InsuranceManagement",
        "dpv:System",
        "ieee-7012:Party",
        "de-gdng:DataHolder",
        "ieee-7012:Analytics2PAllowed",
        "ieee-7012:Analytics3PDisallowed",
        "ieee-7012:AnalyticsDisallowed",
        "ieee-7012:DataSharingAnonymised3PAllowed",
        "ieee-7012:DataSharingDisallowed",
        "ieee-7012:ServiceDeliveryRequired",
        # DPV writes this IRI with a line break before its closing bracket.
        "ieee-7012:Tracking2PAllowed\n",
        "pd:Molecular",
        "pd:PersonalData",
        "sector-health:EHR",
        "tech:AI",
        "tech:TechnologyActor",
    }
)
# A term record's slots that name a term.
TERM_REFERENCES = (
    "rdf_type",
    "broader",
    "related",
    "sameAs",
    "subClassOf",
    "subPropertyOf",
    "domainIncludes",
    "rangeIncludes",
)


@cache
def dpv_prefixes():
    """The prefixes of the namespaces DPV itself mints."""
    return frozenset(
        name
        for name, namespace in C.prefixes().items()
        if namespace.startswith("https://w3id.org/dpv")
    )


def is_dpv(value):
    return value.split(":", 1)[0] in dpv_prefixes()


@cache
def kind_curies():
    """Each kind's IRI as a CURIE, from the classes the schema holds."""
    return frozenset(
        cls["class_uri"]
        for name, cls in conversion.all_classes().items()
        if name.startswith("Dpv") and "class_uri" in cls
    )


@cache
def _reference_slots():
    """Each DPV property slot whose value names a resource."""
    return frozenset(
        name
        for name, slot in conversion.all_slots().items()
        if slot.get("range") == "DpvTerm" and name not in TERM_REFERENCES
    )


def _known(found, where, value, known, message="names no term"):
    if is_dpv(value) and value not in known and value not in DANGLING:
        found.append((where, f"{value} {message}"))


def _term_errors(record, where, known, schemes, vocabularies, examples, agents):
    found = []
    for key in (*TERM_REFERENCES, *sorted(_reference_slots())):
        for position, value in enumerate(record.get(key) or []):
            _known(found, f"{where}/{key}/{position}", value, known)
    for position, value in enumerate(record.get("rdf_type") or []):
        if value not in kind_curies():
            found.append((f"{where}/rdf_type/{position}", f"{value} names no kind"))
    for position, value in enumerate(record.get("inScheme") or []):
        if value not in schemes:
            found.append((f"{where}/inScheme/{position}", f"{value} names no scheme"))
    for position, value in enumerate(record.get("isDefinedBy") or []):
        if C.expand(value) not in vocabularies:
            found.append(
                (f"{where}/isDefinedBy/{position}", f"{value} names no vocabulary")
            )
    for position, value in enumerate(record.get("example") or []):
        if value not in examples:
            found.append((f"{where}/example/{position}", f"{value} names no example"))
    for position, value in enumerate(record.get("contributor") or []):
        if value not in agents:
            found.append((f"{where}/contributor/{position}", f"{value} names no agent"))
    return found


def _resource_errors(resource, where, known, local):
    found = []
    keys = (*TERM_REFERENCES, *sorted(_reference_slots()))
    for key in keys:
        for position, value in enumerate(resource.get(key) or []):
            if value not in local:
                _known(found, f"{where}/{key}/{position}", value, known)
    for index, statement in enumerate(resource.get("statements") or []):
        here = f"{where}/statements/{index}"
        has_reference = "reference" in statement
        if has_reference == ("literal" in statement):
            found.append((here, "a statement holds one of reference and literal"))
        if has_reference and {"datatype", "language"} & statement.keys():
            found.append((here, "a reference takes no datatype or language"))
        if has_reference and statement["reference"] not in local:
            _known(found, f"{here}/reference", statement["reference"], known)
    return found


def rule_errors(document: dict, *, whole_edition: bool = True) -> list[tuple[str, str]]:
    """Each break of a rule in one data file, as (JSON pointer, message). What it names may
    sit in another family's file, so a value resolves against the whole edition's records as
    well as the document's own, unless the caller asks otherwise."""
    found = []
    own = {}
    for key in ("concepts", "properties"):
        for index, record in enumerate(document.get(key) or []):
            identifier = record.get("id")
            if identifier in own:
                found.append((f"/{key}/{index}/id", f"{identifier} is a second record"))
            own[identifier] = record
    known = set(own)
    schemes = {s["id"] for s in document.get("concept_schemes") or []}
    vocabularies = {
        C.expand(v["preferredNamespaceUri"])
        for v in document.get("vocabularies") or []
        if "preferredNamespaceUri" in v
    }
    examples = {e["id"] for e in document.get("examples") or []}
    agents = {a["id"] for a in document.get("agents") or []}
    if whole_edition:
        known |= set(conversion.terms())
        schemes |= set(conversion.records("concept_schemes"))
        vocabularies |= {
            C.expand(v["preferredNamespaceUri"])
            for v in conversion.records("vocabularies").values()
            if "preferredNamespaceUri" in v
        }
        examples |= set(conversion.records("examples"))
        agents |= set(conversion.records("agents"))
    for key in ("concepts", "properties"):
        for index, record in enumerate(document.get(key) or []):
            found += _term_errors(
                record,
                f"/{key}/{index}",
                known,
                schemes,
                vocabularies,
                examples,
                agents,
            )
    for index, example in enumerate(document.get("examples") or []):
        where = f"/examples/{index}"
        resources = example.get("resources") or []
        if example.get("turtle_fault") and resources:
            found.append(
                (where, "an example whose file does not parse holds no resources")
            )
        local = {r["id"] for r in resources}
        for position, resource in enumerate(resources):
            found += _resource_errors(
                resource, f"{where}/resources/{position}", known, local
            )
    for index, agent in enumerate(document.get("agents") or []):
        for position, member in enumerate(agent.get("memberOf") or []):
            if member not in agents:
                where = f"/agents/{index}/memberOf/{position}"
                found.append((where, f"{member} names no agent"))
    return found
