<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# dpv

Data Privacy Vocabulary (DPV) 2.3 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/dpv](https://lmodel.github.io/dpv)

## What it models

The schema renders the [Data Privacy Vocabulary (DPV)](https://w3id.org/dpv) 2.3 of 28 February 2026, from the W3C Data Privacy Vocabularies and Controls Community Group. DPV is the core vocabulary and its extensions for personal data, technology, artificial intelligence, risk, justifications, locations, laws, sectors and standards. DPV states each concept as a class and as an instance of a broader concept, so each kind of concept is a class here, each property a slot under its own IRI, and every term a record.

`src/dpv/data/` holds the terms and DPV's examples as records, `upstream/` holds DPV's files, pinned by hash, and `scripts/dpv_to_linkml.py` writes the first from the second. `project/owl/` describes this schema, and `upstream/2.3/` is DPV's ontology. [docs/about.md](docs/about.md) says what the records leave out and what stays open.

## Mappings

* **DPV's own alignments**: `src/dpv/mappings/` renders the mapping files DPV publishes for [ISO/IEC 29100:2024](https://www.iso.org/standard/85938.html) terms and for [ODRL](https://www.w3.org/TR/odrl-vocab/) as [SSSOM](https://mapping-commons.github.io/sssom/) sets. `tests/test_mappings.py` holds each row to DPV's files.

The 24 other SSSOM sets are gone: a matching tool wrote their rows, and many named terms that do not exist.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the converter from the Turtle and the upstream watch
* [src/dpv/schema/](src/dpv/schema): the LinkML schema. Edit `dpv_core.yaml` and `dpv.yaml`, and the converter writes the rest
* [src/dpv/data/](src/dpv/data): every term and example, which the converter writes
* [src/dpv/mappings/](src/dpv/mappings): DPV's own mappings, which the converter writes
* [src/dpv/datamodel/](src/dpv/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [upstream/](upstream/): DPV's Turtle, examples, mapping files and licence, unchanged
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/dpv.yaml`, is the copy `just lokf-adapt` writes from `src/dpv/schema/dpv.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-dpv.yaml`.

The copy roots `DpvTerm`, `DpvVocabulary`, `DpvConceptScheme`, `DpvAgent`, `DpvExample` and `DpvCatalogue` on `Concept`. A concept that describes a thing in a use case, such as a process, takes `DpvResource`, which holds any DPV property. In Obsidian, add these to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
DpvAISystem, DpvActivityStatus, DpvActor, DpvAdequacyDecision, DpvAgent, DpvAgentNegotiationBehaviour, DpvAgentRequestBehaviour, DpvAggregatedData, DpvAgreement, DpvAgreementNegotiationStatus, DpvAiCapability, DpvApplicability, DpvAuditStatus, DpvAuthority, DpvAutomationLevel, DpvAvailabilityConcept, DpvCatalogue, DpvChangeCategory, DpvCommunicationMechanism, DpvComplianceStatus, DpvConcept, DpvConceptScheme, DpvConfidentialityConcept, DpvConflictResolutionTerm, DpvConformanceStatus, DpvConsentStatus, DpvContractActivationStatus, DpvContractExecutionStatus, DpvContractFulfilmentStatus, DpvContractPerformanceStatus, DpvContractPreparationStatus, DpvContractTerminationStatus, DpvContractualClause, DpvContractualClauseFulfilmentStatus, DpvCountry, DpvDBIARiskStatus, DpvDPIAConformity, DpvDPIANecessityStatus, DpvDPIAOutcomeStatus, DpvDPIAProcessingRecommendation, DpvDPIARiskStatus, DpvDataBreachNotice, DpvDataBreachNoticeRequirement, DpvDataDeletionTerm, DpvDataProtectionAuthority, DpvDataSharingTerm, DpvDataSource, DpvDataSubjectDataSource, DpvDataSubjectScale, DpvDataTransparencyTerm, DpvDataVolume, DpvDeonticInterpretationTerm, DpvDocumentation, DpvDuration, DpvEntityInformedStatus, DpvEntityInvolvementStatus, DpvEntityNonPermissiveInvolvement, DpvEntityPermissiveInvolvement, DpvEuAiactMarketAvailabilityStatus, DpvEuAiactRiskLevel, DpvEuGdprDataProtectionAuthority, DpvEuGdprProcessing, DpvEvaluationScoring, DpvExample, DpvExpectationStatus, DpvFeeRequirement, DpvFrequency, DpvGeographicCoverage, DpvHighRiskAISystem, DpvHumanInvolvement, DpvHumanSubject, DpvImportance, DpvIncidentInvestigationStatus, DpvIncidentNotice, DpvIncidentStatus, DpvInnovativeUseOfTechnology, DpvIntegrityConcept, DpvIntentionStatus, DpvInverseJurisdiction, DpvInvolvementStatus, DpvJurisdiction, DpvJustification, DpvLaw, DpvLawfulness, DpvLegalBasis, DpvLegalEntity, DpvLegalMeasure, DpvLegalObligationStatus, DpvLegitimateInterestStatus, DpvLifecycleStage, DpvLikelihood, DpvLocation, DpvLocationFixture, DpvMarketPlacementStatus, DpvNecessity, DpvNonPersonalData, DpvNoticeStatus, DpvNotificationStatus, DpvObligation, DpvOfficialAuthorityExerciseStatus, DpvOrganisationalMeasure, DpvPartyTransparencyTerm, DpvPdPersonalData, DpvPermission, DpvPersonalData, DpvPhysicalMeasure, DpvPortabilityTerm, DpvPotentialConsequence, DpvPotentialImpact, DpvPotentialRisk, DpvPotentialRiskSource, DpvPreferenceApplicability, DpvProcessing, DpvProcessingContext, DpvProcessingScale, DpvProfilingTerm, DpvProhibitedAISystem, DpvProhibition, DpvProperty, DpvProportionalityStatus, DpvProvisionMethod, DpvProvisionStatus, DpvPublicInterestStatus, DpvPublicRegisterOfEntities, DpvPurpose, DpvPurposeTransparencyTerm, DpvRegion, DpvRegulatedHealthDataHolder, DpvRequestStatus, DpvResource, DpvReuseCompatibility, DpvRight, DpvRiskAnalysis, DpvRiskConcept, DpvRiskControl, DpvRiskLevel, DpvRule, DpvRuleFulfilmentStatus, DpvScoringOfIndividuals, DpvSector, DpvSectorHealthReuseCompatibility, DpvSensitivePersonalData, DpvServiceSupplyStatus, DpvSeverity, DpvSpecialCategoryPersonalData, DpvStatus, DpvSupraNationalUnion, DpvTechCapability, DpvTechMarketAvailabilityStatus, DpvTechnicalMeasure, DpvTechnique, DpvTechnology, DpvTrackingTerm, DpvTrainingTechnique, DpvTransparencyTerm, DpvVitalInterestStatus, DpvVocabulary
```

The copy drops `id` and `rdf_type` for LOKF's `id` and `type`, folds `schema_version` into LOKF's `version`, and renames each key LOKF also has with a `dpv_` prefix, keeping its IRI. A few of DPV's keys are ordinary words that other released copies also use, such as `subject` and `value`, so a host importing both projects them under one IRI. `tests/test_schema_rules.py` lists them.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

DPV's own files and the text taken from them are under the W3C Software and Document License: [NOTICE](NOTICE) reproduces it and says what this project changed. This project is not endorsed by the Community Group or by W3C.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
