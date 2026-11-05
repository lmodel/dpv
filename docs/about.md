# About dpv

This page says how the schema reads DPV, where each part comes from, and what the model leaves out. It is for someone who will use the data or change the converter.

## Terms are records

DPV states each concept three ways at once: `dpv:Marketing a rdfs:Class, skos:Concept, dpv:Purpose`. A LinkML class cannot also be a value, so a schema with one class per term could not say that a process's `hasPurpose` is `dpv:Marketing`.

So the schema gives a class to each concept that terms are instances of, a *kind*, such as `DpvPurpose` for `dpv:Purpose`. Every term of the vocabularies is then a record. `DpvConcept` holds a concept's record, `DpvProperty` a property's, and `DpvResource` a thing a use case describes, such as a process.

| What DPV states | What the schema holds |
| --- | --- |
| A type a concept holds beyond `rdfs:Class` and `skos:Concept` | A class under its own IRI, 149 of them, each under the nearest kind above it along `skos:broader` |
| A property | A slot under its own IRI, with DPV's local name as its key, 307 of them |
| A term | A record in `src/dpv/data/`, its `rdf_type` naming each kind it is an instance of |

Where two namespaces define one property name, the core keeps the name and the other takes its namespace first: `hasRiskLevel` and `eu_aiact_hasRiskLevel`. A kind's class takes the namespace the same way.

A kind's record and its class are the same thing seen two ways. `dpv:Purpose` is a record, and `DpvPurpose` is the class a host names as a concept's `type`. So `project/owl/` describes this schema, and `upstream/*.ttl` is DPV's ontology.

## The parts of a release

`src/dpv/data/` holds one file per namespace family: the core, personal data, technology, artificial intelligence, risk, justifications, locations, laws and authorities, sectors and standards. A further file holds the contributors, and another the examples.

`scripts/dpv_to_linkml.py` writes each file from `upstream/`, along with `dpv_terms.yaml` and the kinds' modules. It stops on a predicate no table names, so a new edition cannot lose a fact unnoticed. `tests/test_coverage.py` walks the Turtle both ways, and `tests/test_catalogue.py` compares the catalogue's JSON-LD projection with it triple by triple.

## What the examples add

DPV's 88 example files are its one published account of how the terms join up in data. `dex:E0026`, for one, describes a process with a purpose and two nested processes. Each file's statements are records in `dpv-2.3-examples.yaml`. The file declares no prefixes, so the converter supplies them: `ex:` as DPV's page says, and `exA:`, `exB:` and a bare colon, which DPV leaves unstated, under `http://example.com`.

A value in a record must look like a reference, and `tests/dpv_rules.py` holds it to a term that exists. An unknown key fails the validator, and that is the gain over a schema of classes with no slots.

## What stays open

DPV uses `dcam:domainIncludes` and `dcam:rangeIncludes`, not `rdfs:domain` and `rdfs:range`. They say what a property usually joins, not what it must. So `DpvResource` holds any property, and the validator refuses no value for leaving those classes. `tests/test_examples.py` reads them anyway, and `tests/example_departures.yaml` lists each place DPV's own examples leave them: 58 values, 65 subjects and 30 literals where a range names a class.

A statement the slots cannot hold, such as a literal under `hasLocation` or a predicate with no slot, goes in the resource's `statements`.

## What the records leave out

- `skos:narrower`, which only the locations state, 68,032 times. 4,959 are the inverse of `skos:broader`. The other 63,073 list what each `loc:non-X` holds: every country but X, and but X's member countries when X is a union. `tests/test_coverage.py` regenerates every pair.
- `schema:domainIncludes` and `schema:rangeIncludes`, which repeat the `dcam:` pair on every property.
- The statements of how DPV's site publishes a file: `prof:hasResource` and the 337 resource descriptors.
- `dpv-27560`, DPV's schema for consent records. Its Turtle file names four classes and states nothing about them, so there is nothing to render.

## What the data shows

These are in DPV's own files. `tests/test_catalogue.py` and `tests/dpv_rules.py` pin them, so a later edition that fixes one fails a test.

- 18 names under DPV's namespaces are used and defined nowhere, such as `dpv:System` and `tech:AI`. One is an IRI with a line break in it.
- 60 statements use `skos:sameAs`, and each vocabulary header `rdfs:Label`. Neither is a term of its vocabulary.
- Three example files do not parse: `E0030`, `E0059` and `E0061`.
- `dcat:Resource` states two creation dates, and five terms name two vocabularies under `rdfs:isDefinedBy`.
- 153 terms have no definition, nearly all laws and authorities.

## Mappings

`src/dpv/mappings/` renders the two mapping files DPV publishes in machine-readable form, for ISO/IEC 29100:2024 terms and for ODRL. A row reads with DPV's term as its subject, as DPV's own statements do, and `skos:broadMatch` stands for DPV's `skos:broader`. `tests/test_mappings.py` holds each row to both the CSV and the Turtle.

DPV's other mapping folders, for DCAT, Dublin Core, gist, PROV, schema.org and SEMIC, hold a web page only, so nothing renders them. `dpv-odrl.ttl` does not parse, so the test reads its comment lines, and one row names `dpv:hasTechnology`, which 2.3 does not state.
