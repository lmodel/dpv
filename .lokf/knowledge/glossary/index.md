# Glossary

* [Term](term.md) - A term: one thing DPV's vocabularies state as a concept or a property, under its own IRI. Each is one record here, a `DpvConcept` or a `DpvProperty`.
* [Kind](kind.md) - A kind: a type a DPV concept holds beyond `rdfs:Class` and `skos:Concept`, such as `dpv:Purpose`. Each of the 149 kinds is a class of this schema, and a record's `rdf_type` names its kinds.
* [Resource](resource.md) - A resource: a thing a use case describes with DPV, such as a process. `DpvResource` holds any DPV property, because DPV states none as limited to a class.
* [Namespace family](namespace-family.md) - A namespace family: the vocabularies this project keeps in one data file, such as `legal`, which holds the law vocabulary of each jurisdiction and each EU law.
* [Departure](departure.md) - A departure: a place DPV's own examples use a property beyond what its `rangeIncludes` or `domainIncludes` name, or give a literal where the range names a class. It breaks no rule of RDF.
* [Adapt copy](adapt-copy.md) - An adapt copy: the form of a schema `lokf adapt` writes so that it can sit beside LOKF's, in which concept classes descend from `Concept` and keys LOKF also has are renamed. Here it is `.lokf/dpv.yaml`.
