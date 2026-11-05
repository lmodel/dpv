# Explanations

* [Why terms are records](terms-as-records.md) - Why the schema holds DPV's terms as records and not as classes: DPV states each concept as a class and as an instance, so one class per term could not say that a process's `hasPurpose` is `dpv:Marketing`.
* [How kinds and slots get their names](kinds-and-slots.md) - How the converter names what it writes: a kind's class takes a `Dpv` prefix and a slot keeps its property's local name, and where two namespaces define one name, the core keeps it and the other takes its namespace first.
* [What stays open](what-stays-open.md) - Why no validator refuses a value for leaving a property's usual classes: DPV states `domainIncludes` and `rangeIncludes`, not `rdfs:domain` and `rdfs:range`, so `DpvResource` holds any property.
* [What the records leave out](what-the-records-leave-out.md) - The facts of DPV's files no record holds, each with its reason: `skos:narrower`, which the records regenerate, the repeated `schema:` domain and range, what says how the site publishes a file, and `dpv-27560`.
* [What the data shows](what-the-data-shows.md) - What DPV's own files hold that a reader would not expect: names defined nowhere, predicates no vocabulary has, three example files that do not parse, and a term with two creation dates.
* [The mappings](mappings.md) - Which mappings this repository holds and why: only what DPV's editors publish in machine-readable form, for ISO/IEC 29100:2024 terms and for ODRL. The other 24 sets, which a matching tool wrote, are gone.
