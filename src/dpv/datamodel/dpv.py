# Auto generated from dpv.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-06-03T22:25:17
# Schema: dpv
#
# id: https://w3id.org/lmodel/dpv
# description: Top-level umbrella LinkML schema for the W3C Data Privacy Vocabulary (DPV) version 2.3. Re-exports the eight semantic-group schemas (common, legal_basis, entities, personal_data, processing, risk_notice, rights, consent), which together provide 1:1 coverage of every class and slot in the upstream DPV 2.3 OWL release.
#
#   Each DPV semantic groups (i.e. `dpv_consent`) imports only its direct upstream module dependencies (i.e. `dpv_common`), avoiding the load cost of a single monolithic schema.
#
#   DPV modules (under `./modules/`) remain usable as standalone scheama,and are intentionally NOT imported here to avoid duplicate class declarations during generation (each shared class would otherwise arrive with two conflicting `from_Schema` URIs).
#
#   DPV extensions (under `./extensions/`, e.g. `ai`, `risk`, `pd``tech`, `legal/*`, `sector/*`) also remain usable as standalone schema, and are intentially NOT imported. This design aims to help consumers import only what they needed, not everything.
# license: CC-BY-4.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.11.0"
version = "2.3"

# Namespaces
COMMON_DOMAIN_MODEL = CurieNamespace('common_domain_model', 'https://w3id.org/lmodel/common-domain-model/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DPV = CurieNamespace('dpv', 'https://w3id.org/lmodel/dpv/')
DPV_OWL = CurieNamespace('dpv_owl', 'https://w3id.org/dpv/owl#')
DPV_UPSTREAM = CurieNamespace('dpv_upstream', 'https://w3id.org/dpv#')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
GISTS = CurieNamespace('gists', 'https://w3id.org/lmodel/gists/')
ISO22989 = CurieNamespace('iso22989', 'https://w3id.org/lmodel/iso22989/')
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
ISO29100 = CurieNamespace('iso29100', 'https://w3id.org/lmodel/iso29100/')
ISO42001 = CurieNamespace('iso42001', 'https://w3id.org/lmodel/iso42001/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_AI_RMF = CurieNamespace('nist_ai_rmf', 'https://w3id.org/lmodel/nist-ai-rmf/')
NIST_CSF_V2 = CurieNamespace('nist_csf_v2', 'https://w3id.org/lmodel/nist-csf-v2/')
OCSF = CurieNamespace('ocsf', 'https://w3id.org/lmodel/ocsf/')
ORG = CurieNamespace('org', 'http://www.w3.org/ns/org#')
OSCAL = CurieNamespace('oscal', 'https://w3id.org/lmodel/oscal/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROF = CurieNamespace('prof', 'http://www.w3.org/ns/dx/prof/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SVD = CurieNamespace('svd', 'https://specialprivacy.ercim.eu/vocabs/data#')
SVPR = CurieNamespace('svpr', 'https://specialprivacy.ercim.eu/vocabs/processing#')
SVPU = CurieNamespace('svpu', 'https://specialprivacy.ercim.eu/vocabs/purposes#')
USAGE_POLICY = CurieNamespace('usage_policy', 'https://specialprivacy.ercim.eu/langs/usage-policy#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = DPV


# Types

# Class references
class DpvThingId(URIorCURIE):
    pass


class ContextId(DpvThingId):
    pass


class ApplicabilityId(ContextId):
    pass


class DpvDurationId(ContextId):
    pass


class EndlessDurationId(DpvDurationId):
    pass


class ExpectationStatusId(DpvThingId):
    pass


class ExpectedId(ExpectationStatusId):
    pass


class FeeRequirementId(ContextId):
    pass


class FeeNotRequiredId(FeeRequirementId):
    pass


class FeeRequiredId(FeeRequirementId):
    pass


class FixedOccurrencesDurationId(DpvDurationId):
    pass


class FrequencyId(ContextId):
    pass


class ContinuousFrequencyId(FrequencyId):
    pass


class ImportanceId(ContextId):
    pass


class IndeterminateDurationId(DpvDurationId):
    pass


class JustificationId(ContextId):
    pass


class NecessityId(ContextId):
    pass


class DpvOptionalId(NecessityId):
    pass


class NotApplicableId(ApplicabilityId):
    pass


class NotAvailableId(ApplicabilityId):
    pass


class NotRequiredId(NecessityId):
    pass


class OftenFrequencyId(FrequencyId):
    pass


class PrimaryImportanceId(ImportanceId):
    pass


class RequiredId(NecessityId):
    pass


class RuleId(DpvThingId):
    pass


class AcceptableRuleId(RuleId):
    pass


class ObligationId(AcceptableRuleId):
    pass


class PermissionId(AcceptableRuleId):
    pass


class RecommendationId(AcceptableRuleId):
    pass


class ScopeId(ContextId):
    pass


class SecondaryImportanceId(ImportanceId):
    pass


class SingularFrequencyId(FrequencyId):
    pass


class SporadicFrequencyId(FrequencyId):
    pass


class StatusId(ContextId):
    pass


class ActivityStatusId(StatusId):
    pass


class ActivityCompletedId(ActivityStatusId):
    pass


class ActivityHaltedId(ActivityStatusId):
    pass


class ActivityNotCompletedId(ActivityStatusId):
    pass


class ActivityOngoingId(ActivityStatusId):
    pass


class ActivityPlannedId(ActivityStatusId):
    pass


class ActivityProposedId(ActivityStatusId):
    pass


class AuditStatusId(StatusId):
    pass


class AuditApprovedId(AuditStatusId):
    pass


class AuditConditionallyApprovedId(AuditStatusId):
    pass


class AuditNotRequiredId(AuditStatusId):
    pass


class AuditRejectedId(AuditStatusId):
    pass


class AuditRequestedId(AuditStatusId):
    pass


class AuditRequiredId(AuditStatusId):
    pass


class ComplianceStatusId(StatusId):
    pass


class ComplianceIndeterminateId(ComplianceStatusId):
    pass


class ComplianceUnknownId(ComplianceStatusId):
    pass


class ComplianceViolationId(ComplianceStatusId):
    pass


class CompliantId(ComplianceStatusId):
    pass


class ConformanceStatusId(StatusId):
    pass


class ConformantId(ConformanceStatusId):
    pass


class EntityInformedStatusId(StatusId):
    pass


class EntityInformedId(EntityInformedStatusId):
    pass


class AuthorityInformedId(EntityInformedId):
    pass


class ControllerInformedId(EntityInformedId):
    pass


class DataSubjectInformedId(EntityInformedId):
    pass


class EntityUninformedId(EntityInformedStatusId):
    pass


class AuthorityUninformedId(EntityUninformedId):
    pass


class ControllerUninformedId(EntityUninformedId):
    pass


class DataSubjectUninformedId(EntityUninformedId):
    pass


class IntentionStatusId(StatusId):
    pass


class IntendedId(IntentionStatusId):
    pass


class InvolvementStatusId(StatusId):
    pass


class ActivelyInvolvedId(InvolvementStatusId):
    pass


class LawfulnessId(ComplianceStatusId):
    pass


class LawfulId(LawfulnessId):
    pass


class LawfulnessUnknownId(LawfulnessId):
    pass


class NonCompliantId(ComplianceStatusId):
    pass


class NonConformantId(ConformanceStatusId):
    pass


class NotInvolvedId(InvolvementStatusId):
    pass


class NotificationStatusId(StatusId):
    pass


class NotificationCompletedId(NotificationStatusId):
    pass


class NotificationFailedId(NotificationStatusId):
    pass


class NotificationNotNeededId(NotificationStatusId):
    pass


class NotificationOngoingId(NotificationStatusId):
    pass


class NotificationPlannedId(NotificationStatusId):
    pass


class PartiallyCompliantId(ComplianceStatusId):
    pass


class PassivelyInvolvedId(InvolvementStatusId):
    pass


class RecipientInformedId(EntityInformedId):
    pass


class RecipientUninformedId(EntityUninformedId):
    pass


class RequestStatusId(StatusId):
    pass


class RequestAcceptedId(RequestStatusId):
    pass


class RequestAcknowledgedId(RequestStatusId):
    pass


class RequestActionDelayedId(RequestStatusId):
    pass


class RequestFulfilledId(RequestStatusId):
    pass


class RequestInitiatedId(RequestStatusId):
    pass


class RequestRejectedId(RequestStatusId):
    pass


class RequestRequiredActionPerformedId(RequestStatusId):
    pass


class RequestRequiresActionId(RequestStatusId):
    pass


class RequestStatusQueryId(RequestStatusId):
    pass


class RequestUnfulfilledId(RequestStatusId):
    pass


class ReuseCompatibilityId(StatusId):
    pass


class CompatibilityUnknownId(ReuseCompatibilityId):
    pass


class PrimaryUseId(ReuseCompatibilityId):
    pass


class RuleFulfilmentStatusId(StatusId):
    pass


class RuleFulfilledId(RuleFulfilmentStatusId):
    pass


class DeterrenceFollowedId(RuleFulfilledId):
    pass


class ObligationFulfilledId(RuleFulfilledId):
    pass


class PermissionNotUtilisedId(RuleFulfilledId):
    pass


class PermissionUtilisedId(RuleFulfilledId):
    pass


class ProhibitionUnviolatedId(RuleFulfilledId):
    pass


class RecommendationFollowedId(RuleFulfilledId):
    pass


class RuleUnfulfilledId(RuleFulfilmentStatusId):
    pass


class DeterrenceNotFollowedId(RuleUnfulfilledId):
    pass


class ObligationUnfulfilledId(RuleUnfulfilledId):
    pass


class RecommendationNotFollowedId(RuleUnfulfilledId):
    pass


class RuleViolatedId(RuleFulfilmentStatusId):
    pass


class ObligationViolatedId(RuleViolatedId):
    pass


class ProhibitionViolatedId(RuleViolatedId):
    pass


class SecondaryUseId(ReuseCompatibilityId):
    pass


class TechnicalOrganisationalMeasureId(DpvThingId):
    pass


class LegalMeasureId(TechnicalOrganisationalMeasureId):
    pass


class OrganisationalMeasureId(TechnicalOrganisationalMeasureId):
    pass


class PhysicalMeasureId(TechnicalOrganisationalMeasureId):
    pass


class TechnicalMeasureId(TechnicalOrganisationalMeasureId):
    pass


class TemporalDurationId(DpvDurationId):
    pass


class UnacceptableRuleId(RuleId):
    pass


class DeterrenceId(UnacceptableRuleId):
    pass


class ProhibitionId(UnacceptableRuleId):
    pass


class UnexpectedId(ExpectationStatusId):
    pass


class UnintendedId(IntentionStatusId):
    pass


class UnknownApplicabilityId(ApplicabilityId):
    pass


class UnlawfulId(LawfulnessId):
    pass


class UntilEventDurationId(DpvDurationId):
    pass


class UntilTimeDurationId(DpvDurationId):
    pass


class ContractStatusId(StatusId):
    pass


class ContractActivationStatusId(ContractStatusId):
    pass


class ContractActiveId(ContractActivationStatusId):
    pass


class ContractExecutionStatusId(ContractStatusId):
    pass


class ContractFulfilmentStatusId(ContractStatusId):
    pass


class ContractFulfilledId(ContractFulfilmentStatusId):
    pass


class ContractFullyExecutedId(ContractExecutionStatusId):
    pass


class ContractFullySignedId(ContractExecutionStatusId):
    pass


class ContractInactiveId(ContractActivationStatusId):
    pass


class ContractNotFulfilledId(ContractFulfilmentStatusId):
    pass


class ContractPartiallyFulfilledId(ContractFulfilmentStatusId):
    pass


class ContractPartiallySignedId(ContractExecutionStatusId):
    pass


class ContractPerformanceStatusId(ContractStatusId):
    pass


class ContractAmendedId(ContractPerformanceStatusId):
    pass


class ContractBeingPerformedId(ContractPerformanceStatusId):
    pass


class ContractPreparationStatusId(ContractStatusId):
    pass


class ContractApprovedId(ContractPreparationStatusId):
    pass


class ContractDraftedId(ContractPreparationStatusId):
    pass


class ContractNegotiatedId(ContractPreparationStatusId):
    pass


class ContractOfferedId(ContractPreparationStatusId):
    pass


class ContractRejectedId(ContractPreparationStatusId):
    pass


class ContractRenewedId(ContractPerformanceStatusId):
    pass


class ContractSignedByPartyId(ContractExecutionStatusId):
    pass


class ContractTemporarilySuspendedId(ContractPerformanceStatusId):
    pass


class ContractTerminationStatusId(ContractStatusId):
    pass


class ContractBreachedId(ContractTerminationStatusId):
    pass


class ContractDisputedId(ContractTerminationStatusId):
    pass


class ContractExpiredId(ContractTerminationStatusId):
    pass


class ContractExtendedId(ContractTerminationStatusId):
    pass


class ContractTerminatedId(ContractTerminationStatusId):
    pass


class ContractUnderNegotiationId(ContractPreparationStatusId):
    pass


class ContractUnderReviewId(ContractPreparationStatusId):
    pass


class ContractViolatedId(ContractFulfilmentStatusId):
    pass


class ContractualClauseId(DpvThingId):
    pass


class ContractAmendmentClauseId(ContractualClauseId):
    pass


class ContractConfidentialityClauseId(ContractualClauseId):
    pass


class ContractDefinitionsId(ContractualClauseId):
    pass


class ContractDisputeResolutionClauseId(ContractualClauseId):
    pass


class ContractJurisdictionClauseId(ContractualClauseId):
    pass


class ContractPreambleId(ContractualClauseId):
    pass


class ContractTerminationClauseId(ContractualClauseId):
    pass


class ContractualClauseFulfilmentStatusId(ContractStatusId):
    pass


class ContractualClauseFulfilledId(ContractualClauseFulfilmentStatusId):
    pass


class ContractualClauseNotFulfilledId(ContractualClauseFulfilmentStatusId):
    pass


class ContractualClausePartiallyFulfilledId(ContractualClauseFulfilmentStatusId):
    pass


class ContractualClauseViolatedId(ContractualClauseFulfilmentStatusId):
    pass


class ContractualTermsId(LegalMeasureId):
    pass


class DataHandlingClauseId(ContractualTermsId):
    pass


class DpvLocationId(DpvThingId):
    pass


class DpvJurisdictionId(DpvLocationId):
    pass


class DpvCountryId(DpvJurisdictionId):
    pass


class DpvRegionId(DpvCountryId):
    pass


class CityId(DpvRegionId):
    pass


class EconomicUnionId(DpvJurisdictionId):
    pass


class InverseJurisdictionId(DpvJurisdictionId):
    pass


class LawId(DpvThingId):
    pass


class LegalAgreementId(LegalMeasureId):
    pass


class ConfidentialityAgreementId(LegalAgreementId):
    pass


class LegalBasisId(DpvThingId):
    pass


class ConsentId(LegalBasisId):
    pass


class ContractId(LegalBasisId):
    pass


class ContractByDomainId(ContractId):
    pass


class ContractByEntityTypeId(ContractId):
    pass


class B2BContractId(ContractByEntityTypeId):
    pass


class B2B2CContractId(B2BContractId):
    pass


class B2CContractId(ContractByEntityTypeId):
    pass


class C2BContractId(ContractByEntityTypeId):
    pass


class C2CContractId(ContractByEntityTypeId):
    pass


class ContractByNegotiationTypeId(ContractId):
    pass


class ContractPerformanceId(ContractId):
    pass


class DataProcessingAgreementId(ContractId):
    pass


class DataControllerContractId(DataProcessingAgreementId):
    pass


class DataProcessorContractId(DataProcessingAgreementId):
    pass


class ControllerProcessorAgreementId(DataProcessorContractId):
    pass


class DataSubjectContractId(DataProcessingAgreementId):
    pass


class ControllerDataSubjectAgreementId(DataSubjectContractId):
    pass


class DataTransferLegalBasisId(LegalBasisId):
    pass


class DistributionAgreementId(ContractByDomainId):
    pass


class EmploymentContractId(ContractByDomainId):
    pass


class EnterIntoContractId(ContractId):
    pass


class G2BContractId(ContractByEntityTypeId):
    pass


class G2CContractId(ContractByEntityTypeId):
    pass


class G2GContractId(ContractByEntityTypeId):
    pass


class JointDataControllersAgreementId(DataControllerContractId):
    pass


class LegalObligationId(LegalBasisId):
    pass


class LegalObligationStatusId(StatusId):
    pass


class LegalObligationCompletedId(LegalObligationStatusId):
    pass


class LegalObligationOngoingId(LegalObligationStatusId):
    pass


class LegalObligationPendingId(LegalObligationStatusId):
    pass


class LegitimateInterestId(LegalBasisId):
    pass


class LegitimateInterestOfControllerId(LegitimateInterestId):
    pass


class LegitimateInterestOfDataSubjectId(LegitimateInterestId):
    pass


class LegitimateInterestOfThirdPartyId(LegitimateInterestId):
    pass


class LegitimateInterestStatusId(StatusId):
    pass


class LegitimateInterestInformedId(LegitimateInterestStatusId):
    pass


class LegitimateInterestNotObjectedId(LegitimateInterestStatusId):
    pass


class LegitimateInterestObjectedId(LegitimateInterestStatusId):
    pass


class LegitimateInterestUninformedId(LegitimateInterestStatusId):
    pass


class LicenseAgreementId(ContractByDomainId):
    pass


class EULAId(LicenseAgreementId):
    pass


class LocationFixtureId(DpvThingId):
    pass


class DecentralisedLocationsId(LocationFixtureId):
    pass


class FederatedLocationsId(LocationFixtureId):
    pass


class FixedLocationId(LocationFixtureId):
    pass


class FixedMultipleLocationsId(FixedLocationId):
    pass


class FixedSingularLocationId(FixedLocationId):
    pass


class LocationLocalityId(DpvLocationId):
    pass


class LocalLocationId(LocationLocalityId):
    pass


class NDAId(LegalAgreementId):
    pass


class NegotiatedContractId(ContractByNegotiationTypeId):
    pass


class OfficialAuthorityExerciseStatusId(StatusId):
    pass


class OfficialAuthorityExerciseCompletedId(OfficialAuthorityExerciseStatusId):
    pass


class OfficialAuthorityExerciseOngoingId(OfficialAuthorityExerciseStatusId):
    pass


class OfficialAuthorityExercisePendingId(OfficialAuthorityExerciseStatusId):
    pass


class OfficialAuthorityOfControllerId(LegalBasisId):
    pass


class PrivateLocationId(LocalLocationId):
    pass


class PrivateSpaceId(DpvLocationId):
    pass


class HybridPublicPrivateSpaceId(PrivateSpaceId):
    pass


class PersonalSpaceId(PrivateSpaceId):
    pass


class PrivateCommunalSpaceId(PrivateSpaceId):
    pass


class PrivatelyOperatedPublicSpaceId(HybridPublicPrivateSpaceId):
    pass


class PrivatelyOwnedPublicSpaceId(HybridPublicPrivateSpaceId):
    pass


class PrivatelyOwnedSpaceId(PrivateSpaceId):
    pass


class PublicInterestId(LegalBasisId):
    pass


class PublicInterestStatusId(StatusId):
    pass


class PublicInterestCompletedId(PublicInterestStatusId):
    pass


class PublicInterestObjectedId(PublicInterestStatusId):
    pass


class PublicInterestOngoingId(PublicInterestStatusId):
    pass


class PublicInterestPendingId(PublicInterestStatusId):
    pass


class PublicLocationId(LocalLocationId):
    pass


class PublicSpaceId(DpvLocationId):
    pass


class PubliclyAccessibleSpaceId(PublicSpaceId):
    pass


class PubliclyOwnedSpaceId(PublicSpaceId):
    pass


class RandomLocationId(LocationFixtureId):
    pass


class RemoteLocationId(LocationLocalityId):
    pass


class CloudLocationId(RemoteLocationId):
    pass


class SemiPrivateSpaceId(PrivateSpaceId):
    pass


class ServiceLevelAgreementId(ContractByDomainId):
    pass


class StandardFormContractId(ContractByNegotiationTypeId):
    pass


class ConsumerStandardFormContractId(StandardFormContractId):
    pass


class ProviderStandardFormContractId(StandardFormContractId):
    pass


class StatisticalConfidentialityAgreementId(LegalAgreementId):
    pass


class SubProcessorAgreementId(DataProcessingAgreementId):
    pass


class SupraNationalUnionId(DpvJurisdictionId):
    pass


class TermsOfServiceId(ContractualClauseId):
    pass


class ThirdCountryId(DpvCountryId):
    pass


class ThirdPartyContractId(DataProcessingAgreementId):
    pass


class ThirdPartyAgreementId(ThirdPartyContractId):
    pass


class VariableLocationId(LocationFixtureId):
    pass


class VitalInterestId(LegalBasisId):
    pass


class VitalInterestOfNaturalPersonId(VitalInterestId):
    pass


class VitalInterestOfDataSubjectId(VitalInterestOfNaturalPersonId):
    pass


class VitalInterestStatusId(StatusId):
    pass


class VitalInterestCompletedId(VitalInterestStatusId):
    pass


class VitalInterestObjectedId(VitalInterestStatusId):
    pass


class VitalInterestOngoingId(VitalInterestStatusId):
    pass


class VitalInterestPendingId(VitalInterestStatusId):
    pass


class WithinDeviceId(LocalLocationId):
    pass


class WithinPhysicalEnvironmentId(DpvLocationId):
    pass


class WithinVirtualEnvironmentId(DpvLocationId):
    pass


class DpvEntityId(DpvThingId):
    pass


class DpvAgentId(DpvEntityId):
    pass


class LegalAgentId(DpvAgentId):
    pass


class LegalEntityId(DpvEntityId):
    pass


class CharityOrganisationId(LegalEntityId):
    pass


class DataControllerId(LegalEntityId):
    pass


class DataExporterId(LegalEntityId):
    pass


class DpvOrganisationId(LegalEntityId):
    pass


class AcademicScientificOrganisationId(DpvOrganisationId):
    pass


class ClinicId(DpvOrganisationId):
    pass


class DpvRecipientId(LegalEntityId):
    pass


class DataImporterId(DpvRecipientId):
    pass


class DataProcessorId(DpvRecipientId):
    pass


class DataSubProcessorId(DataProcessorId):
    pass


class EducationalOrganisationId(DpvOrganisationId):
    pass


class EmergencyServiceProviderId(DpvOrganisationId):
    pass


class AmbulanceProviderId(EmergencyServiceProviderId):
    pass


class EmergencyHealthcareProviderId(EmergencyServiceProviderId):
    pass


class FireDepartmentId(EmergencyServiceProviderId):
    pass


class ForProfitOrganisationId(DpvOrganisationId):
    pass


class GovernmentalOrganisationId(DpvOrganisationId):
    pass


class DpvAuthorityId(GovernmentalOrganisationId):
    pass


class DataProtectionAuthorityId(DpvAuthorityId):
    pass


class HealthcareOrganisationId(DpvOrganisationId):
    pass


class HospitalId(DpvOrganisationId):
    pass


class HumanSubjectId(LegalEntityId):
    pass


class AdultId(HumanSubjectId):
    pass


class ApplicantId(HumanSubjectId):
    pass


class CitizenId(HumanSubjectId):
    pass


class DataSubjectId(HumanSubjectId):
    pass


class DpvConsumerId(HumanSubjectId):
    pass


class DpvCustomerId(HumanSubjectId):
    pass


class ClientId(DpvCustomerId):
    pass


class DpvUserId(HumanSubjectId):
    pass


class EmployeeId(HumanSubjectId):
    pass


class GuardianOfHumanId(HumanSubjectId):
    pass


class GuardianOfDataSubjectId(GuardianOfHumanId):
    pass


class ImmigrantId(HumanSubjectId):
    pass


class IndustryConsortiumId(DpvOrganisationId):
    pass


class InternationalOrganisationId(DpvOrganisationId):
    pass


class JobApplicantId(HumanSubjectId):
    pass


class JointDataControllersId(DataControllerId):
    pass


class JudicialOrganisationId(DpvOrganisationId):
    pass


class LawEnforcementOrganisationId(DpvOrganisationId):
    pass


class MemberId(HumanSubjectId):
    pass


class NationalAuthorityId(DpvAuthorityId):
    pass


class NaturalPersonId(DpvEntityId):
    pass


class NonCitizenId(HumanSubjectId):
    pass


class NonGovernmentalOrganisationId(DpvOrganisationId):
    pass


class NonProfitOrganisationId(DpvOrganisationId):
    pass


class OrganisationalUnitId(DpvEntityId):
    pass


class ParentLegalEntityId(DpvOrganisationId):
    pass


class ParentOfHumanId(HumanSubjectId):
    pass


class ParentOfDataSubjectId(ParentOfHumanId):
    pass


class ParticipantId(HumanSubjectId):
    pass


class PatientId(HumanSubjectId):
    pass


class PrivateSectorBodyId(LegalEntityId):
    pass


class PublicRegisterOfEntitiesId(DpvThingId):
    pass


class PublicSectorBodyId(LegalEntityId):
    pass


class RegionalAuthorityId(DpvAuthorityId):
    pass


class ReligiousAssociationsId(DpvOrganisationId):
    pass


class RepresentativeId(LegalEntityId):
    pass


class DataProtectionOfficerId(RepresentativeId):
    pass


class SMEOrganisationId(LegalEntityId):
    pass


class ServiceConsumerId(LegalEntityId):
    pass


class ServiceProviderId(LegalEntityId):
    pass


class StartupOrganisationId(LegalEntityId):
    pass


class StudentId(HumanSubjectId):
    pass


class SubscriberId(HumanSubjectId):
    pass


class SubsidiaryLegalEntityId(DpvOrganisationId):
    pass


class SupraNationalAuthorityId(DpvAuthorityId):
    pass


class ThirdPartyId(LegalEntityId):
    pass


class TouristId(HumanSubjectId):
    pass


class VisitorId(HumanSubjectId):
    pass


class VulnerableHumanId(HumanSubjectId):
    pass


class AsylumSeekerId(VulnerableHumanId):
    pass


class ChildId(VulnerableHumanId):
    pass


class ElderlyHumanId(VulnerableHumanId):
    pass


class MentallyVulnerableHumanId(VulnerableHumanId):
    pass


class MentallyVulnerableDataSubjectId(MentallyVulnerableHumanId):
    pass


class VulnerableDataSubjectId(VulnerableHumanId):
    pass


class ElderlyDataSubjectId(VulnerableDataSubjectId):
    pass


class AccessControlMethodId(TechnicalMeasureId):
    pass


class ActivityMonitoringId(TechnicalMeasureId):
    pass


class AssessmentId(OrganisationalMeasureId):
    pass


class AuditId(OrganisationalMeasureId):
    pass


class AuthenticationProtocolsId(TechnicalMeasureId):
    pass


class AuthorisationProtocolsId(TechnicalMeasureId):
    pass


class BiometricAuthenticationId(AuthenticationProtocolsId):
    pass


class CertificationSealId(OrganisationalMeasureId):
    pass


class CertificationId(CertificationSealId):
    pass


class ComplianceAssessmentId(AssessmentId):
    pass


class ConformanceAssessmentId(AssessmentId):
    pass


class ConsultationId(OrganisationalMeasureId):
    pass


class ConsultationWithAuthorityId(ConsultationId):
    pass


class ConsultationWithDPOId(ConsultationId):
    pass


class ConsultationWithDataSubjectId(ConsultationId):
    pass


class ConsultationWithDataSubjectRepresentativeId(ConsultationWithDataSubjectId):
    pass


class CryptographicAuthenticationId(AuthenticationProtocolsId):
    pass


class AuthenticationABCId(CryptographicAuthenticationId):
    pass


class AuthenticationPABCId(CryptographicAuthenticationId):
    pass


class CryptographicMethodsId(TechnicalMeasureId):
    pass


class AsymmetricCryptographyId(CryptographicMethodsId):
    pass


class CryptographicKeyManagementId(CryptographicMethodsId):
    pass


class DataBackupProtocolsId(TechnicalMeasureId):
    pass


class DataInteroperabilityAssessmentId(AssessmentId):
    pass


class DataQualityAssessmentId(AssessmentId):
    pass


class DataSanitisationTechniqueId(TechnicalMeasureId):
    pass


class DataRedactionId(DataSanitisationTechniqueId):
    pass


class DataSuitabilityAssessmentId(DataQualityAssessmentId):
    pass


class DeidentificationId(DataSanitisationTechniqueId):
    pass


class AnonymisationId(DeidentificationId):
    pass


class DifferentialPrivacyId(CryptographicMethodsId):
    pass


class DigitalLiteracyId(OrganisationalMeasureId):
    pass


class AILiteracyId(DigitalLiteracyId):
    pass


class DataLiteracyId(DigitalLiteracyId):
    pass


class DigitalRightsManagementId(TechnicalMeasureId):
    pass


class DigitalSignaturesId(CryptographicMethodsId):
    pass


class DpvDataId(DpvThingId):
    pass


class CollectedDataId(DpvDataId):
    pass


class CollectedPersonalDataId(CollectedDataId):
    pass


class ConfidentialDataId(DpvDataId):
    pass


class CommerciallyConfidentialDataId(ConfidentialDataId):
    pass


class DerivedDataId(DpvDataId):
    pass


class DerivedPersonalDataId(DerivedDataId):
    pass


class EffectivenessDeterminationProceduresId(AssessmentId):
    pass


class EncryptionId(TechnicalMeasureId):
    pass


class AsymmetricEncryptionId(EncryptionId):
    pass


class EncryptionAtRestId(EncryptionId):
    pass


class EncryptionInTransferId(EncryptionId):
    pass


class EncryptionInUseId(EncryptionId):
    pass


class EndToEndEncryptionId(EncryptionId):
    pass


class EnvironmentalProtectionId(PhysicalMeasureId):
    pass


class FailSafeProtocolsId(TechnicalMeasureId):
    pass


class GeneratedDataId(DpvDataId):
    pass


class GovernanceProceduresId(OrganisationalMeasureId):
    pass


class AIGovernanceId(GovernanceProceduresId):
    pass


class ApprovalProcedureId(GovernanceProceduresId):
    pass


class AssetManagementProceduresId(GovernanceProceduresId):
    pass


class ComplianceMonitoringId(GovernanceProceduresId):
    pass


class DisasterRecoveryProceduresId(GovernanceProceduresId):
    pass


class GuidelinesPrincipleId(OrganisationalMeasureId):
    pass


class CodeOfConductId(GuidelinesPrincipleId):
    pass


class GuidelineId(GuidelinesPrincipleId):
    pass


class HashFunctionsId(CryptographicMethodsId):
    pass


class HashMessageAuthenticationCodeId(CryptographicAuthenticationId):
    pass


class HomomorphicEncryptionId(CryptographicMethodsId):
    pass


class HumanOversightId(GovernanceProceduresId):
    pass


class IncidentManagementProceduresId(GovernanceProceduresId):
    pass


class IncidentReportingCommunicationId(GovernanceProceduresId):
    pass


class IncorrectDataId(DpvDataId):
    pass


class InferredDataId(DerivedDataId):
    pass


class InferredPersonalDataId(DerivedPersonalDataId):
    pass


class InformationAuditId(AuditId):
    pass


class InformationFlowControlId(TechnicalMeasureId):
    pass


class IntellectualPropertyDataId(ConfidentialDataId):
    pass


class LegalComplianceAssessmentId(ComplianceAssessmentId):
    pass


class LegalComplianceAuditId(AuditId):
    pass


class LegitimateInterestAssessmentId(AssessmentId):
    pass


class MessageAuthenticationCodesId(CryptographicAuthenticationId):
    pass


class MultiFactorAuthenticationId(AuthenticationProtocolsId):
    pass


class NonPersonalDataId(DpvDataId):
    pass


class AnonymisedDataId(NonPersonalDataId):
    pass


class NotificationId(OrganisationalMeasureId):
    pass


class ObservedDataId(CollectedDataId):
    pass


class ObservedPersonalDataId(CollectedPersonalDataId):
    pass


class PasswordAuthenticationId(AuthenticationProtocolsId):
    pass


class PersonalDataId(DpvDataId):
    pass


class GeneratedPersonalDataId(PersonalDataId):
    pass


class IdentifyingPersonalDataId(PersonalDataId):
    pass


class PersonalDataAuditId(InformationAuditId):
    pass


class PhysicalAccessControlMethodId(AccessControlMethodId):
    pass


class PhysicalAuthenticationId(PhysicalMeasureId):
    pass


class PhysicalAuthorisationId(PhysicalMeasureId):
    pass


class PhysicalDeviceSecurityId(PhysicalMeasureId):
    pass


class PhysicalInterceptionProtectionId(PhysicalMeasureId):
    pass


class PhysicalInterruptionProtectionId(PhysicalMeasureId):
    pass


class PhysicalNetworkSecurityId(PhysicalMeasureId):
    pass


class PhysicalSecureStorageId(PhysicalMeasureId):
    pass


class PhysicalSupplySecurityId(PhysicalMeasureId):
    pass


class PhysicalSurveillanceId(PhysicalMeasureId):
    pass


class PolicyId(GovernanceProceduresId):
    pass


class AcceptableUsePolicyId(PolicyId):
    pass


class DataProcessingPolicyId(PolicyId):
    pass


class DataDeletionPolicyId(DataProcessingPolicyId):
    pass


class DataErasurePolicyId(DataProcessingPolicyId):
    pass


class DataJurisdictionPolicyId(DataProcessingPolicyId):
    pass


class DataRestorationPolicyId(DataProcessingPolicyId):
    pass


class DataReusePolicyId(DataProcessingPolicyId):
    pass


class DataStoragePolicyId(DataProcessingPolicyId):
    pass


class InformationSecurityPolicyId(PolicyId):
    pass


class LoggingPolicyId(PolicyId):
    pass


class MonitoringPolicyId(PolicyId):
    pass


class PostQuantumCryptographyId(CryptographicMethodsId):
    pass


class PrincipleId(GuidelinesPrincipleId):
    pass


class PrivacyByDefaultId(GuidelinesPrincipleId):
    pass


class PrivacyByDesignId(GuidelinesPrincipleId):
    pass


class PrivacyPreservingProtocolId(CryptographicMethodsId):
    pass


class PrivateInformationRetrievalId(CryptographicMethodsId):
    pass


class ProfessionalConfidentialDataId(ConfidentialDataId):
    pass


class ProvidedDataId(CollectedDataId):
    pass


class ProvidedPersonalDataId(CollectedPersonalDataId):
    pass


class PseudonymisationId(DeidentificationId):
    pass


class DeterministicPseudonymisationId(PseudonymisationId):
    pass


class DocumentRandomisedPseudonymisationId(PseudonymisationId):
    pass


class FullyRandomisedPseudonymisationId(PseudonymisationId):
    pass


class MonotonicCounterPseudonymisationId(PseudonymisationId):
    pass


class PseudonymisedDataId(PersonalDataId):
    pass


class ContextuallyAnonymisedDataId(PseudonymisedDataId):
    pass


class QuantumCryptographyId(CryptographicMethodsId):
    pass


class RNGPseudonymisationId(PseudonymisationId):
    pass


class RecertificationPolicyId(PolicyId):
    pass


class RecordsOfActivitiesId(OrganisationalMeasureId):
    pass


class DataBreachRecordId(RecordsOfActivitiesId):
    pass


class DataProcessingRecordId(RecordsOfActivitiesId):
    pass


class ConsentRecordId(DataProcessingRecordId):
    pass


class ConsentReceiptId(ConsentRecordId):
    pass


class DataTransferRecordId(DataProcessingRecordId):
    pass


class ROPAId(DataProcessingRecordId):
    pass


class ReviewProcedureId(GovernanceProceduresId):
    pass


class RightsManagementId(OrganisationalMeasureId):
    pass


class DataSubjectRightsManagementId(RightsManagementId):
    pass


class IPRManagementId(RightsManagementId):
    pass


class PermissionManagementId(RightsManagementId):
    pass


class ConsentManagementId(PermissionManagementId):
    pass


class SafeguardId(OrganisationalMeasureId):
    pass


class RegulatorySandboxId(SafeguardId):
    pass


class SafeguardForDataTransferId(SafeguardId):
    pass


class SealId(CertificationSealId):
    pass


class SecretSharingSchemesId(CryptographicMethodsId):
    pass


class SecureMultiPartyComputationId(CryptographicMethodsId):
    pass


class SecurityAuditId(AuditId):
    pass


class SecurityIncidentNotificationId(NotificationId):
    pass


class DataBreachNotificationId(SecurityIncidentNotificationId):
    pass


class SecurityIncidentRecordId(RecordsOfActivitiesId):
    pass


class SecurityMethodId(TechnicalMeasureId):
    pass


class DistributedSystemSecurityId(SecurityMethodId):
    pass


class DocumentSecurityId(SecurityMethodId):
    pass


class FileSystemSecurityId(SecurityMethodId):
    pass


class HardwareSecurityProtocolsId(SecurityMethodId):
    pass


class IntrusionDetectionSystemId(SecurityMethodId):
    pass


class MobilePlatformSecurityId(SecurityMethodId):
    pass


class NetworkProxyRoutingId(SecurityMethodId):
    pass


class NetworkSecurityProtocolsId(SecurityMethodId):
    pass


class OperatingSystemSecurityId(SecurityMethodId):
    pass


class PenetrationTestingMethodsId(SecurityMethodId):
    pass


class SecurityProcedureId(OrganisationalMeasureId):
    pass


class AuthorisationProcedureId(SecurityProcedureId):
    pass


class BackgroundChecksId(SecurityProcedureId):
    pass


class CredentialManagementId(AuthorisationProcedureId):
    pass


class IdentityManagementMethodId(AuthorisationProcedureId):
    pass


class SecureProcessingEnvironmentId(SecurityProcedureId):
    pass


class SecurityRoleProceduresId(SecurityProcedureId):
    pass


class SensitiveDataId(DpvDataId):
    pass


class SensitiveNonPersonalDataId(SensitiveDataId):
    pass


class SensitivePersonalDataId(PersonalDataId):
    pass


class SingleSignOnId(AuthenticationProtocolsId):
    pass


class SpecialCategoryPersonalDataId(SensitivePersonalDataId):
    pass


class StaffTrainingId(OrganisationalMeasureId):
    pass


class CybersecurityTrainingId(StaffTrainingId):
    pass


class DataProtectionTrainingId(StaffTrainingId):
    pass


class EducationalTrainingId(StaffTrainingId):
    pass


class ProfessionalTrainingId(StaffTrainingId):
    pass


class SecurityKnowledgeTrainingId(StaffTrainingId):
    pass


class StandardId(GuidelinesPrincipleId):
    pass


class DesignStandardId(StandardId):
    pass


class ManagementStandardId(StandardId):
    pass


class StandardsConformanceId(GovernanceProceduresId):
    pass


class StatisticallyConfidentialDataId(ConfidentialDataId):
    pass


class SupportEntityDecisionMakingId(OrganisationalMeasureId):
    pass


class SupportContractNegotiationId(SupportEntityDecisionMakingId):
    pass


class SupportExchangeOfViewsId(SupportEntityDecisionMakingId):
    pass


class SupportInformedConsentDecisionId(SupportEntityDecisionMakingId):
    pass


class SymmetricCryptographyId(CryptographicMethodsId):
    pass


class SymmetricEncryptionId(EncryptionId):
    pass


class SyntheticDataId(GeneratedDataId):
    pass


class TechnicalStandardId(StandardId):
    pass


class ThirdPartySecurityProceduresId(SecurityProcedureId):
    pass


class TrustedComputingId(CryptographicMethodsId):
    pass


class TrustedExecutionEnvironmentId(CryptographicMethodsId):
    pass


class UncategorisedDataId(DpvDataId):
    pass


class UnstructuredDataId(DpvDataId):
    pass


class UnverifiedDataId(DpvDataId):
    pass


class UsageControlId(AccessControlMethodId):
    pass


class UseSyntheticDataId(SecurityMethodId):
    pass


class VerifiedDataId(DpvDataId):
    pass


class VirtualisationSecurityId(SecurityMethodId):
    pass


class VulnerabilityTestingMethodsId(SecurityMethodId):
    pass


class WebBrowserSecurityId(SecurityMethodId):
    pass


class WebSecurityProtocolsId(SecurityMethodId):
    pass


class WirelessSecurityProtocolsId(SecurityMethodId):
    pass


class ZeroKnowledgeAuthenticationId(AuthenticationProtocolsId):
    pass


class DpvProcessId(DpvThingId):
    pass


class DpvServiceId(DpvProcessId):
    pass


class NonPersonalDataProcessId(DpvProcessId):
    pass


class PersonalDataHandlingId(DpvProcessId):
    pass


class PersonalDataProcessId(DpvProcessId):
    pass


class ProcessingId(DpvThingId):
    pass


class CopyId(ProcessingId):
    pass


class DiscloseId(ProcessingId):
    pass


class DiscloseByTransmissionId(DiscloseId):
    pass


class DisplayId(DiscloseId):
    pass


class DisseminateId(DiscloseId):
    pass


class DownloadId(DiscloseId):
    pass


class ExportId(DiscloseId):
    pass


class MakeAvailableId(DiscloseId):
    pass


class ObtainId(ProcessingId):
    pass


class AcquireId(ObtainId):
    pass


class CollectId(ObtainId):
    pass


class DeriveId(ObtainId):
    pass


class DpvRecordId(ObtainId):
    pass


class GenerateId(ObtainId):
    pass


class InferId(DeriveId):
    pass


class ObserveId(ObtainId):
    pass


class OrganiseId(ProcessingId):
    pass


class ProcessingContextId(ContextId):
    pass


class AlgorithmicLogicId(ProcessingContextId):
    pass


class AutomationLevelId(ProcessingContextId):
    pass


class AssistiveAutomationId(AutomationLevelId):
    pass


class AutonomousId(AutomationLevelId):
    pass


class ConditionalAutomationId(AutomationLevelId):
    pass


class DataSourceId(ProcessingContextId):
    pass


class DataControllerDataSourceId(DataSourceId):
    pass


class DataSubjectDataSourceId(DataSourceId):
    pass


class DataPublishedByDataSubjectId(DataSubjectDataSourceId):
    pass


class DecisionMakingId(ProcessingContextId):
    pass


class AutomatedDecisionMakingId(DecisionMakingId):
    pass


class EntityInvolvementId(ProcessingContextId):
    pass


class ContractControlId(EntityInvolvementId):
    pass


class AcceptContractId(ContractControlId):
    pass


class NegotiateContractId(ContractControlId):
    pass


class OfferContractId(ContractControlId):
    pass


class RefuseContractId(ContractControlId):
    pass


class TerminateContractId(ContractControlId):
    pass


class EntityActiveInvolvementId(EntityInvolvementId):
    pass


class EntityIntendedInvolvementId(EntityInvolvementId):
    pass


class EntityInvolvementStatusId(EntityInvolvementId):
    pass


class EntityInvolvedId(EntityInvolvementStatusId):
    pass


class EntityNonInvolvementId(EntityInvolvementId):
    pass


class EntityNonPermissiveInvolvementId(EntityInvolvementId):
    pass


class CannotChallengeProcessId(EntityNonPermissiveInvolvementId):
    pass


class CannotChallengeProcessInputId(EntityNonPermissiveInvolvementId):
    pass


class CannotChallengeProcessOutputId(EntityNonPermissiveInvolvementId):
    pass


class CannotCorrectProcessId(EntityNonPermissiveInvolvementId):
    pass


class CannotCorrectProcessInputId(EntityNonPermissiveInvolvementId):
    pass


class CannotCorrectProcessOutputId(EntityNonPermissiveInvolvementId):
    pass


class CannotObjectToProcessId(EntityNonPermissiveInvolvementId):
    pass


class CannotOptInToProcessId(EntityNonPermissiveInvolvementId):
    pass


class CannotOptOutFromProcessId(EntityNonPermissiveInvolvementId):
    pass


class CannotReverseProcessEffectsId(EntityNonPermissiveInvolvementId):
    pass


class CannotReverseProcessInputId(EntityNonPermissiveInvolvementId):
    pass


class CannotReverseProcessOutputId(EntityNonPermissiveInvolvementId):
    pass


class CannotWithdrawFromProcessId(EntityNonPermissiveInvolvementId):
    pass


class EntityNotInvolvedId(EntityInvolvementStatusId):
    pass


class EntityPassiveInvolvementId(EntityInvolvementId):
    pass


class EntityPermissiveInvolvementId(EntityInvolvementId):
    pass


class ChallengingProcessId(EntityPermissiveInvolvementId):
    pass


class ChallengingProcessInputId(EntityPermissiveInvolvementId):
    pass


class ChallengingProcessOutputId(EntityPermissiveInvolvementId):
    pass


class CorrectingProcessId(EntityPermissiveInvolvementId):
    pass


class CorrectingProcessInputId(EntityPermissiveInvolvementId):
    pass


class CorrectingProcessOutputId(EntityPermissiveInvolvementId):
    pass


class EntityUnintendedInvolvementId(EntityInvolvementId):
    pass


class EvaluationScoringId(ProcessingContextId):
    pass


class EvaluationOfIndividualsId(EvaluationScoringId):
    pass


class FullAutomationId(AutomationLevelId):
    pass


class HighAutomationId(AutomationLevelId):
    pass


class HumanInvolvementId(EntityInvolvementId):
    pass


class HumanInvolvedId(HumanInvolvementId):
    pass


class HumanInvolvementForControlId(HumanInvolvementId):
    pass


class HumanInvolvementForDecisionId(HumanInvolvementId):
    pass


class HumanInvolvementForInputId(HumanInvolvementId):
    pass


class HumanInvolvementForInterventionId(HumanInvolvementId):
    pass


class HumanInvolvementForOversightId(HumanInvolvementId):
    pass


class HumanInvolvementForVerificationId(HumanInvolvementId):
    pass


class HumanNotInvolvedId(HumanInvolvementId):
    pass


class InnovativeUseOfTechnologyId(ProcessingContextId):
    pass


class InnovativeUseOfExistingTechnologyId(InnovativeUseOfTechnologyId):
    pass


class InnovativeUseOfNewTechnologiesId(InnovativeUseOfTechnologyId):
    pass


class NonPublicDataSourceId(DataSourceId):
    pass


class NotAutomatedId(AutomationLevelId):
    pass


class ObjectingToProcessId(EntityPermissiveInvolvementId):
    pass


class OptingInToProcessId(EntityPermissiveInvolvementId):
    pass


class OptingOutFromProcessId(EntityPermissiveInvolvementId):
    pass


class PartialAutomationId(AutomationLevelId):
    pass


class ProcessingConditionId(ProcessingContextId):
    pass


class ProcessingDurationId(DpvDurationId):
    pass


class ProcessingLocationId(DpvLocationId):
    pass


class PublicDataSourceId(DataSourceId):
    pass


class PurposeId(DpvThingId):
    pass


class AccountManagementId(PurposeId):
    pass


class CommercialPurposeId(PurposeId):
    pass


class CommercialResearchId(CommercialPurposeId):
    pass


class CommunicationManagementId(PurposeId):
    pass


class CommunicationForCustomerCareId(CommunicationManagementId):
    pass


class CustomerManagementId(PurposeId):
    pass


class CustomerCareId(CustomerManagementId):
    pass


class CustomerClaimsManagementId(CustomerManagementId):
    pass


class CustomerOrderManagementId(CustomerManagementId):
    pass


class CustomerRelationshipManagementId(CustomerManagementId):
    pass


class CustomerSolvencyMonitoringId(CustomerManagementId):
    pass


class EnforceSecurityId(PurposeId):
    pass


class EnforceAccessControlId(EnforceSecurityId):
    pass


class EstablishContractualAgreementId(PurposeId):
    pass


class FulfilmentOfObligationId(PurposeId):
    pass


class FulfilmentOfContractualObligationId(FulfilmentOfObligationId):
    pass


class HumanResourceManagementId(PurposeId):
    pass


class IdentityAuthenticationId(EnforceSecurityId):
    pass


class ImproveInternalCRMProcessesId(CustomerRelationshipManagementId):
    pass


class LegalComplianceId(FulfilmentOfObligationId):
    pass


class MarketingId(PurposeId):
    pass


class AdvertisingId(MarketingId):
    pass


class DirectMarketingId(MarketingId):
    pass


class MisusePreventionAndDetectionId(EnforceSecurityId):
    pass


class FraudPreventionAndDetectionId(MisusePreventionAndDetectionId):
    pass


class CounterMoneyLaunderingId(FraudPreventionAndDetectionId):
    pass


class MaintainFraudDatabaseId(FraudPreventionAndDetectionId):
    pass


class NonCommercialPurposeId(PurposeId):
    pass


class NonCommercialResearchId(NonCommercialPurposeId):
    pass


class OrganisationGovernanceId(PurposeId):
    pass


class DataGovernanceId(OrganisationGovernanceId):
    pass


class DataAvailabilityAssessmentId(DataGovernanceId):
    pass


class DataInteroperabilityManagementId(DataGovernanceId):
    pass


class DataInteroperabilityImprovementId(DataInteroperabilityManagementId):
    pass


class DataInventoryManagementId(DataGovernanceId):
    pass


class DataQualityManagementId(DataGovernanceId):
    pass


class DataQualityImprovementId(DataQualityManagementId):
    pass


class DataSecurityManagementId(DataGovernanceId):
    pass


class MetadataManagementId(DataGovernanceId):
    pass


class DisputeManagementId(OrganisationGovernanceId):
    pass


class MemberPartnerManagementId(OrganisationGovernanceId):
    pass


class OrganisationComplianceManagementId(OrganisationGovernanceId):
    pass


class OrganisationRiskManagementId(OrganisationGovernanceId):
    pass


class PersonalisationId(PurposeId):
    pass


class PersonalisedAdvertisingId(AdvertisingId):
    pass


class PersonnelManagementId(HumanResourceManagementId):
    pass


class PersonnelHiringId(PersonnelManagementId):
    pass


class PersonnelMonitoringId(PersonnelManagementId):
    pass


class PersonnelBehaviourMonitoringId(PersonnelMonitoringId):
    pass


class PersonnelOffboardingId(PersonnelManagementId):
    pass


class PersonnelOnboardingId(PersonnelHiringId):
    pass


class PersonnelPaymentId(PersonnelManagementId):
    pass


class PersonnelPerformanceManagementId(PersonnelManagementId):
    pass


class PersonnelPerformanceEvaluationId(PersonnelPerformanceManagementId):
    pass


class PersonnelPerformanceMonitoringId(PersonnelMonitoringId):
    pass


class PersonnelPerformancePredictionId(PersonnelPerformanceManagementId):
    pass


class PersonnelPromotionManagementId(PersonnelManagementId):
    pass


class PersonnelTerminationManagementId(PersonnelManagementId):
    pass


class PersonnelWorkloadManagementId(PersonnelManagementId):
    pass


class PoliticalCampaignId(AdvertisingId):
    pass


class ProtectionOfIPRId(FulfilmentOfObligationId):
    pass


class PublicBenefitId(PurposeId):
    pass


class CombatClimateChangeId(PublicBenefitId):
    pass


class CounterterrorismId(PublicBenefitId):
    pass


class DataAltruismId(PublicBenefitId):
    pass


class ImproveHealthcareId(PublicBenefitId):
    pass


class ImprovePublicServicesId(PublicBenefitId):
    pass


class ImproveTransportMobilityId(PublicBenefitId):
    pass


class ProtectionOfNationalSecurityId(PublicBenefitId):
    pass


class ProtectionOfPublicSecurityId(PublicBenefitId):
    pass


class ProvideOfficialStatisticsId(PublicBenefitId):
    pass


class PublicPolicyMakingId(PublicBenefitId):
    pass


class PublicRelationsId(MarketingId):
    pass


class RecordManagementId(PurposeId):
    pass


class RecruitmentAdvertisingId(AdvertisingId):
    pass


class RecruitmentManagementId(PersonnelHiringId):
    pass


class RecruitmentApplicantBackgroundCheckId(RecruitmentManagementId):
    pass


class RecruitmentApplicantCriminalBackgroundCheckId(RecruitmentManagementId):
    pass


class RecruitmentApplicantInformationAuthenticationId(RecruitmentManagementId):
    pass


class RecruitmentApplicantSelectionId(RecruitmentManagementId):
    pass


class RecruitmentApplicationManagementId(RecruitmentManagementId):
    pass


class RecruitmentApplicationAnalysisId(RecruitmentApplicationManagementId):
    pass


class RecruitmentApplicationScreeningId(RecruitmentApplicationManagementId):
    pass


class RecruitmentInterviewManagementId(RecruitmentManagementId):
    pass


class RecruitmentInterviewAnalysisId(RecruitmentInterviewManagementId):
    pass


class RecruitmentInterviewAssessmentId(RecruitmentInterviewManagementId):
    pass


class RecruitmentInterviewSchedulingId(RecruitmentInterviewManagementId):
    pass


class RecruitmentTargetedAdvertisingId(RecruitmentAdvertisingId):
    pass


class RemoveId(ProcessingId):
    pass


class DeleteId(RemoveId):
    pass


class DestructId(RemoveId):
    pass


class EraseId(RemoveId):
    pass


class ResearchAndDevelopmentId(PurposeId):
    pass


class AcademicResearchId(ResearchAndDevelopmentId):
    pass


class ReversingProcessEffectsId(EntityPermissiveInvolvementId):
    pass


class ReversingProcessInputId(EntityPermissiveInvolvementId):
    pass


class ReversingProcessOutputId(EntityPermissiveInvolvementId):
    pass


class RightsFulfilmentId(LegalObligationId):
    pass


class ScaleId(ProcessingContextId):
    pass


class DataSubjectScaleId(ScaleId):
    pass


class DataVolumeId(ScaleId):
    pass


class GeographicCoverageId(ScaleId):
    pass


class GlobalScaleId(GeographicCoverageId):
    pass


class HugeDataVolumeId(DataVolumeId):
    pass


class HugeScaleOfDataSubjectsId(DataSubjectScaleId):
    pass


class LargeDataVolumeId(DataVolumeId):
    pass


class LargeScaleOfDataSubjectsId(DataSubjectScaleId):
    pass


class LocalEnvironmentScaleId(GeographicCoverageId):
    pass


class LocalityScaleId(GeographicCoverageId):
    pass


class MediumDataVolumeId(DataVolumeId):
    pass


class MediumScaleOfDataSubjectsId(DataSubjectScaleId):
    pass


class MultiNationalScaleId(GeographicCoverageId):
    pass


class NationalScaleId(GeographicCoverageId):
    pass


class NearlyGlobalScaleId(GeographicCoverageId):
    pass


class ProcessingScaleId(ScaleId):
    pass


class LargeScaleProcessingId(ProcessingScaleId):
    pass


class MediumScaleProcessingId(ProcessingScaleId):
    pass


class RegionalScaleId(GeographicCoverageId):
    pass


class ScientificResearchId(ResearchAndDevelopmentId):
    pass


class ScoringOfIndividualsId(EvaluationScoringId):
    pass


class AutomatedScoringOfIndividualsId(ScoringOfIndividualsId):
    pass


class SectorId(DpvThingId):
    pass


class ServiceManagementId(PurposeId):
    pass


class PaymentManagementId(ServiceManagementId):
    pass


class RepairImpairmentsId(ServiceManagementId):
    pass


class ServiceAccessDeterminationId(ServiceManagementId):
    pass


class ServiceMonitoringId(ServiceManagementId):
    pass


class ServiceOptimisationId(ServiceManagementId):
    pass


class OptimisationForConsumerId(ServiceOptimisationId):
    pass


class OptimisationForControllerId(ServiceOptimisationId):
    pass


class ImproveExistingProductsAndServicesId(OptimisationForControllerId):
    pass


class IncreaseServiceRobustnessId(OptimisationForControllerId):
    pass


class InternalResourceOptimisationId(OptimisationForControllerId):
    pass


class OptimiseUserInterfaceId(OptimisationForConsumerId):
    pass


class ServicePersonalisationId(PersonalisationId):
    pass


class PersonalisedBenefitsId(ServicePersonalisationId):
    pass


class ProvidePersonalisedRecommendationsId(ServicePersonalisationId):
    pass


class ProvideEventRecommendationsId(ProvidePersonalisedRecommendationsId):
    pass


class ProvideProductRecommendationsId(ProvidePersonalisedRecommendationsId):
    pass


class ServiceProvisionId(ServiceManagementId):
    pass


class RequestedServiceProvisionId(ServiceProvisionId):
    pass


class DeliveryOfGoodsId(RequestedServiceProvisionId):
    pass


class SearchFunctionalitiesId(ServiceProvisionId):
    pass


class SellProductsId(ServiceProvisionId):
    pass


class SellDataToThirdPartiesId(SellProductsId):
    pass


class SellInsightsFromDataId(SellProductsId):
    pass


class SellProductsToDataSubjectId(SellProductsId):
    pass


class ServiceRegistrationId(ServiceManagementId):
    pass


class ServiceUsageAnalyticsId(ServiceMonitoringId):
    pass


class ShareId(DiscloseId):
    pass


class SingularDataVolumeId(DataVolumeId):
    pass


class SingularScaleOfDataSubjectsId(DataSubjectScaleId):
    pass


class SmallDataVolumeId(DataVolumeId):
    pass


class SmallScaleOfDataSubjectsId(DataSubjectScaleId):
    pass


class SmallScaleProcessingId(ProcessingScaleId):
    pass


class SocialMediaMarketingId(MarketingId):
    pass


class SporadicDataVolumeId(DataVolumeId):
    pass


class SporadicScaleOfDataSubjectsId(DataSubjectScaleId):
    pass


class StorageConditionId(ProcessingConditionId):
    pass


class StorageDeletionId(StorageConditionId):
    pass


class StorageDurationId(ProcessingDurationId):
    pass


class StorageLocationId(ProcessingLocationId):
    pass


class StorageRestorationId(StorageConditionId):
    pass


class StoreId(ProcessingId):
    pass


class StructureId(OrganiseId):
    pass


class FormatId(StructureId):
    pass


class ReformatId(FormatId):
    pass


class SystematicMonitoringId(ProcessingContextId):
    pass


class TargetedAdvertisingId(PersonalisedAdvertisingId):
    pass


class TechnicalServiceProvisionId(ServiceProvisionId):
    pass


class TechnologyId(DpvThingId):
    pass


class ThirdPartyDataSourceId(DataSourceId):
    pass


class TransferId(ProcessingId):
    pass


class CrossBorderTransferId(TransferId):
    pass


class MoveId(TransferId):
    pass


class TransformId(ProcessingId):
    pass


class AdaptId(TransformId):
    pass


class AlignId(TransformId):
    pass


class AlterId(TransformId):
    pass


class AggregateId(AlterId):
    pass


class AnonymiseId(TransformId):
    pass


class CombineId(TransformId):
    pass


class FilterId(TransformId):
    pass


class ModifyId(AlterId):
    pass


class PseudonymiseId(TransformId):
    pass


class RestrictId(TransformId):
    pass


class ScreenId(TransformId):
    pass


class TransmitId(DiscloseId):
    pass


class UseId(ProcessingId):
    pass


class AccessId(UseId):
    pass


class AnalyseId(UseId):
    pass


class AssessId(UseId):
    pass


class ConsultId(UseId):
    pass


class MatchId(UseId):
    pass


class MonitorId(ConsultId):
    pass


class ProfilingId(UseId):
    pass


class QueryId(ConsultId):
    pass


class RetrieveId(UseId):
    pass


class TrackingId(UseId):
    pass


class TrackingByFirstPartyId(TrackingId):
    pass


class TrackingByThirdPartyId(TrackingId):
    pass


class UserInterfacePersonalisationId(ServicePersonalisationId):
    pass


class VendorManagementId(PurposeId):
    pass


class VendorPaymentId(VendorManagementId):
    pass


class VendorRecordsManagementId(VendorManagementId):
    pass


class VendorSelectionAssessmentId(VendorManagementId):
    pass


class VerificationId(EnforceSecurityId):
    pass


class AgeVerificationId(VerificationId):
    pass


class IdentityVerificationId(VerificationId):
    pass


class WithdrawingFromProcessId(EntityPermissiveInvolvementId):
    pass


class LikelihoodId(DpvThingId):
    pass


class NoticeId(OrganisationalMeasureId):
    pass


class AINoticeId(NoticeId):
    pass


class DashboardNoticeId(NoticeId):
    pass


class DataTransferNoticeId(NoticeId):
    pass


class DeviceNoticeId(NoticeId):
    pass


class GraphicalNoticeId(NoticeId):
    pass


class JITNoticeId(NoticeId):
    pass


class LayeredNoticeId(NoticeId):
    pass


class NoticeIconId(DpvThingId):
    pass


class NoticeLayerId(DpvThingId):
    pass


class NoticeStatusId(StatusId):
    pass


class NoticeCommunicatedId(NoticeStatusId):
    pass


class NoticeGeneratedId(NoticeStatusId):
    pass


class NoticeLatestId(NoticeStatusId):
    pass


class NoticeStaleId(NoticeStatusId):
    pass


class NoticeUnusedId(NoticeStatusId):
    pass


class NoticeUpdatedId(NoticeStatusId):
    pass


class NoticeUsedId(NoticeStatusId):
    pass


class OralNoticeId(NoticeId):
    pass


class PostedNoticeId(NoticeId):
    pass


class PrintedNoticeId(NoticeId):
    pass


class PrivacyNoticeId(NoticeId):
    pass


class ConsentNoticeId(PrivacyNoticeId):
    pass


class RiskAssessmentId(AssessmentId):
    pass


class ImpactAssessmentId(RiskAssessmentId):
    pass


class ReviewImpactAssessmentId(ImpactAssessmentId):
    pass


class DataTransferImpactAssessmentId(ImpactAssessmentId):
    pass


class PIAId(ImpactAssessmentId):
    pass


class RightsImpactAssessmentId(ImpactAssessmentId):
    pass


class DPIAId(RightsImpactAssessmentId):
    pass


class DataBreachImpactAssessmentId(RightsImpactAssessmentId):
    pass


class FRIAId(RightsImpactAssessmentId):
    pass


class RiskConceptId(DpvThingId):
    pass


class ConsequenceId(RiskConceptId):
    pass


class ConsequenceAsSideEffectId(ConsequenceId):
    pass


class ConsequenceOfFailureId(ConsequenceId):
    pass


class ConsequenceOfSuccessId(ConsequenceId):
    pass


class ImpactId(ConsequenceId):
    pass


class RiskId(RiskConceptId):
    pass


class ResidualRiskId(RiskId):
    pass


class RiskLevelId(DpvThingId):
    pass


class RiskMitigationMeasureId(TechnicalOrganisationalMeasureId):
    pass


class SecurityAssessmentId(RiskAssessmentId):
    pass


class CybersecurityAssessmentId(SecurityAssessmentId):
    pass


class SecurityIncidentNoticeId(NoticeId):
    pass


class DataBreachNoticeId(SecurityIncidentNoticeId):
    pass


class SeverityId(DpvThingId):
    pass


class SensitivityLevelId(SeverityId):
    pass


class RightId(DpvThingId):
    pass


class ActiveRightId(RightId):
    pass


class DataSubjectRightId(RightId):
    pass


class PassiveRightId(RightId):
    pass


class RightExerciseActivityId(OrganisationalMeasureId):
    pass


class RightExerciseRecordId(RecordsOfActivitiesId):
    pass


class RightNoticeId(NoticeId):
    pass


class RightExerciseNoticeId(RightNoticeId):
    pass


class RightFulfilmentNoticeId(RightExerciseNoticeId):
    pass


class RightNonFulfilmentNoticeId(RightExerciseNoticeId):
    pass


class ConsentControlId(EntityInvolvementId):
    pass


class ConsentStatusId(StatusId):
    pass


class ConsentStatusInvalidForProcessingId(ConsentStatusId):
    pass


class ConsentExpiredId(ConsentStatusInvalidForProcessingId):
    pass


class ConsentInvalidatedId(ConsentStatusInvalidForProcessingId):
    pass


class ConsentRefusedId(ConsentStatusInvalidForProcessingId):
    pass


class ConsentRequestDeferredId(ConsentStatusInvalidForProcessingId):
    pass


class ConsentRequestedId(ConsentStatusInvalidForProcessingId):
    pass


class ConsentRevokedId(ConsentStatusInvalidForProcessingId):
    pass


class ConsentStatusValidForProcessingId(ConsentStatusId):
    pass


class ConsentGivenId(ConsentStatusValidForProcessingId):
    pass


class ConsentUnknownId(ConsentStatusInvalidForProcessingId):
    pass


class ConsentWithdrawnId(ConsentStatusInvalidForProcessingId):
    pass


class InformedConsentId(ConsentId):
    pass


class ExpressedConsentId(InformedConsentId):
    pass


class ExplicitlyExpressedConsentId(ExpressedConsentId):
    pass


class ImpliedConsentId(InformedConsentId):
    pass


class ObtainConsentId(ConsentControlId):
    pass


class ProvideConsentId(ConsentControlId):
    pass


class ManageConsentId(ProvideConsentId):
    pass


class ReaffirmConsentId(ConsentControlId):
    pass


class RefuseConsentId(ConsentControlId):
    pass


class RenewedConsentGivenId(ConsentStatusValidForProcessingId):
    pass


class UninformedConsentId(ConsentId):
    pass


class WithdrawConsentId(ConsentControlId):
    pass


@dataclass(repr=False)
class DpvThing(YAMLRoot):
    """
    Abstract base class for every DPV entity. Provides a uniform ``id``
    identifier slot. Does NOT enumerate DPV properties: the upstream OWL
    declares no ``rdfs:domain`` triples, so any DPV property is semantically
    applicable to any DPV class (open-world). Generators that need a
    closed-world property list per class should consume the W3C DPV OWL
    release directly rather than this LinkML projection.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DpvThing"]
    class_class_curie: ClassVar[str] = "dpv:DpvThing"
    class_name: ClassVar[str] = "DpvThing"
    class_model_uri: ClassVar[URIRef] = DPV.DpvThing

    id: Union[str, DpvThingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvThingId):
            self.id = DpvThingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Context(DpvThing):
    """
    Contextually relevant information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Context"]
    class_class_curie: ClassVar[str] = "dpv:Context"
    class_name: ClassVar[str] = "Context"
    class_model_uri: ClassVar[URIRef] = DPV.Context

    id: Union[str, ContextId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContextId):
            self.id = ContextId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Applicability(Context):
    """
    Concept provided to represent indication of cases where the information
    or context is not applicable (N/A) or not available or this is not known
    or determined yet. If the information is applicable and available, this
    concept should not be used.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Applicability"]
    class_class_curie: ClassVar[str] = "dpv:Applicability"
    class_name: ClassVar[str] = "Applicability"
    class_model_uri: ClassVar[URIRef] = DPV.Applicability

    id: Union[str, ApplicabilityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ApplicabilityId):
            self.id = ApplicabilityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDuration(Context):
    """
    The duration or temporal limitation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Duration"]
    class_class_curie: ClassVar[str] = "dpv:Duration"
    class_name: ClassVar[str] = "DpvDuration"
    class_model_uri: ClassVar[URIRef] = DPV.DpvDuration

    id: Union[str, DpvDurationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDurationId):
            self.id = DpvDurationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EndlessDuration(DpvDuration):
    """
    Duration that is (known or intended to be) open ended or without an end
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EndlessDuration"]
    class_class_curie: ClassVar[str] = "dpv:EndlessDuration"
    class_name: ClassVar[str] = "EndlessDuration"
    class_model_uri: ClassVar[URIRef] = DPV.EndlessDuration

    id: Union[str, EndlessDurationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EndlessDurationId):
            self.id = EndlessDurationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExpectationStatus(DpvThing):
    """
    Status indicating whether the specified context was intended or
    unintended
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ExpectationStatus"]
    class_class_curie: ClassVar[str] = "dpv:ExpectationStatus"
    class_name: ClassVar[str] = "ExpectationStatus"
    class_model_uri: ClassVar[URIRef] = DPV.ExpectationStatus

    id: Union[str, ExpectationStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExpectationStatusId):
            self.id = ExpectationStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Expected(ExpectationStatus):
    """
    Status indicating the specified context was expected
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Expected"]
    class_class_curie: ClassVar[str] = "dpv:Expected"
    class_name: ClassVar[str] = "Expected"
    class_model_uri: ClassVar[URIRef] = DPV.Expected

    id: Union[str, ExpectedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExpectedId):
            self.id = ExpectedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FeeRequirement(Context):
    """
    Concept indicating whether a fee is required
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FeeRequirement"]
    class_class_curie: ClassVar[str] = "dpv:FeeRequirement"
    class_name: ClassVar[str] = "FeeRequirement"
    class_model_uri: ClassVar[URIRef] = DPV.FeeRequirement

    id: Union[str, FeeRequirementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FeeRequirementId):
            self.id = FeeRequirementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FeeNotRequired(FeeRequirement):
    """
    Concept indicating a fee is not required. This is distinct from a Fee of
    zero as it indicates a fee is not applicable in the context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FeeNotRequired"]
    class_class_curie: ClassVar[str] = "dpv:FeeNotRequired"
    class_name: ClassVar[str] = "FeeNotRequired"
    class_model_uri: ClassVar[URIRef] = DPV.FeeNotRequired

    id: Union[str, FeeNotRequiredId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FeeNotRequiredId):
            self.id = FeeNotRequiredId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FeeRequired(FeeRequirement):
    """
    Concept indicating a fee is required. The value of the fee should be
    specified using rdf:value or an another relevant means
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FeeRequired"]
    class_class_curie: ClassVar[str] = "dpv:FeeRequired"
    class_name: ClassVar[str] = "FeeRequired"
    class_model_uri: ClassVar[URIRef] = DPV.FeeRequired

    id: Union[str, FeeRequiredId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FeeRequiredId):
            self.id = FeeRequiredId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixedOccurrencesDuration(DpvDuration):
    """
    Duration that takes place a fixed number of times e.g. 3 times
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FixedOccurrencesDuration"]
    class_class_curie: ClassVar[str] = "dpv:FixedOccurrencesDuration"
    class_name: ClassVar[str] = "FixedOccurrencesDuration"
    class_model_uri: ClassVar[URIRef] = DPV.FixedOccurrencesDuration

    id: Union[str, FixedOccurrencesDurationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FixedOccurrencesDurationId):
            self.id = FixedOccurrencesDurationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Frequency(Context):
    """
    The frequency or information about periods and repetitions in terms of
    recurrence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Frequency"]
    class_class_curie: ClassVar[str] = "dpv:Frequency"
    class_name: ClassVar[str] = "Frequency"
    class_model_uri: ClassVar[URIRef] = DPV.Frequency

    id: Union[str, FrequencyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FrequencyId):
            self.id = FrequencyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContinuousFrequency(Frequency):
    """
    Frequency where occurrences are continuous
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContinuousFrequency"]
    class_class_curie: ClassVar[str] = "dpv:ContinuousFrequency"
    class_name: ClassVar[str] = "ContinuousFrequency"
    class_model_uri: ClassVar[URIRef] = DPV.ContinuousFrequency

    id: Union[str, ContinuousFrequencyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContinuousFrequencyId):
            self.id = ContinuousFrequencyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Importance(Context):
    """
    An indication of 'importance' within a context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Importance"]
    class_class_curie: ClassVar[str] = "dpv:Importance"
    class_name: ClassVar[str] = "Importance"
    class_model_uri: ClassVar[URIRef] = DPV.Importance

    id: Union[str, ImportanceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImportanceId):
            self.id = ImportanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IndeterminateDuration(DpvDuration):
    """
    Duration that is indeterminate or cannot be determined
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["IndeterminateDuration"]
    class_class_curie: ClassVar[str] = "dpv:IndeterminateDuration"
    class_name: ClassVar[str] = "IndeterminateDuration"
    class_model_uri: ClassVar[URIRef] = DPV.IndeterminateDuration

    id: Union[str, IndeterminateDurationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IndeterminateDurationId):
            self.id = IndeterminateDurationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Justification(Context):
    """
    A form of documentation providing reasons, explanations, or
    justifications
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Justification"]
    class_class_curie: ClassVar[str] = "dpv:Justification"
    class_name: ClassVar[str] = "Justification"
    class_model_uri: ClassVar[URIRef] = DPV.Justification

    id: Union[str, JustificationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, JustificationId):
            self.id = JustificationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Necessity(Context):
    """
    An indication of 'necessity' within a context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Necessity"]
    class_class_curie: ClassVar[str] = "dpv:Necessity"
    class_name: ClassVar[str] = "Necessity"
    class_model_uri: ClassVar[URIRef] = DPV.Necessity

    id: Union[str, NecessityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NecessityId):
            self.id = NecessityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvOptional(Necessity):
    """
    Indication of 'optional' or 'voluntary'
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Optional"]
    class_class_curie: ClassVar[str] = "dpv:Optional"
    class_name: ClassVar[str] = "DpvOptional"
    class_model_uri: ClassVar[URIRef] = DPV.DpvOptional

    id: Union[str, DpvOptionalId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvOptionalId):
            self.id = DpvOptionalId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotApplicable(Applicability):
    """
    Concept indicating the information or context is not applicable
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NotApplicable"]
    class_class_curie: ClassVar[str] = "dpv:NotApplicable"
    class_name: ClassVar[str] = "NotApplicable"
    class_model_uri: ClassVar[URIRef] = DPV.NotApplicable

    id: Union[str, NotApplicableId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotApplicableId):
            self.id = NotApplicableId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotAvailable(Applicability):
    """
    Concept indicating the information or context is applicable but
    information is not yet available
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NotAvailable"]
    class_class_curie: ClassVar[str] = "dpv:NotAvailable"
    class_name: ClassVar[str] = "NotAvailable"
    class_model_uri: ClassVar[URIRef] = DPV.NotAvailable

    id: Union[str, NotAvailableId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotAvailableId):
            self.id = NotAvailableId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotRequired(Necessity):
    """
    Indication of neither being required nor optional i.e. not relevant or
    needed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NotRequired"]
    class_class_curie: ClassVar[str] = "dpv:NotRequired"
    class_name: ClassVar[str] = "NotRequired"
    class_model_uri: ClassVar[URIRef] = DPV.NotRequired

    id: Union[str, NotRequiredId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotRequiredId):
            self.id = NotRequiredId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OftenFrequency(Frequency):
    """
    Frequency where occurrences are often or frequent, but not continuous
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OftenFrequency"]
    class_class_curie: ClassVar[str] = "dpv:OftenFrequency"
    class_name: ClassVar[str] = "OftenFrequency"
    class_model_uri: ClassVar[URIRef] = DPV.OftenFrequency

    id: Union[str, OftenFrequencyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OftenFrequencyId):
            self.id = OftenFrequencyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrimaryImportance(Importance):
    """
    Indication of 'primary' or 'main' or 'core' importance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PrimaryImportance"]
    class_class_curie: ClassVar[str] = "dpv:PrimaryImportance"
    class_name: ClassVar[str] = "PrimaryImportance"
    class_model_uri: ClassVar[URIRef] = DPV.PrimaryImportance

    id: Union[str, PrimaryImportanceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrimaryImportanceId):
            self.id = PrimaryImportanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Required(Necessity):
    """
    Indication of 'required' or 'necessary'
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Required"]
    class_class_curie: ClassVar[str] = "dpv:Required"
    class_name: ClassVar[str] = "Required"
    class_model_uri: ClassVar[URIRef] = DPV.Required

    id: Union[str, RequiredId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RequiredId):
            self.id = RequiredId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Rule(DpvThing):
    """
    A rule describing a process or control that directs or determines if and
    how an activity should be conducted
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Rule"]
    class_class_curie: ClassVar[str] = "dpv:Rule"
    class_name: ClassVar[str] = "Rule"
    class_model_uri: ClassVar[URIRef] = DPV.Rule

    id: Union[str, RuleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RuleId):
            self.id = RuleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AcceptableRule(Rule):
    """
    A rule that is acceptable where it is either desirable if it occurs or
    it is not unacceptable if it does
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AcceptableRule"]
    class_class_curie: ClassVar[str] = "dpv:AcceptableRule"
    class_name: ClassVar[str] = "AcceptableRule"
    class_model_uri: ClassVar[URIRef] = DPV.AcceptableRule

    id: Union[str, AcceptableRuleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcceptableRuleId):
            self.id = AcceptableRuleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Obligation(AcceptableRule):
    """
    A rule describing an obligation for performing an activity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Obligation"]
    class_class_curie: ClassVar[str] = "dpv:Obligation"
    class_name: ClassVar[str] = "Obligation"
    class_model_uri: ClassVar[URIRef] = DPV.Obligation

    id: Union[str, ObligationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObligationId):
            self.id = ObligationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Permission(AcceptableRule):
    """
    A rule describing a permission to perform an activity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Permission"]
    class_class_curie: ClassVar[str] = "dpv:Permission"
    class_name: ClassVar[str] = "Permission"
    class_model_uri: ClassVar[URIRef] = DPV.Permission

    id: Union[str, PermissionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PermissionId):
            self.id = PermissionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Recommendation(AcceptableRule):
    """
    A rule describing a recommendation for performing an activity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Recommendation"]
    class_class_curie: ClassVar[str] = "dpv:Recommendation"
    class_name: ClassVar[str] = "Recommendation"
    class_model_uri: ClassVar[URIRef] = DPV.Recommendation

    id: Union[str, RecommendationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecommendationId):
            self.id = RecommendationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Scope(Context):
    """
    Indication of the extent or range or boundaries associated with(in) a
    context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Scope"]
    class_class_curie: ClassVar[str] = "dpv:Scope"
    class_name: ClassVar[str] = "Scope"
    class_model_uri: ClassVar[URIRef] = DPV.Scope

    id: Union[str, ScopeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScopeId):
            self.id = ScopeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecondaryImportance(Importance):
    """
    Indication of 'secondary' or 'minor' or 'auxiliary' importance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SecondaryImportance"]
    class_class_curie: ClassVar[str] = "dpv:SecondaryImportance"
    class_name: ClassVar[str] = "SecondaryImportance"
    class_model_uri: ClassVar[URIRef] = DPV.SecondaryImportance

    id: Union[str, SecondaryImportanceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecondaryImportanceId):
            self.id = SecondaryImportanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SingularFrequency(Frequency):
    """
    Frequency where occurrences are singular i.e. they take place only once
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SingularFrequency"]
    class_class_curie: ClassVar[str] = "dpv:SingularFrequency"
    class_name: ClassVar[str] = "SingularFrequency"
    class_model_uri: ClassVar[URIRef] = DPV.SingularFrequency

    id: Union[str, SingularFrequencyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SingularFrequencyId):
            self.id = SingularFrequencyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SporadicFrequency(Frequency):
    """
    Frequency where occurrences are sporadic or infrequent or sparse
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SporadicFrequency"]
    class_class_curie: ClassVar[str] = "dpv:SporadicFrequency"
    class_name: ClassVar[str] = "SporadicFrequency"
    class_model_uri: ClassVar[URIRef] = DPV.SporadicFrequency

    id: Union[str, SporadicFrequencyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SporadicFrequencyId):
            self.id = SporadicFrequencyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Status(Context):
    """
    The status or state of something
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Status"]
    class_class_curie: ClassVar[str] = "dpv:Status"
    class_name: ClassVar[str] = "Status"
    class_model_uri: ClassVar[URIRef] = DPV.Status

    id: Union[str, StatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StatusId):
            self.id = StatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActivityStatus(Status):
    """
    Status associated with activity operations and lifecycles
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ActivityStatus"]
    class_class_curie: ClassVar[str] = "dpv:ActivityStatus"
    class_name: ClassVar[str] = "ActivityStatus"
    class_model_uri: ClassVar[URIRef] = DPV.ActivityStatus

    id: Union[str, ActivityStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityStatusId):
            self.id = ActivityStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActivityCompleted(ActivityStatus):
    """
    State of an activity that has completed i.e. is fully in the past
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ActivityCompleted"]
    class_class_curie: ClassVar[str] = "dpv:ActivityCompleted"
    class_name: ClassVar[str] = "ActivityCompleted"
    class_model_uri: ClassVar[URIRef] = DPV.ActivityCompleted

    id: Union[str, ActivityCompletedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityCompletedId):
            self.id = ActivityCompletedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActivityHalted(ActivityStatus):
    """
    State of an activity that was occurring in the past, and has been halted
    or paused or stopped
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ActivityHalted"]
    class_class_curie: ClassVar[str] = "dpv:ActivityHalted"
    class_name: ClassVar[str] = "ActivityHalted"
    class_model_uri: ClassVar[URIRef] = DPV.ActivityHalted

    id: Union[str, ActivityHaltedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityHaltedId):
            self.id = ActivityHaltedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActivityNotCompleted(ActivityStatus):
    """
    State of an activity that could not be completed, but has reached some
    end state
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ActivityNotCompleted"]
    class_class_curie: ClassVar[str] = "dpv:ActivityNotCompleted"
    class_name: ClassVar[str] = "ActivityNotCompleted"
    class_model_uri: ClassVar[URIRef] = DPV.ActivityNotCompleted

    id: Union[str, ActivityNotCompletedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityNotCompletedId):
            self.id = ActivityNotCompletedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActivityOngoing(ActivityStatus):
    """
    State of an activity occurring in continuation i.e. currently ongoing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ActivityOngoing"]
    class_class_curie: ClassVar[str] = "dpv:ActivityOngoing"
    class_name: ClassVar[str] = "ActivityOngoing"
    class_model_uri: ClassVar[URIRef] = DPV.ActivityOngoing

    id: Union[str, ActivityOngoingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityOngoingId):
            self.id = ActivityOngoingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActivityPlanned(ActivityStatus):
    """
    State of an activity being planned with concrete plans for
    implementation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ActivityPlanned"]
    class_class_curie: ClassVar[str] = "dpv:ActivityPlanned"
    class_name: ClassVar[str] = "ActivityPlanned"
    class_model_uri: ClassVar[URIRef] = DPV.ActivityPlanned

    id: Union[str, ActivityPlannedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityPlannedId):
            self.id = ActivityPlannedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActivityProposed(ActivityStatus):
    """
    State of an activity being proposed without any concrete plans for
    implementation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ActivityProposed"]
    class_class_curie: ClassVar[str] = "dpv:ActivityProposed"
    class_name: ClassVar[str] = "ActivityProposed"
    class_model_uri: ClassVar[URIRef] = DPV.ActivityProposed

    id: Union[str, ActivityProposedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityProposedId):
            self.id = ActivityProposedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuditStatus(Status):
    """
    Status associated with Auditing or Investigation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AuditStatus"]
    class_class_curie: ClassVar[str] = "dpv:AuditStatus"
    class_name: ClassVar[str] = "AuditStatus"
    class_model_uri: ClassVar[URIRef] = DPV.AuditStatus

    id: Union[str, AuditStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuditStatusId):
            self.id = AuditStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuditApproved(AuditStatus):
    """
    State of being approved through the audit
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AuditApproved"]
    class_class_curie: ClassVar[str] = "dpv:AuditApproved"
    class_name: ClassVar[str] = "AuditApproved"
    class_model_uri: ClassVar[URIRef] = DPV.AuditApproved

    id: Union[str, AuditApprovedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuditApprovedId):
            self.id = AuditApprovedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuditConditionallyApproved(AuditStatus):
    """
    State of being conditionally approved through the audit
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AuditConditionallyApproved"]
    class_class_curie: ClassVar[str] = "dpv:AuditConditionallyApproved"
    class_name: ClassVar[str] = "AuditConditionallyApproved"
    class_model_uri: ClassVar[URIRef] = DPV.AuditConditionallyApproved

    id: Union[str, AuditConditionallyApprovedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuditConditionallyApprovedId):
            self.id = AuditConditionallyApprovedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuditNotRequired(AuditStatus):
    """
    State where an audit is determined as not being required
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AuditNotRequired"]
    class_class_curie: ClassVar[str] = "dpv:AuditNotRequired"
    class_name: ClassVar[str] = "AuditNotRequired"
    class_model_uri: ClassVar[URIRef] = DPV.AuditNotRequired

    id: Union[str, AuditNotRequiredId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuditNotRequiredId):
            self.id = AuditNotRequiredId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuditRejected(AuditStatus):
    """
    State of not being approved or being rejected through the audit
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AuditRejected"]
    class_class_curie: ClassVar[str] = "dpv:AuditRejected"
    class_name: ClassVar[str] = "AuditRejected"
    class_model_uri: ClassVar[URIRef] = DPV.AuditRejected

    id: Union[str, AuditRejectedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuditRejectedId):
            self.id = AuditRejectedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuditRequested(AuditStatus):
    """
    State of an audit being requested whose outcome is not yet known
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AuditRequested"]
    class_class_curie: ClassVar[str] = "dpv:AuditRequested"
    class_name: ClassVar[str] = "AuditRequested"
    class_model_uri: ClassVar[URIRef] = DPV.AuditRequested

    id: Union[str, AuditRequestedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuditRequestedId):
            self.id = AuditRequestedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuditRequired(AuditStatus):
    """
    State where an audit is determined as being required but has not been
    conducted
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AuditRequired"]
    class_class_curie: ClassVar[str] = "dpv:AuditRequired"
    class_name: ClassVar[str] = "AuditRequired"
    class_model_uri: ClassVar[URIRef] = DPV.AuditRequired

    id: Union[str, AuditRequiredId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuditRequiredId):
            self.id = AuditRequiredId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComplianceStatus(Status):
    """
    Status associated with Compliance with some norms, objectives, or
    requirements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ComplianceStatus"]
    class_class_curie: ClassVar[str] = "dpv:ComplianceStatus"
    class_name: ClassVar[str] = "ComplianceStatus"
    class_model_uri: ClassVar[URIRef] = DPV.ComplianceStatus

    id: Union[str, ComplianceStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComplianceStatusId):
            self.id = ComplianceStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComplianceIndeterminate(ComplianceStatus):
    """
    State where the status of compliance has not been fully assessed,
    evaluated, or determined
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ComplianceIndeterminate"]
    class_class_curie: ClassVar[str] = "dpv:ComplianceIndeterminate"
    class_name: ClassVar[str] = "ComplianceIndeterminate"
    class_model_uri: ClassVar[URIRef] = DPV.ComplianceIndeterminate

    id: Union[str, ComplianceIndeterminateId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComplianceIndeterminateId):
            self.id = ComplianceIndeterminateId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComplianceUnknown(ComplianceStatus):
    """
    State where the status of compliance is unknown
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ComplianceUnknown"]
    class_class_curie: ClassVar[str] = "dpv:ComplianceUnknown"
    class_name: ClassVar[str] = "ComplianceUnknown"
    class_model_uri: ClassVar[URIRef] = DPV.ComplianceUnknown

    id: Union[str, ComplianceUnknownId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComplianceUnknownId):
            self.id = ComplianceUnknownId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComplianceViolation(ComplianceStatus):
    """
    State where compliance cannot be achieved due to requirements being
    violated
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ComplianceViolation"]
    class_class_curie: ClassVar[str] = "dpv:ComplianceViolation"
    class_name: ClassVar[str] = "ComplianceViolation"
    class_model_uri: ClassVar[URIRef] = DPV.ComplianceViolation

    id: Union[str, ComplianceViolationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComplianceViolationId):
            self.id = ComplianceViolationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Compliant(ComplianceStatus):
    """
    State of being fully compliant
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Compliant"]
    class_class_curie: ClassVar[str] = "dpv:Compliant"
    class_name: ClassVar[str] = "Compliant"
    class_model_uri: ClassVar[URIRef] = DPV.Compliant

    id: Union[str, CompliantId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompliantId):
            self.id = CompliantId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConformanceStatus(Status):
    """
    Status associated with conformance to a standard, guideline, code, or
    recommendation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConformanceStatus"]
    class_class_curie: ClassVar[str] = "dpv:ConformanceStatus"
    class_name: ClassVar[str] = "ConformanceStatus"
    class_model_uri: ClassVar[URIRef] = DPV.ConformanceStatus

    id: Union[str, ConformanceStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConformanceStatusId):
            self.id = ConformanceStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Conformant(ConformanceStatus):
    """
    State of being conformant
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Conformant"]
    class_class_curie: ClassVar[str] = "dpv:Conformant"
    class_name: ClassVar[str] = "Conformant"
    class_model_uri: ClassVar[URIRef] = DPV.Conformant

    id: Union[str, ConformantId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConformantId):
            self.id = ConformantId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityInformedStatus(Status):
    """
    Status indicating whether an entity is informed or uninformed about
    specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityInformedStatus"]
    class_class_curie: ClassVar[str] = "dpv:EntityInformedStatus"
    class_name: ClassVar[str] = "EntityInformedStatus"
    class_model_uri: ClassVar[URIRef] = DPV.EntityInformedStatus

    id: Union[str, EntityInformedStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityInformedStatusId):
            self.id = EntityInformedStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityInformed(EntityInformedStatus):
    """
    Status indicating entity has been informed about specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityInformed"]
    class_class_curie: ClassVar[str] = "dpv:EntityInformed"
    class_name: ClassVar[str] = "EntityInformed"
    class_model_uri: ClassVar[URIRef] = DPV.EntityInformed

    id: Union[str, EntityInformedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityInformedId):
            self.id = EntityInformedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuthorityInformed(EntityInformed):
    """
    Status indicating Authority has been informed about the specified
    context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AuthorityInformed"]
    class_class_curie: ClassVar[str] = "dpv:AuthorityInformed"
    class_name: ClassVar[str] = "AuthorityInformed"
    class_model_uri: ClassVar[URIRef] = DPV.AuthorityInformed

    id: Union[str, AuthorityInformedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuthorityInformedId):
            self.id = AuthorityInformedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControllerInformed(EntityInformed):
    """
    Status indicating Controller has been informed about the specified
    context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ControllerInformed"]
    class_class_curie: ClassVar[str] = "dpv:ControllerInformed"
    class_name: ClassVar[str] = "ControllerInformed"
    class_model_uri: ClassVar[URIRef] = DPV.ControllerInformed

    id: Union[str, ControllerInformedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControllerInformedId):
            self.id = ControllerInformedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSubjectInformed(EntityInformed):
    """
    Status indicating DataSubject has been informed about the specified
    context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSubjectInformed"]
    class_class_curie: ClassVar[str] = "dpv:DataSubjectInformed"
    class_name: ClassVar[str] = "DataSubjectInformed"
    class_model_uri: ClassVar[URIRef] = DPV.DataSubjectInformed

    id: Union[str, DataSubjectInformedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSubjectInformedId):
            self.id = DataSubjectInformedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityUninformed(EntityInformedStatus):
    """
    Status indicating entity is uninformed i.e. has been not been informed
    about specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityUninformed"]
    class_class_curie: ClassVar[str] = "dpv:EntityUninformed"
    class_name: ClassVar[str] = "EntityUninformed"
    class_model_uri: ClassVar[URIRef] = DPV.EntityUninformed

    id: Union[str, EntityUninformedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityUninformedId):
            self.id = EntityUninformedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuthorityUninformed(EntityUninformed):
    """
    Status indicating Authority is uninformed i.e. has not been informed
    about the specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AuthorityUninformed"]
    class_class_curie: ClassVar[str] = "dpv:AuthorityUninformed"
    class_name: ClassVar[str] = "AuthorityUninformed"
    class_model_uri: ClassVar[URIRef] = DPV.AuthorityUninformed

    id: Union[str, AuthorityUninformedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuthorityUninformedId):
            self.id = AuthorityUninformedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControllerUninformed(EntityUninformed):
    """
    Status indicating Controller is uninformed i.e. has not been informed
    about the specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ControllerUninformed"]
    class_class_curie: ClassVar[str] = "dpv:ControllerUninformed"
    class_name: ClassVar[str] = "ControllerUninformed"
    class_model_uri: ClassVar[URIRef] = DPV.ControllerUninformed

    id: Union[str, ControllerUninformedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControllerUninformedId):
            self.id = ControllerUninformedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSubjectUninformed(EntityUninformed):
    """
    Status indicating DataSubject is uninformed i.e. has not been informed
    about the specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSubjectUninformed"]
    class_class_curie: ClassVar[str] = "dpv:DataSubjectUninformed"
    class_name: ClassVar[str] = "DataSubjectUninformed"
    class_model_uri: ClassVar[URIRef] = DPV.DataSubjectUninformed

    id: Union[str, DataSubjectUninformedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSubjectUninformedId):
            self.id = DataSubjectUninformedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntentionStatus(Status):
    """
    Status indicating whether the specified context was intended or
    unintended
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["IntentionStatus"]
    class_class_curie: ClassVar[str] = "dpv:IntentionStatus"
    class_name: ClassVar[str] = "IntentionStatus"
    class_model_uri: ClassVar[URIRef] = DPV.IntentionStatus

    id: Union[str, IntentionStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntentionStatusId):
            self.id = IntentionStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Intended(IntentionStatus):
    """
    Status indicating the specified context was intended
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Intended"]
    class_class_curie: ClassVar[str] = "dpv:Intended"
    class_name: ClassVar[str] = "Intended"
    class_model_uri: ClassVar[URIRef] = DPV.Intended

    id: Union[str, IntendedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntendedId):
            self.id = IntendedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InvolvementStatus(Status):
    """
    Status indicating whether the involvement of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InvolvementStatus"]
    class_class_curie: ClassVar[str] = "dpv:InvolvementStatus"
    class_name: ClassVar[str] = "InvolvementStatus"
    class_model_uri: ClassVar[URIRef] = DPV.InvolvementStatus

    id: Union[str, InvolvementStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InvolvementStatusId):
            self.id = InvolvementStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActivelyInvolved(InvolvementStatus):
    """
    Status indicating the specified context is 'actively' involved
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ActivelyInvolved"]
    class_class_curie: ClassVar[str] = "dpv:ActivelyInvolved"
    class_name: ClassVar[str] = "ActivelyInvolved"
    class_model_uri: ClassVar[URIRef] = DPV.ActivelyInvolved

    id: Union[str, ActivelyInvolvedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivelyInvolvedId):
            self.id = ActivelyInvolvedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Lawfulness(ComplianceStatus):
    """
    Status associated with expressing lawfulness or legal compliance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Lawfulness"]
    class_class_curie: ClassVar[str] = "dpv:Lawfulness"
    class_name: ClassVar[str] = "Lawfulness"
    class_model_uri: ClassVar[URIRef] = DPV.Lawfulness

    id: Union[str, LawfulnessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LawfulnessId):
            self.id = LawfulnessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Lawful(Lawfulness):
    """
    State of being lawful or legally compliant
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Lawful"]
    class_class_curie: ClassVar[str] = "dpv:Lawful"
    class_name: ClassVar[str] = "Lawful"
    class_model_uri: ClassVar[URIRef] = DPV.Lawful

    id: Union[str, LawfulId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LawfulId):
            self.id = LawfulId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LawfulnessUnknown(Lawfulness):
    """
    State of the lawfulness not being known
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LawfulnessUnknown"]
    class_class_curie: ClassVar[str] = "dpv:LawfulnessUnknown"
    class_name: ClassVar[str] = "LawfulnessUnknown"
    class_model_uri: ClassVar[URIRef] = DPV.LawfulnessUnknown

    id: Union[str, LawfulnessUnknownId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LawfulnessUnknownId):
            self.id = LawfulnessUnknownId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NonCompliant(ComplianceStatus):
    """
    State of non-compliance where objectives have not been met, but have not
    been violated
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NonCompliant"]
    class_class_curie: ClassVar[str] = "dpv:NonCompliant"
    class_name: ClassVar[str] = "NonCompliant"
    class_model_uri: ClassVar[URIRef] = DPV.NonCompliant

    id: Union[str, NonCompliantId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NonCompliantId):
            self.id = NonCompliantId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NonConformant(ConformanceStatus):
    """
    State of being non-conformant
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NonConformant"]
    class_class_curie: ClassVar[str] = "dpv:NonConformant"
    class_name: ClassVar[str] = "NonConformant"
    class_model_uri: ClassVar[URIRef] = DPV.NonConformant

    id: Union[str, NonConformantId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NonConformantId):
            self.id = NonConformantId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotInvolved(InvolvementStatus):
    """
    Status indicating the specified context is 'not' involved
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NotInvolved"]
    class_class_curie: ClassVar[str] = "dpv:NotInvolved"
    class_name: ClassVar[str] = "NotInvolved"
    class_model_uri: ClassVar[URIRef] = DPV.NotInvolved

    id: Union[str, NotInvolvedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotInvolvedId):
            self.id = NotInvolvedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotificationStatus(Status):
    """
    Status indicating whether notification(s) are planned, completed, or
    failed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NotificationStatus"]
    class_class_curie: ClassVar[str] = "dpv:NotificationStatus"
    class_name: ClassVar[str] = "NotificationStatus"
    class_model_uri: ClassVar[URIRef] = DPV.NotificationStatus

    id: Union[str, NotificationStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotificationStatusId):
            self.id = NotificationStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotificationCompleted(NotificationStatus):
    """
    Status indicating notification(s) are completed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NotificationCompleted"]
    class_class_curie: ClassVar[str] = "dpv:NotificationCompleted"
    class_name: ClassVar[str] = "NotificationCompleted"
    class_model_uri: ClassVar[URIRef] = DPV.NotificationCompleted

    id: Union[str, NotificationCompletedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotificationCompletedId):
            self.id = NotificationCompletedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotificationFailed(NotificationStatus):
    """
    Status indicating notification(s) could not be completed due to a
    failure
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NotificationFailed"]
    class_class_curie: ClassVar[str] = "dpv:NotificationFailed"
    class_name: ClassVar[str] = "NotificationFailed"
    class_model_uri: ClassVar[URIRef] = DPV.NotificationFailed

    id: Union[str, NotificationFailedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotificationFailedId):
            self.id = NotificationFailedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotificationNotNeeded(NotificationStatus):
    """
    Status indicating notification(s) are not needed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NotificationNotNeeded"]
    class_class_curie: ClassVar[str] = "dpv:NotificationNotNeeded"
    class_name: ClassVar[str] = "NotificationNotNeeded"
    class_model_uri: ClassVar[URIRef] = DPV.NotificationNotNeeded

    id: Union[str, NotificationNotNeededId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotificationNotNeededId):
            self.id = NotificationNotNeededId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotificationOngoing(NotificationStatus):
    """
    Status indicating notification(s) are ongoing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NotificationOngoing"]
    class_class_curie: ClassVar[str] = "dpv:NotificationOngoing"
    class_name: ClassVar[str] = "NotificationOngoing"
    class_model_uri: ClassVar[URIRef] = DPV.NotificationOngoing

    id: Union[str, NotificationOngoingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotificationOngoingId):
            self.id = NotificationOngoingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotificationPlanned(NotificationStatus):
    """
    Status indicating notification(s) are planned
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NotificationPlanned"]
    class_class_curie: ClassVar[str] = "dpv:NotificationPlanned"
    class_name: ClassVar[str] = "NotificationPlanned"
    class_model_uri: ClassVar[URIRef] = DPV.NotificationPlanned

    id: Union[str, NotificationPlannedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotificationPlannedId):
            self.id = NotificationPlannedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PartiallyCompliant(ComplianceStatus):
    """
    State of partially being compliant i.e. only some objectives have been
    met, and others have not been in violation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PartiallyCompliant"]
    class_class_curie: ClassVar[str] = "dpv:PartiallyCompliant"
    class_name: ClassVar[str] = "PartiallyCompliant"
    class_model_uri: ClassVar[URIRef] = DPV.PartiallyCompliant

    id: Union[str, PartiallyCompliantId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PartiallyCompliantId):
            self.id = PartiallyCompliantId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PassivelyInvolved(InvolvementStatus):
    """
    Status indicating the specified context is 'passively' involved
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PassivelyInvolved"]
    class_class_curie: ClassVar[str] = "dpv:PassivelyInvolved"
    class_name: ClassVar[str] = "PassivelyInvolved"
    class_model_uri: ClassVar[URIRef] = DPV.PassivelyInvolved

    id: Union[str, PassivelyInvolvedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PassivelyInvolvedId):
            self.id = PassivelyInvolvedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecipientInformed(EntityInformed):
    """
    Status indicating Recipient has been informed about the specified
    context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecipientInformed"]
    class_class_curie: ClassVar[str] = "dpv:RecipientInformed"
    class_name: ClassVar[str] = "RecipientInformed"
    class_model_uri: ClassVar[URIRef] = DPV.RecipientInformed

    id: Union[str, RecipientInformedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecipientInformedId):
            self.id = RecipientInformedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecipientUninformed(EntityUninformed):
    """
    Status indicating Recipient is uninformed i.e. has not been informed
    about the specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecipientUninformed"]
    class_class_curie: ClassVar[str] = "dpv:RecipientUninformed"
    class_name: ClassVar[str] = "RecipientUninformed"
    class_model_uri: ClassVar[URIRef] = DPV.RecipientUninformed

    id: Union[str, RecipientUninformedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecipientUninformedId):
            self.id = RecipientUninformedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequestStatus(Status):
    """
    Status associated with requests
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RequestStatus"]
    class_class_curie: ClassVar[str] = "dpv:RequestStatus"
    class_name: ClassVar[str] = "RequestStatus"
    class_model_uri: ClassVar[URIRef] = DPV.RequestStatus

    id: Union[str, RequestStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RequestStatusId):
            self.id = RequestStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequestAccepted(RequestStatus):
    """
    State of a request being accepted towards fulfilment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RequestAccepted"]
    class_class_curie: ClassVar[str] = "dpv:RequestAccepted"
    class_name: ClassVar[str] = "RequestAccepted"
    class_model_uri: ClassVar[URIRef] = DPV.RequestAccepted

    id: Union[str, RequestAcceptedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RequestAcceptedId):
            self.id = RequestAcceptedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequestAcknowledged(RequestStatus):
    """
    State of a request being acknowledged
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RequestAcknowledged"]
    class_class_curie: ClassVar[str] = "dpv:RequestAcknowledged"
    class_name: ClassVar[str] = "RequestAcknowledged"
    class_model_uri: ClassVar[URIRef] = DPV.RequestAcknowledged

    id: Union[str, RequestAcknowledgedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RequestAcknowledgedId):
            self.id = RequestAcknowledgedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequestActionDelayed(RequestStatus):
    """
    State of a request being delayed towards fulfilment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RequestActionDelayed"]
    class_class_curie: ClassVar[str] = "dpv:RequestActionDelayed"
    class_name: ClassVar[str] = "RequestActionDelayed"
    class_model_uri: ClassVar[URIRef] = DPV.RequestActionDelayed

    id: Union[str, RequestActionDelayedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RequestActionDelayedId):
            self.id = RequestActionDelayedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequestFulfilled(RequestStatus):
    """
    State of a request being fulfilled
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RequestFulfilled"]
    class_class_curie: ClassVar[str] = "dpv:RequestFulfilled"
    class_name: ClassVar[str] = "RequestFulfilled"
    class_model_uri: ClassVar[URIRef] = DPV.RequestFulfilled

    id: Union[str, RequestFulfilledId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RequestFulfilledId):
            self.id = RequestFulfilledId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequestInitiated(RequestStatus):
    """
    State of a request being initiated
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RequestInitiated"]
    class_class_curie: ClassVar[str] = "dpv:RequestInitiated"
    class_name: ClassVar[str] = "RequestInitiated"
    class_model_uri: ClassVar[URIRef] = DPV.RequestInitiated

    id: Union[str, RequestInitiatedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RequestInitiatedId):
            self.id = RequestInitiatedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequestRejected(RequestStatus):
    """
    State of a request being rejected towards non-fulfilment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RequestRejected"]
    class_class_curie: ClassVar[str] = "dpv:RequestRejected"
    class_name: ClassVar[str] = "RequestRejected"
    class_model_uri: ClassVar[URIRef] = DPV.RequestRejected

    id: Union[str, RequestRejectedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RequestRejectedId):
            self.id = RequestRejectedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequestRequiredActionPerformed(RequestStatus):
    """
    State of a request's required action having been performed by the other
    party
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RequestRequiredActionPerformed"]
    class_class_curie: ClassVar[str] = "dpv:RequestRequiredActionPerformed"
    class_name: ClassVar[str] = "RequestRequiredActionPerformed"
    class_model_uri: ClassVar[URIRef] = DPV.RequestRequiredActionPerformed

    id: Union[str, RequestRequiredActionPerformedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RequestRequiredActionPerformedId):
            self.id = RequestRequiredActionPerformedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequestRequiresAction(RequestStatus):
    """
    State of a request requiring an action to be performed from another
    party
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RequestRequiresAction"]
    class_class_curie: ClassVar[str] = "dpv:RequestRequiresAction"
    class_name: ClassVar[str] = "RequestRequiresAction"
    class_model_uri: ClassVar[URIRef] = DPV.RequestRequiresAction

    id: Union[str, RequestRequiresActionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RequestRequiresActionId):
            self.id = RequestRequiresActionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequestStatusQuery(RequestStatus):
    """
    State of a request's status being queried
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RequestStatusQuery"]
    class_class_curie: ClassVar[str] = "dpv:RequestStatusQuery"
    class_name: ClassVar[str] = "RequestStatusQuery"
    class_model_uri: ClassVar[URIRef] = DPV.RequestStatusQuery

    id: Union[str, RequestStatusQueryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RequestStatusQueryId):
            self.id = RequestStatusQueryId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequestUnfulfilled(RequestStatus):
    """
    State of a request being unfulfilled
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RequestUnfulfilled"]
    class_class_curie: ClassVar[str] = "dpv:RequestUnfulfilled"
    class_name: ClassVar[str] = "RequestUnfulfilled"
    class_model_uri: ClassVar[URIRef] = DPV.RequestUnfulfilled

    id: Union[str, RequestUnfulfilledId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RequestUnfulfilledId):
            self.id = RequestUnfulfilledId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReuseCompatibility(Status):
    """
    Status indicating whether the specified context is compatible with
    another earlier context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ReuseCompatibility"]
    class_class_curie: ClassVar[str] = "dpv:ReuseCompatibility"
    class_name: ClassVar[str] = "ReuseCompatibility"
    class_model_uri: ClassVar[URIRef] = DPV.ReuseCompatibility

    id: Union[str, ReuseCompatibilityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReuseCompatibilityId):
            self.id = ReuseCompatibilityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CompatibilityUnknown(ReuseCompatibility):
    """
    Status indicating the compatibility of the context with an earlier
    context is currently unknown
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CompatibilityUnknown"]
    class_class_curie: ClassVar[str] = "dpv:CompatibilityUnknown"
    class_name: ClassVar[str] = "CompatibilityUnknown"
    class_model_uri: ClassVar[URIRef] = DPV.CompatibilityUnknown

    id: Union[str, CompatibilityUnknownId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CompatibilityUnknownId):
            self.id = CompatibilityUnknownId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrimaryUse(ReuseCompatibility):
    """
    Status indicating compatibility based on the use being either the
    original context or something that is compatible with it
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PrimaryUse"]
    class_class_curie: ClassVar[str] = "dpv:PrimaryUse"
    class_name: ClassVar[str] = "PrimaryUse"
    class_model_uri: ClassVar[URIRef] = DPV.PrimaryUse

    id: Union[str, PrimaryUseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrimaryUseId):
            self.id = PrimaryUseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RuleFulfilmentStatus(Status):
    """
    Status associated with a rule for indicating whether it is applicable,
    or has been utilised, and whether the requirements of the rule have been
    fulfilled or violated
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RuleFulfilmentStatus"]
    class_class_curie: ClassVar[str] = "dpv:RuleFulfilmentStatus"
    class_name: ClassVar[str] = "RuleFulfilmentStatus"
    class_model_uri: ClassVar[URIRef] = DPV.RuleFulfilmentStatus

    id: Union[str, RuleFulfilmentStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RuleFulfilmentStatusId):
            self.id = RuleFulfilmentStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RuleFulfilled(RuleFulfilmentStatus):
    """
    Status indicating a rule has been fulfilled, completed, or satisfied
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RuleFulfilled"]
    class_class_curie: ClassVar[str] = "dpv:RuleFulfilled"
    class_name: ClassVar[str] = "RuleFulfilled"
    class_model_uri: ClassVar[URIRef] = DPV.RuleFulfilled

    id: Union[str, RuleFulfilledId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RuleFulfilledId):
            self.id = RuleFulfilledId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DeterrenceFollowed(RuleFulfilled):
    """
    Status indicating a deterrence has been followed i.e. the activity
    stated as being deterred has not been carried out
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DeterrenceFollowed"]
    class_class_curie: ClassVar[str] = "dpv:DeterrenceFollowed"
    class_name: ClassVar[str] = "DeterrenceFollowed"
    class_model_uri: ClassVar[URIRef] = DPV.DeterrenceFollowed

    id: Union[str, DeterrenceFollowedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeterrenceFollowedId):
            self.id = DeterrenceFollowedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObligationFulfilled(RuleFulfilled):
    """
    Status indicating an obligation has been fulfilled i.e. the activity
    stated as being required to be carried out has been successfully
    completed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ObligationFulfilled"]
    class_class_curie: ClassVar[str] = "dpv:ObligationFulfilled"
    class_name: ClassVar[str] = "ObligationFulfilled"
    class_model_uri: ClassVar[URIRef] = DPV.ObligationFulfilled

    id: Union[str, ObligationFulfilledId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObligationFulfilledId):
            self.id = ObligationFulfilledId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PermissionNotUtilised(RuleFulfilled):
    """
    Status indicating a permission has not been utilised i.e. the activity
    stated as being permitted has not been carried out
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PermissionNotUtilised"]
    class_class_curie: ClassVar[str] = "dpv:PermissionNotUtilised"
    class_name: ClassVar[str] = "PermissionNotUtilised"
    class_model_uri: ClassVar[URIRef] = DPV.PermissionNotUtilised

    id: Union[str, PermissionNotUtilisedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PermissionNotUtilisedId):
            self.id = PermissionNotUtilisedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PermissionUtilised(RuleFulfilled):
    """
    Status indicating a permission has been utilised i.e. the activity
    stated as being permitted has been carried out
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PermissionUtilised"]
    class_class_curie: ClassVar[str] = "dpv:PermissionUtilised"
    class_name: ClassVar[str] = "PermissionUtilised"
    class_model_uri: ClassVar[URIRef] = DPV.PermissionUtilised

    id: Union[str, PermissionUtilisedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PermissionUtilisedId):
            self.id = PermissionUtilisedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProhibitionUnviolated(RuleFulfilled):
    """
    Status indicating a prohibition has not been violated i.e. the activity
    stated as being prohibited has not been carried out
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProhibitionUnviolated"]
    class_class_curie: ClassVar[str] = "dpv:ProhibitionUnviolated"
    class_name: ClassVar[str] = "ProhibitionUnviolated"
    class_model_uri: ClassVar[URIRef] = DPV.ProhibitionUnviolated

    id: Union[str, ProhibitionUnviolatedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProhibitionUnviolatedId):
            self.id = ProhibitionUnviolatedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecommendationFollowed(RuleFulfilled):
    """
    Status indicating a recommendation has been followed i.e. the activity
    stated as being recommended has been carried out
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecommendationFollowed"]
    class_class_curie: ClassVar[str] = "dpv:RecommendationFollowed"
    class_name: ClassVar[str] = "RecommendationFollowed"
    class_model_uri: ClassVar[URIRef] = DPV.RecommendationFollowed

    id: Union[str, RecommendationFollowedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecommendationFollowedId):
            self.id = RecommendationFollowedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RuleUnfulfilled(RuleFulfilmentStatus):
    """
    Status indicating a rule has not been fulfilled nor violated
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RuleUnfulfilled"]
    class_class_curie: ClassVar[str] = "dpv:RuleUnfulfilled"
    class_name: ClassVar[str] = "RuleUnfulfilled"
    class_model_uri: ClassVar[URIRef] = DPV.RuleUnfulfilled

    id: Union[str, RuleUnfulfilledId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RuleUnfulfilledId):
            self.id = RuleUnfulfilledId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DeterrenceNotFollowed(RuleUnfulfilled):
    """
    Status indicating a deterrence has not been followed i.e. the activity
    stated as being deterred has been carried out
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DeterrenceNotFollowed"]
    class_class_curie: ClassVar[str] = "dpv:DeterrenceNotFollowed"
    class_name: ClassVar[str] = "DeterrenceNotFollowed"
    class_model_uri: ClassVar[URIRef] = DPV.DeterrenceNotFollowed

    id: Union[str, DeterrenceNotFollowedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeterrenceNotFollowedId):
            self.id = DeterrenceNotFollowedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObligationUnfulfilled(RuleUnfulfilled):
    """
    Status indicating an obligation has not been fulfilled i.e. the activity
    stated as being required to be carried out has not been carried out but
    this is not considered as a violation e.g. there is still time to
    conduct the activity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ObligationUnfulfilled"]
    class_class_curie: ClassVar[str] = "dpv:ObligationUnfulfilled"
    class_name: ClassVar[str] = "ObligationUnfulfilled"
    class_model_uri: ClassVar[URIRef] = DPV.ObligationUnfulfilled

    id: Union[str, ObligationUnfulfilledId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObligationUnfulfilledId):
            self.id = ObligationUnfulfilledId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecommendationNotFollowed(RuleUnfulfilled):
    """
    Status indicating a recommendation has not been followed i.e. the
    activity stated as being recommended has not been carried out
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecommendationNotFollowed"]
    class_class_curie: ClassVar[str] = "dpv:RecommendationNotFollowed"
    class_name: ClassVar[str] = "RecommendationNotFollowed"
    class_model_uri: ClassVar[URIRef] = DPV.RecommendationNotFollowed

    id: Union[str, RecommendationNotFollowedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecommendationNotFollowedId):
            self.id = RecommendationNotFollowedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RuleViolated(RuleFulfilmentStatus):
    """
    Status indicating a rule has been violated, breached, broken, or
    infracted
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RuleViolated"]
    class_class_curie: ClassVar[str] = "dpv:RuleViolated"
    class_name: ClassVar[str] = "RuleViolated"
    class_model_uri: ClassVar[URIRef] = DPV.RuleViolated

    id: Union[str, RuleViolatedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RuleViolatedId):
            self.id = RuleViolatedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObligationViolated(RuleViolated):
    """
    Status indicating an obligation has been violated i.e. the activity
    stated as being required to be carried out has not been carried out and
    this is considered as a violation i.e. the activity can no longer be
    carried out to fulfil the obligation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ObligationViolated"]
    class_class_curie: ClassVar[str] = "dpv:ObligationViolated"
    class_name: ClassVar[str] = "ObligationViolated"
    class_model_uri: ClassVar[URIRef] = DPV.ObligationViolated

    id: Union[str, ObligationViolatedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObligationViolatedId):
            self.id = ObligationViolatedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProhibitionViolated(RuleViolated):
    """
    Status indicating a prohibition has been violated i.e. the activity
    stated as being prohibited has been carried out
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProhibitionViolated"]
    class_class_curie: ClassVar[str] = "dpv:ProhibitionViolated"
    class_name: ClassVar[str] = "ProhibitionViolated"
    class_model_uri: ClassVar[URIRef] = DPV.ProhibitionViolated

    id: Union[str, ProhibitionViolatedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProhibitionViolatedId):
            self.id = ProhibitionViolatedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecondaryUse(ReuseCompatibility):
    """
    Status indicating incompatibility based on the use not being compatible
    with an earlier context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SecondaryUse"]
    class_class_curie: ClassVar[str] = "dpv:SecondaryUse"
    class_name: ClassVar[str] = "SecondaryUse"
    class_model_uri: ClassVar[URIRef] = DPV.SecondaryUse

    id: Union[str, SecondaryUseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecondaryUseId):
            self.id = SecondaryUseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TechnicalOrganisationalMeasure(DpvThing):
    """
    Technical and Organisational measures used to safeguard and ensure good
    practices in connection with data and technologies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["TechnicalOrganisationalMeasure"]
    class_class_curie: ClassVar[str] = "dpv:TechnicalOrganisationalMeasure"
    class_name: ClassVar[str] = "TechnicalOrganisationalMeasure"
    class_model_uri: ClassVar[URIRef] = DPV.TechnicalOrganisationalMeasure

    id: Union[str, TechnicalOrganisationalMeasureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TechnicalOrganisationalMeasureId):
            self.id = TechnicalOrganisationalMeasureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalMeasure(TechnicalOrganisationalMeasure):
    """
    Legal measures used to safeguard and ensure good practices in connection
    with data and technologies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalMeasure"]
    class_class_curie: ClassVar[str] = "dpv:LegalMeasure"
    class_name: ClassVar[str] = "LegalMeasure"
    class_model_uri: ClassVar[URIRef] = DPV.LegalMeasure

    id: Union[str, LegalMeasureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalMeasureId):
            self.id = LegalMeasureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrganisationalMeasure(TechnicalOrganisationalMeasure):
    """
    Organisational measures used to safeguard and ensure good practices in
    connection with data and technologies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OrganisationalMeasure"]
    class_class_curie: ClassVar[str] = "dpv:OrganisationalMeasure"
    class_name: ClassVar[str] = "OrganisationalMeasure"
    class_model_uri: ClassVar[URIRef] = DPV.OrganisationalMeasure

    id: Union[str, OrganisationalMeasureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganisationalMeasureId):
            self.id = OrganisationalMeasureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalMeasure(TechnicalOrganisationalMeasure):
    """
    Physical measures used to safeguard and ensure good practices in
    connection with data and technologies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PhysicalMeasure"]
    class_class_curie: ClassVar[str] = "dpv:PhysicalMeasure"
    class_name: ClassVar[str] = "PhysicalMeasure"
    class_model_uri: ClassVar[URIRef] = DPV.PhysicalMeasure

    id: Union[str, PhysicalMeasureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalMeasureId):
            self.id = PhysicalMeasureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TechnicalMeasure(TechnicalOrganisationalMeasure):
    """
    Technical measures used to safeguard and ensure good practices in
    connection with data and technologies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["TechnicalMeasure"]
    class_class_curie: ClassVar[str] = "dpv:TechnicalMeasure"
    class_name: ClassVar[str] = "TechnicalMeasure"
    class_model_uri: ClassVar[URIRef] = DPV.TechnicalMeasure

    id: Union[str, TechnicalMeasureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TechnicalMeasureId):
            self.id = TechnicalMeasureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TemporalDuration(DpvDuration):
    """
    Duration that has a fixed temporal duration e.g. 6 months
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["TemporalDuration"]
    class_class_curie: ClassVar[str] = "dpv:TemporalDuration"
    class_name: ClassVar[str] = "TemporalDuration"
    class_model_uri: ClassVar[URIRef] = DPV.TemporalDuration

    id: Union[str, TemporalDurationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TemporalDurationId):
            self.id = TemporalDurationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UnacceptableRule(Rule):
    """
    A rule that is unacceptable where it is not desirable if it occurs
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["UnacceptableRule"]
    class_class_curie: ClassVar[str] = "dpv:UnacceptableRule"
    class_name: ClassVar[str] = "UnacceptableRule"
    class_model_uri: ClassVar[URIRef] = DPV.UnacceptableRule

    id: Union[str, UnacceptableRuleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnacceptableRuleId):
            self.id = UnacceptableRuleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Deterrence(UnacceptableRule):
    """
    A rule describing a deterrence for performing an activity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Deterrence"]
    class_class_curie: ClassVar[str] = "dpv:Deterrence"
    class_name: ClassVar[str] = "Deterrence"
    class_model_uri: ClassVar[URIRef] = DPV.Deterrence

    id: Union[str, DeterrenceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeterrenceId):
            self.id = DeterrenceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Prohibition(UnacceptableRule):
    """
    A rule describing a prohibition to perform an activity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Prohibition"]
    class_class_curie: ClassVar[str] = "dpv:Prohibition"
    class_name: ClassVar[str] = "Prohibition"
    class_model_uri: ClassVar[URIRef] = DPV.Prohibition

    id: Union[str, ProhibitionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProhibitionId):
            self.id = ProhibitionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Unexpected(ExpectationStatus):
    """
    Status indicating the specified context was unexpected i.e. not expected
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Unexpected"]
    class_class_curie: ClassVar[str] = "dpv:Unexpected"
    class_name: ClassVar[str] = "Unexpected"
    class_model_uri: ClassVar[URIRef] = DPV.Unexpected

    id: Union[str, UnexpectedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnexpectedId):
            self.id = UnexpectedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Unintended(IntentionStatus):
    """
    Status indicating the specified context was unintended i.e. not intended
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Unintended"]
    class_class_curie: ClassVar[str] = "dpv:Unintended"
    class_name: ClassVar[str] = "Unintended"
    class_model_uri: ClassVar[URIRef] = DPV.Unintended

    id: Union[str, UnintendedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnintendedId):
            self.id = UnintendedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UnknownApplicability(Applicability):
    """
    Concept indicating information or context availability is unknown i.e.
    it is not known if the information exists or is applicable and therefore
    statements about its availability cannot be made (yet)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["UnknownApplicability"]
    class_class_curie: ClassVar[str] = "dpv:UnknownApplicability"
    class_name: ClassVar[str] = "UnknownApplicability"
    class_model_uri: ClassVar[URIRef] = DPV.UnknownApplicability

    id: Union[str, UnknownApplicabilityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnknownApplicabilityId):
            self.id = UnknownApplicabilityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Unlawful(Lawfulness):
    """
    State of being unlawful or legally non-compliant
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Unlawful"]
    class_class_curie: ClassVar[str] = "dpv:Unlawful"
    class_name: ClassVar[str] = "Unlawful"
    class_model_uri: ClassVar[URIRef] = DPV.Unlawful

    id: Union[str, UnlawfulId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnlawfulId):
            self.id = UnlawfulId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UntilEventDuration(DpvDuration):
    """
    Duration that takes place until a specific event occurs e.g. Account
    Closure
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["UntilEventDuration"]
    class_class_curie: ClassVar[str] = "dpv:UntilEventDuration"
    class_name: ClassVar[str] = "UntilEventDuration"
    class_model_uri: ClassVar[URIRef] = DPV.UntilEventDuration

    id: Union[str, UntilEventDurationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UntilEventDurationId):
            self.id = UntilEventDurationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UntilTimeDuration(DpvDuration):
    """
    Duration that has a fixed end date e.g. 2022-12-31
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["UntilTimeDuration"]
    class_class_curie: ClassVar[str] = "dpv:UntilTimeDuration"
    class_name: ClassVar[str] = "UntilTimeDuration"
    class_model_uri: ClassVar[URIRef] = DPV.UntilTimeDuration

    id: Union[str, UntilTimeDurationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UntilTimeDurationId):
            self.id = UntilTimeDurationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractStatus(Status):
    """
    Status associated with a contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractStatus"]
    class_class_curie: ClassVar[str] = "dpv:ContractStatus"
    class_name: ClassVar[str] = "ContractStatus"
    class_model_uri: ClassVar[URIRef] = DPV.ContractStatus

    id: Union[str, ContractStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractStatusId):
            self.id = ContractStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractActivationStatus(ContractStatus):
    """
    Status associated with activation of a contract i.e. whether its terms
    are active and are required to be performed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractActivationStatus"]
    class_class_curie: ClassVar[str] = "dpv:ContractActivationStatus"
    class_name: ClassVar[str] = "ContractActivationStatus"
    class_model_uri: ClassVar[URIRef] = DPV.ContractActivationStatus

    id: Union[str, ContractActivationStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractActivationStatusId):
            self.id = ContractActivationStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractActive(ContractActivationStatus):
    """
    Status representing contract that has been fully executed and whose
    terms are considered active i.e. they are applicable and are required to
    be performed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractActive"]
    class_class_curie: ClassVar[str] = "dpv:ContractActive"
    class_name: ClassVar[str] = "ContractActive"
    class_model_uri: ClassVar[URIRef] = DPV.ContractActive

    id: Union[str, ContractActiveId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractActiveId):
            self.id = ContractActiveId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractExecutionStatus(ContractStatus):
    """
    Status associated with execution of a contract (i.e. signing and
    procedural aspects before the contract terms come in to effect)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractExecutionStatus"]
    class_class_curie: ClassVar[str] = "dpv:ContractExecutionStatus"
    class_name: ClassVar[str] = "ContractExecutionStatus"
    class_model_uri: ClassVar[URIRef] = DPV.ContractExecutionStatus

    id: Union[str, ContractExecutionStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractExecutionStatusId):
            self.id = ContractExecutionStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractFulfilmentStatus(ContractStatus):
    """
    Status associated with fulfilment of a contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractFulfilmentStatus"]
    class_class_curie: ClassVar[str] = "dpv:ContractFulfilmentStatus"
    class_name: ClassVar[str] = "ContractFulfilmentStatus"
    class_model_uri: ClassVar[URIRef] = DPV.ContractFulfilmentStatus

    id: Union[str, ContractFulfilmentStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractFulfilmentStatusId):
            self.id = ContractFulfilmentStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractFulfilled(ContractFulfilmentStatus):
    """
    Status representing contract where all its terms have been fulfilled in
    a manner that does not constitute a violation or breach of the contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractFulfilled"]
    class_class_curie: ClassVar[str] = "dpv:ContractFulfilled"
    class_name: ClassVar[str] = "ContractFulfilled"
    class_model_uri: ClassVar[URIRef] = DPV.ContractFulfilled

    id: Union[str, ContractFulfilledId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractFulfilledId):
            self.id = ContractFulfilledId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractFullyExecuted(ContractExecutionStatus):
    """
    Status representing contract has been fully executed i.e. it has been
    signed by all parties and all other procedural aspects such as exchange
    of signed contract copies have been completed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractFullyExecuted"]
    class_class_curie: ClassVar[str] = "dpv:ContractFullyExecuted"
    class_name: ClassVar[str] = "ContractFullyExecuted"
    class_model_uri: ClassVar[URIRef] = DPV.ContractFullyExecuted

    id: Union[str, ContractFullyExecutedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractFullyExecutedId):
            self.id = ContractFullyExecutedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractFullySigned(ContractExecutionStatus):
    """
    Status representing contract has been signed by all concerned parties
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractFullySigned"]
    class_class_curie: ClassVar[str] = "dpv:ContractFullySigned"
    class_name: ClassVar[str] = "ContractFullySigned"
    class_model_uri: ClassVar[URIRef] = DPV.ContractFullySigned

    id: Union[str, ContractFullySignedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractFullySignedId):
            self.id = ContractFullySignedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractInactive(ContractActivationStatus):
    """
    Status representing contract that has been fully executed and whose
    terms are not yet active i.e. they need to be performed at a later time
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractInactive"]
    class_class_curie: ClassVar[str] = "dpv:ContractInactive"
    class_name: ClassVar[str] = "ContractInactive"
    class_model_uri: ClassVar[URIRef] = DPV.ContractInactive

    id: Union[str, ContractInactiveId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractInactiveId):
            self.id = ContractInactiveId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractNotFulfilled(ContractFulfilmentStatus):
    """
    Status representing contract where none of its terms have been fulfilled
    in a manner that does not constitute a violation or breach of the
    contract i.e. there is still time and opportunity to complete the terms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractNotFulfilled"]
    class_class_curie: ClassVar[str] = "dpv:ContractNotFulfilled"
    class_name: ClassVar[str] = "ContractNotFulfilled"
    class_model_uri: ClassVar[URIRef] = DPV.ContractNotFulfilled

    id: Union[str, ContractNotFulfilledId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractNotFulfilledId):
            self.id = ContractNotFulfilledId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractPartiallyFulfilled(ContractFulfilmentStatus):
    """
    Status representing contract where some of its terms have been
    fulfilled, and others are yet to be fulfilled in a manner that does not
    constitute a violation or breach of the contract i.e. there is still
    time and opportunity to complete the terms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractPartiallyFulfilled"]
    class_class_curie: ClassVar[str] = "dpv:ContractPartiallyFulfilled"
    class_name: ClassVar[str] = "ContractPartiallyFulfilled"
    class_model_uri: ClassVar[URIRef] = DPV.ContractPartiallyFulfilled

    id: Union[str, ContractPartiallyFulfilledId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractPartiallyFulfilledId):
            self.id = ContractPartiallyFulfilledId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractPartiallySigned(ContractExecutionStatus):
    """
    Status representing contract has been partially signed by parties i.e.
    some parties have signed the contract and others are yet to make a
    decision to sign it
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractPartiallySigned"]
    class_class_curie: ClassVar[str] = "dpv:ContractPartiallySigned"
    class_name: ClassVar[str] = "ContractPartiallySigned"
    class_model_uri: ClassVar[URIRef] = DPV.ContractPartiallySigned

    id: Union[str, ContractPartiallySignedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractPartiallySignedId):
            self.id = ContractPartiallySignedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractPerformanceStatus(ContractStatus):
    """
    Status associated with performance of a contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractPerformanceStatus"]
    class_class_curie: ClassVar[str] = "dpv:ContractPerformanceStatus"
    class_name: ClassVar[str] = "ContractPerformanceStatus"
    class_model_uri: ClassVar[URIRef] = DPV.ContractPerformanceStatus

    id: Union[str, ContractPerformanceStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractPerformanceStatusId):
            self.id = ContractPerformanceStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractAmended(ContractPerformanceStatus):
    """
    Status representing contract that has been fully executed and whose
    terms have been amended through mutual agreement or other means such
    that the contract is still required to be performed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractAmended"]
    class_class_curie: ClassVar[str] = "dpv:ContractAmended"
    class_name: ClassVar[str] = "ContractAmended"
    class_model_uri: ClassVar[URIRef] = DPV.ContractAmended

    id: Union[str, ContractAmendedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractAmendedId):
            self.id = ContractAmendedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractBeingPerformed(ContractPerformanceStatus):
    """
    Status representing contract that has been fully executed and whose
    terms are being carried out i.e. the contract is being performed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractBeingPerformed"]
    class_class_curie: ClassVar[str] = "dpv:ContractBeingPerformed"
    class_name: ClassVar[str] = "ContractBeingPerformed"
    class_model_uri: ClassVar[URIRef] = DPV.ContractBeingPerformed

    id: Union[str, ContractBeingPerformedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractBeingPerformedId):
            self.id = ContractBeingPerformedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractPreparationStatus(ContractStatus):
    """
    Status associated with preparation of contracts before they are signed
    or accepted or executed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractPreparationStatus"]
    class_class_curie: ClassVar[str] = "dpv:ContractPreparationStatus"
    class_name: ClassVar[str] = "ContractPreparationStatus"
    class_model_uri: ClassVar[URIRef] = DPV.ContractPreparationStatus

    id: Union[str, ContractPreparationStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractPreparationStatusId):
            self.id = ContractPreparationStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractApproved(ContractPreparationStatus):
    """
    Status representing contract has been approved and can be used for
    signing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractApproved"]
    class_class_curie: ClassVar[str] = "dpv:ContractApproved"
    class_name: ClassVar[str] = "ContractApproved"
    class_model_uri: ClassVar[URIRef] = DPV.ContractApproved

    id: Union[str, ContractApprovedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractApprovedId):
            self.id = ContractApprovedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractDrafted(ContractPreparationStatus):
    """
    Status representing the drafting of contract text has been completed and
    it can now be offered for signing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractDrafted"]
    class_class_curie: ClassVar[str] = "dpv:ContractDrafted"
    class_name: ClassVar[str] = "ContractDrafted"
    class_model_uri: ClassVar[URIRef] = DPV.ContractDrafted

    id: Union[str, ContractDraftedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractDraftedId):
            self.id = ContractDraftedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractNegotiated(ContractPreparationStatus):
    """
    Status representing contract has been successfully negotiated by
    involved parties
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractNegotiated"]
    class_class_curie: ClassVar[str] = "dpv:ContractNegotiated"
    class_name: ClassVar[str] = "ContractNegotiated"
    class_model_uri: ClassVar[URIRef] = DPV.ContractNegotiated

    id: Union[str, ContractNegotiatedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractNegotiatedId):
            self.id = ContractNegotiatedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractOffered(ContractPreparationStatus):
    """
    Status representing contract has been offered to a party or to parties
    for reviewing and signing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractOffered"]
    class_class_curie: ClassVar[str] = "dpv:ContractOffered"
    class_name: ClassVar[str] = "ContractOffered"
    class_model_uri: ClassVar[URIRef] = DPV.ContractOffered

    id: Union[str, ContractOfferedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractOfferedId):
            self.id = ContractOfferedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractRejected(ContractPreparationStatus):
    """
    Status representing contract has been rejected and cannot be used for
    signing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractRejected"]
    class_class_curie: ClassVar[str] = "dpv:ContractRejected"
    class_name: ClassVar[str] = "ContractRejected"
    class_model_uri: ClassVar[URIRef] = DPV.ContractRejected

    id: Union[str, ContractRejectedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractRejectedId):
            self.id = ContractRejectedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractRenewed(ContractPerformanceStatus):
    """
    Status representing contract being renewed with new duration and/or
    applicability where the contract has been fully executed in the past
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractRenewed"]
    class_class_curie: ClassVar[str] = "dpv:ContractRenewed"
    class_name: ClassVar[str] = "ContractRenewed"
    class_model_uri: ClassVar[URIRef] = DPV.ContractRenewed

    id: Union[str, ContractRenewedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractRenewedId):
            self.id = ContractRenewedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractSignedByParty(ContractExecutionStatus):
    """
    Status representing contract has been signed by the indicated signing
    party
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractSignedByParty"]
    class_class_curie: ClassVar[str] = "dpv:ContractSignedByParty"
    class_name: ClassVar[str] = "ContractSignedByParty"
    class_model_uri: ClassVar[URIRef] = DPV.ContractSignedByParty

    id: Union[str, ContractSignedByPartyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractSignedByPartyId):
            self.id = ContractSignedByPartyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractTemporarilySuspended(ContractPerformanceStatus):
    """
    Status representing contract that has been temporarily suspended through
    mutual agreement or by some parties
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractTemporarilySuspended"]
    class_class_curie: ClassVar[str] = "dpv:ContractTemporarilySuspended"
    class_name: ClassVar[str] = "ContractTemporarilySuspended"
    class_model_uri: ClassVar[URIRef] = DPV.ContractTemporarilySuspended

    id: Union[str, ContractTemporarilySuspendedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractTemporarilySuspendedId):
            self.id = ContractTemporarilySuspendedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractTerminationStatus(ContractStatus):
    """
    Status associated with termination of a contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractTerminationStatus"]
    class_class_curie: ClassVar[str] = "dpv:ContractTerminationStatus"
    class_name: ClassVar[str] = "ContractTerminationStatus"
    class_model_uri: ClassVar[URIRef] = DPV.ContractTerminationStatus

    id: Union[str, ContractTerminationStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractTerminationStatusId):
            self.id = ContractTerminationStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractBreached(ContractTerminationStatus):
    """
    Status representing contract being breached where its terms are not
    fulfilled or are violated with legal consequences
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractBreached"]
    class_class_curie: ClassVar[str] = "dpv:ContractBreached"
    class_name: ClassVar[str] = "ContractBreached"
    class_model_uri: ClassVar[URIRef] = DPV.ContractBreached

    id: Union[str, ContractBreachedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractBreachedId):
            self.id = ContractBreachedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractDisputed(ContractTerminationStatus):
    """
    Status representing contract being disputed where one or more parties
    have an issue regarding the interpretation and performance of the
    contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractDisputed"]
    class_class_curie: ClassVar[str] = "dpv:ContractDisputed"
    class_name: ClassVar[str] = "ContractDisputed"
    class_model_uri: ClassVar[URIRef] = DPV.ContractDisputed

    id: Union[str, ContractDisputedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractDisputedId):
            self.id = ContractDisputedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractExpired(ContractTerminationStatus):
    """
    Status representing reaching the expiry defined in the contract, such as
    when the stated duration or the stated obligations have been completed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractExpired"]
    class_class_curie: ClassVar[str] = "dpv:ContractExpired"
    class_name: ClassVar[str] = "ContractExpired"
    class_model_uri: ClassVar[URIRef] = DPV.ContractExpired

    id: Union[str, ContractExpiredId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractExpiredId):
            self.id = ContractExpiredId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractExtended(ContractTerminationStatus):
    """
    Status representing the duration associated with a contract being
    extended through mutual agreement or by a party
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractExtended"]
    class_class_curie: ClassVar[str] = "dpv:ContractExtended"
    class_name: ClassVar[str] = "ContractExtended"
    class_model_uri: ClassVar[URIRef] = DPV.ContractExtended

    id: Union[str, ContractExtendedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractExtendedId):
            self.id = ContractExtendedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractTerminated(ContractTerminationStatus):
    """
    Status representing contract being terminated by one or more parties
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractTerminated"]
    class_class_curie: ClassVar[str] = "dpv:ContractTerminated"
    class_name: ClassVar[str] = "ContractTerminated"
    class_model_uri: ClassVar[URIRef] = DPV.ContractTerminated

    id: Union[str, ContractTerminatedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractTerminatedId):
            self.id = ContractTerminatedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractUnderNegotiation(ContractPreparationStatus):
    """
    Status representing contract is under negotiation between parties
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractUnderNegotiation"]
    class_class_curie: ClassVar[str] = "dpv:ContractUnderNegotiation"
    class_name: ClassVar[str] = "ContractUnderNegotiation"
    class_model_uri: ClassVar[URIRef] = DPV.ContractUnderNegotiation

    id: Union[str, ContractUnderNegotiationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractUnderNegotiationId):
            self.id = ContractUnderNegotiationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractUnderReview(ContractPreparationStatus):
    """
    Status representing contract is under review and is being considered for
    signing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractUnderReview"]
    class_class_curie: ClassVar[str] = "dpv:ContractUnderReview"
    class_name: ClassVar[str] = "ContractUnderReview"
    class_model_uri: ClassVar[URIRef] = DPV.ContractUnderReview

    id: Union[str, ContractUnderReviewId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractUnderReviewId):
            self.id = ContractUnderReviewId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractViolated(ContractFulfilmentStatus):
    """
    Status representing contract where one or more terms have not been
    fulfilled or have been fulfilled, where either is considered a violation
    of the terms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractViolated"]
    class_class_curie: ClassVar[str] = "dpv:ContractViolated"
    class_name: ClassVar[str] = "ContractViolated"
    class_model_uri: ClassVar[URIRef] = DPV.ContractViolated

    id: Union[str, ContractViolatedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractViolatedId):
            self.id = ContractViolatedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractualClause(DpvThing):
    """
    A part or component within a contract that outlines its specifics
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractualClause"]
    class_class_curie: ClassVar[str] = "dpv:ContractualClause"
    class_name: ClassVar[str] = "ContractualClause"
    class_model_uri: ClassVar[URIRef] = DPV.ContractualClause

    id: Union[str, ContractualClauseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractualClauseId):
            self.id = ContractualClauseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractAmendmentClause(ContractualClause):
    """
    A provision describing how changes or modifications to the contract can
    be made and the process for implementing them
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractAmendmentClause"]
    class_class_curie: ClassVar[str] = "dpv:ContractAmendmentClause"
    class_name: ClassVar[str] = "ContractAmendmentClause"
    class_model_uri: ClassVar[URIRef] = DPV.ContractAmendmentClause

    id: Union[str, ContractAmendmentClauseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractAmendmentClauseId):
            self.id = ContractAmendmentClauseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractConfidentialityClause(ContractualClause):
    """
    A provision requiring parties to keep certain information confidential
    and not disclose it to third parties
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractConfidentialityClause"]
    class_class_curie: ClassVar[str] = "dpv:ContractConfidentialityClause"
    class_name: ClassVar[str] = "ContractConfidentialityClause"
    class_model_uri: ClassVar[URIRef] = DPV.ContractConfidentialityClause

    id: Union[str, ContractConfidentialityClauseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractConfidentialityClauseId):
            self.id = ContractConfidentialityClauseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractDefinitions(ContractualClause):
    """
    A section specifying the meanings of key terms and phrases used
    throughout the contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractDefinitions"]
    class_class_curie: ClassVar[str] = "dpv:ContractDefinitions"
    class_name: ClassVar[str] = "ContractDefinitions"
    class_model_uri: ClassVar[URIRef] = DPV.ContractDefinitions

    id: Union[str, ContractDefinitionsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractDefinitionsId):
            self.id = ContractDefinitionsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractDisputeResolutionClause(ContractualClause):
    """
    A provision detailing the methods and procedures for resolving
    disagreements or conflicts arising from the contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractDisputeResolutionClause"]
    class_class_curie: ClassVar[str] = "dpv:ContractDisputeResolutionClause"
    class_name: ClassVar[str] = "ContractDisputeResolutionClause"
    class_model_uri: ClassVar[URIRef] = DPV.ContractDisputeResolutionClause

    id: Union[str, ContractDisputeResolutionClauseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractDisputeResolutionClauseId):
            self.id = ContractDisputeResolutionClauseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractJurisdictionClause(ContractualClause):
    """
    A provision specifying the legal jurisdiction or court where disputes
    related to the contract will be resolved
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractJurisdictionClause"]
    class_class_curie: ClassVar[str] = "dpv:ContractJurisdictionClause"
    class_name: ClassVar[str] = "ContractJurisdictionClause"
    class_model_uri: ClassVar[URIRef] = DPV.ContractJurisdictionClause

    id: Union[str, ContractJurisdictionClauseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractJurisdictionClauseId):
            self.id = ContractJurisdictionClauseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractPreamble(ContractualClause):
    """
    An introductory section outlining the background, context, and purpose
    of the contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractPreamble"]
    class_class_curie: ClassVar[str] = "dpv:ContractPreamble"
    class_name: ClassVar[str] = "ContractPreamble"
    class_model_uri: ClassVar[URIRef] = DPV.ContractPreamble

    id: Union[str, ContractPreambleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractPreambleId):
            self.id = ContractPreambleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractTerminationClause(ContractualClause):
    """
    A provision outlining the conditions under which the contract can be
    terminated before its completion, including any penalties or obligations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractTerminationClause"]
    class_class_curie: ClassVar[str] = "dpv:ContractTerminationClause"
    class_name: ClassVar[str] = "ContractTerminationClause"
    class_model_uri: ClassVar[URIRef] = DPV.ContractTerminationClause

    id: Union[str, ContractTerminationClauseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractTerminationClauseId):
            self.id = ContractTerminationClauseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractualClauseFulfilmentStatus(ContractStatus):
    """
    Status associated with fulfilment of a contractual clause
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractualClauseFulfilmentStatus"]
    class_class_curie: ClassVar[str] = "dpv:ContractualClauseFulfilmentStatus"
    class_name: ClassVar[str] = "ContractualClauseFulfilmentStatus"
    class_model_uri: ClassVar[URIRef] = DPV.ContractualClauseFulfilmentStatus

    id: Union[str, ContractualClauseFulfilmentStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractualClauseFulfilmentStatusId):
            self.id = ContractualClauseFulfilmentStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractualClauseFulfilled(ContractualClauseFulfilmentStatus):
    """
    Status indicating the terms of the contractual clause are fulfilled i.e.
    they have been successfully completed without violation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractualClauseFulfilled"]
    class_class_curie: ClassVar[str] = "dpv:ContractualClauseFulfilled"
    class_name: ClassVar[str] = "ContractualClauseFulfilled"
    class_model_uri: ClassVar[URIRef] = DPV.ContractualClauseFulfilled

    id: Union[str, ContractualClauseFulfilledId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractualClauseFulfilledId):
            self.id = ContractualClauseFulfilledId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractualClauseNotFulfilled(ContractualClauseFulfilmentStatus):
    """
    Status indicating the terms of the contractual clause have not yet been
    fulfilled in a manner that does not constitute a violation i.e. there is
    still an opportunity to complete them
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractualClauseNotFulfilled"]
    class_class_curie: ClassVar[str] = "dpv:ContractualClauseNotFulfilled"
    class_name: ClassVar[str] = "ContractualClauseNotFulfilled"
    class_model_uri: ClassVar[URIRef] = DPV.ContractualClauseNotFulfilled

    id: Union[str, ContractualClauseNotFulfilledId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractualClauseNotFulfilledId):
            self.id = ContractualClauseNotFulfilledId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractualClausePartiallyFulfilled(ContractualClauseFulfilmentStatus):
    """
    Status indicating some of the terms of the contractual clause have been
    fulfilled, and others have not yet been fulfilled in a manner that does
    not constitute a violation i.e. there is still an opportunity to
    complete them
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractualClausePartiallyFulfilled"]
    class_class_curie: ClassVar[str] = "dpv:ContractualClausePartiallyFulfilled"
    class_name: ClassVar[str] = "ContractualClausePartiallyFulfilled"
    class_model_uri: ClassVar[URIRef] = DPV.ContractualClausePartiallyFulfilled

    id: Union[str, ContractualClausePartiallyFulfilledId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractualClausePartiallyFulfilledId):
            self.id = ContractualClausePartiallyFulfilledId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractualClauseViolated(ContractualClauseFulfilmentStatus):
    """
    Status indicating the terms of the contractual clause have been violated
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractualClauseViolated"]
    class_class_curie: ClassVar[str] = "dpv:ContractualClauseViolated"
    class_name: ClassVar[str] = "ContractualClauseViolated"
    class_model_uri: ClassVar[URIRef] = DPV.ContractualClauseViolated

    id: Union[str, ContractualClauseViolatedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractualClauseViolatedId):
            self.id = ContractualClauseViolatedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractualTerms(LegalMeasure):
    """
    Contractual terms governing data handling within or with an entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractualTerms"]
    class_class_curie: ClassVar[str] = "dpv:ContractualTerms"
    class_name: ClassVar[str] = "ContractualTerms"
    class_model_uri: ClassVar[URIRef] = DPV.ContractualTerms

    id: Union[str, ContractualTermsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractualTermsId):
            self.id = ContractualTermsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataHandlingClause(ContractualTerms):
    """
    Contractual clauses governing handling of data within or by an entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataHandlingClause"]
    class_class_curie: ClassVar[str] = "dpv:DataHandlingClause"
    class_name: ClassVar[str] = "DataHandlingClause"
    class_model_uri: ClassVar[URIRef] = DPV.DataHandlingClause

    id: Union[str, DataHandlingClauseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataHandlingClauseId):
            self.id = DataHandlingClauseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvLocation(DpvThing):
    """
    A location is a position, site, or area where something is located
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Location"]
    class_class_curie: ClassVar[str] = "dpv:Location"
    class_name: ClassVar[str] = "DpvLocation"
    class_model_uri: ClassVar[URIRef] = DPV.DpvLocation

    id: Union[str, DpvLocationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvLocationId):
            self.id = DpvLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvJurisdiction(DpvLocation):
    """
    A jurisdiction represents the locations that define the extent of
    authority (or control) claimed, granted, or asserted by a legal entity
    (in particular a legal authority) to govern or enforce rules
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Jurisdiction"]
    class_class_curie: ClassVar[str] = "dpv:Jurisdiction"
    class_name: ClassVar[str] = "DpvJurisdiction"
    class_model_uri: ClassVar[URIRef] = DPV.DpvJurisdiction

    id: Union[str, DpvJurisdictionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvJurisdictionId):
            self.id = DpvJurisdictionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvCountry(DpvJurisdiction):
    """
    A political entity indicative of a sovereign or non-sovereign
    territorial state comprising of distinct geographical areas
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Country"]
    class_class_curie: ClassVar[str] = "dpv:Country"
    class_name: ClassVar[str] = "DpvCountry"
    class_model_uri: ClassVar[URIRef] = DPV.DpvCountry

    id: Union[str, DpvCountryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvCountryId):
            self.id = DpvCountryId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvRegion(DpvCountry):
    """
    A region is an area or site that is considered a location
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Region"]
    class_class_curie: ClassVar[str] = "dpv:Region"
    class_name: ClassVar[str] = "DpvRegion"
    class_model_uri: ClassVar[URIRef] = DPV.DpvRegion

    id: Union[str, DpvRegionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvRegionId):
            self.id = DpvRegionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class City(DpvRegion):
    """
    A region consisting of urban population and commerce
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["City"]
    class_class_curie: ClassVar[str] = "dpv:City"
    class_name: ClassVar[str] = "City"
    class_model_uri: ClassVar[URIRef] = DPV.City

    id: Union[str, CityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CityId):
            self.id = CityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EconomicUnion(DpvJurisdiction):
    """
    A political union of two or more countries based on economic or trade
    agreements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EconomicUnion"]
    class_class_curie: ClassVar[str] = "dpv:EconomicUnion"
    class_name: ClassVar[str] = "EconomicUnion"
    class_model_uri: ClassVar[URIRef] = DPV.EconomicUnion

    id: Union[str, EconomicUnionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EconomicUnionId):
            self.id = EconomicUnionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InverseJurisdiction(DpvJurisdiction):
    """
    An inverse jurisdiction for a specific jurisdiction is the set of all
    other jurisdictions that are not part of the specific jurisdiction
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InverseJurisdiction"]
    class_class_curie: ClassVar[str] = "dpv:InverseJurisdiction"
    class_name: ClassVar[str] = "InverseJurisdiction"
    class_model_uri: ClassVar[URIRef] = DPV.InverseJurisdiction

    id: Union[str, InverseJurisdictionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InverseJurisdictionId):
            self.id = InverseJurisdictionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Law(DpvThing):
    """
    A law is a set of rules created by government or authorities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Law"]
    class_class_curie: ClassVar[str] = "dpv:Law"
    class_name: ClassVar[str] = "Law"
    class_model_uri: ClassVar[URIRef] = DPV.Law

    id: Union[str, LawId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LawId):
            self.id = LawId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalAgreement(LegalMeasure):
    """
    A legally binding agreement
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalAgreement"]
    class_class_curie: ClassVar[str] = "dpv:LegalAgreement"
    class_name: ClassVar[str] = "LegalAgreement"
    class_model_uri: ClassVar[URIRef] = DPV.LegalAgreement

    id: Union[str, LegalAgreementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalAgreementId):
            self.id = LegalAgreementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConfidentialityAgreement(LegalAgreement):
    """
    Agreements that enforce confidentiality for e.g. to protect business,
    professional, or company secrets
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConfidentialityAgreement"]
    class_class_curie: ClassVar[str] = "dpv:ConfidentialityAgreement"
    class_name: ClassVar[str] = "ConfidentialityAgreement"
    class_model_uri: ClassVar[URIRef] = DPV.ConfidentialityAgreement

    id: Union[str, ConfidentialityAgreementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConfidentialityAgreementId):
            self.id = ConfidentialityAgreementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalBasis(DpvThing):
    """
    Legal basis used to justify processing of data or use of technology in
    accordance with a law
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalBasis"]
    class_class_curie: ClassVar[str] = "dpv:LegalBasis"
    class_name: ClassVar[str] = "LegalBasis"
    class_model_uri: ClassVar[URIRef] = DPV.LegalBasis

    id: Union[str, LegalBasisId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalBasisId):
            self.id = LegalBasisId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Consent(LegalBasis):
    """
    Consent of the Data Subject for specified process or activity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Consent"]
    class_class_curie: ClassVar[str] = "dpv:Consent"
    class_name: ClassVar[str] = "Consent"
    class_model_uri: ClassVar[URIRef] = DPV.Consent

    id: Union[str, ConsentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentId):
            self.id = ConsentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Contract(LegalBasis):
    """
    Creation, completion, fulfilment, or performance of a contract involving
    specified processing of data or technologies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Contract"]
    class_class_curie: ClassVar[str] = "dpv:Contract"
    class_name: ClassVar[str] = "Contract"
    class_model_uri: ClassVar[URIRef] = DPV.Contract

    id: Union[str, ContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractId):
            self.id = ContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractByDomain(Contract):
    """
    A generic concept representing contracts categorised by specific domains
    which dictate the drafting and interpretation of contracts
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractByDomain"]
    class_class_curie: ClassVar[str] = "dpv:ContractByDomain"
    class_name: ClassVar[str] = "ContractByDomain"
    class_model_uri: ClassVar[URIRef] = DPV.ContractByDomain

    id: Union[str, ContractByDomainId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractByDomainId):
            self.id = ContractByDomainId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractByEntityType(Contract):
    """
    A generic concept representing contracts categorised by the type of
    entities involved - such as Businesses (B), Consumers (C), and
    Governments (G)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractByEntityType"]
    class_class_curie: ClassVar[str] = "dpv:ContractByEntityType"
    class_name: ClassVar[str] = "ContractByEntityType"
    class_model_uri: ClassVar[URIRef] = DPV.ContractByEntityType

    id: Union[str, ContractByEntityTypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractByEntityTypeId):
            self.id = ContractByEntityTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class B2BContract(ContractByEntityType):
    """
    A contract between two businesses
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["B2BContract"]
    class_class_curie: ClassVar[str] = "dpv:B2BContract"
    class_name: ClassVar[str] = "B2BContract"
    class_model_uri: ClassVar[URIRef] = DPV.B2BContract

    id: Union[str, B2BContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, B2BContractId):
            self.id = B2BContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class B2B2CContract(B2BContract):
    """
    A contract between two businesses who partner together to provide
    services to a consumer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["B2B2CContract"]
    class_class_curie: ClassVar[str] = "dpv:B2B2CContract"
    class_name: ClassVar[str] = "B2B2CContract"
    class_model_uri: ClassVar[URIRef] = DPV.B2B2CContract

    id: Union[str, B2B2CContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, B2B2CContractId):
            self.id = B2B2CContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class B2CContract(ContractByEntityType):
    """
    A contract between a business and a consumer where the business provides
    goods or services to the consumer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["B2CContract"]
    class_class_curie: ClassVar[str] = "dpv:B2CContract"
    class_name: ClassVar[str] = "B2CContract"
    class_model_uri: ClassVar[URIRef] = DPV.B2CContract

    id: Union[str, B2CContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, B2CContractId):
            self.id = B2CContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class C2BContract(ContractByEntityType):
    """
    A contract between a consumer and a business where the business
    purchases goods or services from the consumer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["C2BContract"]
    class_class_curie: ClassVar[str] = "dpv:C2BContract"
    class_name: ClassVar[str] = "C2BContract"
    class_model_uri: ClassVar[URIRef] = DPV.C2BContract

    id: Union[str, C2BContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, C2BContractId):
            self.id = C2BContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class C2CContract(ContractByEntityType):
    """
    A contract between two consumers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["C2CContract"]
    class_class_curie: ClassVar[str] = "dpv:C2CContract"
    class_name: ClassVar[str] = "C2CContract"
    class_model_uri: ClassVar[URIRef] = DPV.C2CContract

    id: Union[str, C2CContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, C2CContractId):
            self.id = C2CContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractByNegotiationType(Contract):
    """
    A generic concept representing contracts categorised based on their use
    or absence of negotiation in the contract forming process
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractByNegotiationType"]
    class_class_curie: ClassVar[str] = "dpv:ContractByNegotiationType"
    class_name: ClassVar[str] = "ContractByNegotiationType"
    class_model_uri: ClassVar[URIRef] = DPV.ContractByNegotiationType

    id: Union[str, ContractByNegotiationTypeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractByNegotiationTypeId):
            self.id = ContractByNegotiationTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractPerformance(Contract):
    """
    Fulfilment or performance of a contract involving specified processing
    of data or technologies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractPerformance"]
    class_class_curie: ClassVar[str] = "dpv:ContractPerformance"
    class_name: ClassVar[str] = "ContractPerformance"
    class_model_uri: ClassVar[URIRef] = DPV.ContractPerformance

    id: Union[str, ContractPerformanceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractPerformanceId):
            self.id = ContractPerformanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProcessingAgreement(Contract):
    """
    An agreement outlining conditions, criteria, obligations,
    responsibilities, and specifics for carrying out processing of data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataProcessingAgreement"]
    class_class_curie: ClassVar[str] = "dpv:DataProcessingAgreement"
    class_name: ClassVar[str] = "DataProcessingAgreement"
    class_model_uri: ClassVar[URIRef] = DPV.DataProcessingAgreement

    id: Union[str, DataProcessingAgreementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataProcessingAgreementId):
            self.id = DataProcessingAgreementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataControllerContract(DataProcessingAgreement):
    """
    Creation, completion, fulfilment, or performance of a contract, with
    Data Controllers as parties being Joint Data Controllers, and involving
    specified processing of data or technologies. NOTE: This concept is
    being deprecated - use dpv:JointDataControllersAgreement which has a
    more explicit definition of the entities involved and the intent of the
    contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataControllerContract"]
    class_class_curie: ClassVar[str] = "dpv:DataControllerContract"
    class_name: ClassVar[str] = "DataControllerContract"
    class_model_uri: ClassVar[URIRef] = DPV.DataControllerContract

    id: Union[str, DataControllerContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataControllerContractId):
            self.id = DataControllerContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProcessorContract(DataProcessingAgreement):
    """
    Creation, completion, fulfilment, or performance of a contract, with the
    Data Controller and Data Processor as parties, and involving specified
    processing of data or technologies. NOTE: This concept is being
    deprecated - use dpv:ControllerProcessorAgreement which has a more
    explicit definition of the entities involved and the intent of the
    contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataProcessorContract"]
    class_class_curie: ClassVar[str] = "dpv:DataProcessorContract"
    class_name: ClassVar[str] = "DataProcessorContract"
    class_model_uri: ClassVar[URIRef] = DPV.DataProcessorContract

    id: Union[str, DataProcessorContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataProcessorContractId):
            self.id = DataProcessorContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControllerProcessorAgreement(DataProcessorContract):
    """
    An agreement outlining conditions, criteria, obligations,
    responsibilities, and specifics for carrying out processing of data
    between a Data Controller and a Data Processor
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ControllerProcessorAgreement"]
    class_class_curie: ClassVar[str] = "dpv:ControllerProcessorAgreement"
    class_name: ClassVar[str] = "ControllerProcessorAgreement"
    class_model_uri: ClassVar[URIRef] = DPV.ControllerProcessorAgreement

    id: Union[str, ControllerProcessorAgreementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControllerProcessorAgreementId):
            self.id = ControllerProcessorAgreementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSubjectContract(DataProcessingAgreement):
    """
    Creation, completion, fulfilment, or performance of a contract, with the
    Data Controller and Data Subject as parties, and involving specified
    processing of data or technologies. NOTE: This concept is being
    deprecated - use dpv:ControllerDataSubjectAgreement which has a more
    explicit definition of the entities involved and the intent of the
    contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSubjectContract"]
    class_class_curie: ClassVar[str] = "dpv:DataSubjectContract"
    class_name: ClassVar[str] = "DataSubjectContract"
    class_model_uri: ClassVar[URIRef] = DPV.DataSubjectContract

    id: Union[str, DataSubjectContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSubjectContractId):
            self.id = DataSubjectContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControllerDataSubjectAgreement(DataSubjectContract):
    """
    An agreement outlining conditions, criteria, obligations,
    responsibilities, and specifics for carrying out processing of data
    between a Data Controller and a Data Subject
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ControllerDataSubjectAgreement"]
    class_class_curie: ClassVar[str] = "dpv:ControllerDataSubjectAgreement"
    class_name: ClassVar[str] = "ControllerDataSubjectAgreement"
    class_model_uri: ClassVar[URIRef] = DPV.ControllerDataSubjectAgreement

    id: Union[str, ControllerDataSubjectAgreementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ControllerDataSubjectAgreementId):
            self.id = ControllerDataSubjectAgreementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataTransferLegalBasis(LegalBasis):
    """
    Specific or special categories and instances of legal basis intended for
    justifying data transfers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataTransferLegalBasis"]
    class_class_curie: ClassVar[str] = "dpv:DataTransferLegalBasis"
    class_name: ClassVar[str] = "DataTransferLegalBasis"
    class_model_uri: ClassVar[URIRef] = DPV.DataTransferLegalBasis

    id: Union[str, DataTransferLegalBasisId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataTransferLegalBasisId):
            self.id = DataTransferLegalBasisId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DistributionAgreement(ContractByDomain):
    """
    A contract regarding supply of data or technologies between a
    distributor and a supplier
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DistributionAgreement"]
    class_class_curie: ClassVar[str] = "dpv:DistributionAgreement"
    class_name: ClassVar[str] = "DistributionAgreement"
    class_model_uri: ClassVar[URIRef] = DPV.DistributionAgreement

    id: Union[str, DistributionAgreementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DistributionAgreementId):
            self.id = DistributionAgreementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EmploymentContract(ContractByDomain):
    """
    A contract regarding employment between an employer and an employee
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EmploymentContract"]
    class_class_curie: ClassVar[str] = "dpv:EmploymentContract"
    class_name: ClassVar[str] = "EmploymentContract"
    class_model_uri: ClassVar[URIRef] = DPV.EmploymentContract

    id: Union[str, EmploymentContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmploymentContractId):
            self.id = EmploymentContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnterIntoContract(Contract):
    """
    Processing necessary to enter into contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EnterIntoContract"]
    class_class_curie: ClassVar[str] = "dpv:EnterIntoContract"
    class_name: ClassVar[str] = "EnterIntoContract"
    class_model_uri: ClassVar[URIRef] = DPV.EnterIntoContract

    id: Union[str, EnterIntoContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnterIntoContractId):
            self.id = EnterIntoContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class G2BContract(ContractByEntityType):
    """
    A contract between a government and a business
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["G2BContract"]
    class_class_curie: ClassVar[str] = "dpv:G2BContract"
    class_name: ClassVar[str] = "G2BContract"
    class_model_uri: ClassVar[URIRef] = DPV.G2BContract

    id: Union[str, G2BContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, G2BContractId):
            self.id = G2BContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class G2CContract(ContractByEntityType):
    """
    A contract between a government and consumers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["G2CContract"]
    class_class_curie: ClassVar[str] = "dpv:G2CContract"
    class_name: ClassVar[str] = "G2CContract"
    class_model_uri: ClassVar[URIRef] = DPV.G2CContract

    id: Union[str, G2CContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, G2CContractId):
            self.id = G2CContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class G2GContract(ContractByEntityType):
    """
    A contract between two governments or government departments or units
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["G2GContract"]
    class_class_curie: ClassVar[str] = "dpv:G2GContract"
    class_name: ClassVar[str] = "G2GContract"
    class_model_uri: ClassVar[URIRef] = DPV.G2GContract

    id: Union[str, G2GContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, G2GContractId):
            self.id = G2GContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class JointDataControllersAgreement(DataControllerContract):
    """
    An agreement outlining conditions, criteria, obligations,
    responsibilities, and specifics for carrying out processing of data
    between Controllers within a Joint Controllers relationship
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["JointDataControllersAgreement"]
    class_class_curie: ClassVar[str] = "dpv:JointDataControllersAgreement"
    class_name: ClassVar[str] = "JointDataControllersAgreement"
    class_model_uri: ClassVar[URIRef] = DPV.JointDataControllersAgreement

    id: Union[str, JointDataControllersAgreementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, JointDataControllersAgreementId):
            self.id = JointDataControllersAgreementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalObligation(LegalBasis):
    """
    Legal Obligation to conduct the specified activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalObligation"]
    class_class_curie: ClassVar[str] = "dpv:LegalObligation"
    class_name: ClassVar[str] = "LegalObligation"
    class_model_uri: ClassVar[URIRef] = DPV.LegalObligation

    id: Union[str, LegalObligationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalObligationId):
            self.id = LegalObligationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalObligationStatus(Status):
    """
    Status associated with use of Legal Obligation as a legal basis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalObligationStatus"]
    class_class_curie: ClassVar[str] = "dpv:LegalObligationStatus"
    class_name: ClassVar[str] = "LegalObligationStatus"
    class_model_uri: ClassVar[URIRef] = DPV.LegalObligationStatus

    id: Union[str, LegalObligationStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalObligationStatusId):
            self.id = LegalObligationStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalObligationCompleted(LegalObligationStatus):
    """
    Status where the legal obligation has been completed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalObligationCompleted"]
    class_class_curie: ClassVar[str] = "dpv:LegalObligationCompleted"
    class_name: ClassVar[str] = "LegalObligationCompleted"
    class_model_uri: ClassVar[URIRef] = DPV.LegalObligationCompleted

    id: Union[str, LegalObligationCompletedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalObligationCompletedId):
            self.id = LegalObligationCompletedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalObligationOngoing(LegalObligationStatus):
    """
    Status where the legal obligation is being fulfilled
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalObligationOngoing"]
    class_class_curie: ClassVar[str] = "dpv:LegalObligationOngoing"
    class_name: ClassVar[str] = "LegalObligationOngoing"
    class_model_uri: ClassVar[URIRef] = DPV.LegalObligationOngoing

    id: Union[str, LegalObligationOngoingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalObligationOngoingId):
            self.id = LegalObligationOngoingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalObligationPending(LegalObligationStatus):
    """
    Status where the legal obligation has not been started
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalObligationPending"]
    class_class_curie: ClassVar[str] = "dpv:LegalObligationPending"
    class_name: ClassVar[str] = "LegalObligationPending"
    class_model_uri: ClassVar[URIRef] = DPV.LegalObligationPending

    id: Union[str, LegalObligationPendingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalObligationPendingId):
            self.id = LegalObligationPendingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegitimateInterest(LegalBasis):
    """
    Legitimate Interests of a Party as justification for specified
    activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegitimateInterest"]
    class_class_curie: ClassVar[str] = "dpv:LegitimateInterest"
    class_name: ClassVar[str] = "LegitimateInterest"
    class_model_uri: ClassVar[URIRef] = DPV.LegitimateInterest

    id: Union[str, LegitimateInterestId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegitimateInterestId):
            self.id = LegitimateInterestId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegitimateInterestOfController(LegitimateInterest):
    """
    Legitimate Interests of a Data Controller in conducting specified
    activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegitimateInterestOfController"]
    class_class_curie: ClassVar[str] = "dpv:LegitimateInterestOfController"
    class_name: ClassVar[str] = "LegitimateInterestOfController"
    class_model_uri: ClassVar[URIRef] = DPV.LegitimateInterestOfController

    id: Union[str, LegitimateInterestOfControllerId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegitimateInterestOfControllerId):
            self.id = LegitimateInterestOfControllerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegitimateInterestOfDataSubject(LegitimateInterest):
    """
    Legitimate Interests of the Data Subject in conducting specified
    activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegitimateInterestOfDataSubject"]
    class_class_curie: ClassVar[str] = "dpv:LegitimateInterestOfDataSubject"
    class_name: ClassVar[str] = "LegitimateInterestOfDataSubject"
    class_model_uri: ClassVar[URIRef] = DPV.LegitimateInterestOfDataSubject

    id: Union[str, LegitimateInterestOfDataSubjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegitimateInterestOfDataSubjectId):
            self.id = LegitimateInterestOfDataSubjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegitimateInterestOfThirdParty(LegitimateInterest):
    """
    Legitimate Interests of a Third Party in conducting specified activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegitimateInterestOfThirdParty"]
    class_class_curie: ClassVar[str] = "dpv:LegitimateInterestOfThirdParty"
    class_name: ClassVar[str] = "LegitimateInterestOfThirdParty"
    class_model_uri: ClassVar[URIRef] = DPV.LegitimateInterestOfThirdParty

    id: Union[str, LegitimateInterestOfThirdPartyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegitimateInterestOfThirdPartyId):
            self.id = LegitimateInterestOfThirdPartyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegitimateInterestStatus(Status):
    """
    Status associated with use of Legitimate Interest as a legal basis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegitimateInterestStatus"]
    class_class_curie: ClassVar[str] = "dpv:LegitimateInterestStatus"
    class_name: ClassVar[str] = "LegitimateInterestStatus"
    class_model_uri: ClassVar[URIRef] = DPV.LegitimateInterestStatus

    id: Union[str, LegitimateInterestStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegitimateInterestStatusId):
            self.id = LegitimateInterestStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegitimateInterestInformed(LegitimateInterestStatus):
    """
    Status where the Legitimate Interest was informed to the data subject or
    other relevant entities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegitimateInterestInformed"]
    class_class_curie: ClassVar[str] = "dpv:LegitimateInterestInformed"
    class_name: ClassVar[str] = "LegitimateInterestInformed"
    class_model_uri: ClassVar[URIRef] = DPV.LegitimateInterestInformed

    id: Union[str, LegitimateInterestInformedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegitimateInterestInformedId):
            self.id = LegitimateInterestInformedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegitimateInterestNotObjected(LegitimateInterestStatus):
    """
    Status where the use of Legitimate Interest was not objected to
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegitimateInterestNotObjected"]
    class_class_curie: ClassVar[str] = "dpv:LegitimateInterestNotObjected"
    class_name: ClassVar[str] = "LegitimateInterestNotObjected"
    class_model_uri: ClassVar[URIRef] = DPV.LegitimateInterestNotObjected

    id: Union[str, LegitimateInterestNotObjectedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegitimateInterestNotObjectedId):
            self.id = LegitimateInterestNotObjectedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegitimateInterestObjected(LegitimateInterestStatus):
    """
    Status where the use of Legitimate Interest was objected to
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegitimateInterestObjected"]
    class_class_curie: ClassVar[str] = "dpv:LegitimateInterestObjected"
    class_name: ClassVar[str] = "LegitimateInterestObjected"
    class_model_uri: ClassVar[URIRef] = DPV.LegitimateInterestObjected

    id: Union[str, LegitimateInterestObjectedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegitimateInterestObjectedId):
            self.id = LegitimateInterestObjectedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegitimateInterestUninformed(LegitimateInterestStatus):
    """
    Status where the Legitimate Interest was not informed to the data
    subject or other relevant entities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegitimateInterestUninformed"]
    class_class_curie: ClassVar[str] = "dpv:LegitimateInterestUninformed"
    class_name: ClassVar[str] = "LegitimateInterestUninformed"
    class_model_uri: ClassVar[URIRef] = DPV.LegitimateInterestUninformed

    id: Union[str, LegitimateInterestUninformedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegitimateInterestUninformedId):
            self.id = LegitimateInterestUninformedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LicenseAgreement(ContractByDomain):
    """
    A Legal Document providing permission to utilise data or resource and
    outlining the conditions under which such use is considered valid
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LicenseAgreement"]
    class_class_curie: ClassVar[str] = "dpv:LicenseAgreement"
    class_name: ClassVar[str] = "LicenseAgreement"
    class_model_uri: ClassVar[URIRef] = DPV.LicenseAgreement

    id: Union[str, LicenseAgreementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LicenseAgreementId):
            self.id = LicenseAgreementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EULA(LicenseAgreement):
    """
    End User License Agreement is a contract entered into between a software
    (or service) developer or provider with the (end-)user
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EULA"]
    class_class_curie: ClassVar[str] = "dpv:EULA"
    class_name: ClassVar[str] = "EULA"
    class_model_uri: ClassVar[URIRef] = DPV.EULA

    id: Union[str, EULAId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EULAId):
            self.id = EULAId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LocationFixture(DpvThing):
    """
    The fixture of location refers to whether the location is fixed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LocationFixture"]
    class_class_curie: ClassVar[str] = "dpv:LocationFixture"
    class_name: ClassVar[str] = "LocationFixture"
    class_model_uri: ClassVar[URIRef] = DPV.LocationFixture

    id: Union[str, LocationFixtureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LocationFixtureId):
            self.id = LocationFixtureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DecentralisedLocations(LocationFixture):
    """
    Location that is spread across multiple separate areas with no
    distinction between their importance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DecentralisedLocations"]
    class_class_curie: ClassVar[str] = "dpv:DecentralisedLocations"
    class_name: ClassVar[str] = "DecentralisedLocations"
    class_model_uri: ClassVar[URIRef] = DPV.DecentralisedLocations

    id: Union[str, DecentralisedLocationsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DecentralisedLocationsId):
            self.id = DecentralisedLocationsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FederatedLocations(LocationFixture):
    """
    Location that is federated across multiple separate areas with
    designation of a primary or central location
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FederatedLocations"]
    class_class_curie: ClassVar[str] = "dpv:FederatedLocations"
    class_name: ClassVar[str] = "FederatedLocations"
    class_model_uri: ClassVar[URIRef] = DPV.FederatedLocations

    id: Union[str, FederatedLocationsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FederatedLocationsId):
            self.id = FederatedLocationsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixedLocation(LocationFixture):
    """
    Location that is fixed i.e. known to occur at a specific place
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FixedLocation"]
    class_class_curie: ClassVar[str] = "dpv:FixedLocation"
    class_name: ClassVar[str] = "FixedLocation"
    class_model_uri: ClassVar[URIRef] = DPV.FixedLocation

    id: Union[str, FixedLocationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FixedLocationId):
            self.id = FixedLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixedMultipleLocations(FixedLocation):
    """
    Location that is fixed with multiple places e.g. multiple cities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FixedMultipleLocations"]
    class_class_curie: ClassVar[str] = "dpv:FixedMultipleLocations"
    class_name: ClassVar[str] = "FixedMultipleLocations"
    class_model_uri: ClassVar[URIRef] = DPV.FixedMultipleLocations

    id: Union[str, FixedMultipleLocationsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FixedMultipleLocationsId):
            self.id = FixedMultipleLocationsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixedSingularLocation(FixedLocation):
    """
    Location that is fixed at a specific place e.g. a city
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FixedSingularLocation"]
    class_class_curie: ClassVar[str] = "dpv:FixedSingularLocation"
    class_name: ClassVar[str] = "FixedSingularLocation"
    class_model_uri: ClassVar[URIRef] = DPV.FixedSingularLocation

    id: Union[str, FixedSingularLocationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FixedSingularLocationId):
            self.id = FixedSingularLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LocationLocality(DpvLocation):
    """
    Locality refers to whether the specified location is local within some
    context, e.g. for the user
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LocationLocality"]
    class_class_curie: ClassVar[str] = "dpv:LocationLocality"
    class_name: ClassVar[str] = "LocationLocality"
    class_model_uri: ClassVar[URIRef] = DPV.LocationLocality

    id: Union[str, LocationLocalityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LocationLocalityId):
            self.id = LocationLocalityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LocalLocation(LocationLocality):
    """
    Location is local
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LocalLocation"]
    class_class_curie: ClassVar[str] = "dpv:LocalLocation"
    class_name: ClassVar[str] = "LocalLocation"
    class_model_uri: ClassVar[URIRef] = DPV.LocalLocation

    id: Union[str, LocalLocationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LocalLocationId):
            self.id = LocalLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NDA(LegalAgreement):
    """
    Non-disclosure Agreements e.g. preserving confidentiality of information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NDA"]
    class_class_curie: ClassVar[str] = "dpv:NDA"
    class_name: ClassVar[str] = "NDA"
    class_model_uri: ClassVar[URIRef] = DPV.NDA

    id: Union[str, NDAId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NDAId):
            self.id = NDAId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NegotiatedContract(ContractByNegotiationType):
    """
    A contract where the terms and conditions are determined with all
    parties having the ability to negotiate the terms and conditions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NegotiatedContract"]
    class_class_curie: ClassVar[str] = "dpv:NegotiatedContract"
    class_name: ClassVar[str] = "NegotiatedContract"
    class_model_uri: ClassVar[URIRef] = DPV.NegotiatedContract

    id: Union[str, NegotiatedContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NegotiatedContractId):
            self.id = NegotiatedContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OfficialAuthorityExerciseStatus(Status):
    """
    Status associated with use of Official Authority as a legal basis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OfficialAuthorityExerciseStatus"]
    class_class_curie: ClassVar[str] = "dpv:OfficialAuthorityExerciseStatus"
    class_name: ClassVar[str] = "OfficialAuthorityExerciseStatus"
    class_model_uri: ClassVar[URIRef] = DPV.OfficialAuthorityExerciseStatus

    id: Union[str, OfficialAuthorityExerciseStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OfficialAuthorityExerciseStatusId):
            self.id = OfficialAuthorityExerciseStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OfficialAuthorityExerciseCompleted(OfficialAuthorityExerciseStatus):
    """
    Status where the official authority has been exercised to completion
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OfficialAuthorityExerciseCompleted"]
    class_class_curie: ClassVar[str] = "dpv:OfficialAuthorityExerciseCompleted"
    class_name: ClassVar[str] = "OfficialAuthorityExerciseCompleted"
    class_model_uri: ClassVar[URIRef] = DPV.OfficialAuthorityExerciseCompleted

    id: Union[str, OfficialAuthorityExerciseCompletedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OfficialAuthorityExerciseCompletedId):
            self.id = OfficialAuthorityExerciseCompletedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OfficialAuthorityExerciseOngoing(OfficialAuthorityExerciseStatus):
    """
    Status where the official authority is being exercised
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OfficialAuthorityExerciseOngoing"]
    class_class_curie: ClassVar[str] = "dpv:OfficialAuthorityExerciseOngoing"
    class_name: ClassVar[str] = "OfficialAuthorityExerciseOngoing"
    class_model_uri: ClassVar[URIRef] = DPV.OfficialAuthorityExerciseOngoing

    id: Union[str, OfficialAuthorityExerciseOngoingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OfficialAuthorityExerciseOngoingId):
            self.id = OfficialAuthorityExerciseOngoingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OfficialAuthorityExercisePending(OfficialAuthorityExerciseStatus):
    """
    Status where the official authority has not been exercised
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OfficialAuthorityExercisePending"]
    class_class_curie: ClassVar[str] = "dpv:OfficialAuthorityExercisePending"
    class_name: ClassVar[str] = "OfficialAuthorityExercisePending"
    class_model_uri: ClassVar[URIRef] = DPV.OfficialAuthorityExercisePending

    id: Union[str, OfficialAuthorityExercisePendingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OfficialAuthorityExercisePendingId):
            self.id = OfficialAuthorityExercisePendingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OfficialAuthorityOfController(LegalBasis):
    """
    Activities are necessary or authorised through the official authority
    granted to or vested in the Data Controller
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OfficialAuthorityOfController"]
    class_class_curie: ClassVar[str] = "dpv:OfficialAuthorityOfController"
    class_name: ClassVar[str] = "OfficialAuthorityOfController"
    class_model_uri: ClassVar[URIRef] = DPV.OfficialAuthorityOfController

    id: Union[str, OfficialAuthorityOfControllerId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OfficialAuthorityOfControllerId):
            self.id = OfficialAuthorityOfControllerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivateLocation(LocalLocation):
    """
    Location that is not or cannot be accessed by the public and is
    controlled as a private space
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PrivateLocation"]
    class_class_curie: ClassVar[str] = "dpv:PrivateLocation"
    class_name: ClassVar[str] = "PrivateLocation"
    class_model_uri: ClassVar[URIRef] = DPV.PrivateLocation

    id: Union[str, PrivateLocationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivateLocationId):
            self.id = PrivateLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivateSpace(DpvLocation):
    """
    A space that is owned or controlled by a private entity and where access
    to members of the public is restricted
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PrivateSpace"]
    class_class_curie: ClassVar[str] = "dpv:PrivateSpace"
    class_name: ClassVar[str] = "PrivateSpace"
    class_model_uri: ClassVar[URIRef] = DPV.PrivateSpace

    id: Union[str, PrivateSpaceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivateSpaceId):
            self.id = PrivateSpaceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HybridPublicPrivateSpace(PrivateSpace):
    """
    A space that is a hybrid space i.e it has both public and private
    components - such as by having part of it be a private space or which is
    operated privately
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HybridPublicPrivateSpace"]
    class_class_curie: ClassVar[str] = "dpv:HybridPublicPrivateSpace"
    class_name: ClassVar[str] = "HybridPublicPrivateSpace"
    class_model_uri: ClassVar[URIRef] = DPV.HybridPublicPrivateSpace

    id: Union[str, HybridPublicPrivateSpaceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HybridPublicPrivateSpaceId):
            self.id = HybridPublicPrivateSpaceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonalSpace(PrivateSpace):
    """
    A private space associated with an individual in a personal capacity -
    such as their home or the space around their physical person e.g. my
    home or my room
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonalSpace"]
    class_class_curie: ClassVar[str] = "dpv:PersonalSpace"
    class_name: ClassVar[str] = "PersonalSpace"
    class_model_uri: ClassVar[URIRef] = DPV.PersonalSpace

    id: Union[str, PersonalSpaceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonalSpaceId):
            self.id = PersonalSpaceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivateCommunalSpace(PrivateSpace):
    """
    A space that is accessible to a group or a community within a private
    space and where members of the public do not have access to it e.g.
    society amenities such as gyms and pools
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PrivateCommunalSpace"]
    class_class_curie: ClassVar[str] = "dpv:PrivateCommunalSpace"
    class_name: ClassVar[str] = "PrivateCommunalSpace"
    class_model_uri: ClassVar[URIRef] = DPV.PrivateCommunalSpace

    id: Union[str, PrivateCommunalSpaceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivateCommunalSpaceId):
            self.id = PrivateCommunalSpaceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivatelyOperatedPublicSpace(HybridPublicPrivateSpace):
    """
    A space that is operated or managed by a private entity but which is
    accessible to the public e.g. a public bus station operated by a
    specific company
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PrivatelyOperatedPublicSpace"]
    class_class_curie: ClassVar[str] = "dpv:PrivatelyOperatedPublicSpace"
    class_name: ClassVar[str] = "PrivatelyOperatedPublicSpace"
    class_model_uri: ClassVar[URIRef] = DPV.PrivatelyOperatedPublicSpace

    id: Union[str, PrivatelyOperatedPublicSpaceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivatelyOperatedPublicSpaceId):
            self.id = PrivatelyOperatedPublicSpaceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivatelyOwnedPublicSpace(HybridPublicPrivateSpace):
    """
    A space that is privately owned but which is accessible and usable by
    the public - whether freely or through a process which is open to all
    members of the public e.g. hotel lobby, shopping mall atriums
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PrivatelyOwnedPublicSpace"]
    class_class_curie: ClassVar[str] = "dpv:PrivatelyOwnedPublicSpace"
    class_name: ClassVar[str] = "PrivatelyOwnedPublicSpace"
    class_model_uri: ClassVar[URIRef] = DPV.PrivatelyOwnedPublicSpace

    id: Union[str, PrivatelyOwnedPublicSpaceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivatelyOwnedPublicSpaceId):
            self.id = PrivatelyOwnedPublicSpaceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivatelyOwnedSpace(PrivateSpace):
    """
    A place that is privately owned e.g. offices, malls
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PrivatelyOwnedSpace"]
    class_class_curie: ClassVar[str] = "dpv:PrivatelyOwnedSpace"
    class_name: ClassVar[str] = "PrivatelyOwnedSpace"
    class_model_uri: ClassVar[URIRef] = DPV.PrivatelyOwnedSpace

    id: Union[str, PrivatelyOwnedSpaceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivatelyOwnedSpaceId):
            self.id = PrivatelyOwnedSpaceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicInterest(LegalBasis):
    """
    Activities are necessary or beneficial for interest of the public or
    society at large
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicInterest"]
    class_class_curie: ClassVar[str] = "dpv:PublicInterest"
    class_name: ClassVar[str] = "PublicInterest"
    class_model_uri: ClassVar[URIRef] = DPV.PublicInterest

    id: Union[str, PublicInterestId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicInterestId):
            self.id = PublicInterestId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicInterestStatus(Status):
    """
    Status associated with use of Public Interest as a legal basis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicInterestStatus"]
    class_class_curie: ClassVar[str] = "dpv:PublicInterestStatus"
    class_name: ClassVar[str] = "PublicInterestStatus"
    class_model_uri: ClassVar[URIRef] = DPV.PublicInterestStatus

    id: Union[str, PublicInterestStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicInterestStatusId):
            self.id = PublicInterestStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicInterestCompleted(PublicInterestStatus):
    """
    Status where the public interest activity has been completed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicInterestCompleted"]
    class_class_curie: ClassVar[str] = "dpv:PublicInterestCompleted"
    class_name: ClassVar[str] = "PublicInterestCompleted"
    class_model_uri: ClassVar[URIRef] = DPV.PublicInterestCompleted

    id: Union[str, PublicInterestCompletedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicInterestCompletedId):
            self.id = PublicInterestCompletedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicInterestObjected(PublicInterestStatus):
    """
    Status where the public interest activity was objected to by the Data
    Subject or another relevant entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicInterestObjected"]
    class_class_curie: ClassVar[str] = "dpv:PublicInterestObjected"
    class_name: ClassVar[str] = "PublicInterestObjected"
    class_model_uri: ClassVar[URIRef] = DPV.PublicInterestObjected

    id: Union[str, PublicInterestObjectedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicInterestObjectedId):
            self.id = PublicInterestObjectedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicInterestOngoing(PublicInterestStatus):
    """
    Status where the public interest activity is ongoing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicInterestOngoing"]
    class_class_curie: ClassVar[str] = "dpv:PublicInterestOngoing"
    class_name: ClassVar[str] = "PublicInterestOngoing"
    class_model_uri: ClassVar[URIRef] = DPV.PublicInterestOngoing

    id: Union[str, PublicInterestOngoingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicInterestOngoingId):
            self.id = PublicInterestOngoingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicInterestPending(PublicInterestStatus):
    """
    Status where the public interest activity has not started
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicInterestPending"]
    class_class_curie: ClassVar[str] = "dpv:PublicInterestPending"
    class_name: ClassVar[str] = "PublicInterestPending"
    class_model_uri: ClassVar[URIRef] = DPV.PublicInterestPending

    id: Union[str, PublicInterestPendingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicInterestPendingId):
            self.id = PublicInterestPendingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicLocation(LocalLocation):
    """
    Location that is or can be accessed by the public
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicLocation"]
    class_class_curie: ClassVar[str] = "dpv:PublicLocation"
    class_name: ClassVar[str] = "PublicLocation"
    class_model_uri: ClassVar[URIRef] = DPV.PublicLocation

    id: Union[str, PublicLocationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicLocationId):
            self.id = PublicLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicSpace(DpvLocation):
    """
    Any space that is accessible to the public or is owned by the public
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicSpace"]
    class_class_curie: ClassVar[str] = "dpv:PublicSpace"
    class_name: ClassVar[str] = "PublicSpace"
    class_model_uri: ClassVar[URIRef] = DPV.PublicSpace

    id: Union[str, PublicSpaceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicSpaceId):
            self.id = PublicSpaceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PubliclyAccessibleSpace(PublicSpace):
    """
    A space that is accessible to all members of the public e.g. parks,
    malls, train stations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PubliclyAccessibleSpace"]
    class_class_curie: ClassVar[str] = "dpv:PubliclyAccessibleSpace"
    class_name: ClassVar[str] = "PubliclyAccessibleSpace"
    class_model_uri: ClassVar[URIRef] = DPV.PubliclyAccessibleSpace

    id: Union[str, PubliclyAccessibleSpaceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PubliclyAccessibleSpaceId):
            self.id = PubliclyAccessibleSpaceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PubliclyOwnedSpace(PublicSpace):
    """
    A space that is owned by the public e.g. national parks, forests
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PubliclyOwnedSpace"]
    class_class_curie: ClassVar[str] = "dpv:PubliclyOwnedSpace"
    class_name: ClassVar[str] = "PubliclyOwnedSpace"
    class_model_uri: ClassVar[URIRef] = DPV.PubliclyOwnedSpace

    id: Union[str, PubliclyOwnedSpaceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PubliclyOwnedSpaceId):
            self.id = PubliclyOwnedSpaceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RandomLocation(LocationFixture):
    """
    Location that is random or unknown
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RandomLocation"]
    class_class_curie: ClassVar[str] = "dpv:RandomLocation"
    class_name: ClassVar[str] = "RandomLocation"
    class_model_uri: ClassVar[URIRef] = DPV.RandomLocation

    id: Union[str, RandomLocationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RandomLocationId):
            self.id = RandomLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RemoteLocation(LocationLocality):
    """
    Location is remote i.e. not local
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RemoteLocation"]
    class_class_curie: ClassVar[str] = "dpv:RemoteLocation"
    class_name: ClassVar[str] = "RemoteLocation"
    class_model_uri: ClassVar[URIRef] = DPV.RemoteLocation

    id: Union[str, RemoteLocationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RemoteLocationId):
            self.id = RemoteLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CloudLocation(RemoteLocation):
    """
    Location that is in the 'cloud' i.e. a logical location operated over
    the internet
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CloudLocation"]
    class_class_curie: ClassVar[str] = "dpv:CloudLocation"
    class_name: ClassVar[str] = "CloudLocation"
    class_model_uri: ClassVar[URIRef] = DPV.CloudLocation

    id: Union[str, CloudLocationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CloudLocationId):
            self.id = CloudLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SemiPrivateSpace(PrivateSpace):
    """
    A private space that acts as a shared space with other entities but
    which is still essentially private for the individuals e.g. a
    semi-private hospital room shared with another patient
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SemiPrivateSpace"]
    class_class_curie: ClassVar[str] = "dpv:SemiPrivateSpace"
    class_name: ClassVar[str] = "SemiPrivateSpace"
    class_model_uri: ClassVar[URIRef] = DPV.SemiPrivateSpace

    id: Union[str, SemiPrivateSpaceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SemiPrivateSpaceId):
            self.id = SemiPrivateSpaceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ServiceLevelAgreement(ContractByDomain):
    """
    A contract regarding the provision of a service which outlines the
    acceptable metrics and performance of the service for the consumer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ServiceLevelAgreement"]
    class_class_curie: ClassVar[str] = "dpv:ServiceLevelAgreement"
    class_name: ClassVar[str] = "ServiceLevelAgreement"
    class_model_uri: ClassVar[URIRef] = DPV.ServiceLevelAgreement

    id: Union[str, ServiceLevelAgreementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceLevelAgreementId):
            self.id = ServiceLevelAgreementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StandardFormContract(ContractByNegotiationType):
    """
    A contract where the terms and conditions are determined by one or more
    of the parties, and the other parties have negligible or no ability to
    negotiate the terms and conditions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["StandardFormContract"]
    class_class_curie: ClassVar[str] = "dpv:StandardFormContract"
    class_name: ClassVar[str] = "StandardFormContract"
    class_model_uri: ClassVar[URIRef] = DPV.StandardFormContract

    id: Union[str, StandardFormContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StandardFormContractId):
            self.id = StandardFormContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsumerStandardFormContract(StandardFormContract):
    """
    A contract where the terms and conditions are determined by parties in
    the role of a 'consumer' - whether an entity or an individual, and the
    other parties have negligible or no ability to negotiate the terms and
    conditions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsumerStandardFormContract"]
    class_class_curie: ClassVar[str] = "dpv:ConsumerStandardFormContract"
    class_name: ClassVar[str] = "ConsumerStandardFormContract"
    class_model_uri: ClassVar[URIRef] = DPV.ConsumerStandardFormContract

    id: Union[str, ConsumerStandardFormContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsumerStandardFormContractId):
            self.id = ConsumerStandardFormContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProviderStandardFormContract(StandardFormContract):
    """
    A contract where the terms and conditions are determined by parties in
    the role of a 'provider', and the other parties have negligible or no
    ability to negotiate the terms and conditions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProviderStandardFormContract"]
    class_class_curie: ClassVar[str] = "dpv:ProviderStandardFormContract"
    class_name: ClassVar[str] = "ProviderStandardFormContract"
    class_model_uri: ClassVar[URIRef] = DPV.ProviderStandardFormContract

    id: Union[str, ProviderStandardFormContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProviderStandardFormContractId):
            self.id = ProviderStandardFormContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StatisticalConfidentialityAgreement(LegalAgreement):
    """
    An agreement outlining conditions, criteria, obligations,
    responsibilities, and specifics for classification and management of
    'confidential data' based on a statistical framework
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["StatisticalConfidentialityAgreement"]
    class_class_curie: ClassVar[str] = "dpv:StatisticalConfidentialityAgreement"
    class_name: ClassVar[str] = "StatisticalConfidentialityAgreement"
    class_model_uri: ClassVar[URIRef] = DPV.StatisticalConfidentialityAgreement

    id: Union[str, StatisticalConfidentialityAgreementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StatisticalConfidentialityAgreementId):
            self.id = StatisticalConfidentialityAgreementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubProcessorAgreement(DataProcessingAgreement):
    """
    An agreement outlining conditions, criteria, obligations,
    responsibilities, and specifics for carrying out processing of data
    between a Data Processor and a Data (Sub-)Processor
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SubProcessorAgreement"]
    class_class_curie: ClassVar[str] = "dpv:SubProcessorAgreement"
    class_name: ClassVar[str] = "SubProcessorAgreement"
    class_model_uri: ClassVar[URIRef] = DPV.SubProcessorAgreement

    id: Union[str, SubProcessorAgreementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubProcessorAgreementId):
            self.id = SubProcessorAgreementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupraNationalUnion(DpvJurisdiction):
    """
    A political union of two or more countries with an establishment of
    common authority
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SupraNationalUnion"]
    class_class_curie: ClassVar[str] = "dpv:SupraNationalUnion"
    class_name: ClassVar[str] = "SupraNationalUnion"
    class_model_uri: ClassVar[URIRef] = DPV.SupraNationalUnion

    id: Union[str, SupraNationalUnionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SupraNationalUnionId):
            self.id = SupraNationalUnionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TermsOfService(ContractualClause):
    """
    Contractual clauses outlining the terms and conditions regarding the
    provision of a service, typically between a service provider and a
    service consumer, also know as 'Terms of Use' and 'Terms and Conditions'
    and commonly abbreviated as TOS, ToS, ToU, or T&C
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["TermsOfService"]
    class_class_curie: ClassVar[str] = "dpv:TermsOfService"
    class_name: ClassVar[str] = "TermsOfService"
    class_model_uri: ClassVar[URIRef] = DPV.TermsOfService

    id: Union[str, TermsOfServiceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TermsOfServiceId):
            self.id = TermsOfServiceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThirdCountry(DpvCountry):
    """
    Represents a country outside applicable or compatible jurisdiction as
    outlined in law
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ThirdCountry"]
    class_class_curie: ClassVar[str] = "dpv:ThirdCountry"
    class_name: ClassVar[str] = "ThirdCountry"
    class_model_uri: ClassVar[URIRef] = DPV.ThirdCountry

    id: Union[str, ThirdCountryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThirdCountryId):
            self.id = ThirdCountryId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThirdPartyContract(DataProcessingAgreement):
    """
    Creation, completion, fulfilment, or performance of a contract, with the
    Data Controller and Third Party as parties, and involving specified
    processing of data or technologies. NOTE: This concept is being
    deprecated - use dpv:ThirdPartyAgreement which has a more explicit
    definition of the entities involved and the intent of the contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ThirdPartyContract"]
    class_class_curie: ClassVar[str] = "dpv:ThirdPartyContract"
    class_name: ClassVar[str] = "ThirdPartyContract"
    class_model_uri: ClassVar[URIRef] = DPV.ThirdPartyContract

    id: Union[str, ThirdPartyContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThirdPartyContractId):
            self.id = ThirdPartyContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThirdPartyAgreement(ThirdPartyContract):
    """
    An agreement outlining conditions, criteria, obligations,
    responsibilities, and specifics for carrying out processing of data
    between a Data Controller or Processor and a Third Party
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ThirdPartyAgreement"]
    class_class_curie: ClassVar[str] = "dpv:ThirdPartyAgreement"
    class_name: ClassVar[str] = "ThirdPartyAgreement"
    class_model_uri: ClassVar[URIRef] = DPV.ThirdPartyAgreement

    id: Union[str, ThirdPartyAgreementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThirdPartyAgreementId):
            self.id = ThirdPartyAgreementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VariableLocation(LocationFixture):
    """
    Location that is known but is variable e.g. somewhere within a given
    area
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VariableLocation"]
    class_class_curie: ClassVar[str] = "dpv:VariableLocation"
    class_name: ClassVar[str] = "VariableLocation"
    class_model_uri: ClassVar[URIRef] = DPV.VariableLocation

    id: Union[str, VariableLocationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariableLocationId):
            self.id = VariableLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VitalInterest(LegalBasis):
    """
    Activities are necessary or required to protect vital interests of a
    data subject or other natural person
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VitalInterest"]
    class_class_curie: ClassVar[str] = "dpv:VitalInterest"
    class_name: ClassVar[str] = "VitalInterest"
    class_model_uri: ClassVar[URIRef] = DPV.VitalInterest

    id: Union[str, VitalInterestId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VitalInterestId):
            self.id = VitalInterestId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VitalInterestOfNaturalPerson(VitalInterest):
    """
    Activities are necessary or required to protect vital interests of a
    natural person
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VitalInterestOfNaturalPerson"]
    class_class_curie: ClassVar[str] = "dpv:VitalInterestOfNaturalPerson"
    class_name: ClassVar[str] = "VitalInterestOfNaturalPerson"
    class_model_uri: ClassVar[URIRef] = DPV.VitalInterestOfNaturalPerson

    id: Union[str, VitalInterestOfNaturalPersonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VitalInterestOfNaturalPersonId):
            self.id = VitalInterestOfNaturalPersonId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VitalInterestOfDataSubject(VitalInterestOfNaturalPerson):
    """
    Activities are necessary or required to protect vital interests of a
    data subject
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VitalInterestOfDataSubject"]
    class_class_curie: ClassVar[str] = "dpv:VitalInterestOfDataSubject"
    class_name: ClassVar[str] = "VitalInterestOfDataSubject"
    class_model_uri: ClassVar[URIRef] = DPV.VitalInterestOfDataSubject

    id: Union[str, VitalInterestOfDataSubjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VitalInterestOfDataSubjectId):
            self.id = VitalInterestOfDataSubjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VitalInterestStatus(Status):
    """
    Status associated with use of Vital Interest as a legal basis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VitalInterestStatus"]
    class_class_curie: ClassVar[str] = "dpv:VitalInterestStatus"
    class_name: ClassVar[str] = "VitalInterestStatus"
    class_model_uri: ClassVar[URIRef] = DPV.VitalInterestStatus

    id: Union[str, VitalInterestStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VitalInterestStatusId):
            self.id = VitalInterestStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VitalInterestCompleted(VitalInterestStatus):
    """
    Status where the vital interest activity has been completed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VitalInterestCompleted"]
    class_class_curie: ClassVar[str] = "dpv:VitalInterestCompleted"
    class_name: ClassVar[str] = "VitalInterestCompleted"
    class_model_uri: ClassVar[URIRef] = DPV.VitalInterestCompleted

    id: Union[str, VitalInterestCompletedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VitalInterestCompletedId):
            self.id = VitalInterestCompletedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VitalInterestObjected(VitalInterestStatus):
    """
    Status where the vital interest activity was objected to by the Data
    Subject or another relevant entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VitalInterestObjected"]
    class_class_curie: ClassVar[str] = "dpv:VitalInterestObjected"
    class_name: ClassVar[str] = "VitalInterestObjected"
    class_model_uri: ClassVar[URIRef] = DPV.VitalInterestObjected

    id: Union[str, VitalInterestObjectedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VitalInterestObjectedId):
            self.id = VitalInterestObjectedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VitalInterestOngoing(VitalInterestStatus):
    """
    Status where the vital interest activity is ongoing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VitalInterestOngoing"]
    class_class_curie: ClassVar[str] = "dpv:VitalInterestOngoing"
    class_name: ClassVar[str] = "VitalInterestOngoing"
    class_model_uri: ClassVar[URIRef] = DPV.VitalInterestOngoing

    id: Union[str, VitalInterestOngoingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VitalInterestOngoingId):
            self.id = VitalInterestOngoingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VitalInterestPending(VitalInterestStatus):
    """
    Status where the vital interest activity has not started
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VitalInterestPending"]
    class_class_curie: ClassVar[str] = "dpv:VitalInterestPending"
    class_name: ClassVar[str] = "VitalInterestPending"
    class_model_uri: ClassVar[URIRef] = DPV.VitalInterestPending

    id: Union[str, VitalInterestPendingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VitalInterestPendingId):
            self.id = VitalInterestPendingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WithinDevice(LocalLocation):
    """
    Location is local and entirely within a device, such as a smartphone
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["WithinDevice"]
    class_class_curie: ClassVar[str] = "dpv:WithinDevice"
    class_name: ClassVar[str] = "WithinDevice"
    class_model_uri: ClassVar[URIRef] = DPV.WithinDevice

    id: Union[str, WithinDeviceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WithinDeviceId):
            self.id = WithinDeviceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WithinPhysicalEnvironment(DpvLocation):
    """
    Location is local and entirely within a physical environment, such as a
    room
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["WithinPhysicalEnvironment"]
    class_class_curie: ClassVar[str] = "dpv:WithinPhysicalEnvironment"
    class_name: ClassVar[str] = "WithinPhysicalEnvironment"
    class_model_uri: ClassVar[URIRef] = DPV.WithinPhysicalEnvironment

    id: Union[str, WithinPhysicalEnvironmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WithinPhysicalEnvironmentId):
            self.id = WithinPhysicalEnvironmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WithinVirtualEnvironment(DpvLocation):
    """
    Location is local and entirely within a virtual environment, such as a
    software system
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["WithinVirtualEnvironment"]
    class_class_curie: ClassVar[str] = "dpv:WithinVirtualEnvironment"
    class_name: ClassVar[str] = "WithinVirtualEnvironment"
    class_model_uri: ClassVar[URIRef] = DPV.WithinVirtualEnvironment

    id: Union[str, WithinVirtualEnvironmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WithinVirtualEnvironmentId):
            self.id = WithinVirtualEnvironmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvEntity(DpvThing):
    """
    A human or non-human 'thing' that constitutes as an entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Entity"]
    class_class_curie: ClassVar[str] = "dpv:Entity"
    class_name: ClassVar[str] = "DpvEntity"
    class_model_uri: ClassVar[URIRef] = DPV.DpvEntity

    id: Union[str, DpvEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvEntityId):
            self.id = DpvEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvAgent(DpvEntity):
    """
    An Agent is a dpv:Entity that is (a) acting on behalf of another Entity;
    and (b) is authorised to do so by that Entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Agent"]
    class_class_curie: ClassVar[str] = "dpv:Agent"
    class_name: ClassVar[str] = "DpvAgent"
    class_model_uri: ClassVar[URIRef] = DPV.DpvAgent

    id: Union[str, DpvAgentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvAgentId):
            self.id = DpvAgentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalAgent(DpvAgent):
    """
    A Legal Agent is a Legal Entity that is authorised to act on behalf of
    another entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalAgent"]
    class_class_curie: ClassVar[str] = "dpv:LegalAgent"
    class_name: ClassVar[str] = "LegalAgent"
    class_model_uri: ClassVar[URIRef] = DPV.LegalAgent

    id: Union[str, LegalAgentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalAgentId):
            self.id = LegalAgentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalEntity(DpvEntity):
    """
    A human or non-human 'thing' that constitutes as an entity and which is
    recognised and defined in law
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalEntity"]
    class_class_curie: ClassVar[str] = "dpv:LegalEntity"
    class_name: ClassVar[str] = "LegalEntity"
    class_model_uri: ClassVar[URIRef] = DPV.LegalEntity

    id: Union[str, LegalEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalEntityId):
            self.id = LegalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CharityOrganisation(LegalEntity):
    """
    A nonprofit entity dedicated to providing assistance or raising funds
    for social, educational, religious, or other philanthropic purposes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CharityOrganisation"]
    class_class_curie: ClassVar[str] = "dpv:CharityOrganisation"
    class_name: ClassVar[str] = "CharityOrganisation"
    class_model_uri: ClassVar[URIRef] = DPV.CharityOrganisation

    id: Union[str, CharityOrganisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CharityOrganisationId):
            self.id = CharityOrganisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataController(LegalEntity):
    """
    The individual or organisation that decides (or controls) the purpose(s)
    of processing personal data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataController"]
    class_class_curie: ClassVar[str] = "dpv:DataController"
    class_name: ClassVar[str] = "DataController"
    class_model_uri: ClassVar[URIRef] = DPV.DataController

    id: Union[str, DataControllerId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataControllerId):
            self.id = DataControllerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataExporter(LegalEntity):
    """
    An entity that 'exports' data where exporting is considered a form of
    data transfer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataExporter"]
    class_class_curie: ClassVar[str] = "dpv:DataExporter"
    class_name: ClassVar[str] = "DataExporter"
    class_model_uri: ClassVar[URIRef] = DPV.DataExporter

    id: Union[str, DataExporterId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataExporterId):
            self.id = DataExporterId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvOrganisation(LegalEntity):
    """
    A general term reflecting a company or a business or a group acting as a
    unit
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Organisation"]
    class_class_curie: ClassVar[str] = "dpv:Organisation"
    class_name: ClassVar[str] = "DpvOrganisation"
    class_model_uri: ClassVar[URIRef] = DPV.DpvOrganisation

    id: Union[str, DpvOrganisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvOrganisationId):
            self.id = DpvOrganisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AcademicScientificOrganisation(DpvOrganisation):
    """
    Organisations related to academia or scientific pursuits e.g.
    Universities, Schools, Research Bodies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AcademicScientificOrganisation"]
    class_class_curie: ClassVar[str] = "dpv:AcademicScientificOrganisation"
    class_name: ClassVar[str] = "AcademicScientificOrganisation"
    class_model_uri: ClassVar[URIRef] = DPV.AcademicScientificOrganisation

    id: Union[str, AcademicScientificOrganisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcademicScientificOrganisationId):
            self.id = AcademicScientificOrganisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Clinic(DpvOrganisation):
    """
    An organisation that is a smaller healthcare facility offering
    outpatient medical services for diagnosis and treatment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Clinic"]
    class_class_curie: ClassVar[str] = "dpv:Clinic"
    class_name: ClassVar[str] = "Clinic"
    class_model_uri: ClassVar[URIRef] = DPV.Clinic

    id: Union[str, ClinicId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicId):
            self.id = ClinicId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvRecipient(LegalEntity):
    """
    Entities that receive data or technologies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Recipient"]
    class_class_curie: ClassVar[str] = "dpv:Recipient"
    class_name: ClassVar[str] = "DpvRecipient"
    class_model_uri: ClassVar[URIRef] = DPV.DpvRecipient

    id: Union[str, DpvRecipientId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvRecipientId):
            self.id = DpvRecipientId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataImporter(DpvRecipient):
    """
    An entity that 'imports' data where importing is considered a form of
    data transfer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataImporter"]
    class_class_curie: ClassVar[str] = "dpv:DataImporter"
    class_name: ClassVar[str] = "DataImporter"
    class_model_uri: ClassVar[URIRef] = DPV.DataImporter

    id: Union[str, DataImporterId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataImporterId):
            self.id = DataImporterId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProcessor(DpvRecipient):
    """
    A ‘processor’ means a natural or legal person, public authority, agency
    or other body which processes data on behalf of the controller.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataProcessor"]
    class_class_curie: ClassVar[str] = "dpv:DataProcessor"
    class_name: ClassVar[str] = "DataProcessor"
    class_model_uri: ClassVar[URIRef] = DPV.DataProcessor

    id: Union[str, DataProcessorId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataProcessorId):
            self.id = DataProcessorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSubProcessor(DataProcessor):
    """
    A 'sub-processor' is a processor engaged by another processor
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSubProcessor"]
    class_class_curie: ClassVar[str] = "dpv:DataSubProcessor"
    class_name: ClassVar[str] = "DataSubProcessor"
    class_model_uri: ClassVar[URIRef] = DPV.DataSubProcessor

    id: Union[str, DataSubProcessorId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSubProcessorId):
            self.id = DataSubProcessorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EducationalOrganisation(DpvOrganisation):
    """
    An organisation focused on delivering formal or informal education,
    training, or research
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EducationalOrganisation"]
    class_class_curie: ClassVar[str] = "dpv:EducationalOrganisation"
    class_name: ClassVar[str] = "EducationalOrganisation"
    class_model_uri: ClassVar[URIRef] = DPV.EducationalOrganisation

    id: Union[str, EducationalOrganisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EducationalOrganisationId):
            self.id = EducationalOrganisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EmergencyServiceProvider(DpvOrganisation):
    """
    An organisation tasked with providing emergency services such as by
    responding rapidly to urgent situations to protect lives, property, and
    the environment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EmergencyServiceProvider"]
    class_class_curie: ClassVar[str] = "dpv:EmergencyServiceProvider"
    class_name: ClassVar[str] = "EmergencyServiceProvider"
    class_model_uri: ClassVar[URIRef] = DPV.EmergencyServiceProvider

    id: Union[str, EmergencyServiceProviderId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmergencyServiceProviderId):
            self.id = EmergencyServiceProviderId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AmbulanceProvider(EmergencyServiceProvider):
    """
    An organisation that that offers transportation and medical care to
    patients requiring urgent medical attention
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AmbulanceProvider"]
    class_class_curie: ClassVar[str] = "dpv:AmbulanceProvider"
    class_name: ClassVar[str] = "AmbulanceProvider"
    class_model_uri: ClassVar[URIRef] = DPV.AmbulanceProvider

    id: Union[str, AmbulanceProviderId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AmbulanceProviderId):
            self.id = AmbulanceProviderId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EmergencyHealthcareProvider(EmergencyServiceProvider):
    """
    An organisation that is an emergency service provider focused on
    delivering immediate medical care to patients in critical or
    life-threatening situations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EmergencyHealthcareProvider"]
    class_class_curie: ClassVar[str] = "dpv:EmergencyHealthcareProvider"
    class_name: ClassVar[str] = "EmergencyHealthcareProvider"
    class_model_uri: ClassVar[URIRef] = DPV.EmergencyHealthcareProvider

    id: Union[str, EmergencyHealthcareProviderId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmergencyHealthcareProviderId):
            self.id = EmergencyHealthcareProviderId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FireDepartment(EmergencyServiceProvider):
    """
    An organisation that is an emergency service provider for fire
    prevention, firefighting, and rescue services
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FireDepartment"]
    class_class_curie: ClassVar[str] = "dpv:FireDepartment"
    class_name: ClassVar[str] = "FireDepartment"
    class_model_uri: ClassVar[URIRef] = DPV.FireDepartment

    id: Union[str, FireDepartmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FireDepartmentId):
            self.id = FireDepartmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ForProfitOrganisation(DpvOrganisation):
    """
    An organisation that aims to achieve profit as its primary goal
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ForProfitOrganisation"]
    class_class_curie: ClassVar[str] = "dpv:ForProfitOrganisation"
    class_name: ClassVar[str] = "ForProfitOrganisation"
    class_model_uri: ClassVar[URIRef] = DPV.ForProfitOrganisation

    id: Union[str, ForProfitOrganisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ForProfitOrganisationId):
            self.id = ForProfitOrganisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GovernmentalOrganisation(DpvOrganisation):
    """
    An organisation managed or part of government
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["GovernmentalOrganisation"]
    class_class_curie: ClassVar[str] = "dpv:GovernmentalOrganisation"
    class_name: ClassVar[str] = "GovernmentalOrganisation"
    class_model_uri: ClassVar[URIRef] = DPV.GovernmentalOrganisation

    id: Union[str, GovernmentalOrganisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GovernmentalOrganisationId):
            self.id = GovernmentalOrganisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvAuthority(GovernmentalOrganisation):
    """
    An authority with the power to create or enforce laws, or determine
    their compliance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Authority"]
    class_class_curie: ClassVar[str] = "dpv:Authority"
    class_name: ClassVar[str] = "DpvAuthority"
    class_model_uri: ClassVar[URIRef] = DPV.DpvAuthority

    id: Union[str, DpvAuthorityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvAuthorityId):
            self.id = DpvAuthorityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProtectionAuthority(DpvAuthority):
    """
    An authority tasked with overseeing legal compliance regarding privacy
    and data protection laws.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataProtectionAuthority"]
    class_class_curie: ClassVar[str] = "dpv:DataProtectionAuthority"
    class_name: ClassVar[str] = "DataProtectionAuthority"
    class_model_uri: ClassVar[URIRef] = DPV.DataProtectionAuthority

    id: Union[str, DataProtectionAuthorityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataProtectionAuthorityId):
            self.id = DataProtectionAuthorityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HealthcareOrganisation(DpvOrganisation):
    """
    An organisation that delivers medical services, promotes health, and
    provides care for individuals and communities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HealthcareOrganisation"]
    class_class_curie: ClassVar[str] = "dpv:HealthcareOrganisation"
    class_name: ClassVar[str] = "HealthcareOrganisation"
    class_model_uri: ClassVar[URIRef] = DPV.HealthcareOrganisation

    id: Union[str, HealthcareOrganisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HealthcareOrganisationId):
            self.id = HealthcareOrganisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Hospital(DpvOrganisation):
    """
    An organisation that provides comprehensive medical treatment, including
    emergency care, surgeries, and inpatient services
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Hospital"]
    class_class_curie: ClassVar[str] = "dpv:Hospital"
    class_name: ClassVar[str] = "Hospital"
    class_model_uri: ClassVar[URIRef] = DPV.Hospital

    id: Union[str, HospitalId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HospitalId):
            self.id = HospitalId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanSubject(LegalEntity):
    """
    The individual (or category of individuals) that is the subject within
    some context such as personal data (dpv:DataSubject) or technology
    (tech:Subject)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HumanSubject"]
    class_class_curie: ClassVar[str] = "dpv:HumanSubject"
    class_name: ClassVar[str] = "HumanSubject"
    class_model_uri: ClassVar[URIRef] = DPV.HumanSubject

    id: Union[str, HumanSubjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanSubjectId):
            self.id = HumanSubjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Adult(HumanSubject):
    """
    A natural person that is not a child i.e. has attained some legally
    specified age of adulthood
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Adult"]
    class_class_curie: ClassVar[str] = "dpv:Adult"
    class_name: ClassVar[str] = "Adult"
    class_model_uri: ClassVar[URIRef] = DPV.Adult

    id: Union[str, AdultId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdultId):
            self.id = AdultId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Applicant(HumanSubject):
    """
    Humans that are applicants in some context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Applicant"]
    class_class_curie: ClassVar[str] = "dpv:Applicant"
    class_name: ClassVar[str] = "Applicant"
    class_model_uri: ClassVar[URIRef] = DPV.Applicant

    id: Union[str, ApplicantId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ApplicantId):
            self.id = ApplicantId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Citizen(HumanSubject):
    """
    Humans that are citizens (for a jurisdiction)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Citizen"]
    class_class_curie: ClassVar[str] = "dpv:Citizen"
    class_name: ClassVar[str] = "Citizen"
    class_model_uri: ClassVar[URIRef] = DPV.Citizen

    id: Union[str, CitizenId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CitizenId):
            self.id = CitizenId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSubject(HumanSubject):
    """
    The individual (or category of individuals) whose personal data is being
    processed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSubject"]
    class_class_curie: ClassVar[str] = "dpv:DataSubject"
    class_name: ClassVar[str] = "DataSubject"
    class_model_uri: ClassVar[URIRef] = DPV.DataSubject

    id: Union[str, DataSubjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSubjectId):
            self.id = DataSubjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvConsumer(HumanSubject):
    """
    Humans that consume goods or services for direct use
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Consumer"]
    class_class_curie: ClassVar[str] = "dpv:Consumer"
    class_name: ClassVar[str] = "DpvConsumer"
    class_model_uri: ClassVar[URIRef] = DPV.DpvConsumer

    id: Union[str, DpvConsumerId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvConsumerId):
            self.id = DpvConsumerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvCustomer(HumanSubject):
    """
    Humans that purchase goods or services
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Customer"]
    class_class_curie: ClassVar[str] = "dpv:Customer"
    class_name: ClassVar[str] = "DpvCustomer"
    class_model_uri: ClassVar[URIRef] = DPV.DpvCustomer

    id: Union[str, DpvCustomerId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvCustomerId):
            self.id = DpvCustomerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Client(DpvCustomer):
    """
    Humans that are clients or recipients of services
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Client"]
    class_class_curie: ClassVar[str] = "dpv:Client"
    class_name: ClassVar[str] = "Client"
    class_model_uri: ClassVar[URIRef] = DPV.Client

    id: Union[str, ClientId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClientId):
            self.id = ClientId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvUser(HumanSubject):
    """
    Humans that use service(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["User"]
    class_class_curie: ClassVar[str] = "dpv:User"
    class_name: ClassVar[str] = "DpvUser"
    class_model_uri: ClassVar[URIRef] = DPV.DpvUser

    id: Union[str, DpvUserId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvUserId):
            self.id = DpvUserId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Employee(HumanSubject):
    """
    Humans that are employees
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Employee"]
    class_class_curie: ClassVar[str] = "dpv:Employee"
    class_name: ClassVar[str] = "Employee"
    class_model_uri: ClassVar[URIRef] = DPV.Employee

    id: Union[str, EmployeeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EmployeeId):
            self.id = EmployeeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GuardianOfHuman(HumanSubject):
    """
    Guardian(s) of humans
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["GuardianOfHuman"]
    class_class_curie: ClassVar[str] = "dpv:GuardianOfHuman"
    class_name: ClassVar[str] = "GuardianOfHuman"
    class_model_uri: ClassVar[URIRef] = DPV.GuardianOfHuman

    id: Union[str, GuardianOfHumanId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GuardianOfHumanId):
            self.id = GuardianOfHumanId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GuardianOfDataSubject(GuardianOfHuman):
    """
    Guardian(s) of data subjects such as children
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["GuardianOfDataSubject"]
    class_class_curie: ClassVar[str] = "dpv:GuardianOfDataSubject"
    class_name: ClassVar[str] = "GuardianOfDataSubject"
    class_model_uri: ClassVar[URIRef] = DPV.GuardianOfDataSubject

    id: Union[str, GuardianOfDataSubjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GuardianOfDataSubjectId):
            self.id = GuardianOfDataSubjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Immigrant(HumanSubject):
    """
    Humans that are immigrants (for a jurisdiction)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Immigrant"]
    class_class_curie: ClassVar[str] = "dpv:Immigrant"
    class_name: ClassVar[str] = "Immigrant"
    class_model_uri: ClassVar[URIRef] = DPV.Immigrant

    id: Union[str, ImmigrantId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImmigrantId):
            self.id = ImmigrantId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IndustryConsortium(DpvOrganisation):
    """
    A consortium established and comprising on industry organisations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["IndustryConsortium"]
    class_class_curie: ClassVar[str] = "dpv:IndustryConsortium"
    class_name: ClassVar[str] = "IndustryConsortium"
    class_model_uri: ClassVar[URIRef] = DPV.IndustryConsortium

    id: Union[str, IndustryConsortiumId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IndustryConsortiumId):
            self.id = IndustryConsortiumId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InternationalOrganisation(DpvOrganisation):
    """
    An organisation and its subordinate bodies governed by public
    international law, or any other body which is set up by, or on the basis
    of, an agreement between two or more countries
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InternationalOrganisation"]
    class_class_curie: ClassVar[str] = "dpv:InternationalOrganisation"
    class_name: ClassVar[str] = "InternationalOrganisation"
    class_model_uri: ClassVar[URIRef] = DPV.InternationalOrganisation

    id: Union[str, InternationalOrganisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InternationalOrganisationId):
            self.id = InternationalOrganisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class JobApplicant(HumanSubject):
    """
    Humans that apply for jobs or employments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["JobApplicant"]
    class_class_curie: ClassVar[str] = "dpv:JobApplicant"
    class_name: ClassVar[str] = "JobApplicant"
    class_model_uri: ClassVar[URIRef] = DPV.JobApplicant

    id: Union[str, JobApplicantId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, JobApplicantId):
            self.id = JobApplicantId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class JointDataControllers(DataController):
    """
    A group of Data Controllers that jointly determine the purposes and
    means of processing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["JointDataControllers"]
    class_class_curie: ClassVar[str] = "dpv:JointDataControllers"
    class_name: ClassVar[str] = "JointDataControllers"
    class_model_uri: ClassVar[URIRef] = DPV.JointDataControllers

    id: Union[str, JointDataControllersId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, JointDataControllersId):
            self.id = JointDataControllersId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class JudicialOrganisation(DpvOrganisation):
    """
    An organisation involved in interpreting and applying the law, resolving
    disputes, and administering justice as part of the judicial system
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["JudicialOrganisation"]
    class_class_curie: ClassVar[str] = "dpv:JudicialOrganisation"
    class_name: ClassVar[str] = "JudicialOrganisation"
    class_model_uri: ClassVar[URIRef] = DPV.JudicialOrganisation

    id: Union[str, JudicialOrganisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, JudicialOrganisationId):
            self.id = JudicialOrganisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LawEnforcementOrganisation(DpvOrganisation):
    """
    An organisation that is an agency responsible for enforcing laws,
    maintaining public order, and ensuring public safety
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LawEnforcementOrganisation"]
    class_class_curie: ClassVar[str] = "dpv:LawEnforcementOrganisation"
    class_name: ClassVar[str] = "LawEnforcementOrganisation"
    class_model_uri: ClassVar[URIRef] = DPV.LawEnforcementOrganisation

    id: Union[str, LawEnforcementOrganisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LawEnforcementOrganisationId):
            self.id = LawEnforcementOrganisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Member(HumanSubject):
    """
    Humans that are members of a group, organisation, or other collectives
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Member"]
    class_class_curie: ClassVar[str] = "dpv:Member"
    class_name: ClassVar[str] = "Member"
    class_model_uri: ClassVar[URIRef] = DPV.Member

    id: Union[str, MemberId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MemberId):
            self.id = MemberId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NationalAuthority(DpvAuthority):
    """
    An authority tasked with overseeing legal compliance for a nation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NationalAuthority"]
    class_class_curie: ClassVar[str] = "dpv:NationalAuthority"
    class_name: ClassVar[str] = "NationalAuthority"
    class_model_uri: ClassVar[URIRef] = DPV.NationalAuthority

    id: Union[str, NationalAuthorityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NationalAuthorityId):
            self.id = NationalAuthorityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NaturalPerson(DpvEntity):
    """
    A human
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NaturalPerson"]
    class_class_curie: ClassVar[str] = "dpv:NaturalPerson"
    class_name: ClassVar[str] = "NaturalPerson"
    class_model_uri: ClassVar[URIRef] = DPV.NaturalPerson

    id: Union[str, NaturalPersonId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NaturalPersonId):
            self.id = NaturalPersonId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NonCitizen(HumanSubject):
    """
    Humans that are not citizens (for a jurisdiction)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NonCitizen"]
    class_class_curie: ClassVar[str] = "dpv:NonCitizen"
    class_name: ClassVar[str] = "NonCitizen"
    class_model_uri: ClassVar[URIRef] = DPV.NonCitizen

    id: Union[str, NonCitizenId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NonCitizenId):
            self.id = NonCitizenId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NonGovernmentalOrganisation(DpvOrganisation):
    """
    An organisation not part of or independent from the government
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NonGovernmentalOrganisation"]
    class_class_curie: ClassVar[str] = "dpv:NonGovernmentalOrganisation"
    class_name: ClassVar[str] = "NonGovernmentalOrganisation"
    class_model_uri: ClassVar[URIRef] = DPV.NonGovernmentalOrganisation

    id: Union[str, NonGovernmentalOrganisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NonGovernmentalOrganisationId):
            self.id = NonGovernmentalOrganisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NonProfitOrganisation(DpvOrganisation):
    """
    An organisation that does not aim to achieve profit as its primary goal
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NonProfitOrganisation"]
    class_class_curie: ClassVar[str] = "dpv:NonProfitOrganisation"
    class_name: ClassVar[str] = "NonProfitOrganisation"
    class_model_uri: ClassVar[URIRef] = DPV.NonProfitOrganisation

    id: Union[str, NonProfitOrganisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NonProfitOrganisationId):
            self.id = NonProfitOrganisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrganisationalUnit(DpvEntity):
    """
    Entity within an organisation that does not constitute as a separate
    legal entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OrganisationalUnit"]
    class_class_curie: ClassVar[str] = "dpv:OrganisationalUnit"
    class_name: ClassVar[str] = "OrganisationalUnit"
    class_model_uri: ClassVar[URIRef] = DPV.OrganisationalUnit

    id: Union[str, OrganisationalUnitId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganisationalUnitId):
            self.id = OrganisationalUnitId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParentLegalEntity(DpvOrganisation):
    """
    A legal entity that has one or more subsidiary entities operating under
    it
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ParentLegalEntity"]
    class_class_curie: ClassVar[str] = "dpv:ParentLegalEntity"
    class_name: ClassVar[str] = "ParentLegalEntity"
    class_model_uri: ClassVar[URIRef] = DPV.ParentLegalEntity

    id: Union[str, ParentLegalEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParentLegalEntityId):
            self.id = ParentLegalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParentOfHuman(HumanSubject):
    """
    Parent(s) of humans
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ParentOfHuman"]
    class_class_curie: ClassVar[str] = "dpv:ParentOfHuman"
    class_name: ClassVar[str] = "ParentOfHuman"
    class_model_uri: ClassVar[URIRef] = DPV.ParentOfHuman

    id: Union[str, ParentOfHumanId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParentOfHumanId):
            self.id = ParentOfHumanId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParentOfDataSubject(ParentOfHuman):
    """
    Parent(s) of data subjects such as children
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ParentOfDataSubject"]
    class_class_curie: ClassVar[str] = "dpv:ParentOfDataSubject"
    class_name: ClassVar[str] = "ParentOfDataSubject"
    class_model_uri: ClassVar[URIRef] = DPV.ParentOfDataSubject

    id: Union[str, ParentOfDataSubjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParentOfDataSubjectId):
            self.id = ParentOfDataSubjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Participant(HumanSubject):
    """
    Humans that participate in some context such as volunteers in a function
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Participant"]
    class_class_curie: ClassVar[str] = "dpv:Participant"
    class_name: ClassVar[str] = "Participant"
    class_model_uri: ClassVar[URIRef] = DPV.Participant

    id: Union[str, ParticipantId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParticipantId):
            self.id = ParticipantId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Patient(HumanSubject):
    """
    Humans that receive medical attention, treatment, care, advice, or other
    health related services
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Patient"]
    class_class_curie: ClassVar[str] = "dpv:Patient"
    class_name: ClassVar[str] = "Patient"
    class_model_uri: ClassVar[URIRef] = DPV.Patient

    id: Union[str, PatientId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PatientId):
            self.id = PatientId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivateSectorBody(LegalEntity):
    """
    An organisation owned and operated by private individuals or companies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PrivateSectorBody"]
    class_class_curie: ClassVar[str] = "dpv:PrivateSectorBody"
    class_name: ClassVar[str] = "PrivateSectorBody"
    class_model_uri: ClassVar[URIRef] = DPV.PrivateSectorBody

    id: Union[str, PrivateSectorBodyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivateSectorBodyId):
            self.id = PrivateSectorBodyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicRegisterOfEntities(DpvThing):
    """
    A publicly available list of entities e.g. to indicate which entities
    perform a certain activity within a certain location or jurisdiction
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicRegisterOfEntities"]
    class_class_curie: ClassVar[str] = "dpv:PublicRegisterOfEntities"
    class_name: ClassVar[str] = "PublicRegisterOfEntities"
    class_model_uri: ClassVar[URIRef] = DPV.PublicRegisterOfEntities

    id: Union[str, PublicRegisterOfEntitiesId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicRegisterOfEntitiesId):
            self.id = PublicRegisterOfEntitiesId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicSectorBody(LegalEntity):
    """
    A government-controlled organisation that provides services or goods to
    the public
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicSectorBody"]
    class_class_curie: ClassVar[str] = "dpv:PublicSectorBody"
    class_name: ClassVar[str] = "PublicSectorBody"
    class_model_uri: ClassVar[URIRef] = DPV.PublicSectorBody

    id: Union[str, PublicSectorBodyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicSectorBodyId):
            self.id = PublicSectorBodyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RegionalAuthority(DpvAuthority):
    """
    An authority tasked with overseeing legal compliance for a region
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RegionalAuthority"]
    class_class_curie: ClassVar[str] = "dpv:RegionalAuthority"
    class_name: ClassVar[str] = "RegionalAuthority"
    class_model_uri: ClassVar[URIRef] = DPV.RegionalAuthority

    id: Union[str, RegionalAuthorityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegionalAuthorityId):
            self.id = RegionalAuthorityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReligiousAssociations(DpvOrganisation):
    """
    An organisations that supports the practice, promotion, and management
    of religious activities and beliefs
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ReligiousAssociations"]
    class_class_curie: ClassVar[str] = "dpv:ReligiousAssociations"
    class_name: ClassVar[str] = "ReligiousAssociations"
    class_model_uri: ClassVar[URIRef] = DPV.ReligiousAssociations

    id: Union[str, ReligiousAssociationsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReligiousAssociationsId):
            self.id = ReligiousAssociationsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Representative(LegalEntity):
    """
    A representative of a legal entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Representative"]
    class_class_curie: ClassVar[str] = "dpv:Representative"
    class_name: ClassVar[str] = "Representative"
    class_model_uri: ClassVar[URIRef] = DPV.Representative

    id: Union[str, RepresentativeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RepresentativeId):
            self.id = RepresentativeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProtectionOfficer(Representative):
    """
    An entity within or authorised by an organisation to monitor internal
    compliance, inform and advise on data protection obligations and act as
    a contact point for data subjects and the supervisory authority.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataProtectionOfficer"]
    class_class_curie: ClassVar[str] = "dpv:DataProtectionOfficer"
    class_name: ClassVar[str] = "DataProtectionOfficer"
    class_model_uri: ClassVar[URIRef] = DPV.DataProtectionOfficer

    id: Union[str, DataProtectionOfficerId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataProtectionOfficerId):
            self.id = DataProtectionOfficerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SMEOrganisation(LegalEntity):
    """
    An organisation that is characterised as a Small or Medium-sized
    Enterprise based on limited staff and revenue
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SMEOrganisation"]
    class_class_curie: ClassVar[str] = "dpv:SMEOrganisation"
    class_name: ClassVar[str] = "SMEOrganisation"
    class_model_uri: ClassVar[URIRef] = DPV.SMEOrganisation

    id: Union[str, SMEOrganisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SMEOrganisationId):
            self.id = SMEOrganisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ServiceConsumer(LegalEntity):
    """
    The entity that consumes or receives the service
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ServiceConsumer"]
    class_class_curie: ClassVar[str] = "dpv:ServiceConsumer"
    class_name: ClassVar[str] = "ServiceConsumer"
    class_model_uri: ClassVar[URIRef] = DPV.ServiceConsumer

    id: Union[str, ServiceConsumerId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceConsumerId):
            self.id = ServiceConsumerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ServiceProvider(LegalEntity):
    """
    The entity that provides a service
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ServiceProvider"]
    class_class_curie: ClassVar[str] = "dpv:ServiceProvider"
    class_name: ClassVar[str] = "ServiceProvider"
    class_model_uri: ClassVar[URIRef] = DPV.ServiceProvider

    id: Union[str, ServiceProviderId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceProviderId):
            self.id = ServiceProviderId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StartupOrganisation(LegalEntity):
    """
    An organisation that is newly established and is nascent in terms of
    available resources
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["StartupOrganisation"]
    class_class_curie: ClassVar[str] = "dpv:StartupOrganisation"
    class_name: ClassVar[str] = "StartupOrganisation"
    class_model_uri: ClassVar[URIRef] = DPV.StartupOrganisation

    id: Union[str, StartupOrganisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StartupOrganisationId):
            self.id = StartupOrganisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Student(HumanSubject):
    """
    Humans that are students
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Student"]
    class_class_curie: ClassVar[str] = "dpv:Student"
    class_name: ClassVar[str] = "Student"
    class_model_uri: ClassVar[URIRef] = DPV.Student

    id: Union[str, StudentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudentId):
            self.id = StudentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Subscriber(HumanSubject):
    """
    Humans that subscribe to service(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Subscriber"]
    class_class_curie: ClassVar[str] = "dpv:Subscriber"
    class_name: ClassVar[str] = "Subscriber"
    class_model_uri: ClassVar[URIRef] = DPV.Subscriber

    id: Union[str, SubscriberId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubscriberId):
            self.id = SubscriberId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubsidiaryLegalEntity(DpvOrganisation):
    """
    A legal entity that operates as a subsidiary of another legal entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SubsidiaryLegalEntity"]
    class_class_curie: ClassVar[str] = "dpv:SubsidiaryLegalEntity"
    class_name: ClassVar[str] = "SubsidiaryLegalEntity"
    class_model_uri: ClassVar[URIRef] = DPV.SubsidiaryLegalEntity

    id: Union[str, SubsidiaryLegalEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubsidiaryLegalEntityId):
            self.id = SubsidiaryLegalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupraNationalAuthority(DpvAuthority):
    """
    An authority tasked with overseeing legal compliance for a
    supra-national union e.g. EU
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SupraNationalAuthority"]
    class_class_curie: ClassVar[str] = "dpv:SupraNationalAuthority"
    class_name: ClassVar[str] = "SupraNationalAuthority"
    class_model_uri: ClassVar[URIRef] = DPV.SupraNationalAuthority

    id: Union[str, SupraNationalAuthorityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SupraNationalAuthorityId):
            self.id = SupraNationalAuthorityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThirdParty(LegalEntity):
    """
    A ‘third party’ means any natural or legal person other than - the
    entities directly involved or operating under those directly involved in
    a process
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ThirdParty"]
    class_class_curie: ClassVar[str] = "dpv:ThirdParty"
    class_name: ClassVar[str] = "ThirdParty"
    class_model_uri: ClassVar[URIRef] = DPV.ThirdParty

    id: Union[str, ThirdPartyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThirdPartyId):
            self.id = ThirdPartyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tourist(HumanSubject):
    """
    Humans that are tourists i.e. not citizens and not immigrants
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Tourist"]
    class_class_curie: ClassVar[str] = "dpv:Tourist"
    class_name: ClassVar[str] = "Tourist"
    class_model_uri: ClassVar[URIRef] = DPV.Tourist

    id: Union[str, TouristId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TouristId):
            self.id = TouristId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Visitor(HumanSubject):
    """
    Humans that are temporary visitors
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Visitor"]
    class_class_curie: ClassVar[str] = "dpv:Visitor"
    class_name: ClassVar[str] = "Visitor"
    class_model_uri: ClassVar[URIRef] = DPV.Visitor

    id: Union[str, VisitorId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VisitorId):
            self.id = VisitorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VulnerableHuman(HumanSubject):
    """
    Human(s) which should be considered 'vulnerable' within the context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VulnerableHuman"]
    class_class_curie: ClassVar[str] = "dpv:VulnerableHuman"
    class_name: ClassVar[str] = "VulnerableHuman"
    class_model_uri: ClassVar[URIRef] = DPV.VulnerableHuman

    id: Union[str, VulnerableHumanId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VulnerableHumanId):
            self.id = VulnerableHumanId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AsylumSeeker(VulnerableHuman):
    """
    Humans that are asylum seekers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AsylumSeeker"]
    class_class_curie: ClassVar[str] = "dpv:AsylumSeeker"
    class_name: ClassVar[str] = "AsylumSeeker"
    class_model_uri: ClassVar[URIRef] = DPV.AsylumSeeker

    id: Union[str, AsylumSeekerId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AsylumSeekerId):
            self.id = AsylumSeekerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Child(VulnerableHuman):
    """
    A 'child' is a natural legal person who is below a certain legal age
    depending on the legal jurisdiction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Child"]
    class_class_curie: ClassVar[str] = "dpv:Child"
    class_name: ClassVar[str] = "Child"
    class_model_uri: ClassVar[URIRef] = DPV.Child

    id: Union[str, ChildId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChildId):
            self.id = ChildId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElderlyHuman(VulnerableHuman):
    """
    Humans that are considered elderly (i.e. based on age)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ElderlyHuman"]
    class_class_curie: ClassVar[str] = "dpv:ElderlyHuman"
    class_name: ClassVar[str] = "ElderlyHuman"
    class_model_uri: ClassVar[URIRef] = DPV.ElderlyHuman

    id: Union[str, ElderlyHumanId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElderlyHumanId):
            self.id = ElderlyHumanId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MentallyVulnerableHuman(VulnerableHuman):
    """
    Humans that are considered mentally vulnerable within the context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MentallyVulnerableHuman"]
    class_class_curie: ClassVar[str] = "dpv:MentallyVulnerableHuman"
    class_name: ClassVar[str] = "MentallyVulnerableHuman"
    class_model_uri: ClassVar[URIRef] = DPV.MentallyVulnerableHuman

    id: Union[str, MentallyVulnerableHumanId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MentallyVulnerableHumanId):
            self.id = MentallyVulnerableHumanId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MentallyVulnerableDataSubject(MentallyVulnerableHuman):
    """
    Data subjects that are considered mentally vulnerable
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MentallyVulnerableDataSubject"]
    class_class_curie: ClassVar[str] = "dpv:MentallyVulnerableDataSubject"
    class_name: ClassVar[str] = "MentallyVulnerableDataSubject"
    class_model_uri: ClassVar[URIRef] = DPV.MentallyVulnerableDataSubject

    id: Union[str, MentallyVulnerableDataSubjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MentallyVulnerableDataSubjectId):
            self.id = MentallyVulnerableDataSubjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VulnerableDataSubject(VulnerableHuman):
    """
    Humans which should be considered 'vulnerable' and therefore would
    require additional measures and safeguards
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VulnerableDataSubject"]
    class_class_curie: ClassVar[str] = "dpv:VulnerableDataSubject"
    class_name: ClassVar[str] = "VulnerableDataSubject"
    class_model_uri: ClassVar[URIRef] = DPV.VulnerableDataSubject

    id: Union[str, VulnerableDataSubjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VulnerableDataSubjectId):
            self.id = VulnerableDataSubjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElderlyDataSubject(VulnerableDataSubject):
    """
    Data subjects that are considered elderly (i.e. based on age)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ElderlyDataSubject"]
    class_class_curie: ClassVar[str] = "dpv:ElderlyDataSubject"
    class_name: ClassVar[str] = "ElderlyDataSubject"
    class_model_uri: ClassVar[URIRef] = DPV.ElderlyDataSubject

    id: Union[str, ElderlyDataSubjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ElderlyDataSubjectId):
            self.id = ElderlyDataSubjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AccessControlMethod(TechnicalMeasure):
    """
    Methods which restrict access to a place or resource
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AccessControlMethod"]
    class_class_curie: ClassVar[str] = "dpv:AccessControlMethod"
    class_name: ClassVar[str] = "AccessControlMethod"
    class_model_uri: ClassVar[URIRef] = DPV.AccessControlMethod

    id: Union[str, AccessControlMethodId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AccessControlMethodId):
            self.id = AccessControlMethodId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActivityMonitoring(TechnicalMeasure):
    """
    Monitoring of activities including assessing whether they have been
    successfully initiated and completed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ActivityMonitoring"]
    class_class_curie: ClassVar[str] = "dpv:ActivityMonitoring"
    class_name: ClassVar[str] = "ActivityMonitoring"
    class_model_uri: ClassVar[URIRef] = DPV.ActivityMonitoring

    id: Union[str, ActivityMonitoringId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityMonitoringId):
            self.id = ActivityMonitoringId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Assessment(OrganisationalMeasure):
    """
    The document, plan, or process for assessment or determination towards a
    purpose e.g. assessment of legality or impact assessments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Assessment"]
    class_class_curie: ClassVar[str] = "dpv:Assessment"
    class_name: ClassVar[str] = "Assessment"
    class_model_uri: ClassVar[URIRef] = DPV.Assessment

    id: Union[str, AssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssessmentId):
            self.id = AssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Audit(OrganisationalMeasure):
    """
    An audit is a systematic examination or evaluation of records,
    processes, or systems towards a specific objective such as to assess
    accuracy, compliance, effectiveness, or performance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Audit"]
    class_class_curie: ClassVar[str] = "dpv:Audit"
    class_name: ClassVar[str] = "Audit"
    class_model_uri: ClassVar[URIRef] = DPV.Audit

    id: Union[str, AuditId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuditId):
            self.id = AuditId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuthenticationProtocols(TechnicalMeasure):
    """
    Protocols involving validation of identity i.e. authentication of a
    person or information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AuthenticationProtocols"]
    class_class_curie: ClassVar[str] = "dpv:AuthenticationProtocols"
    class_name: ClassVar[str] = "AuthenticationProtocols"
    class_model_uri: ClassVar[URIRef] = DPV.AuthenticationProtocols

    id: Union[str, AuthenticationProtocolsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuthenticationProtocolsId):
            self.id = AuthenticationProtocolsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuthorisationProtocols(TechnicalMeasure):
    """
    Protocols involving authorisation of roles or profiles to determine
    permission, rights, or privileges
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AuthorisationProtocols"]
    class_class_curie: ClassVar[str] = "dpv:AuthorisationProtocols"
    class_name: ClassVar[str] = "AuthorisationProtocols"
    class_model_uri: ClassVar[URIRef] = DPV.AuthorisationProtocols

    id: Union[str, AuthorisationProtocolsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuthorisationProtocolsId):
            self.id = AuthorisationProtocolsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiometricAuthentication(AuthenticationProtocols):
    """
    Use of biometric data for authentication
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["BiometricAuthentication"]
    class_class_curie: ClassVar[str] = "dpv:BiometricAuthentication"
    class_name: ClassVar[str] = "BiometricAuthentication"
    class_model_uri: ClassVar[URIRef] = DPV.BiometricAuthentication

    id: Union[str, BiometricAuthenticationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiometricAuthenticationId):
            self.id = BiometricAuthenticationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CertificationSeal(OrganisationalMeasure):
    """
    Certifications, seals, and marks indicating compliance to regulations or
    practices
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CertificationSeal"]
    class_class_curie: ClassVar[str] = "dpv:CertificationSeal"
    class_name: ClassVar[str] = "CertificationSeal"
    class_model_uri: ClassVar[URIRef] = DPV.CertificationSeal

    id: Union[str, CertificationSealId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CertificationSealId):
            self.id = CertificationSealId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Certification(CertificationSeal):
    """
    Certification mechanisms, seals, and marks for the purpose of
    demonstrating compliance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Certification"]
    class_class_curie: ClassVar[str] = "dpv:Certification"
    class_name: ClassVar[str] = "Certification"
    class_model_uri: ClassVar[URIRef] = DPV.Certification

    id: Union[str, CertificationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CertificationId):
            self.id = CertificationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComplianceAssessment(Assessment):
    """
    Assessment regarding compliance (e.g. internal policy, regulations)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ComplianceAssessment"]
    class_class_curie: ClassVar[str] = "dpv:ComplianceAssessment"
    class_name: ClassVar[str] = "ComplianceAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.ComplianceAssessment

    id: Union[str, ComplianceAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComplianceAssessmentId):
            self.id = ComplianceAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConformanceAssessment(Assessment):
    """
    Assessment regarding conformance with standards or norms or guidelines
    or similar instruments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConformanceAssessment"]
    class_class_curie: ClassVar[str] = "dpv:ConformanceAssessment"
    class_name: ClassVar[str] = "ConformanceAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.ConformanceAssessment

    id: Union[str, ConformanceAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConformanceAssessmentId):
            self.id = ConformanceAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Consultation(OrganisationalMeasure):
    """
    Consultation is a process of receiving feedback, advice, or opinion from
    an external agency
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Consultation"]
    class_class_curie: ClassVar[str] = "dpv:Consultation"
    class_name: ClassVar[str] = "Consultation"
    class_model_uri: ClassVar[URIRef] = DPV.Consultation

    id: Union[str, ConsultationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsultationId):
            self.id = ConsultationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsultationWithAuthority(Consultation):
    """
    Consultation with an authority or authoritative entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsultationWithAuthority"]
    class_class_curie: ClassVar[str] = "dpv:ConsultationWithAuthority"
    class_name: ClassVar[str] = "ConsultationWithAuthority"
    class_model_uri: ClassVar[URIRef] = DPV.ConsultationWithAuthority

    id: Union[str, ConsultationWithAuthorityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsultationWithAuthorityId):
            self.id = ConsultationWithAuthorityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsultationWithDPO(Consultation):
    """
    Consultation with Data Protection Officer(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsultationWithDPO"]
    class_class_curie: ClassVar[str] = "dpv:ConsultationWithDPO"
    class_name: ClassVar[str] = "ConsultationWithDPO"
    class_model_uri: ClassVar[URIRef] = DPV.ConsultationWithDPO

    id: Union[str, ConsultationWithDPOId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsultationWithDPOId):
            self.id = ConsultationWithDPOId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsultationWithDataSubject(Consultation):
    """
    Consultation with data subject(s) or their representative(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsultationWithDataSubject"]
    class_class_curie: ClassVar[str] = "dpv:ConsultationWithDataSubject"
    class_name: ClassVar[str] = "ConsultationWithDataSubject"
    class_model_uri: ClassVar[URIRef] = DPV.ConsultationWithDataSubject

    id: Union[str, ConsultationWithDataSubjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsultationWithDataSubjectId):
            self.id = ConsultationWithDataSubjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsultationWithDataSubjectRepresentative(ConsultationWithDataSubject):
    """
    Consultation with representative of data subject(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsultationWithDataSubjectRepresentative"]
    class_class_curie: ClassVar[str] = "dpv:ConsultationWithDataSubjectRepresentative"
    class_name: ClassVar[str] = "ConsultationWithDataSubjectRepresentative"
    class_model_uri: ClassVar[URIRef] = DPV.ConsultationWithDataSubjectRepresentative

    id: Union[str, ConsultationWithDataSubjectRepresentativeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsultationWithDataSubjectRepresentativeId):
            self.id = ConsultationWithDataSubjectRepresentativeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CryptographicAuthentication(AuthenticationProtocols):
    """
    Use of cryptography for authentication
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CryptographicAuthentication"]
    class_class_curie: ClassVar[str] = "dpv:CryptographicAuthentication"
    class_name: ClassVar[str] = "CryptographicAuthentication"
    class_model_uri: ClassVar[URIRef] = DPV.CryptographicAuthentication

    id: Union[str, CryptographicAuthenticationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CryptographicAuthenticationId):
            self.id = CryptographicAuthenticationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuthenticationABC(CryptographicAuthentication):
    """
    Use of Attribute Based Credentials (ABC) to perform and manage
    authentication
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Authentication-ABC"]
    class_class_curie: ClassVar[str] = "dpv:Authentication-ABC"
    class_name: ClassVar[str] = "AuthenticationABC"
    class_model_uri: ClassVar[URIRef] = DPV.AuthenticationABC

    id: Union[str, AuthenticationABCId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuthenticationABCId):
            self.id = AuthenticationABCId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuthenticationPABC(CryptographicAuthentication):
    """
    Use of Privacy-enhancing Attribute Based Credentials (ABC) to perform
    and manage authentication
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Authentication-PABC"]
    class_class_curie: ClassVar[str] = "dpv:Authentication-PABC"
    class_name: ClassVar[str] = "AuthenticationPABC"
    class_model_uri: ClassVar[URIRef] = DPV.AuthenticationPABC

    id: Union[str, AuthenticationPABCId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuthenticationPABCId):
            self.id = AuthenticationPABCId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CryptographicMethods(TechnicalMeasure):
    """
    Use of cryptographic methods to perform tasks
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CryptographicMethods"]
    class_class_curie: ClassVar[str] = "dpv:CryptographicMethods"
    class_name: ClassVar[str] = "CryptographicMethods"
    class_model_uri: ClassVar[URIRef] = DPV.CryptographicMethods

    id: Union[str, CryptographicMethodsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CryptographicMethodsId):
            self.id = CryptographicMethodsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AsymmetricCryptography(CryptographicMethods):
    """
    Use of public-key cryptography or asymmetric cryptography involving a
    public and private pair of keys
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AsymmetricCryptography"]
    class_class_curie: ClassVar[str] = "dpv:AsymmetricCryptography"
    class_name: ClassVar[str] = "AsymmetricCryptography"
    class_model_uri: ClassVar[URIRef] = DPV.AsymmetricCryptography

    id: Union[str, AsymmetricCryptographyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AsymmetricCryptographyId):
            self.id = AsymmetricCryptographyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CryptographicKeyManagement(CryptographicMethods):
    """
    Management of cryptographic keys, including their generation, storage,
    assessment, and safekeeping
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CryptographicKeyManagement"]
    class_class_curie: ClassVar[str] = "dpv:CryptographicKeyManagement"
    class_name: ClassVar[str] = "CryptographicKeyManagement"
    class_model_uri: ClassVar[URIRef] = DPV.CryptographicKeyManagement

    id: Union[str, CryptographicKeyManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CryptographicKeyManagementId):
            self.id = CryptographicKeyManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataBackupProtocols(TechnicalMeasure):
    """
    Protocols or plans for backing up of data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataBackupProtocols"]
    class_class_curie: ClassVar[str] = "dpv:DataBackupProtocols"
    class_name: ClassVar[str] = "DataBackupProtocols"
    class_model_uri: ClassVar[URIRef] = DPV.DataBackupProtocols

    id: Union[str, DataBackupProtocolsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataBackupProtocolsId):
            self.id = DataBackupProtocolsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataInteroperabilityAssessment(Assessment):
    """
    Measures associated with assessment of data interoperability
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataInteroperabilityAssessment"]
    class_class_curie: ClassVar[str] = "dpv:DataInteroperabilityAssessment"
    class_name: ClassVar[str] = "DataInteroperabilityAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.DataInteroperabilityAssessment

    id: Union[str, DataInteroperabilityAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataInteroperabilityAssessmentId):
            self.id = DataInteroperabilityAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataQualityAssessment(Assessment):
    """
    Measures associated with assessment of data quality
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataQualityAssessment"]
    class_class_curie: ClassVar[str] = "dpv:DataQualityAssessment"
    class_name: ClassVar[str] = "DataQualityAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.DataQualityAssessment

    id: Union[str, DataQualityAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataQualityAssessmentId):
            self.id = DataQualityAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSanitisationTechnique(TechnicalMeasure):
    """
    Cleaning or any removal or re-organisation of elements in data based on
    selective criteria
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSanitisationTechnique"]
    class_class_curie: ClassVar[str] = "dpv:DataSanitisationTechnique"
    class_name: ClassVar[str] = "DataSanitisationTechnique"
    class_model_uri: ClassVar[URIRef] = DPV.DataSanitisationTechnique

    id: Union[str, DataSanitisationTechniqueId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSanitisationTechniqueId):
            self.id = DataSanitisationTechniqueId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataRedaction(DataSanitisationTechnique):
    """
    Removal of sensitive information from a data or document
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataRedaction"]
    class_class_curie: ClassVar[str] = "dpv:DataRedaction"
    class_name: ClassVar[str] = "DataRedaction"
    class_model_uri: ClassVar[URIRef] = DPV.DataRedaction

    id: Union[str, DataRedactionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataRedactionId):
            self.id = DataRedactionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSuitabilityAssessment(DataQualityAssessment):
    """
    Measures associated with assessment of suitability of data for specific
    task(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSuitabilityAssessment"]
    class_class_curie: ClassVar[str] = "dpv:DataSuitabilityAssessment"
    class_name: ClassVar[str] = "DataSuitabilityAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.DataSuitabilityAssessment

    id: Union[str, DataSuitabilityAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSuitabilityAssessmentId):
            self.id = DataSuitabilityAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Deidentification(DataSanitisationTechnique):
    """
    Removal of identity or information to reduce identifiability
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Deidentification"]
    class_class_curie: ClassVar[str] = "dpv:Deidentification"
    class_name: ClassVar[str] = "Deidentification"
    class_model_uri: ClassVar[URIRef] = DPV.Deidentification

    id: Union[str, DeidentificationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeidentificationId):
            self.id = DeidentificationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Anonymisation(Deidentification):
    """
    Anonymisation is the process by which data is irreversibly altered in
    such a way that a data subject can no longer be identified directly or
    indirectly, either by the entity holding the data alone or in
    collaboration with other entities and information sources
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Anonymisation"]
    class_class_curie: ClassVar[str] = "dpv:Anonymisation"
    class_name: ClassVar[str] = "Anonymisation"
    class_model_uri: ClassVar[URIRef] = DPV.Anonymisation

    id: Union[str, AnonymisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnonymisationId):
            self.id = AnonymisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DifferentialPrivacy(CryptographicMethods):
    """
    Utilisation of differential privacy where information is shared as
    patterns or groups to withhold individual elements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DifferentialPrivacy"]
    class_class_curie: ClassVar[str] = "dpv:DifferentialPrivacy"
    class_name: ClassVar[str] = "DifferentialPrivacy"
    class_model_uri: ClassVar[URIRef] = DPV.DifferentialPrivacy

    id: Union[str, DifferentialPrivacyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DifferentialPrivacyId):
            self.id = DifferentialPrivacyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DigitalLiteracy(OrganisationalMeasure):
    """
    Providing skills, knowledge, and understanding to enable reading,
    writing, analysing, reasoning, and communicating regarding digital
    technologies and their implications
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DigitalLiteracy"]
    class_class_curie: ClassVar[str] = "dpv:DigitalLiteracy"
    class_name: ClassVar[str] = "DigitalLiteracy"
    class_model_uri: ClassVar[URIRef] = DPV.DigitalLiteracy

    id: Union[str, DigitalLiteracyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DigitalLiteracyId):
            self.id = DigitalLiteracyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AILiteracy(DigitalLiteracy):
    """
    Providing skills, knowledge, and understanding to enable reading,
    writing, analysing, reasoning, and communicating regarding AI
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AILiteracy"]
    class_class_curie: ClassVar[str] = "dpv:AILiteracy"
    class_name: ClassVar[str] = "AILiteracy"
    class_model_uri: ClassVar[URIRef] = DPV.AILiteracy

    id: Union[str, AILiteracyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AILiteracyId):
            self.id = AILiteracyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataLiteracy(DigitalLiteracy):
    """
    Providing skills, knowledge, and understanding to enable reading,
    writing, analysing, reasoning, and communicating regarding data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataLiteracy"]
    class_class_curie: ClassVar[str] = "dpv:DataLiteracy"
    class_name: ClassVar[str] = "DataLiteracy"
    class_model_uri: ClassVar[URIRef] = DPV.DataLiteracy

    id: Union[str, DataLiteracyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataLiteracyId):
            self.id = DataLiteracyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DigitalRightsManagement(TechnicalMeasure):
    """
    Management of access, use, and other operations associated with digital
    content
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DigitalRightsManagement"]
    class_class_curie: ClassVar[str] = "dpv:DigitalRightsManagement"
    class_name: ClassVar[str] = "DigitalRightsManagement"
    class_model_uri: ClassVar[URIRef] = DPV.DigitalRightsManagement

    id: Union[str, DigitalRightsManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DigitalRightsManagementId):
            self.id = DigitalRightsManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DigitalSignatures(CryptographicMethods):
    """
    Expression and authentication of identity through digital information
    containing cryptographic signatures
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DigitalSignatures"]
    class_class_curie: ClassVar[str] = "dpv:DigitalSignatures"
    class_name: ClassVar[str] = "DigitalSignatures"
    class_model_uri: ClassVar[URIRef] = DPV.DigitalSignatures

    id: Union[str, DigitalSignaturesId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DigitalSignaturesId):
            self.id = DigitalSignaturesId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvData(DpvThing):
    """
    A broad concept representing 'data' or 'information'
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Data"]
    class_class_curie: ClassVar[str] = "dpv:Data"
    class_name: ClassVar[str] = "DpvData"
    class_model_uri: ClassVar[URIRef] = DPV.DpvData

    id: Union[str, DpvDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDataId):
            self.id = DpvDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CollectedData(DpvData):
    """
    Data that has been obtained by collecting it from a source
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CollectedData"]
    class_class_curie: ClassVar[str] = "dpv:CollectedData"
    class_name: ClassVar[str] = "CollectedData"
    class_model_uri: ClassVar[URIRef] = DPV.CollectedData

    id: Union[str, CollectedDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CollectedDataId):
            self.id = CollectedDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CollectedPersonalData(CollectedData):
    """
    Personal Data that has been collected from another source such as the
    Data Subject
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CollectedPersonalData"]
    class_class_curie: ClassVar[str] = "dpv:CollectedPersonalData"
    class_name: ClassVar[str] = "CollectedPersonalData"
    class_model_uri: ClassVar[URIRef] = DPV.CollectedPersonalData

    id: Union[str, CollectedPersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CollectedPersonalDataId):
            self.id = CollectedPersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConfidentialData(DpvData):
    """
    Data deemed confidential
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConfidentialData"]
    class_class_curie: ClassVar[str] = "dpv:ConfidentialData"
    class_name: ClassVar[str] = "ConfidentialData"
    class_model_uri: ClassVar[URIRef] = DPV.ConfidentialData

    id: Union[str, ConfidentialDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConfidentialDataId):
            self.id = ConfidentialDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommerciallyConfidentialData(ConfidentialData):
    """
    Data that is considered confidential due to business/trade secrets,
    confidentiality agreements, or company secrets
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CommerciallyConfidentialData"]
    class_class_curie: ClassVar[str] = "dpv:CommerciallyConfidentialData"
    class_name: ClassVar[str] = "CommerciallyConfidentialData"
    class_model_uri: ClassVar[URIRef] = DPV.CommerciallyConfidentialData

    id: Union[str, CommerciallyConfidentialDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommerciallyConfidentialDataId):
            self.id = CommerciallyConfidentialDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DerivedData(DpvData):
    """
    Data that has been obtained through derivations of other data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DerivedData"]
    class_class_curie: ClassVar[str] = "dpv:DerivedData"
    class_name: ClassVar[str] = "DerivedData"
    class_model_uri: ClassVar[URIRef] = DPV.DerivedData

    id: Union[str, DerivedDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DerivedDataId):
            self.id = DerivedDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DerivedPersonalData(DerivedData):
    """
    Personal Data that is obtained or derived from other data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DerivedPersonalData"]
    class_class_curie: ClassVar[str] = "dpv:DerivedPersonalData"
    class_name: ClassVar[str] = "DerivedPersonalData"
    class_model_uri: ClassVar[URIRef] = DPV.DerivedPersonalData

    id: Union[str, DerivedPersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DerivedPersonalDataId):
            self.id = DerivedPersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EffectivenessDeterminationProcedures(Assessment):
    """
    Procedures intended to determine effectiveness of other measures
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EffectivenessDeterminationProcedures"]
    class_class_curie: ClassVar[str] = "dpv:EffectivenessDeterminationProcedures"
    class_name: ClassVar[str] = "EffectivenessDeterminationProcedures"
    class_model_uri: ClassVar[URIRef] = DPV.EffectivenessDeterminationProcedures

    id: Union[str, EffectivenessDeterminationProceduresId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EffectivenessDeterminationProceduresId):
            self.id = EffectivenessDeterminationProceduresId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Encryption(TechnicalMeasure):
    """
    Technical measures consisting of encryption
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Encryption"]
    class_class_curie: ClassVar[str] = "dpv:Encryption"
    class_name: ClassVar[str] = "Encryption"
    class_model_uri: ClassVar[URIRef] = DPV.Encryption

    id: Union[str, EncryptionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EncryptionId):
            self.id = EncryptionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AsymmetricEncryption(Encryption):
    """
    Use of asymmetric cryptography to encrypt data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AsymmetricEncryption"]
    class_class_curie: ClassVar[str] = "dpv:AsymmetricEncryption"
    class_name: ClassVar[str] = "AsymmetricEncryption"
    class_model_uri: ClassVar[URIRef] = DPV.AsymmetricEncryption

    id: Union[str, AsymmetricEncryptionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AsymmetricEncryptionId):
            self.id = AsymmetricEncryptionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EncryptionAtRest(Encryption):
    """
    Encryption of data when being stored (persistent encryption)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EncryptionAtRest"]
    class_class_curie: ClassVar[str] = "dpv:EncryptionAtRest"
    class_name: ClassVar[str] = "EncryptionAtRest"
    class_model_uri: ClassVar[URIRef] = DPV.EncryptionAtRest

    id: Union[str, EncryptionAtRestId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EncryptionAtRestId):
            self.id = EncryptionAtRestId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EncryptionInTransfer(Encryption):
    """
    Encryption of data in transit e.g. when being transferred from one
    location to another, including sharing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EncryptionInTransfer"]
    class_class_curie: ClassVar[str] = "dpv:EncryptionInTransfer"
    class_name: ClassVar[str] = "EncryptionInTransfer"
    class_model_uri: ClassVar[URIRef] = DPV.EncryptionInTransfer

    id: Union[str, EncryptionInTransferId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EncryptionInTransferId):
            self.id = EncryptionInTransferId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EncryptionInUse(Encryption):
    """
    Encryption of data when it is being used
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EncryptionInUse"]
    class_class_curie: ClassVar[str] = "dpv:EncryptionInUse"
    class_name: ClassVar[str] = "EncryptionInUse"
    class_model_uri: ClassVar[URIRef] = DPV.EncryptionInUse

    id: Union[str, EncryptionInUseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EncryptionInUseId):
            self.id = EncryptionInUseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EndToEndEncryption(Encryption):
    """
    Encrypted communications where data is encrypted by the sender and
    decrypted by the intended receiver to prevent access to any third party
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EndToEndEncryption"]
    class_class_curie: ClassVar[str] = "dpv:EndToEndEncryption"
    class_name: ClassVar[str] = "EndToEndEncryption"
    class_model_uri: ClassVar[URIRef] = DPV.EndToEndEncryption

    id: Union[str, EndToEndEncryptionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EndToEndEncryptionId):
            self.id = EndToEndEncryptionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentalProtection(PhysicalMeasure):
    """
    Physical protection against environmental threats such as fire, floods,
    storms, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EnvironmentalProtection"]
    class_class_curie: ClassVar[str] = "dpv:EnvironmentalProtection"
    class_name: ClassVar[str] = "EnvironmentalProtection"
    class_model_uri: ClassVar[URIRef] = DPV.EnvironmentalProtection

    id: Union[str, EnvironmentalProtectionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalProtectionId):
            self.id = EnvironmentalProtectionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FailSafeProtocols(TechnicalMeasure):
    """
    Use of fail-safe measures and protocols
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FailSafeProtocols"]
    class_class_curie: ClassVar[str] = "dpv:FailSafeProtocols"
    class_name: ClassVar[str] = "FailSafeProtocols"
    class_model_uri: ClassVar[URIRef] = DPV.FailSafeProtocols

    id: Union[str, FailSafeProtocolsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FailSafeProtocolsId):
            self.id = FailSafeProtocolsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneratedData(DpvData):
    """
    Data that is generated or brought into existence without relation to
    existing data i.e. it is not derived or inferred from other data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["GeneratedData"]
    class_class_curie: ClassVar[str] = "dpv:GeneratedData"
    class_name: ClassVar[str] = "GeneratedData"
    class_model_uri: ClassVar[URIRef] = DPV.GeneratedData

    id: Union[str, GeneratedDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneratedDataId):
            self.id = GeneratedDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GovernanceProcedures(OrganisationalMeasure):
    """
    Procedures related to governance (e.g. organisation, unit, team,
    process, system)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["GovernanceProcedures"]
    class_class_curie: ClassVar[str] = "dpv:GovernanceProcedures"
    class_name: ClassVar[str] = "GovernanceProcedures"
    class_model_uri: ClassVar[URIRef] = DPV.GovernanceProcedures

    id: Union[str, GovernanceProceduresId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GovernanceProceduresId):
            self.id = GovernanceProceduresId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AIGovernance(GovernanceProcedures):
    """
    Procedures related to governance of AI, including its procurement,
    development, deployment, and assessments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AIGovernance"]
    class_class_curie: ClassVar[str] = "dpv:AIGovernance"
    class_name: ClassVar[str] = "AIGovernance"
    class_model_uri: ClassVar[URIRef] = DPV.AIGovernance

    id: Union[str, AIGovernanceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AIGovernanceId):
            self.id = AIGovernanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ApprovalProcedure(GovernanceProcedures):
    """
    A procedure or process for determining and managing approvals for
    activities as part of governance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ApprovalProcedure"]
    class_class_curie: ClassVar[str] = "dpv:ApprovalProcedure"
    class_name: ClassVar[str] = "ApprovalProcedure"
    class_model_uri: ClassVar[URIRef] = DPV.ApprovalProcedure

    id: Union[str, ApprovalProcedureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ApprovalProcedureId):
            self.id = ApprovalProcedureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssetManagementProcedures(GovernanceProcedures):
    """
    Procedures related to management of assets
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AssetManagementProcedures"]
    class_class_curie: ClassVar[str] = "dpv:AssetManagementProcedures"
    class_name: ClassVar[str] = "AssetManagementProcedures"
    class_model_uri: ClassVar[URIRef] = DPV.AssetManagementProcedures

    id: Union[str, AssetManagementProceduresId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssetManagementProceduresId):
            self.id = AssetManagementProceduresId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComplianceMonitoring(GovernanceProcedures):
    """
    Monitoring of compliance (e.g. internal policy, regulations)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ComplianceMonitoring"]
    class_class_curie: ClassVar[str] = "dpv:ComplianceMonitoring"
    class_name: ClassVar[str] = "ComplianceMonitoring"
    class_model_uri: ClassVar[URIRef] = DPV.ComplianceMonitoring

    id: Union[str, ComplianceMonitoringId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ComplianceMonitoringId):
            self.id = ComplianceMonitoringId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DisasterRecoveryProcedures(GovernanceProcedures):
    """
    Procedures related to management of disasters and recovery
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DisasterRecoveryProcedures"]
    class_class_curie: ClassVar[str] = "dpv:DisasterRecoveryProcedures"
    class_name: ClassVar[str] = "DisasterRecoveryProcedures"
    class_model_uri: ClassVar[URIRef] = DPV.DisasterRecoveryProcedures

    id: Union[str, DisasterRecoveryProceduresId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DisasterRecoveryProceduresId):
            self.id = DisasterRecoveryProceduresId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GuidelinesPrinciple(OrganisationalMeasure):
    """
    Guidelines or Principles regarding processing and operational measures
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["GuidelinesPrinciple"]
    class_class_curie: ClassVar[str] = "dpv:GuidelinesPrinciple"
    class_name: ClassVar[str] = "GuidelinesPrinciple"
    class_model_uri: ClassVar[URIRef] = DPV.GuidelinesPrinciple

    id: Union[str, GuidelinesPrincipleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GuidelinesPrincipleId):
            self.id = GuidelinesPrincipleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CodeOfConduct(GuidelinesPrinciple):
    """
    A set of rules or procedures outlining the norms and practices for
    conducting activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CodeOfConduct"]
    class_class_curie: ClassVar[str] = "dpv:CodeOfConduct"
    class_name: ClassVar[str] = "CodeOfConduct"
    class_model_uri: ClassVar[URIRef] = DPV.CodeOfConduct

    id: Union[str, CodeOfConductId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CodeOfConductId):
            self.id = CodeOfConductId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Guideline(GuidelinesPrinciple):
    """
    Practices that specify how activities must be conducted
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Guideline"]
    class_class_curie: ClassVar[str] = "dpv:Guideline"
    class_name: ClassVar[str] = "Guideline"
    class_model_uri: ClassVar[URIRef] = DPV.Guideline

    id: Union[str, GuidelineId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GuidelineId):
            self.id = GuidelineId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HashFunctions(CryptographicMethods):
    """
    Use of hash functions to map information or to retrieve a prior
    categorisation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HashFunctions"]
    class_class_curie: ClassVar[str] = "dpv:HashFunctions"
    class_name: ClassVar[str] = "HashFunctions"
    class_model_uri: ClassVar[URIRef] = DPV.HashFunctions

    id: Union[str, HashFunctionsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HashFunctionsId):
            self.id = HashFunctionsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HashMessageAuthenticationCode(CryptographicAuthentication):
    """
    Use of HMAC where message authentication code (MAC) utilise a
    cryptographic hash function and a secret cryptographic key
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HashMessageAuthenticationCode"]
    class_class_curie: ClassVar[str] = "dpv:HashMessageAuthenticationCode"
    class_name: ClassVar[str] = "HashMessageAuthenticationCode"
    class_model_uri: ClassVar[URIRef] = DPV.HashMessageAuthenticationCode

    id: Union[str, HashMessageAuthenticationCodeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HashMessageAuthenticationCodeId):
            self.id = HashMessageAuthenticationCodeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HomomorphicEncryption(CryptographicMethods):
    """
    Use of Homomorphic encryption that permits computations on encrypted
    data without decrypting it
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HomomorphicEncryption"]
    class_class_curie: ClassVar[str] = "dpv:HomomorphicEncryption"
    class_name: ClassVar[str] = "HomomorphicEncryption"
    class_model_uri: ClassVar[URIRef] = DPV.HomomorphicEncryption

    id: Union[str, HomomorphicEncryptionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HomomorphicEncryptionId):
            self.id = HomomorphicEncryptionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanOversight(GovernanceProcedures):
    """
    Procedures related to implementing and ensuring human oversight, which
    includes ability for humans to oversee, understand, control, and reverse
    processes, and to have sufficient monitoring capability to detect and
    address anomalies, dysfunctions, or unexpected performance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HumanOversight"]
    class_class_curie: ClassVar[str] = "dpv:HumanOversight"
    class_name: ClassVar[str] = "HumanOversight"
    class_model_uri: ClassVar[URIRef] = DPV.HumanOversight

    id: Union[str, HumanOversightId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanOversightId):
            self.id = HumanOversightId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IncidentManagementProcedures(GovernanceProcedures):
    """
    Procedures related to management of incidents
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["IncidentManagementProcedures"]
    class_class_curie: ClassVar[str] = "dpv:IncidentManagementProcedures"
    class_name: ClassVar[str] = "IncidentManagementProcedures"
    class_model_uri: ClassVar[URIRef] = DPV.IncidentManagementProcedures

    id: Union[str, IncidentManagementProceduresId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IncidentManagementProceduresId):
            self.id = IncidentManagementProceduresId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IncidentReportingCommunication(GovernanceProcedures):
    """
    Procedures related to management of incident reporting
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["IncidentReportingCommunication"]
    class_class_curie: ClassVar[str] = "dpv:IncidentReportingCommunication"
    class_name: ClassVar[str] = "IncidentReportingCommunication"
    class_model_uri: ClassVar[URIRef] = DPV.IncidentReportingCommunication

    id: Union[str, IncidentReportingCommunicationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IncidentReportingCommunicationId):
            self.id = IncidentReportingCommunicationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IncorrectData(DpvData):
    """
    Data that is known to be incorrect or inconsistent with some
    requirements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["IncorrectData"]
    class_class_curie: ClassVar[str] = "dpv:IncorrectData"
    class_name: ClassVar[str] = "IncorrectData"
    class_model_uri: ClassVar[URIRef] = DPV.IncorrectData

    id: Union[str, IncorrectDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IncorrectDataId):
            self.id = IncorrectDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InferredData(DerivedData):
    """
    Data that has been obtained through inferences of other data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InferredData"]
    class_class_curie: ClassVar[str] = "dpv:InferredData"
    class_name: ClassVar[str] = "InferredData"
    class_model_uri: ClassVar[URIRef] = DPV.InferredData

    id: Union[str, InferredDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InferredDataId):
            self.id = InferredDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InferredPersonalData(DerivedPersonalData):
    """
    Personal Data that is obtained through inference from other data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InferredPersonalData"]
    class_class_curie: ClassVar[str] = "dpv:InferredPersonalData"
    class_name: ClassVar[str] = "InferredPersonalData"
    class_model_uri: ClassVar[URIRef] = DPV.InferredPersonalData

    id: Union[str, InferredPersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InferredPersonalDataId):
            self.id = InferredPersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InformationAudit(Audit):
    """
    An audit that systematically examines the existence and use of
    information along with its associated resources (e.g. where it is
    stored) and flows (e.g. where it originates and with whom it is being
    shared)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InformationAudit"]
    class_class_curie: ClassVar[str] = "dpv:InformationAudit"
    class_name: ClassVar[str] = "InformationAudit"
    class_model_uri: ClassVar[URIRef] = DPV.InformationAudit

    id: Union[str, InformationAuditId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationAuditId):
            self.id = InformationAuditId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InformationFlowControl(TechnicalMeasure):
    """
    Use of measures to control information flows
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InformationFlowControl"]
    class_class_curie: ClassVar[str] = "dpv:InformationFlowControl"
    class_name: ClassVar[str] = "InformationFlowControl"
    class_model_uri: ClassVar[URIRef] = DPV.InformationFlowControl

    id: Union[str, InformationFlowControlId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationFlowControlId):
            self.id = InformationFlowControlId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntellectualPropertyData(ConfidentialData):
    """
    Data protected by Intellectual Property rights and regulations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["IntellectualPropertyData"]
    class_class_curie: ClassVar[str] = "dpv:IntellectualPropertyData"
    class_name: ClassVar[str] = "IntellectualPropertyData"
    class_model_uri: ClassVar[URIRef] = DPV.IntellectualPropertyData

    id: Union[str, IntellectualPropertyDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntellectualPropertyDataId):
            self.id = IntellectualPropertyDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalComplianceAssessment(ComplianceAssessment):
    """
    Assessment regarding legal compliance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalComplianceAssessment"]
    class_class_curie: ClassVar[str] = "dpv:LegalComplianceAssessment"
    class_name: ClassVar[str] = "LegalComplianceAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.LegalComplianceAssessment

    id: Union[str, LegalComplianceAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalComplianceAssessmentId):
            self.id = LegalComplianceAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalComplianceAudit(Audit):
    """
    An audit that systematically examines the state of legal compliance by
    reviewing policies and procedures related to obligations and compliance
    requirements for specific laws and regulations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalComplianceAudit"]
    class_class_curie: ClassVar[str] = "dpv:LegalComplianceAudit"
    class_name: ClassVar[str] = "LegalComplianceAudit"
    class_model_uri: ClassVar[URIRef] = DPV.LegalComplianceAudit

    id: Union[str, LegalComplianceAuditId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalComplianceAuditId):
            self.id = LegalComplianceAuditId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegitimateInterestAssessment(Assessment):
    """
    Indicates an assessment regarding the use of legitimate interest as a
    lawful basis by the data controller
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegitimateInterestAssessment"]
    class_class_curie: ClassVar[str] = "dpv:LegitimateInterestAssessment"
    class_name: ClassVar[str] = "LegitimateInterestAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.LegitimateInterestAssessment

    id: Union[str, LegitimateInterestAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegitimateInterestAssessmentId):
            self.id = LegitimateInterestAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MessageAuthenticationCodes(CryptographicAuthentication):
    """
    Use of cryptographic methods to authenticate messages
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MessageAuthenticationCodes"]
    class_class_curie: ClassVar[str] = "dpv:MessageAuthenticationCodes"
    class_name: ClassVar[str] = "MessageAuthenticationCodes"
    class_model_uri: ClassVar[URIRef] = DPV.MessageAuthenticationCodes

    id: Union[str, MessageAuthenticationCodesId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MessageAuthenticationCodesId):
            self.id = MessageAuthenticationCodesId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MultiFactorAuthentication(AuthenticationProtocols):
    """
    An authentication system that uses two or more methods to authenticate
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MultiFactorAuthentication"]
    class_class_curie: ClassVar[str] = "dpv:MultiFactorAuthentication"
    class_name: ClassVar[str] = "MultiFactorAuthentication"
    class_model_uri: ClassVar[URIRef] = DPV.MultiFactorAuthentication

    id: Union[str, MultiFactorAuthenticationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MultiFactorAuthenticationId):
            self.id = MultiFactorAuthenticationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NonPersonalData(DpvData):
    """
    Data that is not Personal Data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NonPersonalData"]
    class_class_curie: ClassVar[str] = "dpv:NonPersonalData"
    class_name: ClassVar[str] = "NonPersonalData"
    class_model_uri: ClassVar[URIRef] = DPV.NonPersonalData

    id: Union[str, NonPersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NonPersonalDataId):
            self.id = NonPersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnonymisedData(NonPersonalData):
    """
    Personal Data that has been (fully and completely) anonymised so that it
    is no longer considered Personal Data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AnonymisedData"]
    class_class_curie: ClassVar[str] = "dpv:AnonymisedData"
    class_name: ClassVar[str] = "AnonymisedData"
    class_model_uri: ClassVar[URIRef] = DPV.AnonymisedData

    id: Union[str, AnonymisedDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnonymisedDataId):
            self.id = AnonymisedDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Notification(OrganisationalMeasure):
    """
    Notification represents the provision of a notice i.e. notifying
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Notification"]
    class_class_curie: ClassVar[str] = "dpv:Notification"
    class_name: ClassVar[str] = "Notification"
    class_model_uri: ClassVar[URIRef] = DPV.Notification

    id: Union[str, NotificationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotificationId):
            self.id = NotificationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObservedData(CollectedData):
    """
    Data that has been obtained through observations of a source
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ObservedData"]
    class_class_curie: ClassVar[str] = "dpv:ObservedData"
    class_name: ClassVar[str] = "ObservedData"
    class_model_uri: ClassVar[URIRef] = DPV.ObservedData

    id: Union[str, ObservedDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservedDataId):
            self.id = ObservedDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObservedPersonalData(CollectedPersonalData):
    """
    Personal Data that has been collected through observation of the Data
    Subject(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ObservedPersonalData"]
    class_class_curie: ClassVar[str] = "dpv:ObservedPersonalData"
    class_name: ClassVar[str] = "ObservedPersonalData"
    class_model_uri: ClassVar[URIRef] = DPV.ObservedPersonalData

    id: Union[str, ObservedPersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObservedPersonalDataId):
            self.id = ObservedPersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PasswordAuthentication(AuthenticationProtocols):
    """
    Use of passwords to perform authentication
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PasswordAuthentication"]
    class_class_curie: ClassVar[str] = "dpv:PasswordAuthentication"
    class_name: ClassVar[str] = "PasswordAuthentication"
    class_model_uri: ClassVar[URIRef] = DPV.PasswordAuthentication

    id: Union[str, PasswordAuthenticationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PasswordAuthenticationId):
            self.id = PasswordAuthenticationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonalData(DpvData):
    """
    Data directly or indirectly associated or related to an individual
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonalData"]
    class_class_curie: ClassVar[str] = "dpv:PersonalData"
    class_name: ClassVar[str] = "PersonalData"
    class_model_uri: ClassVar[URIRef] = DPV.PersonalData

    id: Union[str, PersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonalDataId):
            self.id = PersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeneratedPersonalData(PersonalData):
    """
    Personal Data that is generated or brought into existence without
    relation to existing data i.e. it is not derived or inferred from other
    data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["GeneratedPersonalData"]
    class_class_curie: ClassVar[str] = "dpv:GeneratedPersonalData"
    class_name: ClassVar[str] = "GeneratedPersonalData"
    class_model_uri: ClassVar[URIRef] = DPV.GeneratedPersonalData

    id: Union[str, GeneratedPersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneratedPersonalDataId):
            self.id = GeneratedPersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdentifyingPersonalData(PersonalData):
    """
    Personal Data that explicitly and by itself is sufficient to identify a
    person
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["IdentifyingPersonalData"]
    class_class_curie: ClassVar[str] = "dpv:IdentifyingPersonalData"
    class_name: ClassVar[str] = "IdentifyingPersonalData"
    class_model_uri: ClassVar[URIRef] = DPV.IdentifyingPersonalData

    id: Union[str, IdentifyingPersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdentifyingPersonalDataId):
            self.id = IdentifyingPersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonalDataAudit(InformationAudit):
    """
    An audit that systematically examines the existence and use of personal
    data along with its associated resources (e.g. where it is stored) and
    flows (e.g. where it originates and with whom it is being shared)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonalDataAudit"]
    class_class_curie: ClassVar[str] = "dpv:PersonalDataAudit"
    class_name: ClassVar[str] = "PersonalDataAudit"
    class_model_uri: ClassVar[URIRef] = DPV.PersonalDataAudit

    id: Union[str, PersonalDataAuditId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonalDataAuditId):
            self.id = PersonalDataAuditId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalAccessControlMethod(AccessControlMethod):
    """
    Access control applied for physical access e.g. premises or equipment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PhysicalAccessControlMethod"]
    class_class_curie: ClassVar[str] = "dpv:PhysicalAccessControlMethod"
    class_name: ClassVar[str] = "PhysicalAccessControlMethod"
    class_model_uri: ClassVar[URIRef] = DPV.PhysicalAccessControlMethod

    id: Union[str, PhysicalAccessControlMethodId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalAccessControlMethodId):
            self.id = PhysicalAccessControlMethodId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalAuthentication(PhysicalMeasure):
    """
    Physical implementation of authentication e.g. by matching the person to
    their ID card
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PhysicalAuthentication"]
    class_class_curie: ClassVar[str] = "dpv:PhysicalAuthentication"
    class_name: ClassVar[str] = "PhysicalAuthentication"
    class_model_uri: ClassVar[URIRef] = DPV.PhysicalAuthentication

    id: Union[str, PhysicalAuthenticationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalAuthenticationId):
            self.id = PhysicalAuthenticationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalAuthorisation(PhysicalMeasure):
    """
    Physical implementation of authorisation e.g. by stamping a visitor pass
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PhysicalAuthorisation"]
    class_class_curie: ClassVar[str] = "dpv:PhysicalAuthorisation"
    class_name: ClassVar[str] = "PhysicalAuthorisation"
    class_model_uri: ClassVar[URIRef] = DPV.PhysicalAuthorisation

    id: Union[str, PhysicalAuthorisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalAuthorisationId):
            self.id = PhysicalAuthorisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalDeviceSecurity(PhysicalMeasure):
    """
    Physical protection for devices and equipment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PhysicalDeviceSecurity"]
    class_class_curie: ClassVar[str] = "dpv:PhysicalDeviceSecurity"
    class_name: ClassVar[str] = "PhysicalDeviceSecurity"
    class_model_uri: ClassVar[URIRef] = DPV.PhysicalDeviceSecurity

    id: Union[str, PhysicalDeviceSecurityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalDeviceSecurityId):
            self.id = PhysicalDeviceSecurityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalInterceptionProtection(PhysicalMeasure):
    """
    Physical protection against interception e.g. by posting a guard
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PhysicalInterceptionProtection"]
    class_class_curie: ClassVar[str] = "dpv:PhysicalInterceptionProtection"
    class_name: ClassVar[str] = "PhysicalInterceptionProtection"
    class_model_uri: ClassVar[URIRef] = DPV.PhysicalInterceptionProtection

    id: Union[str, PhysicalInterceptionProtectionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalInterceptionProtectionId):
            self.id = PhysicalInterceptionProtectionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalInterruptionProtection(PhysicalMeasure):
    """
    Physical protection against interruptions e.g. electrical supply
    interruption
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PhysicalInterruptionProtection"]
    class_class_curie: ClassVar[str] = "dpv:PhysicalInterruptionProtection"
    class_name: ClassVar[str] = "PhysicalInterruptionProtection"
    class_model_uri: ClassVar[URIRef] = DPV.PhysicalInterruptionProtection

    id: Union[str, PhysicalInterruptionProtectionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalInterruptionProtectionId):
            self.id = PhysicalInterruptionProtectionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalNetworkSecurity(PhysicalMeasure):
    """
    Physical protection for networks and networking related infrastructure
    e.g. by isolating networking equipments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PhysicalNetworkSecurity"]
    class_class_curie: ClassVar[str] = "dpv:PhysicalNetworkSecurity"
    class_name: ClassVar[str] = "PhysicalNetworkSecurity"
    class_model_uri: ClassVar[URIRef] = DPV.PhysicalNetworkSecurity

    id: Union[str, PhysicalNetworkSecurityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalNetworkSecurityId):
            self.id = PhysicalNetworkSecurityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalSecureStorage(PhysicalMeasure):
    """
    Physical protection for storage of information or equipment e.g. secure
    storage for files
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PhysicalSecureStorage"]
    class_class_curie: ClassVar[str] = "dpv:PhysicalSecureStorage"
    class_name: ClassVar[str] = "PhysicalSecureStorage"
    class_model_uri: ClassVar[URIRef] = DPV.PhysicalSecureStorage

    id: Union[str, PhysicalSecureStorageId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalSecureStorageId):
            self.id = PhysicalSecureStorageId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalSupplySecurity(PhysicalMeasure):
    """
    Physically securing the supply of resources
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PhysicalSupplySecurity"]
    class_class_curie: ClassVar[str] = "dpv:PhysicalSupplySecurity"
    class_name: ClassVar[str] = "PhysicalSupplySecurity"
    class_model_uri: ClassVar[URIRef] = DPV.PhysicalSupplySecurity

    id: Union[str, PhysicalSupplySecurityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalSupplySecurityId):
            self.id = PhysicalSupplySecurityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhysicalSurveillance(PhysicalMeasure):
    """
    Physically monitoring areas via surveillance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PhysicalSurveillance"]
    class_class_curie: ClassVar[str] = "dpv:PhysicalSurveillance"
    class_name: ClassVar[str] = "PhysicalSurveillance"
    class_model_uri: ClassVar[URIRef] = DPV.PhysicalSurveillance

    id: Union[str, PhysicalSurveillanceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhysicalSurveillanceId):
            self.id = PhysicalSurveillanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Policy(GovernanceProcedures):
    """
    A guidance document outlining any of: procedures, plans, principles,
    decisions, intent, or protocols.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Policy"]
    class_class_curie: ClassVar[str] = "dpv:Policy"
    class_name: ClassVar[str] = "Policy"
    class_model_uri: ClassVar[URIRef] = DPV.Policy

    id: Union[str, PolicyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PolicyId):
            self.id = PolicyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AcceptableUsePolicy(Policy):
    """
    Acceptable Use Policy (AUP) refers to conditions, contexts, or uses
    which are considered acceptable with the implication that those not
    covered by such a policy are to be considered unacceptable
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AcceptableUsePolicy"]
    class_class_curie: ClassVar[str] = "dpv:AcceptableUsePolicy"
    class_name: ClassVar[str] = "AcceptableUsePolicy"
    class_model_uri: ClassVar[URIRef] = DPV.AcceptableUsePolicy

    id: Union[str, AcceptableUsePolicyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcceptableUsePolicyId):
            self.id = AcceptableUsePolicyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProcessingPolicy(Policy):
    """
    Policy regarding data processing activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataProcessingPolicy"]
    class_class_curie: ClassVar[str] = "dpv:DataProcessingPolicy"
    class_name: ClassVar[str] = "DataProcessingPolicy"
    class_model_uri: ClassVar[URIRef] = DPV.DataProcessingPolicy

    id: Union[str, DataProcessingPolicyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataProcessingPolicyId):
            self.id = DataProcessingPolicyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataDeletionPolicy(DataProcessingPolicy):
    """
    Policy regarding deletion of data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataDeletionPolicy"]
    class_class_curie: ClassVar[str] = "dpv:DataDeletionPolicy"
    class_name: ClassVar[str] = "DataDeletionPolicy"
    class_model_uri: ClassVar[URIRef] = DPV.DataDeletionPolicy

    id: Union[str, DataDeletionPolicyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataDeletionPolicyId):
            self.id = DataDeletionPolicyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataErasurePolicy(DataProcessingPolicy):
    """
    Policy regarding erasure of data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataErasurePolicy"]
    class_class_curie: ClassVar[str] = "dpv:DataErasurePolicy"
    class_name: ClassVar[str] = "DataErasurePolicy"
    class_model_uri: ClassVar[URIRef] = DPV.DataErasurePolicy

    id: Union[str, DataErasurePolicyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataErasurePolicyId):
            self.id = DataErasurePolicyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataJurisdictionPolicy(DataProcessingPolicy):
    """
    Policy specifying jurisdictional requirements for data processing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataJurisdictionPolicy"]
    class_class_curie: ClassVar[str] = "dpv:DataJurisdictionPolicy"
    class_name: ClassVar[str] = "DataJurisdictionPolicy"
    class_model_uri: ClassVar[URIRef] = DPV.DataJurisdictionPolicy

    id: Union[str, DataJurisdictionPolicyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataJurisdictionPolicyId):
            self.id = DataJurisdictionPolicyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataRestorationPolicy(DataProcessingPolicy):
    """
    Policy regarding restoration of data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataRestorationPolicy"]
    class_class_curie: ClassVar[str] = "dpv:DataRestorationPolicy"
    class_name: ClassVar[str] = "DataRestorationPolicy"
    class_model_uri: ClassVar[URIRef] = DPV.DataRestorationPolicy

    id: Union[str, DataRestorationPolicyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataRestorationPolicyId):
            self.id = DataRestorationPolicyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataReusePolicy(DataProcessingPolicy):
    """
    Policy regarding reuse of data i.e. using data for purposes other than
    its initial purpose
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataReusePolicy"]
    class_class_curie: ClassVar[str] = "dpv:DataReusePolicy"
    class_name: ClassVar[str] = "DataReusePolicy"
    class_model_uri: ClassVar[URIRef] = DPV.DataReusePolicy

    id: Union[str, DataReusePolicyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataReusePolicyId):
            self.id = DataReusePolicyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataStoragePolicy(DataProcessingPolicy):
    """
    Policy regarding storage of data, including the manner, duration,
    location, and conditions for storage
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataStoragePolicy"]
    class_class_curie: ClassVar[str] = "dpv:DataStoragePolicy"
    class_name: ClassVar[str] = "DataStoragePolicy"
    class_model_uri: ClassVar[URIRef] = DPV.DataStoragePolicy

    id: Union[str, DataStoragePolicyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataStoragePolicyId):
            self.id = DataStoragePolicyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InformationSecurityPolicy(Policy):
    """
    Policy regarding security of information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InformationSecurityPolicy"]
    class_class_curie: ClassVar[str] = "dpv:InformationSecurityPolicy"
    class_name: ClassVar[str] = "InformationSecurityPolicy"
    class_model_uri: ClassVar[URIRef] = DPV.InformationSecurityPolicy

    id: Union[str, InformationSecurityPolicyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationSecurityPolicyId):
            self.id = InformationSecurityPolicyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LoggingPolicy(Policy):
    """
    Policy for logging of information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LoggingPolicy"]
    class_class_curie: ClassVar[str] = "dpv:LoggingPolicy"
    class_name: ClassVar[str] = "LoggingPolicy"
    class_model_uri: ClassVar[URIRef] = DPV.LoggingPolicy

    id: Union[str, LoggingPolicyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LoggingPolicyId):
            self.id = LoggingPolicyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MonitoringPolicy(Policy):
    """
    Policy for monitoring (e.g. progress, performance)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MonitoringPolicy"]
    class_class_curie: ClassVar[str] = "dpv:MonitoringPolicy"
    class_name: ClassVar[str] = "MonitoringPolicy"
    class_model_uri: ClassVar[URIRef] = DPV.MonitoringPolicy

    id: Union[str, MonitoringPolicyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MonitoringPolicyId):
            self.id = MonitoringPolicyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PostQuantumCryptography(CryptographicMethods):
    """
    Use of algorithms that are intended to be secure against cryptanalytic
    attack by a quantum computer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PostQuantumCryptography"]
    class_class_curie: ClassVar[str] = "dpv:PostQuantumCryptography"
    class_name: ClassVar[str] = "PostQuantumCryptography"
    class_model_uri: ClassVar[URIRef] = DPV.PostQuantumCryptography

    id: Union[str, PostQuantumCryptographyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PostQuantumCryptographyId):
            self.id = PostQuantumCryptographyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Principle(GuidelinesPrinciple):
    """
    A representation of values or norms that must be taken into
    consideration when conducting activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Principle"]
    class_class_curie: ClassVar[str] = "dpv:Principle"
    class_name: ClassVar[str] = "Principle"
    class_model_uri: ClassVar[URIRef] = DPV.Principle

    id: Union[str, PrincipleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrincipleId):
            self.id = PrincipleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivacyByDefault(GuidelinesPrinciple):
    """
    Practices regarding setting the default configurations of information
    and services to implement data protection and privacy (synonymous with
    Data Protection by Default)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PrivacyByDefault"]
    class_class_curie: ClassVar[str] = "dpv:PrivacyByDefault"
    class_name: ClassVar[str] = "PrivacyByDefault"
    class_model_uri: ClassVar[URIRef] = DPV.PrivacyByDefault

    id: Union[str, PrivacyByDefaultId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivacyByDefaultId):
            self.id = PrivacyByDefaultId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivacyByDesign(GuidelinesPrinciple):
    """
    Practices regarding incorporating data protection and privacy in the
    design of information and services (synonymous with Data Protection by
    Design)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PrivacyByDesign"]
    class_class_curie: ClassVar[str] = "dpv:PrivacyByDesign"
    class_name: ClassVar[str] = "PrivacyByDesign"
    class_model_uri: ClassVar[URIRef] = DPV.PrivacyByDesign

    id: Union[str, PrivacyByDesignId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivacyByDesignId):
            self.id = PrivacyByDesignId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivacyPreservingProtocol(CryptographicMethods):
    """
    Use of protocols designed with the intention of provided additional
    guarantees regarding privacy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PrivacyPreservingProtocol"]
    class_class_curie: ClassVar[str] = "dpv:PrivacyPreservingProtocol"
    class_name: ClassVar[str] = "PrivacyPreservingProtocol"
    class_model_uri: ClassVar[URIRef] = DPV.PrivacyPreservingProtocol

    id: Union[str, PrivacyPreservingProtocolId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivacyPreservingProtocolId):
            self.id = PrivacyPreservingProtocolId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivateInformationRetrieval(CryptographicMethods):
    """
    Use of cryptographic methods to retrieve a record from a system without
    revealing which record is retrieved
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PrivateInformationRetrieval"]
    class_class_curie: ClassVar[str] = "dpv:PrivateInformationRetrieval"
    class_name: ClassVar[str] = "PrivateInformationRetrieval"
    class_model_uri: ClassVar[URIRef] = DPV.PrivateInformationRetrieval

    id: Union[str, PrivateInformationRetrievalId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivateInformationRetrievalId):
            self.id = PrivateInformationRetrievalId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProfessionalConfidentialData(ConfidentialData):
    """
    Data protected by professional secrecy or confidentiality, including but
    not limited to data covered by professional privilege or secrecy
    obligations such as that covered by lawyer or doctor-patient
    confidentiality and other forms of recognised professional
    confidentiality obligations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProfessionalConfidentialData"]
    class_class_curie: ClassVar[str] = "dpv:ProfessionalConfidentialData"
    class_name: ClassVar[str] = "ProfessionalConfidentialData"
    class_model_uri: ClassVar[URIRef] = DPV.ProfessionalConfidentialData

    id: Union[str, ProfessionalConfidentialDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProfessionalConfidentialDataId):
            self.id = ProfessionalConfidentialDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProvidedData(CollectedData):
    """
    Data that has been provided by an entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProvidedData"]
    class_class_curie: ClassVar[str] = "dpv:ProvidedData"
    class_name: ClassVar[str] = "ProvidedData"
    class_model_uri: ClassVar[URIRef] = DPV.ProvidedData

    id: Union[str, ProvidedDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProvidedDataId):
            self.id = ProvidedDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProvidedPersonalData(CollectedPersonalData):
    """
    Personal Data that has been provided by an entity such as the Data
    Subject
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProvidedPersonalData"]
    class_class_curie: ClassVar[str] = "dpv:ProvidedPersonalData"
    class_name: ClassVar[str] = "ProvidedPersonalData"
    class_model_uri: ClassVar[URIRef] = DPV.ProvidedPersonalData

    id: Union[str, ProvidedPersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProvidedPersonalDataId):
            self.id = ProvidedPersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Pseudonymisation(Deidentification):
    """
    Pseudonymisation means the processing of personal data in such a manner
    that the personal data can no longer be attributed to a specific data
    subject without the use of additional information, provided that such
    additional information is kept separately and is subject to technical
    and organisational measures to ensure that the personal data are not
    attributed to an identified or identifiable natural person;
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Pseudonymisation"]
    class_class_curie: ClassVar[str] = "dpv:Pseudonymisation"
    class_name: ClassVar[str] = "Pseudonymisation"
    class_model_uri: ClassVar[URIRef] = DPV.Pseudonymisation

    id: Union[str, PseudonymisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PseudonymisationId):
            self.id = PseudonymisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DeterministicPseudonymisation(Pseudonymisation):
    """
    Pseudonymisation achieved through a deterministic function
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DeterministicPseudonymisation"]
    class_class_curie: ClassVar[str] = "dpv:DeterministicPseudonymisation"
    class_name: ClassVar[str] = "DeterministicPseudonymisation"
    class_model_uri: ClassVar[URIRef] = DPV.DeterministicPseudonymisation

    id: Union[str, DeterministicPseudonymisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeterministicPseudonymisationId):
            self.id = DeterministicPseudonymisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DocumentRandomisedPseudonymisation(Pseudonymisation):
    """
    Use of randomised pseudonymisation where the same elements are assigned
    different values in the same document or database
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DocumentRandomisedPseudonymisation"]
    class_class_curie: ClassVar[str] = "dpv:DocumentRandomisedPseudonymisation"
    class_name: ClassVar[str] = "DocumentRandomisedPseudonymisation"
    class_model_uri: ClassVar[URIRef] = DPV.DocumentRandomisedPseudonymisation

    id: Union[str, DocumentRandomisedPseudonymisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DocumentRandomisedPseudonymisationId):
            self.id = DocumentRandomisedPseudonymisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FullyRandomisedPseudonymisation(Pseudonymisation):
    """
    Use of randomised pseudonymisation where the same elements are assigned
    different values each time they occur
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FullyRandomisedPseudonymisation"]
    class_class_curie: ClassVar[str] = "dpv:FullyRandomisedPseudonymisation"
    class_name: ClassVar[str] = "FullyRandomisedPseudonymisation"
    class_model_uri: ClassVar[URIRef] = DPV.FullyRandomisedPseudonymisation

    id: Union[str, FullyRandomisedPseudonymisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FullyRandomisedPseudonymisationId):
            self.id = FullyRandomisedPseudonymisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MonotonicCounterPseudonymisation(Pseudonymisation):
    """
    A simple pseudonymisation method where identifiers are substituted by a
    number chosen by a monotonic counter
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MonotonicCounterPseudonymisation"]
    class_class_curie: ClassVar[str] = "dpv:MonotonicCounterPseudonymisation"
    class_name: ClassVar[str] = "MonotonicCounterPseudonymisation"
    class_model_uri: ClassVar[URIRef] = DPV.MonotonicCounterPseudonymisation

    id: Union[str, MonotonicCounterPseudonymisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MonotonicCounterPseudonymisationId):
            self.id = MonotonicCounterPseudonymisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PseudonymisedData(PersonalData):
    """
    Pseudonymised Data is data that has gone a partial or incomplete
    anonymisation process by replacing the identifiable information with
    artificial identifiers or 'pseudonyms', and is still considered as
    personal data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PseudonymisedData"]
    class_class_curie: ClassVar[str] = "dpv:PseudonymisedData"
    class_name: ClassVar[str] = "PseudonymisedData"
    class_model_uri: ClassVar[URIRef] = DPV.PseudonymisedData

    id: Union[str, PseudonymisedDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PseudonymisedDataId):
            self.id = PseudonymisedDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContextuallyAnonymisedData(PseudonymisedData):
    """
    Data that can be considered as being fully anonymised within the context
    but in actuality is not fully anonymised and is still personal data as
    it can be de-anonymised outside that context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContextuallyAnonymisedData"]
    class_class_curie: ClassVar[str] = "dpv:ContextuallyAnonymisedData"
    class_name: ClassVar[str] = "ContextuallyAnonymisedData"
    class_model_uri: ClassVar[URIRef] = DPV.ContextuallyAnonymisedData

    id: Union[str, ContextuallyAnonymisedDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContextuallyAnonymisedDataId):
            self.id = ContextuallyAnonymisedDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantumCryptography(CryptographicMethods):
    """
    Cryptographic methods that utilise quantum mechanical properties to
    perform cryptographic tasks
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["QuantumCryptography"]
    class_class_curie: ClassVar[str] = "dpv:QuantumCryptography"
    class_name: ClassVar[str] = "QuantumCryptography"
    class_model_uri: ClassVar[URIRef] = DPV.QuantumCryptography

    id: Union[str, QuantumCryptographyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuantumCryptographyId):
            self.id = QuantumCryptographyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RNGPseudonymisation(Pseudonymisation):
    """
    A pseudonymisation method where identifiers are substituted by a number
    chosen by a Random Number Generator (RNG)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RNGPseudonymisation"]
    class_class_curie: ClassVar[str] = "dpv:RNGPseudonymisation"
    class_name: ClassVar[str] = "RNGPseudonymisation"
    class_model_uri: ClassVar[URIRef] = DPV.RNGPseudonymisation

    id: Union[str, RNGPseudonymisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RNGPseudonymisationId):
            self.id = RNGPseudonymisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecertificationPolicy(Policy):
    """
    Policy regarding repetition or renewal of existing certification(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecertificationPolicy"]
    class_class_curie: ClassVar[str] = "dpv:RecertificationPolicy"
    class_name: ClassVar[str] = "RecertificationPolicy"
    class_model_uri: ClassVar[URIRef] = DPV.RecertificationPolicy

    id: Union[str, RecertificationPolicyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecertificationPolicyId):
            self.id = RecertificationPolicyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecordsOfActivities(OrganisationalMeasure):
    """
    Records of activities within some context such as maintenance tasks or
    governance functions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecordsOfActivities"]
    class_class_curie: ClassVar[str] = "dpv:RecordsOfActivities"
    class_name: ClassVar[str] = "RecordsOfActivities"
    class_model_uri: ClassVar[URIRef] = DPV.RecordsOfActivities

    id: Union[str, RecordsOfActivitiesId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecordsOfActivitiesId):
            self.id = RecordsOfActivitiesId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataBreachRecord(RecordsOfActivities):
    """
    Record of a data breach incident
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataBreachRecord"]
    class_class_curie: ClassVar[str] = "dpv:DataBreachRecord"
    class_name: ClassVar[str] = "DataBreachRecord"
    class_model_uri: ClassVar[URIRef] = DPV.DataBreachRecord

    id: Union[str, DataBreachRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataBreachRecordId):
            self.id = DataBreachRecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProcessingRecord(RecordsOfActivities):
    """
    Record of data processing, whether ex-ante or ex-post
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataProcessingRecord"]
    class_class_curie: ClassVar[str] = "dpv:DataProcessingRecord"
    class_name: ClassVar[str] = "DataProcessingRecord"
    class_model_uri: ClassVar[URIRef] = DPV.DataProcessingRecord

    id: Union[str, DataProcessingRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataProcessingRecordId):
            self.id = DataProcessingRecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentRecord(DataProcessingRecord):
    """
    A Record of Consent or Consent related activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentRecord"]
    class_class_curie: ClassVar[str] = "dpv:ConsentRecord"
    class_name: ClassVar[str] = "ConsentRecord"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentRecord

    id: Union[str, ConsentRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentRecordId):
            self.id = ConsentRecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentReceipt(ConsentRecord):
    """
    A record of consent or consent related activities that is provided to
    another entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentReceipt"]
    class_class_curie: ClassVar[str] = "dpv:ConsentReceipt"
    class_name: ClassVar[str] = "ConsentReceipt"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentReceipt

    id: Union[str, ConsentReceiptId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentReceiptId):
            self.id = ConsentReceiptId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataTransferRecord(DataProcessingRecord):
    """
    Record of data transfer activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataTransferRecord"]
    class_class_curie: ClassVar[str] = "dpv:DataTransferRecord"
    class_name: ClassVar[str] = "DataTransferRecord"
    class_model_uri: ClassVar[URIRef] = DPV.DataTransferRecord

    id: Union[str, DataTransferRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataTransferRecordId):
            self.id = DataTransferRecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ROPA(DataProcessingRecord):
    """
    A Record of Processing Activities (ROPA) is a document detailing
    processing activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ROPA"]
    class_class_curie: ClassVar[str] = "dpv:ROPA"
    class_name: ClassVar[str] = "ROPA"
    class_model_uri: ClassVar[URIRef] = DPV.ROPA

    id: Union[str, ROPAId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ROPAId):
            self.id = ROPAId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReviewProcedure(GovernanceProcedures):
    """
    A procedure or process that reviews the correctness and validity of
    other procedures and policies e.g. to ensure continued validity,
    adequacy for intended purposes, and conformance of processes with
    findings
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ReviewProcedure"]
    class_class_curie: ClassVar[str] = "dpv:ReviewProcedure"
    class_name: ClassVar[str] = "ReviewProcedure"
    class_model_uri: ClassVar[URIRef] = DPV.ReviewProcedure

    id: Union[str, ReviewProcedureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReviewProcedureId):
            self.id = ReviewProcedureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RightsManagement(OrganisationalMeasure):
    """
    Methods associated with rights management where 'rights' refer to
    controlling who can do what with a resource
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RightsManagement"]
    class_class_curie: ClassVar[str] = "dpv:RightsManagement"
    class_name: ClassVar[str] = "RightsManagement"
    class_model_uri: ClassVar[URIRef] = DPV.RightsManagement

    id: Union[str, RightsManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RightsManagementId):
            self.id = RightsManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSubjectRightsManagement(RightsManagement):
    """
    Methods to provide, implement, and exercise data subjects' rights
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSubjectRightsManagement"]
    class_class_curie: ClassVar[str] = "dpv:DataSubjectRightsManagement"
    class_name: ClassVar[str] = "DataSubjectRightsManagement"
    class_model_uri: ClassVar[URIRef] = DPV.DataSubjectRightsManagement

    id: Union[str, DataSubjectRightsManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSubjectRightsManagementId):
            self.id = DataSubjectRightsManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IPRManagement(RightsManagement):
    """
    Management of Intellectual Property Rights with a view to identify and
    safeguard and enforce them
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["IPRManagement"]
    class_class_curie: ClassVar[str] = "dpv:IPRManagement"
    class_name: ClassVar[str] = "IPRManagement"
    class_model_uri: ClassVar[URIRef] = DPV.IPRManagement

    id: Union[str, IPRManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IPRManagementId):
            self.id = IPRManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PermissionManagement(RightsManagement):
    """
    Methods to obtain, provide, modify, and withdraw permissions along with
    maintaining a record of permissions, retrieving records, and processing
    changes in permission states
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PermissionManagement"]
    class_class_curie: ClassVar[str] = "dpv:PermissionManagement"
    class_name: ClassVar[str] = "PermissionManagement"
    class_model_uri: ClassVar[URIRef] = DPV.PermissionManagement

    id: Union[str, PermissionManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PermissionManagementId):
            self.id = PermissionManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentManagement(PermissionManagement):
    """
    Methods to obtain, provide, modify, and withdraw consent along with
    maintaining a record of consent, retrieving records, and processing
    changes in consent states
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentManagement"]
    class_class_curie: ClassVar[str] = "dpv:ConsentManagement"
    class_name: ClassVar[str] = "ConsentManagement"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentManagement

    id: Union[str, ConsentManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentManagementId):
            self.id = ConsentManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Safeguard(OrganisationalMeasure):
    """
    A safeguard is a precautionary measure for the protection against or
    mitigation of negative effects
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Safeguard"]
    class_class_curie: ClassVar[str] = "dpv:Safeguard"
    class_name: ClassVar[str] = "Safeguard"
    class_model_uri: ClassVar[URIRef] = DPV.Safeguard

    id: Union[str, SafeguardId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SafeguardId):
            self.id = SafeguardId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RegulatorySandbox(Safeguard):
    """
    Mechanism used by regulators and businesses for gauging the
    compatibility of regulations and innovative products, particularly in
    the context of digitalisation, in a controlled real-world environment
    with appropriate safeguards in place
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RegulatorySandbox"]
    class_class_curie: ClassVar[str] = "dpv:RegulatorySandbox"
    class_name: ClassVar[str] = "RegulatorySandbox"
    class_model_uri: ClassVar[URIRef] = DPV.RegulatorySandbox

    id: Union[str, RegulatorySandboxId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegulatorySandboxId):
            self.id = RegulatorySandboxId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SafeguardForDataTransfer(Safeguard):
    """
    Represents a safeguard used for data transfer. Can include technical or
    organisational measures.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SafeguardForDataTransfer"]
    class_class_curie: ClassVar[str] = "dpv:SafeguardForDataTransfer"
    class_name: ClassVar[str] = "SafeguardForDataTransfer"
    class_model_uri: ClassVar[URIRef] = DPV.SafeguardForDataTransfer

    id: Union[str, SafeguardForDataTransferId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SafeguardForDataTransferId):
            self.id = SafeguardForDataTransferId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Seal(CertificationSeal):
    """
    A seal or a mark indicating proof of certification to some certification
    or standard
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Seal"]
    class_class_curie: ClassVar[str] = "dpv:Seal"
    class_name: ClassVar[str] = "Seal"
    class_model_uri: ClassVar[URIRef] = DPV.Seal

    id: Union[str, SealId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SealId):
            self.id = SealId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecretSharingSchemes(CryptographicMethods):
    """
    Use of secret sharing schemes where the secret can only be reconstructed
    through combination of sufficient number of individuals
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SecretSharingSchemes"]
    class_class_curie: ClassVar[str] = "dpv:SecretSharingSchemes"
    class_name: ClassVar[str] = "SecretSharingSchemes"
    class_model_uri: ClassVar[URIRef] = DPV.SecretSharingSchemes

    id: Union[str, SecretSharingSchemesId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecretSharingSchemesId):
            self.id = SecretSharingSchemesId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecureMultiPartyComputation(CryptographicMethods):
    """
    Use of cryptographic methods for entities to jointly compute functions
    without revealing inputs
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SecureMultiPartyComputation"]
    class_class_curie: ClassVar[str] = "dpv:SecureMultiPartyComputation"
    class_name: ClassVar[str] = "SecureMultiPartyComputation"
    class_model_uri: ClassVar[URIRef] = DPV.SecureMultiPartyComputation

    id: Union[str, SecureMultiPartyComputationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecureMultiPartyComputationId):
            self.id = SecureMultiPartyComputationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecurityAudit(Audit):
    """
    An audit that systematically examines the existence and use of security
    risks and measures within information systems, networks, and security
    policies to identify vulnerabilities, risks, and gaps
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SecurityAudit"]
    class_class_curie: ClassVar[str] = "dpv:SecurityAudit"
    class_name: ClassVar[str] = "SecurityAudit"
    class_model_uri: ClassVar[URIRef] = DPV.SecurityAudit

    id: Union[str, SecurityAuditId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecurityAuditId):
            self.id = SecurityAuditId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecurityIncidentNotification(Notification):
    """
    Notification of information about security incident(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SecurityIncidentNotification"]
    class_class_curie: ClassVar[str] = "dpv:SecurityIncidentNotification"
    class_name: ClassVar[str] = "SecurityIncidentNotification"
    class_model_uri: ClassVar[URIRef] = DPV.SecurityIncidentNotification

    id: Union[str, SecurityIncidentNotificationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecurityIncidentNotificationId):
            self.id = SecurityIncidentNotificationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataBreachNotification(SecurityIncidentNotification):
    """
    Notification of information about data breach(es) i.e. unauthorised
    transfer, access, use, or modification of data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataBreachNotification"]
    class_class_curie: ClassVar[str] = "dpv:DataBreachNotification"
    class_name: ClassVar[str] = "DataBreachNotification"
    class_model_uri: ClassVar[URIRef] = DPV.DataBreachNotification

    id: Union[str, DataBreachNotificationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataBreachNotificationId):
            self.id = DataBreachNotificationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecurityIncidentRecord(RecordsOfActivities):
    """
    Record of a security incident
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SecurityIncidentRecord"]
    class_class_curie: ClassVar[str] = "dpv:SecurityIncidentRecord"
    class_name: ClassVar[str] = "SecurityIncidentRecord"
    class_model_uri: ClassVar[URIRef] = DPV.SecurityIncidentRecord

    id: Union[str, SecurityIncidentRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecurityIncidentRecordId):
            self.id = SecurityIncidentRecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecurityMethod(TechnicalMeasure):
    """
    Methods that relate to creating and providing security
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SecurityMethod"]
    class_class_curie: ClassVar[str] = "dpv:SecurityMethod"
    class_name: ClassVar[str] = "SecurityMethod"
    class_model_uri: ClassVar[URIRef] = DPV.SecurityMethod

    id: Union[str, SecurityMethodId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecurityMethodId):
            self.id = SecurityMethodId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DistributedSystemSecurity(SecurityMethod):
    """
    Security implementations provided using or over a distributed system
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DistributedSystemSecurity"]
    class_class_curie: ClassVar[str] = "dpv:DistributedSystemSecurity"
    class_name: ClassVar[str] = "DistributedSystemSecurity"
    class_model_uri: ClassVar[URIRef] = DPV.DistributedSystemSecurity

    id: Union[str, DistributedSystemSecurityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DistributedSystemSecurityId):
            self.id = DistributedSystemSecurityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DocumentSecurity(SecurityMethod):
    """
    Security measures enacted over documents to protect against tampering or
    restrict access
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DocumentSecurity"]
    class_class_curie: ClassVar[str] = "dpv:DocumentSecurity"
    class_name: ClassVar[str] = "DocumentSecurity"
    class_model_uri: ClassVar[URIRef] = DPV.DocumentSecurity

    id: Union[str, DocumentSecurityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DocumentSecurityId):
            self.id = DocumentSecurityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FileSystemSecurity(SecurityMethod):
    """
    Security implemented over a file system
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FileSystemSecurity"]
    class_class_curie: ClassVar[str] = "dpv:FileSystemSecurity"
    class_name: ClassVar[str] = "FileSystemSecurity"
    class_model_uri: ClassVar[URIRef] = DPV.FileSystemSecurity

    id: Union[str, FileSystemSecurityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FileSystemSecurityId):
            self.id = FileSystemSecurityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HardwareSecurityProtocols(SecurityMethod):
    """
    Security protocols implemented at or within hardware
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HardwareSecurityProtocols"]
    class_class_curie: ClassVar[str] = "dpv:HardwareSecurityProtocols"
    class_name: ClassVar[str] = "HardwareSecurityProtocols"
    class_model_uri: ClassVar[URIRef] = DPV.HardwareSecurityProtocols

    id: Union[str, HardwareSecurityProtocolsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HardwareSecurityProtocolsId):
            self.id = HardwareSecurityProtocolsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IntrusionDetectionSystem(SecurityMethod):
    """
    Use of measures to detect intrusions and other unauthorised attempts to
    gain access to a system
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["IntrusionDetectionSystem"]
    class_class_curie: ClassVar[str] = "dpv:IntrusionDetectionSystem"
    class_name: ClassVar[str] = "IntrusionDetectionSystem"
    class_model_uri: ClassVar[URIRef] = DPV.IntrusionDetectionSystem

    id: Union[str, IntrusionDetectionSystemId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntrusionDetectionSystemId):
            self.id = IntrusionDetectionSystemId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MobilePlatformSecurity(SecurityMethod):
    """
    Security implemented over a mobile platform
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MobilePlatformSecurity"]
    class_class_curie: ClassVar[str] = "dpv:MobilePlatformSecurity"
    class_name: ClassVar[str] = "MobilePlatformSecurity"
    class_model_uri: ClassVar[URIRef] = DPV.MobilePlatformSecurity

    id: Union[str, MobilePlatformSecurityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MobilePlatformSecurityId):
            self.id = MobilePlatformSecurityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NetworkProxyRouting(SecurityMethod):
    """
    Use of network routing using proxy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NetworkProxyRouting"]
    class_class_curie: ClassVar[str] = "dpv:NetworkProxyRouting"
    class_name: ClassVar[str] = "NetworkProxyRouting"
    class_model_uri: ClassVar[URIRef] = DPV.NetworkProxyRouting

    id: Union[str, NetworkProxyRoutingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NetworkProxyRoutingId):
            self.id = NetworkProxyRoutingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NetworkSecurityProtocols(SecurityMethod):
    """
    Security implemented at or over networks protocols
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NetworkSecurityProtocols"]
    class_class_curie: ClassVar[str] = "dpv:NetworkSecurityProtocols"
    class_name: ClassVar[str] = "NetworkSecurityProtocols"
    class_model_uri: ClassVar[URIRef] = DPV.NetworkSecurityProtocols

    id: Union[str, NetworkSecurityProtocolsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NetworkSecurityProtocolsId):
            self.id = NetworkSecurityProtocolsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OperatingSystemSecurity(SecurityMethod):
    """
    Security implemented at or through operating systems
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OperatingSystemSecurity"]
    class_class_curie: ClassVar[str] = "dpv:OperatingSystemSecurity"
    class_name: ClassVar[str] = "OperatingSystemSecurity"
    class_model_uri: ClassVar[URIRef] = DPV.OperatingSystemSecurity

    id: Union[str, OperatingSystemSecurityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OperatingSystemSecurityId):
            self.id = OperatingSystemSecurityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PenetrationTestingMethods(SecurityMethod):
    """
    Use of penetration testing to identify weaknesses and vulnerabilities
    through simulations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PenetrationTestingMethods"]
    class_class_curie: ClassVar[str] = "dpv:PenetrationTestingMethods"
    class_name: ClassVar[str] = "PenetrationTestingMethods"
    class_model_uri: ClassVar[URIRef] = DPV.PenetrationTestingMethods

    id: Union[str, PenetrationTestingMethodsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PenetrationTestingMethodsId):
            self.id = PenetrationTestingMethodsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecurityProcedure(OrganisationalMeasure):
    """
    Procedures associated with assessing, implementing, and evaluating
    security
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SecurityProcedure"]
    class_class_curie: ClassVar[str] = "dpv:SecurityProcedure"
    class_name: ClassVar[str] = "SecurityProcedure"
    class_model_uri: ClassVar[URIRef] = DPV.SecurityProcedure

    id: Union[str, SecurityProcedureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecurityProcedureId):
            self.id = SecurityProcedureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AuthorisationProcedure(SecurityProcedure):
    """
    Procedures for determining authorisation through permission or authority
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AuthorisationProcedure"]
    class_class_curie: ClassVar[str] = "dpv:AuthorisationProcedure"
    class_name: ClassVar[str] = "AuthorisationProcedure"
    class_model_uri: ClassVar[URIRef] = DPV.AuthorisationProcedure

    id: Union[str, AuthorisationProcedureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AuthorisationProcedureId):
            self.id = AuthorisationProcedureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BackgroundChecks(SecurityProcedure):
    """
    Procedure where the background of an entity is assessed to identity
    vulnerabilities and threats due to their current or intended role
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["BackgroundChecks"]
    class_class_curie: ClassVar[str] = "dpv:BackgroundChecks"
    class_name: ClassVar[str] = "BackgroundChecks"
    class_model_uri: ClassVar[URIRef] = DPV.BackgroundChecks

    id: Union[str, BackgroundChecksId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BackgroundChecksId):
            self.id = BackgroundChecksId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CredentialManagement(AuthorisationProcedure):
    """
    Management of credentials and their use in authorisations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CredentialManagement"]
    class_class_curie: ClassVar[str] = "dpv:CredentialManagement"
    class_name: ClassVar[str] = "CredentialManagement"
    class_model_uri: ClassVar[URIRef] = DPV.CredentialManagement

    id: Union[str, CredentialManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CredentialManagementId):
            self.id = CredentialManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdentityManagementMethod(AuthorisationProcedure):
    """
    Management of identity and identity-based processes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["IdentityManagementMethod"]
    class_class_curie: ClassVar[str] = "dpv:IdentityManagementMethod"
    class_name: ClassVar[str] = "IdentityManagementMethod"
    class_model_uri: ClassVar[URIRef] = DPV.IdentityManagementMethod

    id: Union[str, IdentityManagementMethodId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdentityManagementMethodId):
            self.id = IdentityManagementMethodId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecureProcessingEnvironment(SecurityProcedure):
    """
    A physical or virtual environment supported by organisational means that
    integrates security and compliance requirements and allows supervising
    data processing actions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SecureProcessingEnvironment"]
    class_class_curie: ClassVar[str] = "dpv:SecureProcessingEnvironment"
    class_name: ClassVar[str] = "SecureProcessingEnvironment"
    class_model_uri: ClassVar[URIRef] = DPV.SecureProcessingEnvironment

    id: Union[str, SecureProcessingEnvironmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecureProcessingEnvironmentId):
            self.id = SecureProcessingEnvironmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecurityRoleProcedures(SecurityProcedure):
    """
    Procedures related to security roles
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SecurityRoleProcedures"]
    class_class_curie: ClassVar[str] = "dpv:SecurityRoleProcedures"
    class_name: ClassVar[str] = "SecurityRoleProcedures"
    class_model_uri: ClassVar[URIRef] = DPV.SecurityRoleProcedures

    id: Union[str, SecurityRoleProceduresId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecurityRoleProceduresId):
            self.id = SecurityRoleProceduresId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SensitiveData(DpvData):
    """
    Data deemed sensitive
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SensitiveData"]
    class_class_curie: ClassVar[str] = "dpv:SensitiveData"
    class_name: ClassVar[str] = "SensitiveData"
    class_model_uri: ClassVar[URIRef] = DPV.SensitiveData

    id: Union[str, SensitiveDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SensitiveDataId):
            self.id = SensitiveDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SensitiveNonPersonalData(SensitiveData):
    """
    Non-personal data deemed sensitive
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SensitiveNonPersonalData"]
    class_class_curie: ClassVar[str] = "dpv:SensitiveNonPersonalData"
    class_name: ClassVar[str] = "SensitiveNonPersonalData"
    class_model_uri: ClassVar[URIRef] = DPV.SensitiveNonPersonalData

    id: Union[str, SensitiveNonPersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SensitiveNonPersonalDataId):
            self.id = SensitiveNonPersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SensitivePersonalData(PersonalData):
    """
    Personal data that is considered 'sensitive' in terms of privacy and/or
    impact, and therefore requires additional considerations and/or
    protection
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SensitivePersonalData"]
    class_class_curie: ClassVar[str] = "dpv:SensitivePersonalData"
    class_name: ClassVar[str] = "SensitivePersonalData"
    class_model_uri: ClassVar[URIRef] = DPV.SensitivePersonalData

    id: Union[str, SensitivePersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SensitivePersonalDataId):
            self.id = SensitivePersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SingleSignOn(AuthenticationProtocols):
    """
    Use of credentials or processes that enable using one set of credentials
    to authenticate multiple contexts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SingleSignOn"]
    class_class_curie: ClassVar[str] = "dpv:SingleSignOn"
    class_name: ClassVar[str] = "SingleSignOn"
    class_model_uri: ClassVar[URIRef] = DPV.SingleSignOn

    id: Union[str, SingleSignOnId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SingleSignOnId):
            self.id = SingleSignOnId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecialCategoryPersonalData(SensitivePersonalData):
    """
    Sensitive Personal Data whose use requires specific additional legal
    permission or justification
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SpecialCategoryPersonalData"]
    class_class_curie: ClassVar[str] = "dpv:SpecialCategoryPersonalData"
    class_name: ClassVar[str] = "SpecialCategoryPersonalData"
    class_model_uri: ClassVar[URIRef] = DPV.SpecialCategoryPersonalData

    id: Union[str, SpecialCategoryPersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SpecialCategoryPersonalDataId):
            self.id = SpecialCategoryPersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StaffTraining(OrganisationalMeasure):
    """
    Practices and policies regarding training of staff members
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["StaffTraining"]
    class_class_curie: ClassVar[str] = "dpv:StaffTraining"
    class_name: ClassVar[str] = "StaffTraining"
    class_model_uri: ClassVar[URIRef] = DPV.StaffTraining

    id: Union[str, StaffTrainingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StaffTrainingId):
            self.id = StaffTrainingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CybersecurityTraining(StaffTraining):
    """
    Training methods related to cybersecurity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CybersecurityTraining"]
    class_class_curie: ClassVar[str] = "dpv:CybersecurityTraining"
    class_name: ClassVar[str] = "CybersecurityTraining"
    class_model_uri: ClassVar[URIRef] = DPV.CybersecurityTraining

    id: Union[str, CybersecurityTrainingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CybersecurityTrainingId):
            self.id = CybersecurityTrainingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataProtectionTraining(StaffTraining):
    """
    Training intended to increase knowledge regarding data protection
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataProtectionTraining"]
    class_class_curie: ClassVar[str] = "dpv:DataProtectionTraining"
    class_name: ClassVar[str] = "DataProtectionTraining"
    class_model_uri: ClassVar[URIRef] = DPV.DataProtectionTraining

    id: Union[str, DataProtectionTrainingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataProtectionTrainingId):
            self.id = DataProtectionTrainingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EducationalTraining(StaffTraining):
    """
    Training methods that are intended to provide education on topic(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EducationalTraining"]
    class_class_curie: ClassVar[str] = "dpv:EducationalTraining"
    class_name: ClassVar[str] = "EducationalTraining"
    class_model_uri: ClassVar[URIRef] = DPV.EducationalTraining

    id: Union[str, EducationalTrainingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EducationalTrainingId):
            self.id = EducationalTrainingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProfessionalTraining(StaffTraining):
    """
    Training methods that are intended to provide professional knowledge and
    expertise
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProfessionalTraining"]
    class_class_curie: ClassVar[str] = "dpv:ProfessionalTraining"
    class_name: ClassVar[str] = "ProfessionalTraining"
    class_model_uri: ClassVar[URIRef] = DPV.ProfessionalTraining

    id: Union[str, ProfessionalTrainingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProfessionalTrainingId):
            self.id = ProfessionalTrainingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecurityKnowledgeTraining(StaffTraining):
    """
    Training intended to increase knowledge regarding security
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SecurityKnowledgeTraining"]
    class_class_curie: ClassVar[str] = "dpv:SecurityKnowledgeTraining"
    class_name: ClassVar[str] = "SecurityKnowledgeTraining"
    class_model_uri: ClassVar[URIRef] = DPV.SecurityKnowledgeTraining

    id: Union[str, SecurityKnowledgeTrainingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecurityKnowledgeTrainingId):
            self.id = SecurityKnowledgeTrainingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Standard(GuidelinesPrinciple):
    """
    A set of requirements or norms that are agreed upon i.e. they are
    considered a 'standard'
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Standard"]
    class_class_curie: ClassVar[str] = "dpv:Standard"
    class_name: ClassVar[str] = "Standard"
    class_model_uri: ClassVar[URIRef] = DPV.Standard

    id: Union[str, StandardId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StandardId):
            self.id = StandardId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DesignStandard(Standard):
    """
    A set of rules or guidelines outlining criterias for design
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DesignStandard"]
    class_class_curie: ClassVar[str] = "dpv:DesignStandard"
    class_name: ClassVar[str] = "DesignStandard"
    class_model_uri: ClassVar[URIRef] = DPV.DesignStandard

    id: Union[str, DesignStandardId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DesignStandardId):
            self.id = DesignStandardId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ManagementStandard(Standard):
    """
    A management standard is a standard that establishes norms or
    requirements regarding the management operations and processes e.g. in
    an organisation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ManagementStandard"]
    class_class_curie: ClassVar[str] = "dpv:ManagementStandard"
    class_name: ClassVar[str] = "ManagementStandard"
    class_model_uri: ClassVar[URIRef] = DPV.ManagementStandard

    id: Union[str, ManagementStandardId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ManagementStandardId):
            self.id = ManagementStandardId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StandardsConformance(GovernanceProcedures):
    """
    Purposes associated with activities undertaken to ensure or achieve
    conformance with standards
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["StandardsConformance"]
    class_class_curie: ClassVar[str] = "dpv:StandardsConformance"
    class_name: ClassVar[str] = "StandardsConformance"
    class_model_uri: ClassVar[URIRef] = DPV.StandardsConformance

    id: Union[str, StandardsConformanceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StandardsConformanceId):
            self.id = StandardsConformanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StatisticallyConfidentialData(ConfidentialData):
    """
    Data protected through Statistical Confidentiality regulations and
    agreements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["StatisticallyConfidentialData"]
    class_class_curie: ClassVar[str] = "dpv:StatisticallyConfidentialData"
    class_name: ClassVar[str] = "StatisticallyConfidentialData"
    class_model_uri: ClassVar[URIRef] = DPV.StatisticallyConfidentialData

    id: Union[str, StatisticallyConfidentialDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StatisticallyConfidentialDataId):
            self.id = StatisticallyConfidentialDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupportEntityDecisionMaking(OrganisationalMeasure):
    """
    Supporting entities, including individuals, in making decisions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SupportEntityDecisionMaking"]
    class_class_curie: ClassVar[str] = "dpv:SupportEntityDecisionMaking"
    class_name: ClassVar[str] = "SupportEntityDecisionMaking"
    class_model_uri: ClassVar[URIRef] = DPV.SupportEntityDecisionMaking

    id: Union[str, SupportEntityDecisionMakingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SupportEntityDecisionMakingId):
            self.id = SupportEntityDecisionMakingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupportContractNegotiation(SupportEntityDecisionMaking):
    """
    Supporting entities, including individuals, with negotiating a contract
    and its terms and conditions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SupportContractNegotiation"]
    class_class_curie: ClassVar[str] = "dpv:SupportContractNegotiation"
    class_name: ClassVar[str] = "SupportContractNegotiation"
    class_model_uri: ClassVar[URIRef] = DPV.SupportContractNegotiation

    id: Union[str, SupportContractNegotiationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SupportContractNegotiationId):
            self.id = SupportContractNegotiationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupportExchangeOfViews(SupportEntityDecisionMaking):
    """
    Supporting individuals and entities in exchanging views e.g. regarding
    data processing purposes for their best interests
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SupportExchangeOfViews"]
    class_class_curie: ClassVar[str] = "dpv:SupportExchangeOfViews"
    class_name: ClassVar[str] = "SupportExchangeOfViews"
    class_model_uri: ClassVar[URIRef] = DPV.SupportExchangeOfViews

    id: Union[str, SupportExchangeOfViewsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SupportExchangeOfViewsId):
            self.id = SupportExchangeOfViewsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupportInformedConsentDecision(SupportEntityDecisionMaking):
    """
    Supporting individuals with making a decision regarding their informed
    consent
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SupportInformedConsentDecision"]
    class_class_curie: ClassVar[str] = "dpv:SupportInformedConsentDecision"
    class_name: ClassVar[str] = "SupportInformedConsentDecision"
    class_model_uri: ClassVar[URIRef] = DPV.SupportInformedConsentDecision

    id: Union[str, SupportInformedConsentDecisionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SupportInformedConsentDecisionId):
            self.id = SupportInformedConsentDecisionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SymmetricCryptography(CryptographicMethods):
    """
    Use of cryptography where the same keys are utilised for encryption and
    decryption of information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SymmetricCryptography"]
    class_class_curie: ClassVar[str] = "dpv:SymmetricCryptography"
    class_name: ClassVar[str] = "SymmetricCryptography"
    class_model_uri: ClassVar[URIRef] = DPV.SymmetricCryptography

    id: Union[str, SymmetricCryptographyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SymmetricCryptographyId):
            self.id = SymmetricCryptographyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SymmetricEncryption(Encryption):
    """
    Use of symmetric cryptography to encrypt data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SymmetricEncryption"]
    class_class_curie: ClassVar[str] = "dpv:SymmetricEncryption"
    class_name: ClassVar[str] = "SymmetricEncryption"
    class_model_uri: ClassVar[URIRef] = DPV.SymmetricEncryption

    id: Union[str, SymmetricEncryptionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SymmetricEncryptionId):
            self.id = SymmetricEncryptionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SyntheticData(GeneratedData):
    """
    Synthetic data refers to artificially created data such that it is
    intended to resemble real data (personal or non-personal), but does not
    refer to any specific identified or identifiable individual, or to the
    real measure of an observable parameter in the case of non-personal data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SyntheticData"]
    class_class_curie: ClassVar[str] = "dpv:SyntheticData"
    class_name: ClassVar[str] = "SyntheticData"
    class_model_uri: ClassVar[URIRef] = DPV.SyntheticData

    id: Union[str, SyntheticDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SyntheticDataId):
            self.id = SyntheticDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TechnicalStandard(Standard):
    """
    A technical standard is a standard that establishes norms or
    requirements regarding technology or technical processes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["TechnicalStandard"]
    class_class_curie: ClassVar[str] = "dpv:TechnicalStandard"
    class_name: ClassVar[str] = "TechnicalStandard"
    class_model_uri: ClassVar[URIRef] = DPV.TechnicalStandard

    id: Union[str, TechnicalStandardId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TechnicalStandardId):
            self.id = TechnicalStandardId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThirdPartySecurityProcedures(SecurityProcedure):
    """
    Procedures related to security associated with Third Parties
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ThirdPartySecurityProcedures"]
    class_class_curie: ClassVar[str] = "dpv:ThirdPartySecurityProcedures"
    class_name: ClassVar[str] = "ThirdPartySecurityProcedures"
    class_model_uri: ClassVar[URIRef] = DPV.ThirdPartySecurityProcedures

    id: Union[str, ThirdPartySecurityProceduresId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThirdPartySecurityProceduresId):
            self.id = ThirdPartySecurityProceduresId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TrustedComputing(CryptographicMethods):
    """
    Use of cryptographic methods to restrict access and execution to trusted
    parties and code
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["TrustedComputing"]
    class_class_curie: ClassVar[str] = "dpv:TrustedComputing"
    class_name: ClassVar[str] = "TrustedComputing"
    class_model_uri: ClassVar[URIRef] = DPV.TrustedComputing

    id: Union[str, TrustedComputingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TrustedComputingId):
            self.id = TrustedComputingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TrustedExecutionEnvironment(CryptographicMethods):
    """
    Use of cryptographic methods to restrict access and execution to trusted
    parties and code within a dedicated execution environment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["TrustedExecutionEnvironment"]
    class_class_curie: ClassVar[str] = "dpv:TrustedExecutionEnvironment"
    class_name: ClassVar[str] = "TrustedExecutionEnvironment"
    class_model_uri: ClassVar[URIRef] = DPV.TrustedExecutionEnvironment

    id: Union[str, TrustedExecutionEnvironmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TrustedExecutionEnvironmentId):
            self.id = TrustedExecutionEnvironmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UncategorisedData(DpvData):
    """
    Data whose categorisation is not known e.g. whether it is personal or
    non-personal data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["UncategorisedData"]
    class_class_curie: ClassVar[str] = "dpv:UncategorisedData"
    class_name: ClassVar[str] = "UncategorisedData"
    class_model_uri: ClassVar[URIRef] = DPV.UncategorisedData

    id: Union[str, UncategorisedDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UncategorisedDataId):
            self.id = UncategorisedDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UnstructuredData(DpvData):
    """
    Data that is without a predefined data model or is not organised in a
    pre-defined manner
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["UnstructuredData"]
    class_class_curie: ClassVar[str] = "dpv:UnstructuredData"
    class_name: ClassVar[str] = "UnstructuredData"
    class_model_uri: ClassVar[URIRef] = DPV.UnstructuredData

    id: Union[str, UnstructuredDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnstructuredDataId):
            self.id = UnstructuredDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UnverifiedData(DpvData):
    """
    Data that has not been verified in terms of accuracy, inconsistency, or
    quality
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["UnverifiedData"]
    class_class_curie: ClassVar[str] = "dpv:UnverifiedData"
    class_name: ClassVar[str] = "UnverifiedData"
    class_model_uri: ClassVar[URIRef] = DPV.UnverifiedData

    id: Union[str, UnverifiedDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnverifiedDataId):
            self.id = UnverifiedDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UsageControl(AccessControlMethod):
    """
    Management of usage, which is intended to be broader than access control
    and may cover trust, digital rights, or other relevant controls
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["UsageControl"]
    class_class_curie: ClassVar[str] = "dpv:UsageControl"
    class_name: ClassVar[str] = "UsageControl"
    class_model_uri: ClassVar[URIRef] = DPV.UsageControl

    id: Union[str, UsageControlId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UsageControlId):
            self.id = UsageControlId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UseSyntheticData(SecurityMethod):
    """
    Use of synthetic data to preserve privacy, security, or other effects
    and side-effects
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["UseSyntheticData"]
    class_class_curie: ClassVar[str] = "dpv:UseSyntheticData"
    class_name: ClassVar[str] = "UseSyntheticData"
    class_model_uri: ClassVar[URIRef] = DPV.UseSyntheticData

    id: Union[str, UseSyntheticDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UseSyntheticDataId):
            self.id = UseSyntheticDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VerifiedData(DpvData):
    """
    Data that has been verified in terms of accuracy, consistency, or
    quality
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VerifiedData"]
    class_class_curie: ClassVar[str] = "dpv:VerifiedData"
    class_name: ClassVar[str] = "VerifiedData"
    class_model_uri: ClassVar[URIRef] = DPV.VerifiedData

    id: Union[str, VerifiedDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VerifiedDataId):
            self.id = VerifiedDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VirtualisationSecurity(SecurityMethod):
    """
    Security implemented at or through virtualised environments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VirtualisationSecurity"]
    class_class_curie: ClassVar[str] = "dpv:VirtualisationSecurity"
    class_name: ClassVar[str] = "VirtualisationSecurity"
    class_model_uri: ClassVar[URIRef] = DPV.VirtualisationSecurity

    id: Union[str, VirtualisationSecurityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VirtualisationSecurityId):
            self.id = VirtualisationSecurityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VulnerabilityTestingMethods(SecurityMethod):
    """
    Methods that assess or discover vulnerabilities in a system
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VulnerabilityTestingMethods"]
    class_class_curie: ClassVar[str] = "dpv:VulnerabilityTestingMethods"
    class_name: ClassVar[str] = "VulnerabilityTestingMethods"
    class_model_uri: ClassVar[URIRef] = DPV.VulnerabilityTestingMethods

    id: Union[str, VulnerabilityTestingMethodsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VulnerabilityTestingMethodsId):
            self.id = VulnerabilityTestingMethodsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WebBrowserSecurity(SecurityMethod):
    """
    Security implemented at or over web browsers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["WebBrowserSecurity"]
    class_class_curie: ClassVar[str] = "dpv:WebBrowserSecurity"
    class_name: ClassVar[str] = "WebBrowserSecurity"
    class_model_uri: ClassVar[URIRef] = DPV.WebBrowserSecurity

    id: Union[str, WebBrowserSecurityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WebBrowserSecurityId):
            self.id = WebBrowserSecurityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WebSecurityProtocols(SecurityMethod):
    """
    Security implemented at or over web-based protocols
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["WebSecurityProtocols"]
    class_class_curie: ClassVar[str] = "dpv:WebSecurityProtocols"
    class_name: ClassVar[str] = "WebSecurityProtocols"
    class_model_uri: ClassVar[URIRef] = DPV.WebSecurityProtocols

    id: Union[str, WebSecurityProtocolsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WebSecurityProtocolsId):
            self.id = WebSecurityProtocolsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WirelessSecurityProtocols(SecurityMethod):
    """
    Security implemented at or over wireless communication protocols
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["WirelessSecurityProtocols"]
    class_class_curie: ClassVar[str] = "dpv:WirelessSecurityProtocols"
    class_name: ClassVar[str] = "WirelessSecurityProtocols"
    class_model_uri: ClassVar[URIRef] = DPV.WirelessSecurityProtocols

    id: Union[str, WirelessSecurityProtocolsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WirelessSecurityProtocolsId):
            self.id = WirelessSecurityProtocolsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ZeroKnowledgeAuthentication(AuthenticationProtocols):
    """
    Authentication using Zero-Knowledge proofs
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ZeroKnowledgeAuthentication"]
    class_class_curie: ClassVar[str] = "dpv:ZeroKnowledgeAuthentication"
    class_name: ClassVar[str] = "ZeroKnowledgeAuthentication"
    class_model_uri: ClassVar[URIRef] = DPV.ZeroKnowledgeAuthentication

    id: Union[str, ZeroKnowledgeAuthenticationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ZeroKnowledgeAuthenticationId):
            self.id = ZeroKnowledgeAuthenticationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvProcess(DpvThing):
    """
    An action, activity, or method
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Process"]
    class_class_curie: ClassVar[str] = "dpv:Process"
    class_name: ClassVar[str] = "DpvProcess"
    class_model_uri: ClassVar[URIRef] = DPV.DpvProcess

    id: Union[str, DpvProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvProcessId):
            self.id = DpvProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvService(DpvProcess):
    """
    A service is a process where one entity provides some benefit or
    assistance to another entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Service"]
    class_class_curie: ClassVar[str] = "dpv:Service"
    class_name: ClassVar[str] = "DpvService"
    class_model_uri: ClassVar[URIRef] = DPV.DpvService

    id: Union[str, DpvServiceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvServiceId):
            self.id = DpvServiceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NonPersonalDataProcess(DpvProcess):
    """
    An action, activity, or method involving non-personal data, and
    asserting that no personal data is involved
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NonPersonalDataProcess"]
    class_class_curie: ClassVar[str] = "dpv:NonPersonalDataProcess"
    class_name: ClassVar[str] = "NonPersonalDataProcess"
    class_model_uri: ClassVar[URIRef] = DPV.NonPersonalDataProcess

    id: Union[str, NonPersonalDataProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NonPersonalDataProcessId):
            self.id = NonPersonalDataProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonalDataHandling(DpvProcess):
    """
    An abstract concept describing 'personal data handling'
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonalDataHandling"]
    class_class_curie: ClassVar[str] = "dpv:PersonalDataHandling"
    class_name: ClassVar[str] = "PersonalDataHandling"
    class_model_uri: ClassVar[URIRef] = DPV.PersonalDataHandling

    id: Union[str, PersonalDataHandlingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonalDataHandlingId):
            self.id = PersonalDataHandlingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonalDataProcess(DpvProcess):
    """
    An action, activity, or method involving personal data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonalDataProcess"]
    class_class_curie: ClassVar[str] = "dpv:PersonalDataProcess"
    class_name: ClassVar[str] = "PersonalDataProcess"
    class_model_uri: ClassVar[URIRef] = DPV.PersonalDataProcess

    id: Union[str, PersonalDataProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonalDataProcessId):
            self.id = PersonalDataProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Processing(DpvThing):
    """
    Operations or 'processing' performed on data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Processing"]
    class_class_curie: ClassVar[str] = "dpv:Processing"
    class_name: ClassVar[str] = "Processing"
    class_model_uri: ClassVar[URIRef] = DPV.Processing

    id: Union[str, ProcessingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessingId):
            self.id = ProcessingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Copy(Processing):
    """
    to produce an exact reproduction of the data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Copy"]
    class_class_curie: ClassVar[str] = "dpv:Copy"
    class_name: ClassVar[str] = "Copy"
    class_model_uri: ClassVar[URIRef] = DPV.Copy

    id: Union[str, CopyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CopyId):
            self.id = CopyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Disclose(Processing):
    """
    to make data known
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Disclose"]
    class_class_curie: ClassVar[str] = "dpv:Disclose"
    class_name: ClassVar[str] = "Disclose"
    class_model_uri: ClassVar[URIRef] = DPV.Disclose

    id: Union[str, DiscloseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiscloseId):
            self.id = DiscloseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DiscloseByTransmission(Disclose):
    """
    to disclose data by means of transmission
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DiscloseByTransmission"]
    class_class_curie: ClassVar[str] = "dpv:DiscloseByTransmission"
    class_name: ClassVar[str] = "DiscloseByTransmission"
    class_model_uri: ClassVar[URIRef] = DPV.DiscloseByTransmission

    id: Union[str, DiscloseByTransmissionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiscloseByTransmissionId):
            self.id = DiscloseByTransmissionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Display(Disclose):
    """
    to present or show data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Display"]
    class_class_curie: ClassVar[str] = "dpv:Display"
    class_name: ClassVar[str] = "Display"
    class_model_uri: ClassVar[URIRef] = DPV.Display

    id: Union[str, DisplayId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DisplayId):
            self.id = DisplayId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Disseminate(Disclose):
    """
    to spread data throughout
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Disseminate"]
    class_class_curie: ClassVar[str] = "dpv:Disseminate"
    class_name: ClassVar[str] = "Disseminate"
    class_model_uri: ClassVar[URIRef] = DPV.Disseminate

    id: Union[str, DisseminateId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DisseminateId):
            self.id = DisseminateId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Download(Disclose):
    """
    to provide a copy or to receive a copy of data over a network or
    internet
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Download"]
    class_class_curie: ClassVar[str] = "dpv:Download"
    class_name: ClassVar[str] = "Download"
    class_model_uri: ClassVar[URIRef] = DPV.Download

    id: Union[str, DownloadId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DownloadId):
            self.id = DownloadId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Export(Disclose):
    """
    to provide a copy of data from one system to another
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Export"]
    class_class_curie: ClassVar[str] = "dpv:Export"
    class_name: ClassVar[str] = "Export"
    class_model_uri: ClassVar[URIRef] = DPV.Export

    id: Union[str, ExportId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExportId):
            self.id = ExportId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MakeAvailable(Disclose):
    """
    to transform or publish data to be used
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MakeAvailable"]
    class_class_curie: ClassVar[str] = "dpv:MakeAvailable"
    class_name: ClassVar[str] = "MakeAvailable"
    class_model_uri: ClassVar[URIRef] = DPV.MakeAvailable

    id: Union[str, MakeAvailableId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MakeAvailableId):
            self.id = MakeAvailableId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Obtain(Processing):
    """
    to solicit or gather data from someone
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Obtain"]
    class_class_curie: ClassVar[str] = "dpv:Obtain"
    class_name: ClassVar[str] = "Obtain"
    class_model_uri: ClassVar[URIRef] = DPV.Obtain

    id: Union[str, ObtainId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObtainId):
            self.id = ObtainId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Acquire(Obtain):
    """
    to come into possession or control of the data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Acquire"]
    class_class_curie: ClassVar[str] = "dpv:Acquire"
    class_name: ClassVar[str] = "Acquire"
    class_model_uri: ClassVar[URIRef] = DPV.Acquire

    id: Union[str, AcquireId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcquireId):
            self.id = AcquireId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Collect(Obtain):
    """
    to gather data from someone
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Collect"]
    class_class_curie: ClassVar[str] = "dpv:Collect"
    class_name: ClassVar[str] = "Collect"
    class_model_uri: ClassVar[URIRef] = DPV.Collect

    id: Union[str, CollectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CollectId):
            self.id = CollectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Derive(Obtain):
    """
    to create new derivative data from the original data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Derive"]
    class_class_curie: ClassVar[str] = "dpv:Derive"
    class_name: ClassVar[str] = "Derive"
    class_model_uri: ClassVar[URIRef] = DPV.Derive

    id: Union[str, DeriveId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeriveId):
            self.id = DeriveId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvRecord(Obtain):
    """
    to make a record (especially media)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Record"]
    class_class_curie: ClassVar[str] = "dpv:Record"
    class_name: ClassVar[str] = "DpvRecord"
    class_model_uri: ClassVar[URIRef] = DPV.DpvRecord

    id: Union[str, DpvRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvRecordId):
            self.id = DpvRecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Generate(Obtain):
    """
    to generate or create data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Generate"]
    class_class_curie: ClassVar[str] = "dpv:Generate"
    class_name: ClassVar[str] = "Generate"
    class_model_uri: ClassVar[URIRef] = DPV.Generate

    id: Union[str, GenerateId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GenerateId):
            self.id = GenerateId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Infer(Derive):
    """
    to infer data from existing data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Infer"]
    class_class_curie: ClassVar[str] = "dpv:Infer"
    class_name: ClassVar[str] = "Infer"
    class_model_uri: ClassVar[URIRef] = DPV.Infer

    id: Union[str, InferId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InferId):
            self.id = InferId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Observe(Obtain):
    """
    to obtain data through observation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Observe"]
    class_class_curie: ClassVar[str] = "dpv:Observe"
    class_name: ClassVar[str] = "Observe"
    class_model_uri: ClassVar[URIRef] = DPV.Observe

    id: Union[str, ObserveId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObserveId):
            self.id = ObserveId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Organise(Processing):
    """
    to organize data for arranging or classifying
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Organise"]
    class_class_curie: ClassVar[str] = "dpv:Organise"
    class_name: ClassVar[str] = "Organise"
    class_model_uri: ClassVar[URIRef] = DPV.Organise

    id: Union[str, OrganiseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganiseId):
            self.id = OrganiseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProcessingContext(Context):
    """
    Context or conditions within which processing takes place
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProcessingContext"]
    class_class_curie: ClassVar[str] = "dpv:ProcessingContext"
    class_name: ClassVar[str] = "ProcessingContext"
    class_model_uri: ClassVar[URIRef] = DPV.ProcessingContext

    id: Union[str, ProcessingContextId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessingContextId):
            self.id = ProcessingContextId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AlgorithmicLogic(ProcessingContext):
    """
    The algorithmic logic applied or used
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AlgorithmicLogic"]
    class_class_curie: ClassVar[str] = "dpv:AlgorithmicLogic"
    class_name: ClassVar[str] = "AlgorithmicLogic"
    class_model_uri: ClassVar[URIRef] = DPV.AlgorithmicLogic

    id: Union[str, AlgorithmicLogicId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlgorithmicLogicId):
            self.id = AlgorithmicLogicId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AutomationLevel(ProcessingContext):
    """
    Indication of degree or level of automation associated with specified
    context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AutomationLevel"]
    class_class_curie: ClassVar[str] = "dpv:AutomationLevel"
    class_name: ClassVar[str] = "AutomationLevel"
    class_model_uri: ClassVar[URIRef] = DPV.AutomationLevel

    id: Union[str, AutomationLevelId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AutomationLevelId):
            self.id = AutomationLevelId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AssistiveAutomation(AutomationLevel):
    """
    Level of automation corresponding to Level 1 in ISO/IEC 22989:2022 where
    automation is limited to parts of the system or a specific part of the
    system in a manner that does not change the control of the human in
    using/driving the system
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AssistiveAutomation"]
    class_class_curie: ClassVar[str] = "dpv:AssistiveAutomation"
    class_name: ClassVar[str] = "AssistiveAutomation"
    class_model_uri: ClassVar[URIRef] = DPV.AssistiveAutomation

    id: Union[str, AssistiveAutomationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssistiveAutomationId):
            self.id = AssistiveAutomationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Autonomous(AutomationLevel):
    """
    Level of automation corresponding to Level 6 in ISO/IEC 22989:2022 where
    the automation in system is capable of modifying its operation domain or
    its goals without external intervention, control or oversight
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Autonomous"]
    class_class_curie: ClassVar[str] = "dpv:Autonomous"
    class_name: ClassVar[str] = "Autonomous"
    class_model_uri: ClassVar[URIRef] = DPV.Autonomous

    id: Union[str, AutonomousId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AutonomousId):
            self.id = AutonomousId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConditionalAutomation(AutomationLevel):
    """
    Level of automation corresponding to Level 3 in ISO/IEC 22989:2022 where
    the automation is sufficient to perform most tasks of the system with
    the human present to take over where necessary
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConditionalAutomation"]
    class_class_curie: ClassVar[str] = "dpv:ConditionalAutomation"
    class_name: ClassVar[str] = "ConditionalAutomation"
    class_model_uri: ClassVar[URIRef] = DPV.ConditionalAutomation

    id: Union[str, ConditionalAutomationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConditionalAutomationId):
            self.id = ConditionalAutomationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSource(ProcessingContext):
    """
    The source or origin of data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSource"]
    class_class_curie: ClassVar[str] = "dpv:DataSource"
    class_name: ClassVar[str] = "DataSource"
    class_model_uri: ClassVar[URIRef] = DPV.DataSource

    id: Union[str, DataSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSourceId):
            self.id = DataSourceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataControllerDataSource(DataSource):
    """
    Data Sourced from Data Controller(s), e.g. a Controller inferring data
    or generating data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataControllerDataSource"]
    class_class_curie: ClassVar[str] = "dpv:DataControllerDataSource"
    class_name: ClassVar[str] = "DataControllerDataSource"
    class_model_uri: ClassVar[URIRef] = DPV.DataControllerDataSource

    id: Union[str, DataControllerDataSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataControllerDataSourceId):
            self.id = DataControllerDataSourceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSubjectDataSource(DataSource):
    """
    Data Sourced from Data Subject(s), e.g. when data is collected via a
    form or observed from their activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSubjectDataSource"]
    class_class_curie: ClassVar[str] = "dpv:DataSubjectDataSource"
    class_name: ClassVar[str] = "DataSubjectDataSource"
    class_model_uri: ClassVar[URIRef] = DPV.DataSubjectDataSource

    id: Union[str, DataSubjectDataSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSubjectDataSourceId):
            self.id = DataSubjectDataSourceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataPublishedByDataSubject(DataSubjectDataSource):
    """
    Data is published by the data subject
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataPublishedByDataSubject"]
    class_class_curie: ClassVar[str] = "dpv:DataPublishedByDataSubject"
    class_name: ClassVar[str] = "DataPublishedByDataSubject"
    class_model_uri: ClassVar[URIRef] = DPV.DataPublishedByDataSubject

    id: Union[str, DataPublishedByDataSubjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataPublishedByDataSubjectId):
            self.id = DataPublishedByDataSubjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DecisionMaking(ProcessingContext):
    """
    Processing that involves decision making
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DecisionMaking"]
    class_class_curie: ClassVar[str] = "dpv:DecisionMaking"
    class_name: ClassVar[str] = "DecisionMaking"
    class_model_uri: ClassVar[URIRef] = DPV.DecisionMaking

    id: Union[str, DecisionMakingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DecisionMakingId):
            self.id = DecisionMakingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AutomatedDecisionMaking(DecisionMaking):
    """
    Processing that involves automated decision making
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AutomatedDecisionMaking"]
    class_class_curie: ClassVar[str] = "dpv:AutomatedDecisionMaking"
    class_name: ClassVar[str] = "AutomatedDecisionMaking"
    class_model_uri: ClassVar[URIRef] = DPV.AutomatedDecisionMaking

    id: Union[str, AutomatedDecisionMakingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AutomatedDecisionMakingId):
            self.id = AutomatedDecisionMakingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityInvolvement(ProcessingContext):
    """
    Involvement of an entity in specific context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityInvolvement"]
    class_class_curie: ClassVar[str] = "dpv:EntityInvolvement"
    class_name: ClassVar[str] = "EntityInvolvement"
    class_model_uri: ClassVar[URIRef] = DPV.EntityInvolvement

    id: Union[str, EntityInvolvementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityInvolvementId):
            self.id = EntityInvolvementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ContractControl(EntityInvolvement):
    """
    The control or activity associated with accepting, refusing, and other
    actions associated with a contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractControl"]
    class_class_curie: ClassVar[str] = "dpv:ContractControl"
    class_name: ClassVar[str] = "ContractControl"
    class_model_uri: ClassVar[URIRef] = DPV.ContractControl

    id: Union[str, ContractControlId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContractControlId):
            self.id = ContractControlId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AcceptContract(ContractControl):
    """
    Control for accepting a contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AcceptContract"]
    class_class_curie: ClassVar[str] = "dpv:AcceptContract"
    class_name: ClassVar[str] = "AcceptContract"
    class_model_uri: ClassVar[URIRef] = DPV.AcceptContract

    id: Union[str, AcceptContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcceptContractId):
            self.id = AcceptContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NegotiateContract(ContractControl):
    """
    Control for negotiating a contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NegotiateContract"]
    class_class_curie: ClassVar[str] = "dpv:NegotiateContract"
    class_name: ClassVar[str] = "NegotiateContract"
    class_model_uri: ClassVar[URIRef] = DPV.NegotiateContract

    id: Union[str, NegotiateContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NegotiateContractId):
            self.id = NegotiateContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OfferContract(ContractControl):
    """
    Control for offering a contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OfferContract"]
    class_class_curie: ClassVar[str] = "dpv:OfferContract"
    class_name: ClassVar[str] = "OfferContract"
    class_model_uri: ClassVar[URIRef] = DPV.OfferContract

    id: Union[str, OfferContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OfferContractId):
            self.id = OfferContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RefuseContract(ContractControl):
    """
    Control for refusing a contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RefuseContract"]
    class_class_curie: ClassVar[str] = "dpv:RefuseContract"
    class_name: ClassVar[str] = "RefuseContract"
    class_model_uri: ClassVar[URIRef] = DPV.RefuseContract

    id: Union[str, RefuseContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RefuseContractId):
            self.id = RefuseContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TerminateContract(ContractControl):
    """
    Control for terminating a contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["TerminateContract"]
    class_class_curie: ClassVar[str] = "dpv:TerminateContract"
    class_name: ClassVar[str] = "TerminateContract"
    class_model_uri: ClassVar[URIRef] = DPV.TerminateContract

    id: Union[str, TerminateContractId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TerminateContractId):
            self.id = TerminateContractId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityActiveInvolvement(EntityInvolvement):
    """
    Involvement where entity is 'actively' involved
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityActiveInvolvement"]
    class_class_curie: ClassVar[str] = "dpv:EntityActiveInvolvement"
    class_name: ClassVar[str] = "EntityActiveInvolvement"
    class_model_uri: ClassVar[URIRef] = DPV.EntityActiveInvolvement

    id: Union[str, EntityActiveInvolvementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityActiveInvolvementId):
            self.id = EntityActiveInvolvementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityIntendedInvolvement(EntityInvolvement):
    """
    Status indicating the involvement of the entity is intended
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityIntendedInvolvement"]
    class_class_curie: ClassVar[str] = "dpv:EntityIntendedInvolvement"
    class_name: ClassVar[str] = "EntityIntendedInvolvement"
    class_model_uri: ClassVar[URIRef] = DPV.EntityIntendedInvolvement

    id: Union[str, EntityIntendedInvolvementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityIntendedInvolvementId):
            self.id = EntityIntendedInvolvementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityInvolvementStatus(EntityInvolvement):
    """
    Status indicating whether an entity is involved
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityInvolvementStatus"]
    class_class_curie: ClassVar[str] = "dpv:EntityInvolvementStatus"
    class_name: ClassVar[str] = "EntityInvolvementStatus"
    class_model_uri: ClassVar[URIRef] = DPV.EntityInvolvementStatus

    id: Union[str, EntityInvolvementStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityInvolvementStatusId):
            self.id = EntityInvolvementStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityInvolved(EntityInvolvementStatus):
    """
    Status indicating the entity is involved
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityInvolved"]
    class_class_curie: ClassVar[str] = "dpv:EntityInvolved"
    class_name: ClassVar[str] = "EntityInvolved"
    class_model_uri: ClassVar[URIRef] = DPV.EntityInvolved

    id: Union[str, EntityInvolvedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityInvolvedId):
            self.id = EntityInvolvedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityNonInvolvement(EntityInvolvement):
    """
    Indicating entity is not involved
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityNonInvolvement"]
    class_class_curie: ClassVar[str] = "dpv:EntityNonInvolvement"
    class_name: ClassVar[str] = "EntityNonInvolvement"
    class_model_uri: ClassVar[URIRef] = DPV.EntityNonInvolvement

    id: Union[str, EntityNonInvolvementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityNonInvolvementId):
            self.id = EntityNonInvolvementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityNonPermissiveInvolvement(EntityInvolvement):
    """
    Involvement of an entity in specific context where it is not permitted
    or able to do something
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityNonPermissiveInvolvement"]
    class_class_curie: ClassVar[str] = "dpv:EntityNonPermissiveInvolvement"
    class_name: ClassVar[str] = "EntityNonPermissiveInvolvement"
    class_model_uri: ClassVar[URIRef] = DPV.EntityNonPermissiveInvolvement

    id: Union[str, EntityNonPermissiveInvolvementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityNonPermissiveInvolvementId):
            self.id = EntityNonPermissiveInvolvementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CannotChallengeProcess(EntityNonPermissiveInvolvement):
    """
    Involvement where entity cannot challenge the process of specified
    context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CannotChallengeProcess"]
    class_class_curie: ClassVar[str] = "dpv:CannotChallengeProcess"
    class_name: ClassVar[str] = "CannotChallengeProcess"
    class_model_uri: ClassVar[URIRef] = DPV.CannotChallengeProcess

    id: Union[str, CannotChallengeProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CannotChallengeProcessId):
            self.id = CannotChallengeProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CannotChallengeProcessInput(EntityNonPermissiveInvolvement):
    """
    Involvement where entity cannot challenge input of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CannotChallengeProcessInput"]
    class_class_curie: ClassVar[str] = "dpv:CannotChallengeProcessInput"
    class_name: ClassVar[str] = "CannotChallengeProcessInput"
    class_model_uri: ClassVar[URIRef] = DPV.CannotChallengeProcessInput

    id: Union[str, CannotChallengeProcessInputId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CannotChallengeProcessInputId):
            self.id = CannotChallengeProcessInputId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CannotChallengeProcessOutput(EntityNonPermissiveInvolvement):
    """
    Involvement where entity cannot challenge the output of specified
    context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CannotChallengeProcessOutput"]
    class_class_curie: ClassVar[str] = "dpv:CannotChallengeProcessOutput"
    class_name: ClassVar[str] = "CannotChallengeProcessOutput"
    class_model_uri: ClassVar[URIRef] = DPV.CannotChallengeProcessOutput

    id: Union[str, CannotChallengeProcessOutputId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CannotChallengeProcessOutputId):
            self.id = CannotChallengeProcessOutputId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CannotCorrectProcess(EntityNonPermissiveInvolvement):
    """
    Involvement where entity cannot correct the process of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CannotCorrectProcess"]
    class_class_curie: ClassVar[str] = "dpv:CannotCorrectProcess"
    class_name: ClassVar[str] = "CannotCorrectProcess"
    class_model_uri: ClassVar[URIRef] = DPV.CannotCorrectProcess

    id: Union[str, CannotCorrectProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CannotCorrectProcessId):
            self.id = CannotCorrectProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CannotCorrectProcessInput(EntityNonPermissiveInvolvement):
    """
    Involvement where entity cannot correct input of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CannotCorrectProcessInput"]
    class_class_curie: ClassVar[str] = "dpv:CannotCorrectProcessInput"
    class_name: ClassVar[str] = "CannotCorrectProcessInput"
    class_model_uri: ClassVar[URIRef] = DPV.CannotCorrectProcessInput

    id: Union[str, CannotCorrectProcessInputId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CannotCorrectProcessInputId):
            self.id = CannotCorrectProcessInputId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CannotCorrectProcessOutput(EntityNonPermissiveInvolvement):
    """
    Involvement where entity cannot correct the output of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CannotCorrectProcessOutput"]
    class_class_curie: ClassVar[str] = "dpv:CannotCorrectProcessOutput"
    class_name: ClassVar[str] = "CannotCorrectProcessOutput"
    class_model_uri: ClassVar[URIRef] = DPV.CannotCorrectProcessOutput

    id: Union[str, CannotCorrectProcessOutputId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CannotCorrectProcessOutputId):
            self.id = CannotCorrectProcessOutputId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CannotObjectToProcess(EntityNonPermissiveInvolvement):
    """
    Involvement where entity cannot object to process of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CannotObjectToProcess"]
    class_class_curie: ClassVar[str] = "dpv:CannotObjectToProcess"
    class_name: ClassVar[str] = "CannotObjectToProcess"
    class_model_uri: ClassVar[URIRef] = DPV.CannotObjectToProcess

    id: Union[str, CannotObjectToProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CannotObjectToProcessId):
            self.id = CannotObjectToProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CannotOptInToProcess(EntityNonPermissiveInvolvement):
    """
    Involvement where entity cannot opt-in to specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CannotOptInToProcess"]
    class_class_curie: ClassVar[str] = "dpv:CannotOptInToProcess"
    class_name: ClassVar[str] = "CannotOptInToProcess"
    class_model_uri: ClassVar[URIRef] = DPV.CannotOptInToProcess

    id: Union[str, CannotOptInToProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CannotOptInToProcessId):
            self.id = CannotOptInToProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CannotOptOutFromProcess(EntityNonPermissiveInvolvement):
    """
    Involvement where entity cannot opt-out from specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CannotOptOutFromProcess"]
    class_class_curie: ClassVar[str] = "dpv:CannotOptOutFromProcess"
    class_name: ClassVar[str] = "CannotOptOutFromProcess"
    class_model_uri: ClassVar[URIRef] = DPV.CannotOptOutFromProcess

    id: Union[str, CannotOptOutFromProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CannotOptOutFromProcessId):
            self.id = CannotOptOutFromProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CannotReverseProcessEffects(EntityNonPermissiveInvolvement):
    """
    Involvement where entity cannot reverse effects of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CannotReverseProcessEffects"]
    class_class_curie: ClassVar[str] = "dpv:CannotReverseProcessEffects"
    class_name: ClassVar[str] = "CannotReverseProcessEffects"
    class_model_uri: ClassVar[URIRef] = DPV.CannotReverseProcessEffects

    id: Union[str, CannotReverseProcessEffectsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CannotReverseProcessEffectsId):
            self.id = CannotReverseProcessEffectsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CannotReverseProcessInput(EntityNonPermissiveInvolvement):
    """
    Involvement where entity cannot reverse input of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CannotReverseProcessInput"]
    class_class_curie: ClassVar[str] = "dpv:CannotReverseProcessInput"
    class_name: ClassVar[str] = "CannotReverseProcessInput"
    class_model_uri: ClassVar[URIRef] = DPV.CannotReverseProcessInput

    id: Union[str, CannotReverseProcessInputId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CannotReverseProcessInputId):
            self.id = CannotReverseProcessInputId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CannotReverseProcessOutput(EntityNonPermissiveInvolvement):
    """
    Involvement where entity cannot reverse output of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CannotReverseProcessOutput"]
    class_class_curie: ClassVar[str] = "dpv:CannotReverseProcessOutput"
    class_name: ClassVar[str] = "CannotReverseProcessOutput"
    class_model_uri: ClassVar[URIRef] = DPV.CannotReverseProcessOutput

    id: Union[str, CannotReverseProcessOutputId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CannotReverseProcessOutputId):
            self.id = CannotReverseProcessOutputId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CannotWithdrawFromProcess(EntityNonPermissiveInvolvement):
    """
    Involvement where entity cannot withdraw a previously given assent from
    specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CannotWithdrawFromProcess"]
    class_class_curie: ClassVar[str] = "dpv:CannotWithdrawFromProcess"
    class_name: ClassVar[str] = "CannotWithdrawFromProcess"
    class_model_uri: ClassVar[URIRef] = DPV.CannotWithdrawFromProcess

    id: Union[str, CannotWithdrawFromProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CannotWithdrawFromProcessId):
            self.id = CannotWithdrawFromProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityNotInvolved(EntityInvolvementStatus):
    """
    Status indicating the entity is not involved
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityNotInvolved"]
    class_class_curie: ClassVar[str] = "dpv:EntityNotInvolved"
    class_name: ClassVar[str] = "EntityNotInvolved"
    class_model_uri: ClassVar[URIRef] = DPV.EntityNotInvolved

    id: Union[str, EntityNotInvolvedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityNotInvolvedId):
            self.id = EntityNotInvolvedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityPassiveInvolvement(EntityInvolvement):
    """
    Involvement where entity is 'passively' or 'not actively' involved
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityPassiveInvolvement"]
    class_class_curie: ClassVar[str] = "dpv:EntityPassiveInvolvement"
    class_name: ClassVar[str] = "EntityPassiveInvolvement"
    class_model_uri: ClassVar[URIRef] = DPV.EntityPassiveInvolvement

    id: Union[str, EntityPassiveInvolvementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityPassiveInvolvementId):
            self.id = EntityPassiveInvolvementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityPermissiveInvolvement(EntityInvolvement):
    """
    Involvement of an entity in specific context where it is permitted or
    able to do something
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityPermissiveInvolvement"]
    class_class_curie: ClassVar[str] = "dpv:EntityPermissiveInvolvement"
    class_name: ClassVar[str] = "EntityPermissiveInvolvement"
    class_model_uri: ClassVar[URIRef] = DPV.EntityPermissiveInvolvement

    id: Union[str, EntityPermissiveInvolvementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityPermissiveInvolvementId):
            self.id = EntityPermissiveInvolvementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChallengingProcess(EntityPermissiveInvolvement):
    """
    Involvement where entity can challenge the process of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ChallengingProcess"]
    class_class_curie: ClassVar[str] = "dpv:ChallengingProcess"
    class_name: ClassVar[str] = "ChallengingProcess"
    class_model_uri: ClassVar[URIRef] = DPV.ChallengingProcess

    id: Union[str, ChallengingProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChallengingProcessId):
            self.id = ChallengingProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChallengingProcessInput(EntityPermissiveInvolvement):
    """
    Involvement where entity can challenge input of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ChallengingProcessInput"]
    class_class_curie: ClassVar[str] = "dpv:ChallengingProcessInput"
    class_name: ClassVar[str] = "ChallengingProcessInput"
    class_model_uri: ClassVar[URIRef] = DPV.ChallengingProcessInput

    id: Union[str, ChallengingProcessInputId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChallengingProcessInputId):
            self.id = ChallengingProcessInputId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChallengingProcessOutput(EntityPermissiveInvolvement):
    """
    Involvement where entity can challenge the output of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ChallengingProcessOutput"]
    class_class_curie: ClassVar[str] = "dpv:ChallengingProcessOutput"
    class_name: ClassVar[str] = "ChallengingProcessOutput"
    class_model_uri: ClassVar[URIRef] = DPV.ChallengingProcessOutput

    id: Union[str, ChallengingProcessOutputId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChallengingProcessOutputId):
            self.id = ChallengingProcessOutputId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CorrectingProcess(EntityPermissiveInvolvement):
    """
    Involvement where entity can correct the process of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CorrectingProcess"]
    class_class_curie: ClassVar[str] = "dpv:CorrectingProcess"
    class_name: ClassVar[str] = "CorrectingProcess"
    class_model_uri: ClassVar[URIRef] = DPV.CorrectingProcess

    id: Union[str, CorrectingProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CorrectingProcessId):
            self.id = CorrectingProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CorrectingProcessInput(EntityPermissiveInvolvement):
    """
    Involvement where entity can correct input of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CorrectingProcessInput"]
    class_class_curie: ClassVar[str] = "dpv:CorrectingProcessInput"
    class_name: ClassVar[str] = "CorrectingProcessInput"
    class_model_uri: ClassVar[URIRef] = DPV.CorrectingProcessInput

    id: Union[str, CorrectingProcessInputId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CorrectingProcessInputId):
            self.id = CorrectingProcessInputId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CorrectingProcessOutput(EntityPermissiveInvolvement):
    """
    Involvement where entity can correct the output of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CorrectingProcessOutput"]
    class_class_curie: ClassVar[str] = "dpv:CorrectingProcessOutput"
    class_name: ClassVar[str] = "CorrectingProcessOutput"
    class_model_uri: ClassVar[URIRef] = DPV.CorrectingProcessOutput

    id: Union[str, CorrectingProcessOutputId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CorrectingProcessOutputId):
            self.id = CorrectingProcessOutputId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntityUnintendedInvolvement(EntityInvolvement):
    """
    Status indicating the involvement of the entity is not intended
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityUnintendedInvolvement"]
    class_class_curie: ClassVar[str] = "dpv:EntityUnintendedInvolvement"
    class_name: ClassVar[str] = "EntityUnintendedInvolvement"
    class_model_uri: ClassVar[URIRef] = DPV.EntityUnintendedInvolvement

    id: Union[str, EntityUnintendedInvolvementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityUnintendedInvolvementId):
            self.id = EntityUnintendedInvolvementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvaluationScoring(ProcessingContext):
    """
    Processing that involves evaluation and scoring of individuals
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EvaluationScoring"]
    class_class_curie: ClassVar[str] = "dpv:EvaluationScoring"
    class_name: ClassVar[str] = "EvaluationScoring"
    class_model_uri: ClassVar[URIRef] = DPV.EvaluationScoring

    id: Union[str, EvaluationScoringId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvaluationScoringId):
            self.id = EvaluationScoringId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvaluationOfIndividuals(EvaluationScoring):
    """
    Processing that involves evaluation of individuals
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EvaluationOfIndividuals"]
    class_class_curie: ClassVar[str] = "dpv:EvaluationOfIndividuals"
    class_name: ClassVar[str] = "EvaluationOfIndividuals"
    class_model_uri: ClassVar[URIRef] = DPV.EvaluationOfIndividuals

    id: Union[str, EvaluationOfIndividualsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvaluationOfIndividualsId):
            self.id = EvaluationOfIndividualsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FullAutomation(AutomationLevel):
    """
    Level of automation corresponding to Level 5 in ISO/IEC 22989:2022 where
    the automation in system is capable of performing all its tasks
    regardless of the conditions without human involvement
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FullAutomation"]
    class_class_curie: ClassVar[str] = "dpv:FullAutomation"
    class_name: ClassVar[str] = "FullAutomation"
    class_model_uri: ClassVar[URIRef] = DPV.FullAutomation

    id: Union[str, FullAutomationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FullAutomationId):
            self.id = FullAutomationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HighAutomation(AutomationLevel):
    """
    Level of automation corresponding to Level 4 in ISO/IEC 22989:2022 where
    the automation in system is capable of performing all its tasks within
    specific controlled conditions without human involvement
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HighAutomation"]
    class_class_curie: ClassVar[str] = "dpv:HighAutomation"
    class_name: ClassVar[str] = "HighAutomation"
    class_model_uri: ClassVar[URIRef] = DPV.HighAutomation

    id: Union[str, HighAutomationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HighAutomationId):
            self.id = HighAutomationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInvolvement(EntityInvolvement):
    """
    The involvement of humans in specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HumanInvolvement"]
    class_class_curie: ClassVar[str] = "dpv:HumanInvolvement"
    class_name: ClassVar[str] = "HumanInvolvement"
    class_model_uri: ClassVar[URIRef] = DPV.HumanInvolvement

    id: Union[str, HumanInvolvementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanInvolvementId):
            self.id = HumanInvolvementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInvolved(HumanInvolvement):
    """
    Humans are involved in the specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HumanInvolved"]
    class_class_curie: ClassVar[str] = "dpv:HumanInvolved"
    class_name: ClassVar[str] = "HumanInvolved"
    class_model_uri: ClassVar[URIRef] = DPV.HumanInvolved

    id: Union[str, HumanInvolvedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanInvolvedId):
            self.id = HumanInvolvedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInvolvementForControl(HumanInvolvement):
    """
    Human involvement for the purposes of exercising control over the
    specified operations in context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HumanInvolvementForControl"]
    class_class_curie: ClassVar[str] = "dpv:HumanInvolvementForControl"
    class_name: ClassVar[str] = "HumanInvolvementForControl"
    class_model_uri: ClassVar[URIRef] = DPV.HumanInvolvementForControl

    id: Union[str, HumanInvolvementForControlId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanInvolvementForControlId):
            self.id = HumanInvolvementForControlId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInvolvementForDecision(HumanInvolvement):
    """
    Human involvement for the purposes of exercising decisions over the
    specified operations in context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HumanInvolvementForDecision"]
    class_class_curie: ClassVar[str] = "dpv:HumanInvolvementForDecision"
    class_name: ClassVar[str] = "HumanInvolvementForDecision"
    class_model_uri: ClassVar[URIRef] = DPV.HumanInvolvementForDecision

    id: Union[str, HumanInvolvementForDecisionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanInvolvementForDecisionId):
            self.id = HumanInvolvementForDecisionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInvolvementForInput(HumanInvolvement):
    """
    Human involvement for the purposes of providing inputs to the specified
    context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HumanInvolvementForInput"]
    class_class_curie: ClassVar[str] = "dpv:HumanInvolvementForInput"
    class_name: ClassVar[str] = "HumanInvolvementForInput"
    class_model_uri: ClassVar[URIRef] = DPV.HumanInvolvementForInput

    id: Union[str, HumanInvolvementForInputId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanInvolvementForInputId):
            self.id = HumanInvolvementForInputId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInvolvementForIntervention(HumanInvolvement):
    """
    Human involvement for the purposes of exercising interventions over the
    specified operations in context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HumanInvolvementForIntervention"]
    class_class_curie: ClassVar[str] = "dpv:HumanInvolvementForIntervention"
    class_name: ClassVar[str] = "HumanInvolvementForIntervention"
    class_model_uri: ClassVar[URIRef] = DPV.HumanInvolvementForIntervention

    id: Union[str, HumanInvolvementForInterventionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanInvolvementForInterventionId):
            self.id = HumanInvolvementForInterventionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInvolvementForOversight(HumanInvolvement):
    """
    Human involvement for the purposes of having oversight over the
    specified context regarding its operations, inputs, or outputs
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HumanInvolvementForOversight"]
    class_class_curie: ClassVar[str] = "dpv:HumanInvolvementForOversight"
    class_name: ClassVar[str] = "HumanInvolvementForOversight"
    class_model_uri: ClassVar[URIRef] = DPV.HumanInvolvementForOversight

    id: Union[str, HumanInvolvementForOversightId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanInvolvementForOversightId):
            self.id = HumanInvolvementForOversightId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanInvolvementForVerification(HumanInvolvement):
    """
    Human involvement for the purposes of verification of specified context
    to ensure its operations, inputs, or outputs are correct or are
    acceptable.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HumanInvolvementForVerification"]
    class_class_curie: ClassVar[str] = "dpv:HumanInvolvementForVerification"
    class_name: ClassVar[str] = "HumanInvolvementForVerification"
    class_model_uri: ClassVar[URIRef] = DPV.HumanInvolvementForVerification

    id: Union[str, HumanInvolvementForVerificationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanInvolvementForVerificationId):
            self.id = HumanInvolvementForVerificationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanNotInvolved(HumanInvolvement):
    """
    Humans are not involved in the specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HumanNotInvolved"]
    class_class_curie: ClassVar[str] = "dpv:HumanNotInvolved"
    class_name: ClassVar[str] = "HumanNotInvolved"
    class_model_uri: ClassVar[URIRef] = DPV.HumanNotInvolved

    id: Union[str, HumanNotInvolvedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanNotInvolvedId):
            self.id = HumanNotInvolvedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InnovativeUseOfTechnology(ProcessingContext):
    """
    Indicates that technology is being used in an innovative manner
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InnovativeUseOfTechnology"]
    class_class_curie: ClassVar[str] = "dpv:InnovativeUseOfTechnology"
    class_name: ClassVar[str] = "InnovativeUseOfTechnology"
    class_model_uri: ClassVar[URIRef] = DPV.InnovativeUseOfTechnology

    id: Union[str, InnovativeUseOfTechnologyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InnovativeUseOfTechnologyId):
            self.id = InnovativeUseOfTechnologyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InnovativeUseOfExistingTechnology(InnovativeUseOfTechnology):
    """
    Involvement of existing technologies used in an innovative manner
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InnovativeUseOfExistingTechnology"]
    class_class_curie: ClassVar[str] = "dpv:InnovativeUseOfExistingTechnology"
    class_name: ClassVar[str] = "InnovativeUseOfExistingTechnology"
    class_model_uri: ClassVar[URIRef] = DPV.InnovativeUseOfExistingTechnology

    id: Union[str, InnovativeUseOfExistingTechnologyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InnovativeUseOfExistingTechnologyId):
            self.id = InnovativeUseOfExistingTechnologyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InnovativeUseOfNewTechnologies(InnovativeUseOfTechnology):
    """
    Involvement of a new (innovative) technologies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InnovativeUseOfNewTechnologies"]
    class_class_curie: ClassVar[str] = "dpv:InnovativeUseOfNewTechnologies"
    class_name: ClassVar[str] = "InnovativeUseOfNewTechnologies"
    class_model_uri: ClassVar[URIRef] = DPV.InnovativeUseOfNewTechnologies

    id: Union[str, InnovativeUseOfNewTechnologiesId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InnovativeUseOfNewTechnologiesId):
            self.id = InnovativeUseOfNewTechnologiesId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NonPublicDataSource(DataSource):
    """
    A source of data that is not publicly accessible or available
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NonPublicDataSource"]
    class_class_curie: ClassVar[str] = "dpv:NonPublicDataSource"
    class_name: ClassVar[str] = "NonPublicDataSource"
    class_model_uri: ClassVar[URIRef] = DPV.NonPublicDataSource

    id: Union[str, NonPublicDataSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NonPublicDataSourceId):
            self.id = NonPublicDataSourceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NotAutomated(AutomationLevel):
    """
    Level of automation corresponding to Level 0 in ISO/IEC 22989:2022 where
    there is no automation in the system
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NotAutomated"]
    class_class_curie: ClassVar[str] = "dpv:NotAutomated"
    class_name: ClassVar[str] = "NotAutomated"
    class_model_uri: ClassVar[URIRef] = DPV.NotAutomated

    id: Union[str, NotAutomatedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NotAutomatedId):
            self.id = NotAutomatedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObjectingToProcess(EntityPermissiveInvolvement):
    """
    Involvement where entity can object to process of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ObjectingToProcess"]
    class_class_curie: ClassVar[str] = "dpv:ObjectingToProcess"
    class_name: ClassVar[str] = "ObjectingToProcess"
    class_model_uri: ClassVar[URIRef] = DPV.ObjectingToProcess

    id: Union[str, ObjectingToProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObjectingToProcessId):
            self.id = ObjectingToProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptingInToProcess(EntityPermissiveInvolvement):
    """
    Involvement where entity can opt-in to specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OptingInToProcess"]
    class_class_curie: ClassVar[str] = "dpv:OptingInToProcess"
    class_name: ClassVar[str] = "OptingInToProcess"
    class_model_uri: ClassVar[URIRef] = DPV.OptingInToProcess

    id: Union[str, OptingInToProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OptingInToProcessId):
            self.id = OptingInToProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptingOutFromProcess(EntityPermissiveInvolvement):
    """
    Involvement where entity can opt-out from specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OptingOutFromProcess"]
    class_class_curie: ClassVar[str] = "dpv:OptingOutFromProcess"
    class_name: ClassVar[str] = "OptingOutFromProcess"
    class_model_uri: ClassVar[URIRef] = DPV.OptingOutFromProcess

    id: Union[str, OptingOutFromProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OptingOutFromProcessId):
            self.id = OptingOutFromProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PartialAutomation(AutomationLevel):
    """
    Level of automation corresponding to Level 2 in ISO/IEC 22989:2022 where
    the automation is present in multiple parts of the system or in a manner
    that does not require the human to control/use these parts while still
    retaining control over the system
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PartialAutomation"]
    class_class_curie: ClassVar[str] = "dpv:PartialAutomation"
    class_name: ClassVar[str] = "PartialAutomation"
    class_model_uri: ClassVar[URIRef] = DPV.PartialAutomation

    id: Union[str, PartialAutomationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PartialAutomationId):
            self.id = PartialAutomationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProcessingCondition(ProcessingContext):
    """
    Conditions required or followed regarding processing of data or use of
    technologies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProcessingCondition"]
    class_class_curie: ClassVar[str] = "dpv:ProcessingCondition"
    class_name: ClassVar[str] = "ProcessingCondition"
    class_model_uri: ClassVar[URIRef] = DPV.ProcessingCondition

    id: Union[str, ProcessingConditionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessingConditionId):
            self.id = ProcessingConditionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProcessingDuration(DpvDuration):
    """
    Conditions regarding duration or temporal limitation for processing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProcessingDuration"]
    class_class_curie: ClassVar[str] = "dpv:ProcessingDuration"
    class_name: ClassVar[str] = "ProcessingDuration"
    class_model_uri: ClassVar[URIRef] = DPV.ProcessingDuration

    id: Union[str, ProcessingDurationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessingDurationId):
            self.id = ProcessingDurationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProcessingLocation(DpvLocation):
    """
    Conditions regarding location or geospatial scope where processing takes
    places
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProcessingLocation"]
    class_class_curie: ClassVar[str] = "dpv:ProcessingLocation"
    class_name: ClassVar[str] = "ProcessingLocation"
    class_model_uri: ClassVar[URIRef] = DPV.ProcessingLocation

    id: Union[str, ProcessingLocationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessingLocationId):
            self.id = ProcessingLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicDataSource(DataSource):
    """
    A source of data that is publicly accessible or available
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicDataSource"]
    class_class_curie: ClassVar[str] = "dpv:PublicDataSource"
    class_name: ClassVar[str] = "PublicDataSource"
    class_model_uri: ClassVar[URIRef] = DPV.PublicDataSource

    id: Union[str, PublicDataSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicDataSourceId):
            self.id = PublicDataSourceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Purpose(DpvThing):
    """
    Purpose or (broader) Goal associated with data or technology
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Purpose"]
    class_class_curie: ClassVar[str] = "dpv:Purpose"
    class_name: ClassVar[str] = "Purpose"
    class_model_uri: ClassVar[URIRef] = DPV.Purpose

    id: Union[str, PurposeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PurposeId):
            self.id = PurposeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AccountManagement(Purpose):
    """
    Account Management refers to purposes associated with account
    management, such as to create, provide, maintain, and manage accounts
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AccountManagement"]
    class_class_curie: ClassVar[str] = "dpv:AccountManagement"
    class_name: ClassVar[str] = "AccountManagement"
    class_model_uri: ClassVar[URIRef] = DPV.AccountManagement

    id: Union[str, AccountManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AccountManagementId):
            self.id = AccountManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommercialPurpose(Purpose):
    """
    Purposes associated with processing activities performed in a commercial
    setting or with intention to commercialise
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CommercialPurpose"]
    class_class_curie: ClassVar[str] = "dpv:CommercialPurpose"
    class_name: ClassVar[str] = "CommercialPurpose"
    class_model_uri: ClassVar[URIRef] = DPV.CommercialPurpose

    id: Union[str, CommercialPurposeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommercialPurposeId):
            self.id = CommercialPurposeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommercialResearch(CommercialPurpose):
    """
    Purposes associated with conducting research in a commercial setting or
    with intention to commercialise e.g. in a company or sponsored by a
    company
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CommercialResearch"]
    class_class_curie: ClassVar[str] = "dpv:CommercialResearch"
    class_name: ClassVar[str] = "CommercialResearch"
    class_model_uri: ClassVar[URIRef] = DPV.CommercialResearch

    id: Union[str, CommercialResearchId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommercialResearchId):
            self.id = CommercialResearchId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommunicationManagement(Purpose):
    """
    Communication Management refers to purposes associated with providing or
    managing communication activities e.g. to send an email for notifying
    some information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CommunicationManagement"]
    class_class_curie: ClassVar[str] = "dpv:CommunicationManagement"
    class_name: ClassVar[str] = "CommunicationManagement"
    class_model_uri: ClassVar[URIRef] = DPV.CommunicationManagement

    id: Union[str, CommunicationManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommunicationManagementId):
            self.id = CommunicationManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommunicationForCustomerCare(CommunicationManagement):
    """
    Customer Care Communication refers to purposes associated with
    communicating with customers for assisting them, resolving issues,
    ensuring satisfaction, etc. in relation to services provided
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CommunicationForCustomerCare"]
    class_class_curie: ClassVar[str] = "dpv:CommunicationForCustomerCare"
    class_name: ClassVar[str] = "CommunicationForCustomerCare"
    class_model_uri: ClassVar[URIRef] = DPV.CommunicationForCustomerCare

    id: Union[str, CommunicationForCustomerCareId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CommunicationForCustomerCareId):
            self.id = CommunicationForCustomerCareId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CustomerManagement(Purpose):
    """
    Customer Management refers to purposes associated with managing
    activities related with past, current, and future customers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CustomerManagement"]
    class_class_curie: ClassVar[str] = "dpv:CustomerManagement"
    class_name: ClassVar[str] = "CustomerManagement"
    class_model_uri: ClassVar[URIRef] = DPV.CustomerManagement

    id: Union[str, CustomerManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CustomerManagementId):
            self.id = CustomerManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CustomerCare(CustomerManagement):
    """
    Customer Care refers to purposes associated with purposes for providing
    assistance, resolving issues, ensuring satisfaction, etc. in relation to
    services provided
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CustomerCare"]
    class_class_curie: ClassVar[str] = "dpv:CustomerCare"
    class_name: ClassVar[str] = "CustomerCare"
    class_model_uri: ClassVar[URIRef] = DPV.CustomerCare

    id: Union[str, CustomerCareId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CustomerCareId):
            self.id = CustomerCareId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CustomerClaimsManagement(CustomerManagement):
    """
    Customer Claims Management refers to purposes associated with managing
    claims, including repayment of monies owed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CustomerClaimsManagement"]
    class_class_curie: ClassVar[str] = "dpv:CustomerClaimsManagement"
    class_name: ClassVar[str] = "CustomerClaimsManagement"
    class_model_uri: ClassVar[URIRef] = DPV.CustomerClaimsManagement

    id: Union[str, CustomerClaimsManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CustomerClaimsManagementId):
            self.id = CustomerClaimsManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CustomerOrderManagement(CustomerManagement):
    """
    Customer Order Management refers to purposes associated with managing
    customer orders i.e. processing of an order related to customer's
    purchase of good or services
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CustomerOrderManagement"]
    class_class_curie: ClassVar[str] = "dpv:CustomerOrderManagement"
    class_name: ClassVar[str] = "CustomerOrderManagement"
    class_model_uri: ClassVar[URIRef] = DPV.CustomerOrderManagement

    id: Union[str, CustomerOrderManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CustomerOrderManagementId):
            self.id = CustomerOrderManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CustomerRelationshipManagement(CustomerManagement):
    """
    Customer Relationship Management refers to purposes associated with
    managing and analysing interactions with past, current, and potential
    customers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CustomerRelationshipManagement"]
    class_class_curie: ClassVar[str] = "dpv:CustomerRelationshipManagement"
    class_name: ClassVar[str] = "CustomerRelationshipManagement"
    class_model_uri: ClassVar[URIRef] = DPV.CustomerRelationshipManagement

    id: Union[str, CustomerRelationshipManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CustomerRelationshipManagementId):
            self.id = CustomerRelationshipManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CustomerSolvencyMonitoring(CustomerManagement):
    """
    Customer Solvency Monitoring refers to purposes associated with monitor
    solvency of customers for financial diligence
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CustomerSolvencyMonitoring"]
    class_class_curie: ClassVar[str] = "dpv:CustomerSolvencyMonitoring"
    class_name: ClassVar[str] = "CustomerSolvencyMonitoring"
    class_model_uri: ClassVar[URIRef] = DPV.CustomerSolvencyMonitoring

    id: Union[str, CustomerSolvencyMonitoringId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CustomerSolvencyMonitoringId):
            self.id = CustomerSolvencyMonitoringId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnforceSecurity(Purpose):
    """
    Purposes associated with ensuring and enforcing security for data,
    personnel, or other related matters
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EnforceSecurity"]
    class_class_curie: ClassVar[str] = "dpv:EnforceSecurity"
    class_name: ClassVar[str] = "EnforceSecurity"
    class_model_uri: ClassVar[URIRef] = DPV.EnforceSecurity

    id: Union[str, EnforceSecurityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnforceSecurityId):
            self.id = EnforceSecurityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnforceAccessControl(EnforceSecurity):
    """
    Purposes associated with conducting or enforcing access control as a
    form of security
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EnforceAccessControl"]
    class_class_curie: ClassVar[str] = "dpv:EnforceAccessControl"
    class_name: ClassVar[str] = "EnforceAccessControl"
    class_model_uri: ClassVar[URIRef] = DPV.EnforceAccessControl

    id: Union[str, EnforceAccessControlId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnforceAccessControlId):
            self.id = EnforceAccessControlId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EstablishContractualAgreement(Purpose):
    """
    Purposes associated with carrying out data processing to establish an
    agreement, such as for entering into a contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EstablishContractualAgreement"]
    class_class_curie: ClassVar[str] = "dpv:EstablishContractualAgreement"
    class_name: ClassVar[str] = "EstablishContractualAgreement"
    class_model_uri: ClassVar[URIRef] = DPV.EstablishContractualAgreement

    id: Union[str, EstablishContractualAgreementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EstablishContractualAgreementId):
            self.id = EstablishContractualAgreementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FulfilmentOfObligation(Purpose):
    """
    Purposes associated with carrying out data processing to fulfill an
    obligation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FulfilmentOfObligation"]
    class_class_curie: ClassVar[str] = "dpv:FulfilmentOfObligation"
    class_name: ClassVar[str] = "FulfilmentOfObligation"
    class_model_uri: ClassVar[URIRef] = DPV.FulfilmentOfObligation

    id: Union[str, FulfilmentOfObligationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FulfilmentOfObligationId):
            self.id = FulfilmentOfObligationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FulfilmentOfContractualObligation(FulfilmentOfObligation):
    """
    Purposes associated with carrying out data processing to fulfill a
    contractual obligation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FulfilmentOfContractualObligation"]
    class_class_curie: ClassVar[str] = "dpv:FulfilmentOfContractualObligation"
    class_name: ClassVar[str] = "FulfilmentOfContractualObligation"
    class_model_uri: ClassVar[URIRef] = DPV.FulfilmentOfContractualObligation

    id: Union[str, FulfilmentOfContractualObligationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FulfilmentOfContractualObligationId):
            self.id = FulfilmentOfContractualObligationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanResourceManagement(Purpose):
    """
    Purposes associated with managing humans and 'human resources' within
    the organisation for effective and efficient operations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HumanResourceManagement"]
    class_class_curie: ClassVar[str] = "dpv:HumanResourceManagement"
    class_name: ClassVar[str] = "HumanResourceManagement"
    class_model_uri: ClassVar[URIRef] = DPV.HumanResourceManagement

    id: Union[str, HumanResourceManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanResourceManagementId):
            self.id = HumanResourceManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdentityAuthentication(EnforceSecurity):
    """
    Purposes associated with performing authentication based on identity as
    a form of security
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["IdentityAuthentication"]
    class_class_curie: ClassVar[str] = "dpv:IdentityAuthentication"
    class_name: ClassVar[str] = "IdentityAuthentication"
    class_model_uri: ClassVar[URIRef] = DPV.IdentityAuthentication

    id: Union[str, IdentityAuthenticationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdentityAuthenticationId):
            self.id = IdentityAuthenticationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImproveInternalCRMProcesses(CustomerRelationshipManagement):
    """
    Purposes associated with improving customer-relationship management
    (CRM) processes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ImproveInternalCRMProcesses"]
    class_class_curie: ClassVar[str] = "dpv:ImproveInternalCRMProcesses"
    class_name: ClassVar[str] = "ImproveInternalCRMProcesses"
    class_model_uri: ClassVar[URIRef] = DPV.ImproveInternalCRMProcesses

    id: Union[str, ImproveInternalCRMProcessesId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImproveInternalCRMProcessesId):
            self.id = ImproveInternalCRMProcessesId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalCompliance(FulfilmentOfObligation):
    """
    Purposes associated with carrying out data processing to fulfill a legal
    or statutory obligation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalCompliance"]
    class_class_curie: ClassVar[str] = "dpv:LegalCompliance"
    class_name: ClassVar[str] = "LegalCompliance"
    class_model_uri: ClassVar[URIRef] = DPV.LegalCompliance

    id: Union[str, LegalComplianceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalComplianceId):
            self.id = LegalComplianceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Marketing(Purpose):
    """
    Purposes associated with conducting marketing in relation to
    organisation or products or services e.g. promoting, selling, and
    distributing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Marketing"]
    class_class_curie: ClassVar[str] = "dpv:Marketing"
    class_name: ClassVar[str] = "Marketing"
    class_model_uri: ClassVar[URIRef] = DPV.Marketing

    id: Union[str, MarketingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MarketingId):
            self.id = MarketingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Advertising(Marketing):
    """
    Purposes associated with conducting advertising i.e. process or artefact
    used to call attention to a product, service, etc. through
    announcements, notices, or other forms of communication
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Advertising"]
    class_class_curie: ClassVar[str] = "dpv:Advertising"
    class_name: ClassVar[str] = "Advertising"
    class_model_uri: ClassVar[URIRef] = DPV.Advertising

    id: Union[str, AdvertisingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdvertisingId):
            self.id = AdvertisingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DirectMarketing(Marketing):
    """
    Purposes associated with conducting direct marketing i.e. marketing
    communicated directly to the individual
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DirectMarketing"]
    class_class_curie: ClassVar[str] = "dpv:DirectMarketing"
    class_name: ClassVar[str] = "DirectMarketing"
    class_model_uri: ClassVar[URIRef] = DPV.DirectMarketing

    id: Union[str, DirectMarketingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DirectMarketingId):
            self.id = DirectMarketingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MisusePreventionAndDetection(EnforceSecurity):
    """
    Prevention and Detection of Misuse or Abuse of services
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MisusePreventionAndDetection"]
    class_class_curie: ClassVar[str] = "dpv:MisusePreventionAndDetection"
    class_name: ClassVar[str] = "MisusePreventionAndDetection"
    class_model_uri: ClassVar[URIRef] = DPV.MisusePreventionAndDetection

    id: Union[str, MisusePreventionAndDetectionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MisusePreventionAndDetectionId):
            self.id = MisusePreventionAndDetectionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FraudPreventionAndDetection(MisusePreventionAndDetection):
    """
    Purposes associated with fraud detection, prevention, and mitigation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FraudPreventionAndDetection"]
    class_class_curie: ClassVar[str] = "dpv:FraudPreventionAndDetection"
    class_name: ClassVar[str] = "FraudPreventionAndDetection"
    class_model_uri: ClassVar[URIRef] = DPV.FraudPreventionAndDetection

    id: Union[str, FraudPreventionAndDetectionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FraudPreventionAndDetectionId):
            self.id = FraudPreventionAndDetectionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CounterMoneyLaundering(FraudPreventionAndDetection):
    """
    Purposes associated with detection, prevention, and mitigation of
    mitigate money laundering
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CounterMoneyLaundering"]
    class_class_curie: ClassVar[str] = "dpv:CounterMoneyLaundering"
    class_name: ClassVar[str] = "CounterMoneyLaundering"
    class_model_uri: ClassVar[URIRef] = DPV.CounterMoneyLaundering

    id: Union[str, CounterMoneyLaunderingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CounterMoneyLaunderingId):
            self.id = CounterMoneyLaunderingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MaintainFraudDatabase(FraudPreventionAndDetection):
    """
    Purposes associated with maintaining a database related to identifying
    and identified fraud risks and fraud incidents
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MaintainFraudDatabase"]
    class_class_curie: ClassVar[str] = "dpv:MaintainFraudDatabase"
    class_name: ClassVar[str] = "MaintainFraudDatabase"
    class_model_uri: ClassVar[URIRef] = DPV.MaintainFraudDatabase

    id: Union[str, MaintainFraudDatabaseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaintainFraudDatabaseId):
            self.id = MaintainFraudDatabaseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NonCommercialPurpose(Purpose):
    """
    Purposes associated with processing activities performed in a
    non-commercial setting or without intention to commercialise
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NonCommercialPurpose"]
    class_class_curie: ClassVar[str] = "dpv:NonCommercialPurpose"
    class_name: ClassVar[str] = "NonCommercialPurpose"
    class_model_uri: ClassVar[URIRef] = DPV.NonCommercialPurpose

    id: Union[str, NonCommercialPurposeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NonCommercialPurposeId):
            self.id = NonCommercialPurposeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NonCommercialResearch(NonCommercialPurpose):
    """
    Purposes associated with conducting research in a non-commercial setting
    e.g. for a non-profit-organisation (NGO)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NonCommercialResearch"]
    class_class_curie: ClassVar[str] = "dpv:NonCommercialResearch"
    class_name: ClassVar[str] = "NonCommercialResearch"
    class_model_uri: ClassVar[URIRef] = DPV.NonCommercialResearch

    id: Union[str, NonCommercialResearchId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NonCommercialResearchId):
            self.id = NonCommercialResearchId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrganisationGovernance(Purpose):
    """
    Purposes associated with conducting activities and functions for
    governance of an organisation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OrganisationGovernance"]
    class_class_curie: ClassVar[str] = "dpv:OrganisationGovernance"
    class_name: ClassVar[str] = "OrganisationGovernance"
    class_model_uri: ClassVar[URIRef] = DPV.OrganisationGovernance

    id: Union[str, OrganisationGovernanceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganisationGovernanceId):
            self.id = OrganisationGovernanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataGovernance(OrganisationGovernance):
    """
    Measures associated with topics typically considered to be part of 'Data
    Governance'
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataGovernance"]
    class_class_curie: ClassVar[str] = "dpv:DataGovernance"
    class_name: ClassVar[str] = "DataGovernance"
    class_model_uri: ClassVar[URIRef] = DPV.DataGovernance

    id: Union[str, DataGovernanceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataGovernanceId):
            self.id = DataGovernanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataAvailabilityAssessment(DataGovernance):
    """
    Measures associated with assessment of availability of data for specific
    task(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataAvailabilityAssessment"]
    class_class_curie: ClassVar[str] = "dpv:DataAvailabilityAssessment"
    class_name: ClassVar[str] = "DataAvailabilityAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.DataAvailabilityAssessment

    id: Union[str, DataAvailabilityAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataAvailabilityAssessmentId):
            self.id = DataAvailabilityAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataInteroperabilityManagement(DataGovernance):
    """
    Measures associated with management of data interoperability
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataInteroperabilityManagement"]
    class_class_curie: ClassVar[str] = "dpv:DataInteroperabilityManagement"
    class_name: ClassVar[str] = "DataInteroperabilityManagement"
    class_model_uri: ClassVar[URIRef] = DPV.DataInteroperabilityManagement

    id: Union[str, DataInteroperabilityManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataInteroperabilityManagementId):
            self.id = DataInteroperabilityManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataInteroperabilityImprovement(DataInteroperabilityManagement):
    """
    Measures associated with improvement of data interoperability
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataInteroperabilityImprovement"]
    class_class_curie: ClassVar[str] = "dpv:DataInteroperabilityImprovement"
    class_name: ClassVar[str] = "DataInteroperabilityImprovement"
    class_model_uri: ClassVar[URIRef] = DPV.DataInteroperabilityImprovement

    id: Union[str, DataInteroperabilityImprovementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataInteroperabilityImprovementId):
            self.id = DataInteroperabilityImprovementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataInventoryManagement(DataGovernance):
    """
    Measures associated with management of data inventory or a data asset
    list
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataInventoryManagement"]
    class_class_curie: ClassVar[str] = "dpv:DataInventoryManagement"
    class_name: ClassVar[str] = "DataInventoryManagement"
    class_model_uri: ClassVar[URIRef] = DPV.DataInventoryManagement

    id: Union[str, DataInventoryManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataInventoryManagementId):
            self.id = DataInventoryManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataQualityManagement(DataGovernance):
    """
    Measures associated with management of data quality
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataQualityManagement"]
    class_class_curie: ClassVar[str] = "dpv:DataQualityManagement"
    class_name: ClassVar[str] = "DataQualityManagement"
    class_model_uri: ClassVar[URIRef] = DPV.DataQualityManagement

    id: Union[str, DataQualityManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataQualityManagementId):
            self.id = DataQualityManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataQualityImprovement(DataQualityManagement):
    """
    Measures associated with improvement of data quality
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataQualityImprovement"]
    class_class_curie: ClassVar[str] = "dpv:DataQualityImprovement"
    class_name: ClassVar[str] = "DataQualityImprovement"
    class_model_uri: ClassVar[URIRef] = DPV.DataQualityImprovement

    id: Union[str, DataQualityImprovementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataQualityImprovementId):
            self.id = DataQualityImprovementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSecurityManagement(DataGovernance):
    """
    Measures associated with management of data security
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSecurityManagement"]
    class_class_curie: ClassVar[str] = "dpv:DataSecurityManagement"
    class_name: ClassVar[str] = "DataSecurityManagement"
    class_model_uri: ClassVar[URIRef] = DPV.DataSecurityManagement

    id: Union[str, DataSecurityManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSecurityManagementId):
            self.id = DataSecurityManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetadataManagement(DataGovernance):
    """
    Measures associated with management of metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MetadataManagement"]
    class_class_curie: ClassVar[str] = "dpv:MetadataManagement"
    class_name: ClassVar[str] = "MetadataManagement"
    class_model_uri: ClassVar[URIRef] = DPV.MetadataManagement

    id: Union[str, MetadataManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MetadataManagementId):
            self.id = MetadataManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DisputeManagement(OrganisationGovernance):
    """
    Purposes associated with activities that manage disputes by natural
    persons, private bodies, or public authorities relevant to organisation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DisputeManagement"]
    class_class_curie: ClassVar[str] = "dpv:DisputeManagement"
    class_name: ClassVar[str] = "DisputeManagement"
    class_model_uri: ClassVar[URIRef] = DPV.DisputeManagement

    id: Union[str, DisputeManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DisputeManagementId):
            self.id = DisputeManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MemberPartnerManagement(OrganisationGovernance):
    """
    Purposes associated with maintaining a registry of shareholders,
    members, or partners for governance, administration, and management
    functions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MemberPartnerManagement"]
    class_class_curie: ClassVar[str] = "dpv:MemberPartnerManagement"
    class_name: ClassVar[str] = "MemberPartnerManagement"
    class_model_uri: ClassVar[URIRef] = DPV.MemberPartnerManagement

    id: Union[str, MemberPartnerManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MemberPartnerManagementId):
            self.id = MemberPartnerManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrganisationComplianceManagement(OrganisationGovernance):
    """
    Purposes associated with managing compliance for organisation in
    relation to internal policies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OrganisationComplianceManagement"]
    class_class_curie: ClassVar[str] = "dpv:OrganisationComplianceManagement"
    class_name: ClassVar[str] = "OrganisationComplianceManagement"
    class_model_uri: ClassVar[URIRef] = DPV.OrganisationComplianceManagement

    id: Union[str, OrganisationComplianceManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganisationComplianceManagementId):
            self.id = OrganisationComplianceManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OrganisationRiskManagement(OrganisationGovernance):
    """
    Purposes associated with managing risk for organisation's activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OrganisationRiskManagement"]
    class_class_curie: ClassVar[str] = "dpv:OrganisationRiskManagement"
    class_name: ClassVar[str] = "OrganisationRiskManagement"
    class_model_uri: ClassVar[URIRef] = DPV.OrganisationRiskManagement

    id: Union[str, OrganisationRiskManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganisationRiskManagementId):
            self.id = OrganisationRiskManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Personalisation(Purpose):
    """
    Purposes associated with creating and providing customisation based on
    attributes and/or needs of person(s) or context(s).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Personalisation"]
    class_class_curie: ClassVar[str] = "dpv:Personalisation"
    class_name: ClassVar[str] = "Personalisation"
    class_model_uri: ClassVar[URIRef] = DPV.Personalisation

    id: Union[str, PersonalisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonalisationId):
            self.id = PersonalisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonalisedAdvertising(Advertising):
    """
    Purposes associated with creating and providing personalised advertising
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonalisedAdvertising"]
    class_class_curie: ClassVar[str] = "dpv:PersonalisedAdvertising"
    class_name: ClassVar[str] = "PersonalisedAdvertising"
    class_model_uri: ClassVar[URIRef] = DPV.PersonalisedAdvertising

    id: Union[str, PersonalisedAdvertisingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonalisedAdvertisingId):
            self.id = PersonalisedAdvertisingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonnelManagement(HumanResourceManagement):
    """
    Purposes associated with management of personnel associated with the
    organisation e.g. evaluation and management of employees and
    intermediaries
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonnelManagement"]
    class_class_curie: ClassVar[str] = "dpv:PersonnelManagement"
    class_name: ClassVar[str] = "PersonnelManagement"
    class_model_uri: ClassVar[URIRef] = DPV.PersonnelManagement

    id: Union[str, PersonnelManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonnelManagementId):
            self.id = PersonnelManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonnelHiring(PersonnelManagement):
    """
    Purposes associated with management and execution of hiring processes of
    personnel
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonnelHiring"]
    class_class_curie: ClassVar[str] = "dpv:PersonnelHiring"
    class_name: ClassVar[str] = "PersonnelHiring"
    class_model_uri: ClassVar[URIRef] = DPV.PersonnelHiring

    id: Union[str, PersonnelHiringId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonnelHiringId):
            self.id = PersonnelHiringId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonnelMonitoring(PersonnelManagement):
    """
    Purposes associated with monitoring of personnel
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonnelMonitoring"]
    class_class_curie: ClassVar[str] = "dpv:PersonnelMonitoring"
    class_name: ClassVar[str] = "PersonnelMonitoring"
    class_model_uri: ClassVar[URIRef] = DPV.PersonnelMonitoring

    id: Union[str, PersonnelMonitoringId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonnelMonitoringId):
            self.id = PersonnelMonitoringId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonnelBehaviourMonitoring(PersonnelMonitoring):
    """
    Purposes associated with monitoring behaviour of personnel
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonnelBehaviourMonitoring"]
    class_class_curie: ClassVar[str] = "dpv:PersonnelBehaviourMonitoring"
    class_name: ClassVar[str] = "PersonnelBehaviourMonitoring"
    class_model_uri: ClassVar[URIRef] = DPV.PersonnelBehaviourMonitoring

    id: Union[str, PersonnelBehaviourMonitoringId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonnelBehaviourMonitoringId):
            self.id = PersonnelBehaviourMonitoringId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonnelOffboarding(PersonnelManagement):
    """
    Purposes associated with offboarding of personnel i.e. activities and
    processes carried out when the person is exiting the company or role
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonnelOffboarding"]
    class_class_curie: ClassVar[str] = "dpv:PersonnelOffboarding"
    class_name: ClassVar[str] = "PersonnelOffboarding"
    class_model_uri: ClassVar[URIRef] = DPV.PersonnelOffboarding

    id: Union[str, PersonnelOffboardingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonnelOffboardingId):
            self.id = PersonnelOffboardingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonnelOnboarding(PersonnelHiring):
    """
    Purposes associated with onboarding and integration of personnel within
    an organisation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonnelOnboarding"]
    class_class_curie: ClassVar[str] = "dpv:PersonnelOnboarding"
    class_name: ClassVar[str] = "PersonnelOnboarding"
    class_model_uri: ClassVar[URIRef] = DPV.PersonnelOnboarding

    id: Union[str, PersonnelOnboardingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonnelOnboardingId):
            self.id = PersonnelOnboardingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonnelPayment(PersonnelManagement):
    """
    Purposes associated with management and execution of payment of
    personnel
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonnelPayment"]
    class_class_curie: ClassVar[str] = "dpv:PersonnelPayment"
    class_name: ClassVar[str] = "PersonnelPayment"
    class_model_uri: ClassVar[URIRef] = DPV.PersonnelPayment

    id: Union[str, PersonnelPaymentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonnelPaymentId):
            self.id = PersonnelPaymentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonnelPerformanceManagement(PersonnelManagement):
    """
    Purposes associated with management of performance of personnel
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonnelPerformanceManagement"]
    class_class_curie: ClassVar[str] = "dpv:PersonnelPerformanceManagement"
    class_name: ClassVar[str] = "PersonnelPerformanceManagement"
    class_model_uri: ClassVar[URIRef] = DPV.PersonnelPerformanceManagement

    id: Union[str, PersonnelPerformanceManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonnelPerformanceManagementId):
            self.id = PersonnelPerformanceManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonnelPerformanceEvaluation(PersonnelPerformanceManagement):
    """
    Purposes associated with evaluation or assessment of performance of
    employees
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonnelPerformanceEvaluation"]
    class_class_curie: ClassVar[str] = "dpv:PersonnelPerformanceEvaluation"
    class_name: ClassVar[str] = "PersonnelPerformanceEvaluation"
    class_model_uri: ClassVar[URIRef] = DPV.PersonnelPerformanceEvaluation

    id: Union[str, PersonnelPerformanceEvaluationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonnelPerformanceEvaluationId):
            self.id = PersonnelPerformanceEvaluationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonnelPerformanceMonitoring(PersonnelMonitoring):
    """
    Purposes associated with monitoring of performance of personnel
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonnelPerformanceMonitoring"]
    class_class_curie: ClassVar[str] = "dpv:PersonnelPerformanceMonitoring"
    class_name: ClassVar[str] = "PersonnelPerformanceMonitoring"
    class_model_uri: ClassVar[URIRef] = DPV.PersonnelPerformanceMonitoring

    id: Union[str, PersonnelPerformanceMonitoringId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonnelPerformanceMonitoringId):
            self.id = PersonnelPerformanceMonitoringId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonnelPerformancePrediction(PersonnelPerformanceManagement):
    """
    Purposes associated with prediction of performance of personnel
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonnelPerformancePrediction"]
    class_class_curie: ClassVar[str] = "dpv:PersonnelPerformancePrediction"
    class_name: ClassVar[str] = "PersonnelPerformancePrediction"
    class_model_uri: ClassVar[URIRef] = DPV.PersonnelPerformancePrediction

    id: Union[str, PersonnelPerformancePredictionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonnelPerformancePredictionId):
            self.id = PersonnelPerformancePredictionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonnelPromotionManagement(PersonnelManagement):
    """
    Purposes associated with determination and management of promotion of
    personnel
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonnelPromotionManagement"]
    class_class_curie: ClassVar[str] = "dpv:PersonnelPromotionManagement"
    class_name: ClassVar[str] = "PersonnelPromotionManagement"
    class_model_uri: ClassVar[URIRef] = DPV.PersonnelPromotionManagement

    id: Union[str, PersonnelPromotionManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonnelPromotionManagementId):
            self.id = PersonnelPromotionManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonnelTerminationManagement(PersonnelManagement):
    """
    Purposes associated with determination and management of termination of
    personnel
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonnelTerminationManagement"]
    class_class_curie: ClassVar[str] = "dpv:PersonnelTerminationManagement"
    class_name: ClassVar[str] = "PersonnelTerminationManagement"
    class_model_uri: ClassVar[URIRef] = DPV.PersonnelTerminationManagement

    id: Union[str, PersonnelTerminationManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonnelTerminationManagementId):
            self.id = PersonnelTerminationManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonnelWorkloadManagement(PersonnelManagement):
    """
    Purposes assocaited with determination, scheduling, planning, and
    carrying out workload management of personnel
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonnelWorkloadManagement"]
    class_class_curie: ClassVar[str] = "dpv:PersonnelWorkloadManagement"
    class_name: ClassVar[str] = "PersonnelWorkloadManagement"
    class_model_uri: ClassVar[URIRef] = DPV.PersonnelWorkloadManagement

    id: Union[str, PersonnelWorkloadManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonnelWorkloadManagementId):
            self.id = PersonnelWorkloadManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PoliticalCampaign(Advertising):
    """
    Purposes associated with political campaign activities related to
    promotion and advertisement of positions and candidates in elections at
    local, state or regional, or national and international levels
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PoliticalCampaign"]
    class_class_curie: ClassVar[str] = "dpv:PoliticalCampaign"
    class_name: ClassVar[str] = "PoliticalCampaign"
    class_model_uri: ClassVar[URIRef] = DPV.PoliticalCampaign

    id: Union[str, PoliticalCampaignId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PoliticalCampaignId):
            self.id = PoliticalCampaignId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProtectionOfIPR(FulfilmentOfObligation):
    """
    Purposes associated with the protection of intellectual property rights
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProtectionOfIPR"]
    class_class_curie: ClassVar[str] = "dpv:ProtectionOfIPR"
    class_name: ClassVar[str] = "ProtectionOfIPR"
    class_model_uri: ClassVar[URIRef] = DPV.ProtectionOfIPR

    id: Union[str, ProtectionOfIPRId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProtectionOfIPRId):
            self.id = ProtectionOfIPRId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicBenefit(Purpose):
    """
    Purposes undertaken and intended to provide benefit to public or society
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicBenefit"]
    class_class_curie: ClassVar[str] = "dpv:PublicBenefit"
    class_name: ClassVar[str] = "PublicBenefit"
    class_model_uri: ClassVar[URIRef] = DPV.PublicBenefit

    id: Union[str, PublicBenefitId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicBenefitId):
            self.id = PublicBenefitId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CombatClimateChange(PublicBenefit):
    """
    Purposes associated with combating the causes and consequences of
    climate change, including reducing gas emissions and fighting
    emergencies such as floods or wildfires
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CombatClimateChange"]
    class_class_curie: ClassVar[str] = "dpv:CombatClimateChange"
    class_name: ClassVar[str] = "CombatClimateChange"
    class_model_uri: ClassVar[URIRef] = DPV.CombatClimateChange

    id: Union[str, CombatClimateChangeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CombatClimateChangeId):
            self.id = CombatClimateChangeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Counterterrorism(PublicBenefit):
    """
    Purposes associated with activities that detect, prevent, mitigate, or
    otherwise perform activities to combat or eliminate terrorism (also
    referred to as anti-terrorism)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Counterterrorism"]
    class_class_curie: ClassVar[str] = "dpv:Counterterrorism"
    class_name: ClassVar[str] = "Counterterrorism"
    class_model_uri: ClassVar[URIRef] = DPV.Counterterrorism

    id: Union[str, CounterterrorismId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CounterterrorismId):
            self.id = CounterterrorismId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataAltruism(PublicBenefit):
    """
    Purposes associated with the voluntary sharing of data for the general
    interest of the public, such as healthcare or combating climate change
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataAltruism"]
    class_class_curie: ClassVar[str] = "dpv:DataAltruism"
    class_name: ClassVar[str] = "DataAltruism"
    class_model_uri: ClassVar[URIRef] = DPV.DataAltruism

    id: Union[str, DataAltruismId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataAltruismId):
            self.id = DataAltruismId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImproveHealthcare(PublicBenefit):
    """
    Purposes associated with improving healthcare systems such as for
    personalised treatments and curing chronic diseases
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ImproveHealthcare"]
    class_class_curie: ClassVar[str] = "dpv:ImproveHealthcare"
    class_name: ClassVar[str] = "ImproveHealthcare"
    class_model_uri: ClassVar[URIRef] = DPV.ImproveHealthcare

    id: Union[str, ImproveHealthcareId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImproveHealthcareId):
            self.id = ImproveHealthcareId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImprovePublicServices(PublicBenefit):
    """
    Purposes associated with improving the provision of public services,
    such as public safety, education or law enforcement
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ImprovePublicServices"]
    class_class_curie: ClassVar[str] = "dpv:ImprovePublicServices"
    class_name: ClassVar[str] = "ImprovePublicServices"
    class_model_uri: ClassVar[URIRef] = DPV.ImprovePublicServices

    id: Union[str, ImprovePublicServicesId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImprovePublicServicesId):
            self.id = ImprovePublicServicesId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImproveTransportMobility(PublicBenefit):
    """
    Purposes associated with improving traffic, public transport systems or
    costs for drivers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ImproveTransportMobility"]
    class_class_curie: ClassVar[str] = "dpv:ImproveTransportMobility"
    class_name: ClassVar[str] = "ImproveTransportMobility"
    class_model_uri: ClassVar[URIRef] = DPV.ImproveTransportMobility

    id: Union[str, ImproveTransportMobilityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImproveTransportMobilityId):
            self.id = ImproveTransportMobilityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProtectionOfNationalSecurity(PublicBenefit):
    """
    Purposes associated with the protection of national security
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProtectionOfNationalSecurity"]
    class_class_curie: ClassVar[str] = "dpv:ProtectionOfNationalSecurity"
    class_name: ClassVar[str] = "ProtectionOfNationalSecurity"
    class_model_uri: ClassVar[URIRef] = DPV.ProtectionOfNationalSecurity

    id: Union[str, ProtectionOfNationalSecurityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProtectionOfNationalSecurityId):
            self.id = ProtectionOfNationalSecurityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProtectionOfPublicSecurity(PublicBenefit):
    """
    Purposes associated with the protection of public security
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProtectionOfPublicSecurity"]
    class_class_curie: ClassVar[str] = "dpv:ProtectionOfPublicSecurity"
    class_name: ClassVar[str] = "ProtectionOfPublicSecurity"
    class_model_uri: ClassVar[URIRef] = DPV.ProtectionOfPublicSecurity

    id: Union[str, ProtectionOfPublicSecurityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProtectionOfPublicSecurityId):
            self.id = ProtectionOfPublicSecurityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProvideOfficialStatistics(PublicBenefit):
    """
    Purposes associated with facilitating the development, production and
    dissemination of reliable official statistics
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProvideOfficialStatistics"]
    class_class_curie: ClassVar[str] = "dpv:ProvideOfficialStatistics"
    class_name: ClassVar[str] = "ProvideOfficialStatistics"
    class_model_uri: ClassVar[URIRef] = DPV.ProvideOfficialStatistics

    id: Union[str, ProvideOfficialStatisticsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProvideOfficialStatisticsId):
            self.id = ProvideOfficialStatisticsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicPolicyMaking(PublicBenefit):
    """
    Purposes associated with public policy making, such as the development
    of new laws
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicPolicyMaking"]
    class_class_curie: ClassVar[str] = "dpv:PublicPolicyMaking"
    class_name: ClassVar[str] = "PublicPolicyMaking"
    class_model_uri: ClassVar[URIRef] = DPV.PublicPolicyMaking

    id: Union[str, PublicPolicyMakingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicPolicyMakingId):
            self.id = PublicPolicyMakingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicRelations(Marketing):
    """
    Purposes associated with managing and conducting public relations
    processes, including creating goodwill for the organisation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicRelations"]
    class_class_curie: ClassVar[str] = "dpv:PublicRelations"
    class_name: ClassVar[str] = "PublicRelations"
    class_model_uri: ClassVar[URIRef] = DPV.PublicRelations

    id: Union[str, PublicRelationsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicRelationsId):
            self.id = PublicRelationsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecordManagement(Purpose):
    """
    Purposes associated with manage creation, storage, and use of records
    relevant to operations, events, and processes e.g. to store logs or
    access requests
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecordManagement"]
    class_class_curie: ClassVar[str] = "dpv:RecordManagement"
    class_name: ClassVar[str] = "RecordManagement"
    class_model_uri: ClassVar[URIRef] = DPV.RecordManagement

    id: Union[str, RecordManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecordManagementId):
            self.id = RecordManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecruitmentAdvertising(Advertising):
    """
    Purposes associated with advertisement for Recruitments and personnel
    hiring
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecruitmentAdvertising"]
    class_class_curie: ClassVar[str] = "dpv:RecruitmentAdvertising"
    class_name: ClassVar[str] = "RecruitmentAdvertising"
    class_model_uri: ClassVar[URIRef] = DPV.RecruitmentAdvertising

    id: Union[str, RecruitmentAdvertisingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecruitmentAdvertisingId):
            self.id = RecruitmentAdvertisingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecruitmentManagement(PersonnelHiring):
    """
    Purposes assocaited with recruitment of personnel, which includes
    identifying, sourcing, screening, filtering, shortlisting, and
    interviewing candidates
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecruitmentManagement"]
    class_class_curie: ClassVar[str] = "dpv:RecruitmentManagement"
    class_name: ClassVar[str] = "RecruitmentManagement"
    class_model_uri: ClassVar[URIRef] = DPV.RecruitmentManagement

    id: Union[str, RecruitmentManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecruitmentManagementId):
            self.id = RecruitmentManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecruitmentApplicantBackgroundCheck(RecruitmentManagement):
    """
    Purposes assocaited with conducting background checks for prospective
    and current job applicants for recruitment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecruitmentApplicantBackgroundCheck"]
    class_class_curie: ClassVar[str] = "dpv:RecruitmentApplicantBackgroundCheck"
    class_name: ClassVar[str] = "RecruitmentApplicantBackgroundCheck"
    class_model_uri: ClassVar[URIRef] = DPV.RecruitmentApplicantBackgroundCheck

    id: Union[str, RecruitmentApplicantBackgroundCheckId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecruitmentApplicantBackgroundCheckId):
            self.id = RecruitmentApplicantBackgroundCheckId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecruitmentApplicantCriminalBackgroundCheck(RecruitmentManagement):
    """
    Purposes associated with conducting criminal background assessment for
    prospective and current job applicants for recruitment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecruitmentApplicantCriminalBackgroundCheck"]
    class_class_curie: ClassVar[str] = "dpv:RecruitmentApplicantCriminalBackgroundCheck"
    class_name: ClassVar[str] = "RecruitmentApplicantCriminalBackgroundCheck"
    class_model_uri: ClassVar[URIRef] = DPV.RecruitmentApplicantCriminalBackgroundCheck

    id: Union[str, RecruitmentApplicantCriminalBackgroundCheckId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecruitmentApplicantCriminalBackgroundCheckId):
            self.id = RecruitmentApplicantCriminalBackgroundCheckId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecruitmentApplicantInformationAuthentication(RecruitmentManagement):
    """
    Purposes associated with authentication and verification of information
    as part of recruitment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecruitmentApplicantInformationAuthentication"]
    class_class_curie: ClassVar[str] = "dpv:RecruitmentApplicantInformationAuthentication"
    class_name: ClassVar[str] = "RecruitmentApplicantInformationAuthentication"
    class_model_uri: ClassVar[URIRef] = DPV.RecruitmentApplicantInformationAuthentication

    id: Union[str, RecruitmentApplicantInformationAuthenticationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecruitmentApplicantInformationAuthenticationId):
            self.id = RecruitmentApplicantInformationAuthenticationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecruitmentApplicantSelection(RecruitmentManagement):
    """
    Purposes associated with determination or selection of candidates,
    whether for a specific job or job pool, or for a specific stage as part
    of recruitment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecruitmentApplicantSelection"]
    class_class_curie: ClassVar[str] = "dpv:RecruitmentApplicantSelection"
    class_name: ClassVar[str] = "RecruitmentApplicantSelection"
    class_model_uri: ClassVar[URIRef] = DPV.RecruitmentApplicantSelection

    id: Union[str, RecruitmentApplicantSelectionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecruitmentApplicantSelectionId):
            self.id = RecruitmentApplicantSelectionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecruitmentApplicationManagement(RecruitmentManagement):
    """
    Purposes associated with managing job applications for recruitment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecruitmentApplicationManagement"]
    class_class_curie: ClassVar[str] = "dpv:RecruitmentApplicationManagement"
    class_name: ClassVar[str] = "RecruitmentApplicationManagement"
    class_model_uri: ClassVar[URIRef] = DPV.RecruitmentApplicationManagement

    id: Union[str, RecruitmentApplicationManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecruitmentApplicationManagementId):
            self.id = RecruitmentApplicationManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecruitmentApplicationAnalysis(RecruitmentApplicationManagement):
    """
    Purposes assocaited with analysis of job applications or job candidates
    for recruitment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecruitmentApplicationAnalysis"]
    class_class_curie: ClassVar[str] = "dpv:RecruitmentApplicationAnalysis"
    class_name: ClassVar[str] = "RecruitmentApplicationAnalysis"
    class_model_uri: ClassVar[URIRef] = DPV.RecruitmentApplicationAnalysis

    id: Union[str, RecruitmentApplicationAnalysisId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecruitmentApplicationAnalysisId):
            self.id = RecruitmentApplicationAnalysisId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecruitmentApplicationScreening(RecruitmentApplicationManagement):
    """
    Purposes associated with screening and filtering of job applications or
    job candidates for recruitment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecruitmentApplicationScreening"]
    class_class_curie: ClassVar[str] = "dpv:RecruitmentApplicationScreening"
    class_name: ClassVar[str] = "RecruitmentApplicationScreening"
    class_model_uri: ClassVar[URIRef] = DPV.RecruitmentApplicationScreening

    id: Union[str, RecruitmentApplicationScreeningId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecruitmentApplicationScreeningId):
            self.id = RecruitmentApplicationScreeningId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecruitmentInterviewManagement(RecruitmentManagement):
    """
    Purposes associated conducting and managing interviews for recruitment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecruitmentInterviewManagement"]
    class_class_curie: ClassVar[str] = "dpv:RecruitmentInterviewManagement"
    class_name: ClassVar[str] = "RecruitmentInterviewManagement"
    class_model_uri: ClassVar[URIRef] = DPV.RecruitmentInterviewManagement

    id: Union[str, RecruitmentInterviewManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecruitmentInterviewManagementId):
            self.id = RecruitmentInterviewManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecruitmentInterviewAnalysis(RecruitmentInterviewManagement):
    """
    Purposes associated with analysis of interviews, including the people
    and involved, for recruitment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecruitmentInterviewAnalysis"]
    class_class_curie: ClassVar[str] = "dpv:RecruitmentInterviewAnalysis"
    class_name: ClassVar[str] = "RecruitmentInterviewAnalysis"
    class_model_uri: ClassVar[URIRef] = DPV.RecruitmentInterviewAnalysis

    id: Union[str, RecruitmentInterviewAnalysisId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecruitmentInterviewAnalysisId):
            self.id = RecruitmentInterviewAnalysisId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecruitmentInterviewAssessment(RecruitmentInterviewManagement):
    """
    Purposes associated with assessment of interviews, including assessment
    of people and information, for recruitment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecruitmentInterviewAssessment"]
    class_class_curie: ClassVar[str] = "dpv:RecruitmentInterviewAssessment"
    class_name: ClassVar[str] = "RecruitmentInterviewAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.RecruitmentInterviewAssessment

    id: Union[str, RecruitmentInterviewAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecruitmentInterviewAssessmentId):
            self.id = RecruitmentInterviewAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecruitmentInterviewScheduling(RecruitmentInterviewManagement):
    """
    Purposes associated with scheduling interviews for recruitment
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecruitmentInterviewScheduling"]
    class_class_curie: ClassVar[str] = "dpv:RecruitmentInterviewScheduling"
    class_name: ClassVar[str] = "RecruitmentInterviewScheduling"
    class_model_uri: ClassVar[URIRef] = DPV.RecruitmentInterviewScheduling

    id: Union[str, RecruitmentInterviewSchedulingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecruitmentInterviewSchedulingId):
            self.id = RecruitmentInterviewSchedulingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RecruitmentTargetedAdvertising(RecruitmentAdvertising):
    """
    Purposes associated with targeted advertisement for Recruitments and
    personnel hiring
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RecruitmentTargetedAdvertising"]
    class_class_curie: ClassVar[str] = "dpv:RecruitmentTargetedAdvertising"
    class_name: ClassVar[str] = "RecruitmentTargetedAdvertising"
    class_model_uri: ClassVar[URIRef] = DPV.RecruitmentTargetedAdvertising

    id: Union[str, RecruitmentTargetedAdvertisingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecruitmentTargetedAdvertisingId):
            self.id = RecruitmentTargetedAdvertisingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Remove(Processing):
    """
    to destruct or erase data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Remove"]
    class_class_curie: ClassVar[str] = "dpv:Remove"
    class_name: ClassVar[str] = "Remove"
    class_model_uri: ClassVar[URIRef] = DPV.Remove

    id: Union[str, RemoveId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RemoveId):
            self.id = RemoveId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Delete(Remove):
    """
    to remove data in a logical fashion i.e. with the possibility of
    retrieval
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Delete"]
    class_class_curie: ClassVar[str] = "dpv:Delete"
    class_name: ClassVar[str] = "Delete"
    class_model_uri: ClassVar[URIRef] = DPV.Delete

    id: Union[str, DeleteId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeleteId):
            self.id = DeleteId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Destruct(Remove):
    """
    to process data in a way it no longer exists or cannot be repaired
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Destruct"]
    class_class_curie: ClassVar[str] = "dpv:Destruct"
    class_name: ClassVar[str] = "Destruct"
    class_model_uri: ClassVar[URIRef] = DPV.Destruct

    id: Union[str, DestructId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DestructId):
            self.id = DestructId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Erase(Remove):
    """
    to remove data from existence i.e. without the possibility of retrieval
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Erase"]
    class_class_curie: ClassVar[str] = "dpv:Erase"
    class_name: ClassVar[str] = "Erase"
    class_model_uri: ClassVar[URIRef] = DPV.Erase

    id: Union[str, EraseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EraseId):
            self.id = EraseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResearchAndDevelopment(Purpose):
    """
    Purposes associated with conducting research and development for new
    methods, products, or services
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ResearchAndDevelopment"]
    class_class_curie: ClassVar[str] = "dpv:ResearchAndDevelopment"
    class_name: ClassVar[str] = "ResearchAndDevelopment"
    class_model_uri: ClassVar[URIRef] = DPV.ResearchAndDevelopment

    id: Union[str, ResearchAndDevelopmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResearchAndDevelopmentId):
            self.id = ResearchAndDevelopmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AcademicResearch(ResearchAndDevelopment):
    """
    Purposes associated with conducting or assisting with research conducted
    in an academic context e.g. within universities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AcademicResearch"]
    class_class_curie: ClassVar[str] = "dpv:AcademicResearch"
    class_name: ClassVar[str] = "AcademicResearch"
    class_model_uri: ClassVar[URIRef] = DPV.AcademicResearch

    id: Union[str, AcademicResearchId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AcademicResearchId):
            self.id = AcademicResearchId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReversingProcessEffects(EntityPermissiveInvolvement):
    """
    Involvement where entity can reverse effects of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ReversingProcessEffects"]
    class_class_curie: ClassVar[str] = "dpv:ReversingProcessEffects"
    class_name: ClassVar[str] = "ReversingProcessEffects"
    class_model_uri: ClassVar[URIRef] = DPV.ReversingProcessEffects

    id: Union[str, ReversingProcessEffectsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReversingProcessEffectsId):
            self.id = ReversingProcessEffectsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReversingProcessInput(EntityPermissiveInvolvement):
    """
    Involvement where entity can reverse input of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ReversingProcessInput"]
    class_class_curie: ClassVar[str] = "dpv:ReversingProcessInput"
    class_name: ClassVar[str] = "ReversingProcessInput"
    class_model_uri: ClassVar[URIRef] = DPV.ReversingProcessInput

    id: Union[str, ReversingProcessInputId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReversingProcessInputId):
            self.id = ReversingProcessInputId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReversingProcessOutput(EntityPermissiveInvolvement):
    """
    Involvement where entity can reverse output of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ReversingProcessOutput"]
    class_class_curie: ClassVar[str] = "dpv:ReversingProcessOutput"
    class_name: ClassVar[str] = "ReversingProcessOutput"
    class_model_uri: ClassVar[URIRef] = DPV.ReversingProcessOutput

    id: Union[str, ReversingProcessOutputId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReversingProcessOutputId):
            self.id = ReversingProcessOutputId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RightsFulfilment(LegalObligation):
    """
    Purposes associated with the fulfillment of rights specified in law
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RightsFulfilment"]
    class_class_curie: ClassVar[str] = "dpv:RightsFulfilment"
    class_name: ClassVar[str] = "RightsFulfilment"
    class_model_uri: ClassVar[URIRef] = DPV.RightsFulfilment

    id: Union[str, RightsFulfilmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RightsFulfilmentId):
            self.id = RightsFulfilmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Scale(ProcessingContext):
    """
    A measurement along some dimension
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Scale"]
    class_class_curie: ClassVar[str] = "dpv:Scale"
    class_name: ClassVar[str] = "Scale"
    class_model_uri: ClassVar[URIRef] = DPV.Scale

    id: Union[str, ScaleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScaleId):
            self.id = ScaleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSubjectScale(Scale):
    """
    Scale of Data Subject(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSubjectScale"]
    class_class_curie: ClassVar[str] = "dpv:DataSubjectScale"
    class_name: ClassVar[str] = "DataSubjectScale"
    class_model_uri: ClassVar[URIRef] = DPV.DataSubjectScale

    id: Union[str, DataSubjectScaleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSubjectScaleId):
            self.id = DataSubjectScaleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataVolume(Scale):
    """
    Volume or Scale of Data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataVolume"]
    class_class_curie: ClassVar[str] = "dpv:DataVolume"
    class_name: ClassVar[str] = "DataVolume"
    class_model_uri: ClassVar[URIRef] = DPV.DataVolume

    id: Union[str, DataVolumeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataVolumeId):
            self.id = DataVolumeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GeographicCoverage(Scale):
    """
    Indicate of scale in terms of geographic coverage
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["GeographicCoverage"]
    class_class_curie: ClassVar[str] = "dpv:GeographicCoverage"
    class_name: ClassVar[str] = "GeographicCoverage"
    class_model_uri: ClassVar[URIRef] = DPV.GeographicCoverage

    id: Union[str, GeographicCoverageId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeographicCoverageId):
            self.id = GeographicCoverageId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GlobalScale(GeographicCoverage):
    """
    Geographic coverage spanning the entire globe
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["GlobalScale"]
    class_class_curie: ClassVar[str] = "dpv:GlobalScale"
    class_name: ClassVar[str] = "GlobalScale"
    class_model_uri: ClassVar[URIRef] = DPV.GlobalScale

    id: Union[str, GlobalScaleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GlobalScaleId):
            self.id = GlobalScaleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HugeDataVolume(DataVolume):
    """
    Data volume that is considered huge or more than large within the
    context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HugeDataVolume"]
    class_class_curie: ClassVar[str] = "dpv:HugeDataVolume"
    class_name: ClassVar[str] = "HugeDataVolume"
    class_model_uri: ClassVar[URIRef] = DPV.HugeDataVolume

    id: Union[str, HugeDataVolumeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HugeDataVolumeId):
            self.id = HugeDataVolumeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HugeScaleOfDataSubjects(DataSubjectScale):
    """
    Scale of data subjects considered huge or more than large within the
    context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HugeScaleOfDataSubjects"]
    class_class_curie: ClassVar[str] = "dpv:HugeScaleOfDataSubjects"
    class_name: ClassVar[str] = "HugeScaleOfDataSubjects"
    class_model_uri: ClassVar[URIRef] = DPV.HugeScaleOfDataSubjects

    id: Union[str, HugeScaleOfDataSubjectsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HugeScaleOfDataSubjectsId):
            self.id = HugeScaleOfDataSubjectsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LargeDataVolume(DataVolume):
    """
    Data volume that is considered large within the context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LargeDataVolume"]
    class_class_curie: ClassVar[str] = "dpv:LargeDataVolume"
    class_name: ClassVar[str] = "LargeDataVolume"
    class_model_uri: ClassVar[URIRef] = DPV.LargeDataVolume

    id: Union[str, LargeDataVolumeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LargeDataVolumeId):
            self.id = LargeDataVolumeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LargeScaleOfDataSubjects(DataSubjectScale):
    """
    Scale of data subjects considered large within the context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LargeScaleOfDataSubjects"]
    class_class_curie: ClassVar[str] = "dpv:LargeScaleOfDataSubjects"
    class_name: ClassVar[str] = "LargeScaleOfDataSubjects"
    class_model_uri: ClassVar[URIRef] = DPV.LargeScaleOfDataSubjects

    id: Union[str, LargeScaleOfDataSubjectsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LargeScaleOfDataSubjectsId):
            self.id = LargeScaleOfDataSubjectsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LocalEnvironmentScale(GeographicCoverage):
    """
    Geographic coverage spanning a specific environment within the locality
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LocalEnvironmentScale"]
    class_class_curie: ClassVar[str] = "dpv:LocalEnvironmentScale"
    class_name: ClassVar[str] = "LocalEnvironmentScale"
    class_model_uri: ClassVar[URIRef] = DPV.LocalEnvironmentScale

    id: Union[str, LocalEnvironmentScaleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LocalEnvironmentScaleId):
            self.id = LocalEnvironmentScaleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LocalityScale(GeographicCoverage):
    """
    Geographic coverage spanning a specific locality
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LocalityScale"]
    class_class_curie: ClassVar[str] = "dpv:LocalityScale"
    class_name: ClassVar[str] = "LocalityScale"
    class_model_uri: ClassVar[URIRef] = DPV.LocalityScale

    id: Union[str, LocalityScaleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LocalityScaleId):
            self.id = LocalityScaleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MediumDataVolume(DataVolume):
    """
    Data volume that is considered medium i.e. neither large nor small
    within the context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MediumDataVolume"]
    class_class_curie: ClassVar[str] = "dpv:MediumDataVolume"
    class_name: ClassVar[str] = "MediumDataVolume"
    class_model_uri: ClassVar[URIRef] = DPV.MediumDataVolume

    id: Union[str, MediumDataVolumeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MediumDataVolumeId):
            self.id = MediumDataVolumeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MediumScaleOfDataSubjects(DataSubjectScale):
    """
    Scale of data subjects considered medium i.e. neither large nor small
    within the context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MediumScaleOfDataSubjects"]
    class_class_curie: ClassVar[str] = "dpv:MediumScaleOfDataSubjects"
    class_name: ClassVar[str] = "MediumScaleOfDataSubjects"
    class_model_uri: ClassVar[URIRef] = DPV.MediumScaleOfDataSubjects

    id: Union[str, MediumScaleOfDataSubjectsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MediumScaleOfDataSubjectsId):
            self.id = MediumScaleOfDataSubjectsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MultiNationalScale(GeographicCoverage):
    """
    Geographic coverage spanning multiple nations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MultiNationalScale"]
    class_class_curie: ClassVar[str] = "dpv:MultiNationalScale"
    class_name: ClassVar[str] = "MultiNationalScale"
    class_model_uri: ClassVar[URIRef] = DPV.MultiNationalScale

    id: Union[str, MultiNationalScaleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MultiNationalScaleId):
            self.id = MultiNationalScaleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NationalScale(GeographicCoverage):
    """
    Geographic coverage spanning a nation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NationalScale"]
    class_class_curie: ClassVar[str] = "dpv:NationalScale"
    class_name: ClassVar[str] = "NationalScale"
    class_model_uri: ClassVar[URIRef] = DPV.NationalScale

    id: Union[str, NationalScaleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NationalScaleId):
            self.id = NationalScaleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NearlyGlobalScale(GeographicCoverage):
    """
    Geographic coverage nearly spanning the entire globe
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NearlyGlobalScale"]
    class_class_curie: ClassVar[str] = "dpv:NearlyGlobalScale"
    class_name: ClassVar[str] = "NearlyGlobalScale"
    class_model_uri: ClassVar[URIRef] = DPV.NearlyGlobalScale

    id: Union[str, NearlyGlobalScaleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NearlyGlobalScaleId):
            self.id = NearlyGlobalScaleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProcessingScale(Scale):
    """
    Scale of Processing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProcessingScale"]
    class_class_curie: ClassVar[str] = "dpv:ProcessingScale"
    class_name: ClassVar[str] = "ProcessingScale"
    class_model_uri: ClassVar[URIRef] = DPV.ProcessingScale

    id: Union[str, ProcessingScaleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessingScaleId):
            self.id = ProcessingScaleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LargeScaleProcessing(ProcessingScale):
    """
    Processing that takes place at large scales (as specified by some
    criteria)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LargeScaleProcessing"]
    class_class_curie: ClassVar[str] = "dpv:LargeScaleProcessing"
    class_name: ClassVar[str] = "LargeScaleProcessing"
    class_model_uri: ClassVar[URIRef] = DPV.LargeScaleProcessing

    id: Union[str, LargeScaleProcessingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LargeScaleProcessingId):
            self.id = LargeScaleProcessingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MediumScaleProcessing(ProcessingScale):
    """
    Processing that takes place at medium scales (as specified by some
    criteria)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["MediumScaleProcessing"]
    class_class_curie: ClassVar[str] = "dpv:MediumScaleProcessing"
    class_name: ClassVar[str] = "MediumScaleProcessing"
    class_model_uri: ClassVar[URIRef] = DPV.MediumScaleProcessing

    id: Union[str, MediumScaleProcessingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MediumScaleProcessingId):
            self.id = MediumScaleProcessingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RegionalScale(GeographicCoverage):
    """
    Geographic coverage spanning a specific region or regions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RegionalScale"]
    class_class_curie: ClassVar[str] = "dpv:RegionalScale"
    class_name: ClassVar[str] = "RegionalScale"
    class_model_uri: ClassVar[URIRef] = DPV.RegionalScale

    id: Union[str, RegionalScaleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RegionalScaleId):
            self.id = RegionalScaleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScientificResearch(ResearchAndDevelopment):
    """
    Purposes associated with scientific research
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ScientificResearch"]
    class_class_curie: ClassVar[str] = "dpv:ScientificResearch"
    class_name: ClassVar[str] = "ScientificResearch"
    class_model_uri: ClassVar[URIRef] = DPV.ScientificResearch

    id: Union[str, ScientificResearchId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientificResearchId):
            self.id = ScientificResearchId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScoringOfIndividuals(EvaluationScoring):
    """
    Processing that involves scoring of individuals
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ScoringOfIndividuals"]
    class_class_curie: ClassVar[str] = "dpv:ScoringOfIndividuals"
    class_name: ClassVar[str] = "ScoringOfIndividuals"
    class_model_uri: ClassVar[URIRef] = DPV.ScoringOfIndividuals

    id: Union[str, ScoringOfIndividualsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScoringOfIndividualsId):
            self.id = ScoringOfIndividualsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AutomatedScoringOfIndividuals(ScoringOfIndividuals):
    """
    Processing that involves automated scoring of individuals
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AutomatedScoringOfIndividuals"]
    class_class_curie: ClassVar[str] = "dpv:AutomatedScoringOfIndividuals"
    class_name: ClassVar[str] = "AutomatedScoringOfIndividuals"
    class_model_uri: ClassVar[URIRef] = DPV.AutomatedScoringOfIndividuals

    id: Union[str, AutomatedScoringOfIndividualsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AutomatedScoringOfIndividualsId):
            self.id = AutomatedScoringOfIndividualsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sector(DpvThing):
    """
    Sector describes the area of application or domain that indicates or
    restricts scope for interpretation and application of purpose e.g.
    Agriculture, Banking
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Sector"]
    class_class_curie: ClassVar[str] = "dpv:Sector"
    class_name: ClassVar[str] = "Sector"
    class_model_uri: ClassVar[URIRef] = DPV.Sector

    id: Union[str, SectorId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SectorId):
            self.id = SectorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ServiceManagement(Purpose):
    """
    Purposes associated with the management of services or products
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ServiceManagement"]
    class_class_curie: ClassVar[str] = "dpv:ServiceManagement"
    class_name: ClassVar[str] = "ServiceManagement"
    class_model_uri: ClassVar[URIRef] = DPV.ServiceManagement

    id: Union[str, ServiceManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceManagementId):
            self.id = ServiceManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PaymentManagement(ServiceManagement):
    """
    Purposes associated with processing and managing payment in relation to
    service, including invoicing and records
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PaymentManagement"]
    class_class_curie: ClassVar[str] = "dpv:PaymentManagement"
    class_name: ClassVar[str] = "PaymentManagement"
    class_model_uri: ClassVar[URIRef] = DPV.PaymentManagement

    id: Union[str, PaymentManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PaymentManagementId):
            self.id = PaymentManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RepairImpairments(ServiceManagement):
    """
    Purposes associated with identifying, rectifying, or otherwise
    undertaking activities intended to fix or repair impairments to existing
    functionalities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RepairImpairments"]
    class_class_curie: ClassVar[str] = "dpv:RepairImpairments"
    class_name: ClassVar[str] = "RepairImpairments"
    class_model_uri: ClassVar[URIRef] = DPV.RepairImpairments

    id: Union[str, RepairImpairmentsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RepairImpairmentsId):
            self.id = RepairImpairmentsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ServiceAccessDetermination(ServiceManagement):
    """
    Purposes associated with the determination of whether specific
    conditions or criteria are met for accessing, using, or gaining access
    to a service
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ServiceAccessDetermination"]
    class_class_curie: ClassVar[str] = "dpv:ServiceAccessDetermination"
    class_name: ClassVar[str] = "ServiceAccessDetermination"
    class_model_uri: ClassVar[URIRef] = DPV.ServiceAccessDetermination

    id: Union[str, ServiceAccessDeterminationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceAccessDeterminationId):
            self.id = ServiceAccessDeterminationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ServiceMonitoring(ServiceManagement):
    """
    Purposes associated with the monitoring of services or products to
    understand their performance and utilisation with a view to inform their
    management
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ServiceMonitoring"]
    class_class_curie: ClassVar[str] = "dpv:ServiceMonitoring"
    class_name: ClassVar[str] = "ServiceMonitoring"
    class_model_uri: ClassVar[URIRef] = DPV.ServiceMonitoring

    id: Union[str, ServiceMonitoringId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceMonitoringId):
            self.id = ServiceMonitoringId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ServiceOptimisation(ServiceManagement):
    """
    Purposes associated with optimisation of services or activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ServiceOptimisation"]
    class_class_curie: ClassVar[str] = "dpv:ServiceOptimisation"
    class_name: ClassVar[str] = "ServiceOptimisation"
    class_model_uri: ClassVar[URIRef] = DPV.ServiceOptimisation

    id: Union[str, ServiceOptimisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceOptimisationId):
            self.id = ServiceOptimisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptimisationForConsumer(ServiceOptimisation):
    """
    Purposes associated with optimisation of activities and services for
    consumer or user
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OptimisationForConsumer"]
    class_class_curie: ClassVar[str] = "dpv:OptimisationForConsumer"
    class_name: ClassVar[str] = "OptimisationForConsumer"
    class_model_uri: ClassVar[URIRef] = DPV.OptimisationForConsumer

    id: Union[str, OptimisationForConsumerId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OptimisationForConsumerId):
            self.id = OptimisationForConsumerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptimisationForController(ServiceOptimisation):
    """
    Purposes associated with optimisation of activities and services for
    provider or controller
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OptimisationForController"]
    class_class_curie: ClassVar[str] = "dpv:OptimisationForController"
    class_name: ClassVar[str] = "OptimisationForController"
    class_model_uri: ClassVar[URIRef] = DPV.OptimisationForController

    id: Union[str, OptimisationForControllerId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OptimisationForControllerId):
            self.id = OptimisationForControllerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImproveExistingProductsAndServices(OptimisationForController):
    """
    Purposes associated with improving existing products and services
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ImproveExistingProductsAndServices"]
    class_class_curie: ClassVar[str] = "dpv:ImproveExistingProductsAndServices"
    class_name: ClassVar[str] = "ImproveExistingProductsAndServices"
    class_model_uri: ClassVar[URIRef] = DPV.ImproveExistingProductsAndServices

    id: Union[str, ImproveExistingProductsAndServicesId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImproveExistingProductsAndServicesId):
            self.id = ImproveExistingProductsAndServicesId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IncreaseServiceRobustness(OptimisationForController):
    """
    Purposes associated with improving robustness and resilience of services
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["IncreaseServiceRobustness"]
    class_class_curie: ClassVar[str] = "dpv:IncreaseServiceRobustness"
    class_name: ClassVar[str] = "IncreaseServiceRobustness"
    class_model_uri: ClassVar[URIRef] = DPV.IncreaseServiceRobustness

    id: Union[str, IncreaseServiceRobustnessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IncreaseServiceRobustnessId):
            self.id = IncreaseServiceRobustnessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InternalResourceOptimisation(OptimisationForController):
    """
    Purposes associated with optimisation of internal resource availability
    and usage for organisation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InternalResourceOptimisation"]
    class_class_curie: ClassVar[str] = "dpv:InternalResourceOptimisation"
    class_name: ClassVar[str] = "InternalResourceOptimisation"
    class_model_uri: ClassVar[URIRef] = DPV.InternalResourceOptimisation

    id: Union[str, InternalResourceOptimisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InternalResourceOptimisationId):
            self.id = InternalResourceOptimisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptimiseUserInterface(OptimisationForConsumer):
    """
    Purposes associated with optimisation of interfaces presented to the
    user
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OptimiseUserInterface"]
    class_class_curie: ClassVar[str] = "dpv:OptimiseUserInterface"
    class_name: ClassVar[str] = "OptimiseUserInterface"
    class_model_uri: ClassVar[URIRef] = DPV.OptimiseUserInterface

    id: Union[str, OptimiseUserInterfaceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OptimiseUserInterfaceId):
            self.id = OptimiseUserInterfaceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ServicePersonalisation(Personalisation):
    """
    Purposes associated with providing personalisation within services or
    product or activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ServicePersonalisation"]
    class_class_curie: ClassVar[str] = "dpv:ServicePersonalisation"
    class_name: ClassVar[str] = "ServicePersonalisation"
    class_model_uri: ClassVar[URIRef] = DPV.ServicePersonalisation

    id: Union[str, ServicePersonalisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServicePersonalisationId):
            self.id = ServicePersonalisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonalisedBenefits(ServicePersonalisation):
    """
    Purposes associated with creating and providing personalised benefits
    for a service
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonalisedBenefits"]
    class_class_curie: ClassVar[str] = "dpv:PersonalisedBenefits"
    class_name: ClassVar[str] = "PersonalisedBenefits"
    class_model_uri: ClassVar[URIRef] = DPV.PersonalisedBenefits

    id: Union[str, PersonalisedBenefitsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonalisedBenefitsId):
            self.id = PersonalisedBenefitsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProvidePersonalisedRecommendations(ServicePersonalisation):
    """
    Purposes associated with creating and providing personalised
    recommendations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProvidePersonalisedRecommendations"]
    class_class_curie: ClassVar[str] = "dpv:ProvidePersonalisedRecommendations"
    class_name: ClassVar[str] = "ProvidePersonalisedRecommendations"
    class_model_uri: ClassVar[URIRef] = DPV.ProvidePersonalisedRecommendations

    id: Union[str, ProvidePersonalisedRecommendationsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProvidePersonalisedRecommendationsId):
            self.id = ProvidePersonalisedRecommendationsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProvideEventRecommendations(ProvidePersonalisedRecommendations):
    """
    Purposes associated with creating and providing personalised
    recommendations for events
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProvideEventRecommendations"]
    class_class_curie: ClassVar[str] = "dpv:ProvideEventRecommendations"
    class_name: ClassVar[str] = "ProvideEventRecommendations"
    class_model_uri: ClassVar[URIRef] = DPV.ProvideEventRecommendations

    id: Union[str, ProvideEventRecommendationsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProvideEventRecommendationsId):
            self.id = ProvideEventRecommendationsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProvideProductRecommendations(ProvidePersonalisedRecommendations):
    """
    Purposes associated with creating and providing product recommendations
    e.g. suggest similar products
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProvideProductRecommendations"]
    class_class_curie: ClassVar[str] = "dpv:ProvideProductRecommendations"
    class_name: ClassVar[str] = "ProvideProductRecommendations"
    class_model_uri: ClassVar[URIRef] = DPV.ProvideProductRecommendations

    id: Union[str, ProvideProductRecommendationsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProvideProductRecommendationsId):
            self.id = ProvideProductRecommendationsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ServiceProvision(ServiceManagement):
    """
    Purposes associated with providing service or product or activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ServiceProvision"]
    class_class_curie: ClassVar[str] = "dpv:ServiceProvision"
    class_name: ClassVar[str] = "ServiceProvision"
    class_model_uri: ClassVar[URIRef] = DPV.ServiceProvision

    id: Union[str, ServiceProvisionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceProvisionId):
            self.id = ServiceProvisionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequestedServiceProvision(ServiceProvision):
    """
    Purposes associated with delivering services as requested by user or
    consumer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RequestedServiceProvision"]
    class_class_curie: ClassVar[str] = "dpv:RequestedServiceProvision"
    class_name: ClassVar[str] = "RequestedServiceProvision"
    class_model_uri: ClassVar[URIRef] = DPV.RequestedServiceProvision

    id: Union[str, RequestedServiceProvisionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RequestedServiceProvisionId):
            self.id = RequestedServiceProvisionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DeliveryOfGoods(RequestedServiceProvision):
    """
    Purposes associated with delivering goods and services requested or
    asked by consumer
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DeliveryOfGoods"]
    class_class_curie: ClassVar[str] = "dpv:DeliveryOfGoods"
    class_name: ClassVar[str] = "DeliveryOfGoods"
    class_model_uri: ClassVar[URIRef] = DPV.DeliveryOfGoods

    id: Union[str, DeliveryOfGoodsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeliveryOfGoodsId):
            self.id = DeliveryOfGoodsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SearchFunctionalities(ServiceProvision):
    """
    Purposes associated with providing searching, querying, or other forms
    of information retrieval related functionalities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SearchFunctionalities"]
    class_class_curie: ClassVar[str] = "dpv:SearchFunctionalities"
    class_name: ClassVar[str] = "SearchFunctionalities"
    class_model_uri: ClassVar[URIRef] = DPV.SearchFunctionalities

    id: Union[str, SearchFunctionalitiesId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SearchFunctionalitiesId):
            self.id = SearchFunctionalitiesId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SellProducts(ServiceProvision):
    """
    Purposes associated with selling products or services
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SellProducts"]
    class_class_curie: ClassVar[str] = "dpv:SellProducts"
    class_name: ClassVar[str] = "SellProducts"
    class_model_uri: ClassVar[URIRef] = DPV.SellProducts

    id: Union[str, SellProductsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SellProductsId):
            self.id = SellProductsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SellDataToThirdParties(SellProducts):
    """
    Purposes associated with selling or sharing data or information to third
    parties
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SellDataToThirdParties"]
    class_class_curie: ClassVar[str] = "dpv:SellDataToThirdParties"
    class_name: ClassVar[str] = "SellDataToThirdParties"
    class_model_uri: ClassVar[URIRef] = DPV.SellDataToThirdParties

    id: Union[str, SellDataToThirdPartiesId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SellDataToThirdPartiesId):
            self.id = SellDataToThirdPartiesId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SellInsightsFromData(SellProducts):
    """
    Purposes associated with selling or sharing insights obtained from
    analysis of data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SellInsightsFromData"]
    class_class_curie: ClassVar[str] = "dpv:SellInsightsFromData"
    class_name: ClassVar[str] = "SellInsightsFromData"
    class_model_uri: ClassVar[URIRef] = DPV.SellInsightsFromData

    id: Union[str, SellInsightsFromDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SellInsightsFromDataId):
            self.id = SellInsightsFromDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SellProductsToDataSubject(SellProducts):
    """
    Purposes associated with selling products or services to the user,
    consumer, or data subjects
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SellProductsToDataSubject"]
    class_class_curie: ClassVar[str] = "dpv:SellProductsToDataSubject"
    class_name: ClassVar[str] = "SellProductsToDataSubject"
    class_model_uri: ClassVar[URIRef] = DPV.SellProductsToDataSubject

    id: Union[str, SellProductsToDataSubjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SellProductsToDataSubjectId):
            self.id = SellProductsToDataSubjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ServiceRegistration(ServiceManagement):
    """
    Purposes associated with registering users and collecting information
    required for providing a service
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ServiceRegistration"]
    class_class_curie: ClassVar[str] = "dpv:ServiceRegistration"
    class_name: ClassVar[str] = "ServiceRegistration"
    class_model_uri: ClassVar[URIRef] = DPV.ServiceRegistration

    id: Union[str, ServiceRegistrationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceRegistrationId):
            self.id = ServiceRegistrationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ServiceUsageAnalytics(ServiceMonitoring):
    """
    Purposes associated with conducting analysis and reporting related to
    usage of services or products
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ServiceUsageAnalytics"]
    class_class_curie: ClassVar[str] = "dpv:ServiceUsageAnalytics"
    class_name: ClassVar[str] = "ServiceUsageAnalytics"
    class_model_uri: ClassVar[URIRef] = DPV.ServiceUsageAnalytics

    id: Union[str, ServiceUsageAnalyticsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ServiceUsageAnalyticsId):
            self.id = ServiceUsageAnalyticsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Share(Disclose):
    """
    to give data (or a portion of it) to others
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Share"]
    class_class_curie: ClassVar[str] = "dpv:Share"
    class_name: ClassVar[str] = "Share"
    class_model_uri: ClassVar[URIRef] = DPV.Share

    id: Union[str, ShareId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ShareId):
            self.id = ShareId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SingularDataVolume(DataVolume):
    """
    Data volume that is considered singular i.e. a specific instance or
    single item
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SingularDataVolume"]
    class_class_curie: ClassVar[str] = "dpv:SingularDataVolume"
    class_name: ClassVar[str] = "SingularDataVolume"
    class_model_uri: ClassVar[URIRef] = DPV.SingularDataVolume

    id: Union[str, SingularDataVolumeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SingularDataVolumeId):
            self.id = SingularDataVolumeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SingularScaleOfDataSubjects(DataSubjectScale):
    """
    Scale of data subjects considered singular i.e. a specific data subject
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SingularScaleOfDataSubjects"]
    class_class_curie: ClassVar[str] = "dpv:SingularScaleOfDataSubjects"
    class_name: ClassVar[str] = "SingularScaleOfDataSubjects"
    class_model_uri: ClassVar[URIRef] = DPV.SingularScaleOfDataSubjects

    id: Union[str, SingularScaleOfDataSubjectsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SingularScaleOfDataSubjectsId):
            self.id = SingularScaleOfDataSubjectsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SmallDataVolume(DataVolume):
    """
    Data volume that is considered small or limited within the context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SmallDataVolume"]
    class_class_curie: ClassVar[str] = "dpv:SmallDataVolume"
    class_name: ClassVar[str] = "SmallDataVolume"
    class_model_uri: ClassVar[URIRef] = DPV.SmallDataVolume

    id: Union[str, SmallDataVolumeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SmallDataVolumeId):
            self.id = SmallDataVolumeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SmallScaleOfDataSubjects(DataSubjectScale):
    """
    Scale of data subjects considered small or limited within the context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SmallScaleOfDataSubjects"]
    class_class_curie: ClassVar[str] = "dpv:SmallScaleOfDataSubjects"
    class_name: ClassVar[str] = "SmallScaleOfDataSubjects"
    class_model_uri: ClassVar[URIRef] = DPV.SmallScaleOfDataSubjects

    id: Union[str, SmallScaleOfDataSubjectsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SmallScaleOfDataSubjectsId):
            self.id = SmallScaleOfDataSubjectsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SmallScaleProcessing(ProcessingScale):
    """
    Processing that takes place at small scales (as specified by some
    criteria)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SmallScaleProcessing"]
    class_class_curie: ClassVar[str] = "dpv:SmallScaleProcessing"
    class_name: ClassVar[str] = "SmallScaleProcessing"
    class_model_uri: ClassVar[URIRef] = DPV.SmallScaleProcessing

    id: Union[str, SmallScaleProcessingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SmallScaleProcessingId):
            self.id = SmallScaleProcessingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SocialMediaMarketing(Marketing):
    """
    Purposes associated with conducting marketing through social media
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SocialMediaMarketing"]
    class_class_curie: ClassVar[str] = "dpv:SocialMediaMarketing"
    class_name: ClassVar[str] = "SocialMediaMarketing"
    class_model_uri: ClassVar[URIRef] = DPV.SocialMediaMarketing

    id: Union[str, SocialMediaMarketingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SocialMediaMarketingId):
            self.id = SocialMediaMarketingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SporadicDataVolume(DataVolume):
    """
    Data volume that is considered sporadic or sparse within the context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SporadicDataVolume"]
    class_class_curie: ClassVar[str] = "dpv:SporadicDataVolume"
    class_name: ClassVar[str] = "SporadicDataVolume"
    class_model_uri: ClassVar[URIRef] = DPV.SporadicDataVolume

    id: Union[str, SporadicDataVolumeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SporadicDataVolumeId):
            self.id = SporadicDataVolumeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SporadicScaleOfDataSubjects(DataSubjectScale):
    """
    Scale of data subjects considered sporadic or sparse within the context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SporadicScaleOfDataSubjects"]
    class_class_curie: ClassVar[str] = "dpv:SporadicScaleOfDataSubjects"
    class_name: ClassVar[str] = "SporadicScaleOfDataSubjects"
    class_model_uri: ClassVar[URIRef] = DPV.SporadicScaleOfDataSubjects

    id: Union[str, SporadicScaleOfDataSubjectsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SporadicScaleOfDataSubjectsId):
            self.id = SporadicScaleOfDataSubjectsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StorageCondition(ProcessingCondition):
    """
    Conditions required or followed regarding storage of data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["StorageCondition"]
    class_class_curie: ClassVar[str] = "dpv:StorageCondition"
    class_name: ClassVar[str] = "StorageCondition"
    class_model_uri: ClassVar[URIRef] = DPV.StorageCondition

    id: Union[str, StorageConditionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StorageConditionId):
            self.id = StorageConditionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StorageDeletion(StorageCondition):
    """
    Deletion or Erasure of data including any deletion guarantees
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["StorageDeletion"]
    class_class_curie: ClassVar[str] = "dpv:StorageDeletion"
    class_name: ClassVar[str] = "StorageDeletion"
    class_model_uri: ClassVar[URIRef] = DPV.StorageDeletion

    id: Union[str, StorageDeletionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StorageDeletionId):
            self.id = StorageDeletionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StorageDuration(ProcessingDuration):
    """
    Duration or temporal limitation on storage of data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["StorageDuration"]
    class_class_curie: ClassVar[str] = "dpv:StorageDuration"
    class_name: ClassVar[str] = "StorageDuration"
    class_model_uri: ClassVar[URIRef] = DPV.StorageDuration

    id: Union[str, StorageDurationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StorageDurationId):
            self.id = StorageDurationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StorageLocation(ProcessingLocation):
    """
    Location or geospatial scope where the data is stored
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["StorageLocation"]
    class_class_curie: ClassVar[str] = "dpv:StorageLocation"
    class_name: ClassVar[str] = "StorageLocation"
    class_model_uri: ClassVar[URIRef] = DPV.StorageLocation

    id: Union[str, StorageLocationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StorageLocationId):
            self.id = StorageLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StorageRestoration(StorageCondition):
    """
    Regularity and temporal span of data restoration/backup mechanisms that
    guarantee that data is preserved
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["StorageRestoration"]
    class_class_curie: ClassVar[str] = "dpv:StorageRestoration"
    class_name: ClassVar[str] = "StorageRestoration"
    class_model_uri: ClassVar[URIRef] = DPV.StorageRestoration

    id: Union[str, StorageRestorationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StorageRestorationId):
            self.id = StorageRestorationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Store(Processing):
    """
    to keep data for future use
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Store"]
    class_class_curie: ClassVar[str] = "dpv:Store"
    class_name: ClassVar[str] = "Store"
    class_model_uri: ClassVar[URIRef] = DPV.Store

    id: Union[str, StoreId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StoreId):
            self.id = StoreId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Structure(Organise):
    """
    to arrange data according to a structure
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Structure"]
    class_class_curie: ClassVar[str] = "dpv:Structure"
    class_name: ClassVar[str] = "Structure"
    class_model_uri: ClassVar[URIRef] = DPV.Structure

    id: Union[str, StructureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StructureId):
            self.id = StructureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Format(Structure):
    """
    to arrange or structure data in a specific form
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Format"]
    class_class_curie: ClassVar[str] = "dpv:Format"
    class_name: ClassVar[str] = "Format"
    class_model_uri: ClassVar[URIRef] = DPV.Format

    id: Union[str, FormatId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FormatId):
            self.id = FormatId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reformat(Format):
    """
    to rearrange or restructure data to change its form
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Reformat"]
    class_class_curie: ClassVar[str] = "dpv:Reformat"
    class_name: ClassVar[str] = "Reformat"
    class_model_uri: ClassVar[URIRef] = DPV.Reformat

    id: Union[str, ReformatId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReformatId):
            self.id = ReformatId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SystematicMonitoring(ProcessingContext):
    """
    Processing that involves systematic monitoring of individuals
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SystematicMonitoring"]
    class_class_curie: ClassVar[str] = "dpv:SystematicMonitoring"
    class_name: ClassVar[str] = "SystematicMonitoring"
    class_model_uri: ClassVar[URIRef] = DPV.SystematicMonitoring

    id: Union[str, SystematicMonitoringId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SystematicMonitoringId):
            self.id = SystematicMonitoringId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TargetedAdvertising(PersonalisedAdvertising):
    """
    Purposes associated with creating and providing personalised
    advertisement where the personalisation is targeted to a specific
    individual or group of individuals
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["TargetedAdvertising"]
    class_class_curie: ClassVar[str] = "dpv:TargetedAdvertising"
    class_name: ClassVar[str] = "TargetedAdvertising"
    class_model_uri: ClassVar[URIRef] = DPV.TargetedAdvertising

    id: Union[str, TargetedAdvertisingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TargetedAdvertisingId):
            self.id = TargetedAdvertisingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TechnicalServiceProvision(ServiceProvision):
    """
    Purposes associated with managing and providing technical processes and
    functions necessary for delivering services
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["TechnicalServiceProvision"]
    class_class_curie: ClassVar[str] = "dpv:TechnicalServiceProvision"
    class_name: ClassVar[str] = "TechnicalServiceProvision"
    class_model_uri: ClassVar[URIRef] = DPV.TechnicalServiceProvision

    id: Union[str, TechnicalServiceProvisionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TechnicalServiceProvisionId):
            self.id = TechnicalServiceProvisionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Technology(DpvThing):
    """
    The technology, technological implementation, or any techniques, skills,
    methods, and processes used or applied
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Technology"]
    class_class_curie: ClassVar[str] = "dpv:Technology"
    class_name: ClassVar[str] = "Technology"
    class_model_uri: ClassVar[URIRef] = DPV.Technology

    id: Union[str, TechnologyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TechnologyId):
            self.id = TechnologyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThirdPartyDataSource(DataSource):
    """
    Data Sourced from a Third Party, e.g. when data is collected from an
    entity that is neither the Controller nor the Data Subject
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ThirdPartyDataSource"]
    class_class_curie: ClassVar[str] = "dpv:ThirdPartyDataSource"
    class_name: ClassVar[str] = "ThirdPartyDataSource"
    class_model_uri: ClassVar[URIRef] = DPV.ThirdPartyDataSource

    id: Union[str, ThirdPartyDataSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThirdPartyDataSourceId):
            self.id = ThirdPartyDataSourceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Transfer(Processing):
    """
    to move data from one place to another
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Transfer"]
    class_class_curie: ClassVar[str] = "dpv:Transfer"
    class_name: ClassVar[str] = "Transfer"
    class_model_uri: ClassVar[URIRef] = DPV.Transfer

    id: Union[str, TransferId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TransferId):
            self.id = TransferId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CrossBorderTransfer(Transfer):
    """
    to move data from one jurisdiction (border) to another
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CrossBorderTransfer"]
    class_class_curie: ClassVar[str] = "dpv:CrossBorderTransfer"
    class_name: ClassVar[str] = "CrossBorderTransfer"
    class_model_uri: ClassVar[URIRef] = DPV.CrossBorderTransfer

    id: Union[str, CrossBorderTransferId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CrossBorderTransferId):
            self.id = CrossBorderTransferId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Move(Transfer):
    """
    to move data from one location to another including deleting the
    original copy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Move"]
    class_class_curie: ClassVar[str] = "dpv:Move"
    class_name: ClassVar[str] = "Move"
    class_model_uri: ClassVar[URIRef] = DPV.Move

    id: Union[str, MoveId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MoveId):
            self.id = MoveId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Transform(Processing):
    """
    to change the form or nature of data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Transform"]
    class_class_curie: ClassVar[str] = "dpv:Transform"
    class_name: ClassVar[str] = "Transform"
    class_model_uri: ClassVar[URIRef] = DPV.Transform

    id: Union[str, TransformId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TransformId):
            self.id = TransformId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Adapt(Transform):
    """
    to modify the data, often rewritten into a new form for a new use
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Adapt"]
    class_class_curie: ClassVar[str] = "dpv:Adapt"
    class_name: ClassVar[str] = "Adapt"
    class_model_uri: ClassVar[URIRef] = DPV.Adapt

    id: Union[str, AdaptId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdaptId):
            self.id = AdaptId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Align(Transform):
    """
    to adjust the data to be in relation to another data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Align"]
    class_class_curie: ClassVar[str] = "dpv:Align"
    class_name: ClassVar[str] = "Align"
    class_model_uri: ClassVar[URIRef] = DPV.Align

    id: Union[str, AlignId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlignId):
            self.id = AlignId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Alter(Transform):
    """
    to change the data without changing it into something else
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Alter"]
    class_class_curie: ClassVar[str] = "dpv:Alter"
    class_name: ClassVar[str] = "Alter"
    class_model_uri: ClassVar[URIRef] = DPV.Alter

    id: Union[str, AlterId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlterId):
            self.id = AlterId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aggregate(Alter):
    """
    to aggregate data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Aggregate"]
    class_class_curie: ClassVar[str] = "dpv:Aggregate"
    class_name: ClassVar[str] = "Aggregate"
    class_model_uri: ClassVar[URIRef] = DPV.Aggregate

    id: Union[str, AggregateId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AggregateId):
            self.id = AggregateId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Anonymise(Transform):
    """
    to irreversibly alter personal data in such a way that an unique data
    subject can no longer be identified directly or indirectly or in
    combination with other data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Anonymise"]
    class_class_curie: ClassVar[str] = "dpv:Anonymise"
    class_name: ClassVar[str] = "Anonymise"
    class_model_uri: ClassVar[URIRef] = DPV.Anonymise

    id: Union[str, AnonymiseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnonymiseId):
            self.id = AnonymiseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Combine(Transform):
    """
    to join or merge data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Combine"]
    class_class_curie: ClassVar[str] = "dpv:Combine"
    class_name: ClassVar[str] = "Combine"
    class_model_uri: ClassVar[URIRef] = DPV.Combine

    id: Union[str, CombineId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CombineId):
            self.id = CombineId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Filter(Transform):
    """
    to filter or keep data for some criteria
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Filter"]
    class_class_curie: ClassVar[str] = "dpv:Filter"
    class_name: ClassVar[str] = "Filter"
    class_model_uri: ClassVar[URIRef] = DPV.Filter

    id: Union[str, FilterId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FilterId):
            self.id = FilterId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Modify(Alter):
    """
    to modify or change data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Modify"]
    class_class_curie: ClassVar[str] = "dpv:Modify"
    class_name: ClassVar[str] = "Modify"
    class_model_uri: ClassVar[URIRef] = DPV.Modify

    id: Union[str, ModifyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModifyId):
            self.id = ModifyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Pseudonymise(Transform):
    """
    to replace personal identifiable information by artificial identifiers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Pseudonymise"]
    class_class_curie: ClassVar[str] = "dpv:Pseudonymise"
    class_name: ClassVar[str] = "Pseudonymise"
    class_model_uri: ClassVar[URIRef] = DPV.Pseudonymise

    id: Union[str, PseudonymiseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PseudonymiseId):
            self.id = PseudonymiseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Restrict(Transform):
    """
    to apply a restriction on the processing of specific records
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Restrict"]
    class_class_curie: ClassVar[str] = "dpv:Restrict"
    class_name: ClassVar[str] = "Restrict"
    class_model_uri: ClassVar[URIRef] = DPV.Restrict

    id: Union[str, RestrictId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RestrictId):
            self.id = RestrictId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Screen(Transform):
    """
    to remove data for some criteria
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Screen"]
    class_class_curie: ClassVar[str] = "dpv:Screen"
    class_name: ClassVar[str] = "Screen"
    class_model_uri: ClassVar[URIRef] = DPV.Screen

    id: Union[str, ScreenId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScreenId):
            self.id = ScreenId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Transmit(Disclose):
    """
    to send out data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Transmit"]
    class_class_curie: ClassVar[str] = "dpv:Transmit"
    class_name: ClassVar[str] = "Transmit"
    class_model_uri: ClassVar[URIRef] = DPV.Transmit

    id: Union[str, TransmitId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TransmitId):
            self.id = TransmitId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Use(Processing):
    """
    to use data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Use"]
    class_class_curie: ClassVar[str] = "dpv:Use"
    class_name: ClassVar[str] = "Use"
    class_model_uri: ClassVar[URIRef] = DPV.Use

    id: Union[str, UseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UseId):
            self.id = UseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Access(Use):
    """
    to access data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Access"]
    class_class_curie: ClassVar[str] = "dpv:Access"
    class_name: ClassVar[str] = "Access"
    class_model_uri: ClassVar[URIRef] = DPV.Access

    id: Union[str, AccessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AccessId):
            self.id = AccessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Analyse(Use):
    """
    to study or examine the data in detail
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Analyse"]
    class_class_curie: ClassVar[str] = "dpv:Analyse"
    class_name: ClassVar[str] = "Analyse"
    class_model_uri: ClassVar[URIRef] = DPV.Analyse

    id: Union[str, AnalyseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalyseId):
            self.id = AnalyseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Assess(Use):
    """
    to assess data for some criteria
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Assess"]
    class_class_curie: ClassVar[str] = "dpv:Assess"
    class_name: ClassVar[str] = "Assess"
    class_model_uri: ClassVar[URIRef] = DPV.Assess

    id: Union[str, AssessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AssessId):
            self.id = AssessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Consult(Use):
    """
    to consult or query data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Consult"]
    class_class_curie: ClassVar[str] = "dpv:Consult"
    class_name: ClassVar[str] = "Consult"
    class_model_uri: ClassVar[URIRef] = DPV.Consult

    id: Union[str, ConsultId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsultId):
            self.id = ConsultId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Match(Use):
    """
    to combine, compare, or match data from different sources
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Match"]
    class_class_curie: ClassVar[str] = "dpv:Match"
    class_name: ClassVar[str] = "Match"
    class_model_uri: ClassVar[URIRef] = DPV.Match

    id: Union[str, MatchId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MatchId):
            self.id = MatchId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Monitor(Consult):
    """
    to monitor data for some criteria
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Monitor"]
    class_class_curie: ClassVar[str] = "dpv:Monitor"
    class_name: ClassVar[str] = "Monitor"
    class_model_uri: ClassVar[URIRef] = DPV.Monitor

    id: Union[str, MonitorId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MonitorId):
            self.id = MonitorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Profiling(Use):
    """
    to create a profile that describes or represents a person
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Profiling"]
    class_class_curie: ClassVar[str] = "dpv:Profiling"
    class_name: ClassVar[str] = "Profiling"
    class_model_uri: ClassVar[URIRef] = DPV.Profiling

    id: Union[str, ProfilingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProfilingId):
            self.id = ProfilingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Query(Consult):
    """
    to query or make enquiries over data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Query"]
    class_class_curie: ClassVar[str] = "dpv:Query"
    class_name: ClassVar[str] = "Query"
    class_model_uri: ClassVar[URIRef] = DPV.Query

    id: Union[str, QueryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QueryId):
            self.id = QueryId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Retrieve(Use):
    """
    to retrieve data, often in an automated manner
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Retrieve"]
    class_class_curie: ClassVar[str] = "dpv:Retrieve"
    class_name: ClassVar[str] = "Retrieve"
    class_model_uri: ClassVar[URIRef] = DPV.Retrieve

    id: Union[str, RetrieveId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RetrieveId):
            self.id = RetrieveId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tracking(Use):
    """
    to use data to track a specific factor (e.g. a human or their
    activities) across multiple distinct contexts
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Tracking"]
    class_class_curie: ClassVar[str] = "dpv:Tracking"
    class_name: ClassVar[str] = "Tracking"
    class_model_uri: ClassVar[URIRef] = DPV.Tracking

    id: Union[str, TrackingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TrackingId):
            self.id = TrackingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TrackingByFirstParty(Tracking):
    """
    to perform tracking where the performing entity is a first party within
    the context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["TrackingByFirstParty"]
    class_class_curie: ClassVar[str] = "dpv:TrackingByFirstParty"
    class_name: ClassVar[str] = "TrackingByFirstParty"
    class_model_uri: ClassVar[URIRef] = DPV.TrackingByFirstParty

    id: Union[str, TrackingByFirstPartyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TrackingByFirstPartyId):
            self.id = TrackingByFirstPartyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TrackingByThirdParty(Tracking):
    """
    to perform tracking where the performing entity is a third party within
    the context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["TrackingByThirdParty"]
    class_class_curie: ClassVar[str] = "dpv:TrackingByThirdParty"
    class_name: ClassVar[str] = "TrackingByThirdParty"
    class_model_uri: ClassVar[URIRef] = DPV.TrackingByThirdParty

    id: Union[str, TrackingByThirdPartyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TrackingByThirdPartyId):
            self.id = TrackingByThirdPartyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UserInterfacePersonalisation(ServicePersonalisation):
    """
    Purposes associated with personalisation of interfaces presented to the
    user
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["UserInterfacePersonalisation"]
    class_class_curie: ClassVar[str] = "dpv:UserInterfacePersonalisation"
    class_name: ClassVar[str] = "UserInterfacePersonalisation"
    class_model_uri: ClassVar[URIRef] = DPV.UserInterfacePersonalisation

    id: Union[str, UserInterfacePersonalisationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UserInterfacePersonalisationId):
            self.id = UserInterfacePersonalisationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VendorManagement(Purpose):
    """
    Purposes associated with manage orders, payment, evaluation, and
    prospecting related to vendors
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VendorManagement"]
    class_class_curie: ClassVar[str] = "dpv:VendorManagement"
    class_name: ClassVar[str] = "VendorManagement"
    class_model_uri: ClassVar[URIRef] = DPV.VendorManagement

    id: Union[str, VendorManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VendorManagementId):
            self.id = VendorManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VendorPayment(VendorManagement):
    """
    Purposes associated with managing payment of vendors
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VendorPayment"]
    class_class_curie: ClassVar[str] = "dpv:VendorPayment"
    class_name: ClassVar[str] = "VendorPayment"
    class_model_uri: ClassVar[URIRef] = DPV.VendorPayment

    id: Union[str, VendorPaymentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VendorPaymentId):
            self.id = VendorPaymentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VendorRecordsManagement(VendorManagement):
    """
    Purposes associated with managing records and orders related to vendors
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VendorRecordsManagement"]
    class_class_curie: ClassVar[str] = "dpv:VendorRecordsManagement"
    class_name: ClassVar[str] = "VendorRecordsManagement"
    class_model_uri: ClassVar[URIRef] = DPV.VendorRecordsManagement

    id: Union[str, VendorRecordsManagementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VendorRecordsManagementId):
            self.id = VendorRecordsManagementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VendorSelectionAssessment(VendorManagement):
    """
    Purposes associated with managing selection, assessment, and evaluation
    related to vendors
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VendorSelectionAssessment"]
    class_class_curie: ClassVar[str] = "dpv:VendorSelectionAssessment"
    class_name: ClassVar[str] = "VendorSelectionAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.VendorSelectionAssessment

    id: Union[str, VendorSelectionAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VendorSelectionAssessmentId):
            self.id = VendorSelectionAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Verification(EnforceSecurity):
    """
    Purposes association with verification e.g. information, identity,
    integrity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Verification"]
    class_class_curie: ClassVar[str] = "dpv:Verification"
    class_name: ClassVar[str] = "Verification"
    class_model_uri: ClassVar[URIRef] = DPV.Verification

    id: Union[str, VerificationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VerificationId):
            self.id = VerificationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AgeVerification(Verification):
    """
    Purposes associated with verifying or authenticating age or age related
    information as a form of security
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AgeVerification"]
    class_class_curie: ClassVar[str] = "dpv:AgeVerification"
    class_name: ClassVar[str] = "AgeVerification"
    class_model_uri: ClassVar[URIRef] = DPV.AgeVerification

    id: Union[str, AgeVerificationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgeVerificationId):
            self.id = AgeVerificationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdentityVerification(Verification):
    """
    Purposes associated with verifying or authenticating identity as a form
    of security
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["IdentityVerification"]
    class_class_curie: ClassVar[str] = "dpv:IdentityVerification"
    class_name: ClassVar[str] = "IdentityVerification"
    class_model_uri: ClassVar[URIRef] = DPV.IdentityVerification

    id: Union[str, IdentityVerificationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IdentityVerificationId):
            self.id = IdentityVerificationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WithdrawingFromProcess(EntityPermissiveInvolvement):
    """
    Involvement where entity can withdraw a previously given assent from
    specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["WithdrawingFromProcess"]
    class_class_curie: ClassVar[str] = "dpv:WithdrawingFromProcess"
    class_name: ClassVar[str] = "WithdrawingFromProcess"
    class_model_uri: ClassVar[URIRef] = DPV.WithdrawingFromProcess

    id: Union[str, WithdrawingFromProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WithdrawingFromProcessId):
            self.id = WithdrawingFromProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Likelihood(DpvThing):
    """
    The likelihood or probability or chance of something taking place or
    occurring
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Likelihood"]
    class_class_curie: ClassVar[str] = "dpv:Likelihood"
    class_name: ClassVar[str] = "Likelihood"
    class_model_uri: ClassVar[URIRef] = DPV.Likelihood

    id: Union[str, LikelihoodId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LikelihoodId):
            self.id = LikelihoodId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Notice(OrganisationalMeasure):
    """
    A notice is an artefact for providing information, choices, or controls
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Notice"]
    class_class_curie: ClassVar[str] = "dpv:Notice"
    class_name: ClassVar[str] = "Notice"
    class_model_uri: ClassVar[URIRef] = DPV.Notice

    id: Union[str, NoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoticeId):
            self.id = NoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AINotice(Notice):
    """
    A notice providing information regarding the particulars of an AI system
    such as its intended purpose and proper use
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AINotice"]
    class_class_curie: ClassVar[str] = "dpv:AINotice"
    class_name: ClassVar[str] = "AINotice"
    class_model_uri: ClassVar[URIRef] = DPV.AINotice

    id: Union[str, AINoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AINoticeId):
            self.id = AINoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DashboardNotice(Notice):
    """
    A notice that is provided within a dashboard also used for other
    purposes
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DashboardNotice"]
    class_class_curie: ClassVar[str] = "dpv:DashboardNotice"
    class_name: ClassVar[str] = "DashboardNotice"
    class_model_uri: ClassVar[URIRef] = DPV.DashboardNotice

    id: Union[str, DashboardNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DashboardNoticeId):
            self.id = DashboardNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataTransferNotice(Notice):
    """
    Notice for the legal entity for the transfer of its data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataTransferNotice"]
    class_class_curie: ClassVar[str] = "dpv:DataTransferNotice"
    class_name: ClassVar[str] = "DataTransferNotice"
    class_model_uri: ClassVar[URIRef] = DPV.DataTransferNotice

    id: Union[str, DataTransferNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataTransferNoticeId):
            self.id = DataTransferNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DeviceNotice(Notice):
    """
    A notice provided using the functionality provided by a device e.g.
    using the popup or alert feature
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DeviceNotice"]
    class_class_curie: ClassVar[str] = "dpv:DeviceNotice"
    class_name: ClassVar[str] = "DeviceNotice"
    class_model_uri: ClassVar[URIRef] = DPV.DeviceNotice

    id: Union[str, DeviceNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeviceNoticeId):
            self.id = DeviceNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GraphicalNotice(Notice):
    """
    A notice that uses graphical elements such as visualisations and icons
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["GraphicalNotice"]
    class_class_curie: ClassVar[str] = "dpv:GraphicalNotice"
    class_name: ClassVar[str] = "GraphicalNotice"
    class_model_uri: ClassVar[URIRef] = DPV.GraphicalNotice

    id: Union[str, GraphicalNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GraphicalNoticeId):
            self.id = GraphicalNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class JITNotice(Notice):
    """
    A notice that is provided "just in time" when collecting information or
    performing an activity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["JITNotice"]
    class_class_curie: ClassVar[str] = "dpv:JITNotice"
    class_name: ClassVar[str] = "JITNotice"
    class_model_uri: ClassVar[URIRef] = DPV.JITNotice

    id: Union[str, JITNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, JITNoticeId):
            self.id = JITNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LayeredNotice(Notice):
    """
    A notice that contains layered elements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LayeredNotice"]
    class_class_curie: ClassVar[str] = "dpv:LayeredNotice"
    class_name: ClassVar[str] = "LayeredNotice"
    class_model_uri: ClassVar[URIRef] = DPV.LayeredNotice

    id: Union[str, LayeredNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LayeredNoticeId):
            self.id = LayeredNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NoticeIcon(DpvThing):
    """
    An icon within a notice associated with specific information or elements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NoticeIcon"]
    class_class_curie: ClassVar[str] = "dpv:NoticeIcon"
    class_name: ClassVar[str] = "NoticeIcon"
    class_model_uri: ClassVar[URIRef] = DPV.NoticeIcon

    id: Union[str, NoticeIconId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoticeIconId):
            self.id = NoticeIconId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NoticeLayer(DpvThing):
    """
    A layer within a layered notice where the layer can be used for
    providing specific information or controls
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NoticeLayer"]
    class_class_curie: ClassVar[str] = "dpv:NoticeLayer"
    class_name: ClassVar[str] = "NoticeLayer"
    class_model_uri: ClassVar[URIRef] = DPV.NoticeLayer

    id: Union[str, NoticeLayerId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoticeLayerId):
            self.id = NoticeLayerId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NoticeStatus(Status):
    """
    Status associated with notice provision, use, and management
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NoticeStatus"]
    class_class_curie: ClassVar[str] = "dpv:NoticeStatus"
    class_name: ClassVar[str] = "NoticeStatus"
    class_model_uri: ClassVar[URIRef] = DPV.NoticeStatus

    id: Union[str, NoticeStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoticeStatusId):
            self.id = NoticeStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NoticeCommunicated(NoticeStatus):
    """
    Status indicating the notice has been communicated
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NoticeCommunicated"]
    class_class_curie: ClassVar[str] = "dpv:NoticeCommunicated"
    class_name: ClassVar[str] = "NoticeCommunicated"
    class_model_uri: ClassVar[URIRef] = DPV.NoticeCommunicated

    id: Union[str, NoticeCommunicatedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoticeCommunicatedId):
            self.id = NoticeCommunicatedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NoticeGenerated(NoticeStatus):
    """
    Status indicating the notice has been generated
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NoticeGenerated"]
    class_class_curie: ClassVar[str] = "dpv:NoticeGenerated"
    class_name: ClassVar[str] = "NoticeGenerated"
    class_model_uri: ClassVar[URIRef] = DPV.NoticeGenerated

    id: Union[str, NoticeGeneratedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoticeGeneratedId):
            self.id = NoticeGeneratedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NoticeLatest(NoticeStatus):
    """
    Status indicating the notice is currently at its latest iteration
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NoticeLatest"]
    class_class_curie: ClassVar[str] = "dpv:NoticeLatest"
    class_name: ClassVar[str] = "NoticeLatest"
    class_model_uri: ClassVar[URIRef] = DPV.NoticeLatest

    id: Union[str, NoticeLatestId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoticeLatestId):
            self.id = NoticeLatestId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NoticeStale(NoticeStatus):
    """
    Status indicating the notice is stale or not up to date or not the
    latest version
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NoticeStale"]
    class_class_curie: ClassVar[str] = "dpv:NoticeStale"
    class_name: ClassVar[str] = "NoticeStale"
    class_model_uri: ClassVar[URIRef] = DPV.NoticeStale

    id: Union[str, NoticeStaleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoticeStaleId):
            self.id = NoticeStaleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NoticeUnused(NoticeStatus):
    """
    Status indicating the notice has been communicated but has not yet been
    used e.g. the recipient has not acknowledged it or has not taken the
    intended action
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NoticeUnused"]
    class_class_curie: ClassVar[str] = "dpv:NoticeUnused"
    class_name: ClassVar[str] = "NoticeUnused"
    class_model_uri: ClassVar[URIRef] = DPV.NoticeUnused

    id: Union[str, NoticeUnusedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoticeUnusedId):
            self.id = NoticeUnusedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NoticeUpdated(NoticeStatus):
    """
    Status indicating the notice has been updated and its contents or
    implications have changed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NoticeUpdated"]
    class_class_curie: ClassVar[str] = "dpv:NoticeUpdated"
    class_name: ClassVar[str] = "NoticeUpdated"
    class_model_uri: ClassVar[URIRef] = DPV.NoticeUpdated

    id: Union[str, NoticeUpdatedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoticeUpdatedId):
            self.id = NoticeUpdatedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NoticeUsed(NoticeStatus):
    """
    Status indicating the notice has been communicated and has been used
    e.g. the recipient has acknowledged it or taken the intended action
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NoticeUsed"]
    class_class_curie: ClassVar[str] = "dpv:NoticeUsed"
    class_name: ClassVar[str] = "NoticeUsed"
    class_model_uri: ClassVar[URIRef] = DPV.NoticeUsed

    id: Union[str, NoticeUsedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NoticeUsedId):
            self.id = NoticeUsedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OralNotice(Notice):
    """
    A notice provided orally or verbally
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OralNotice"]
    class_class_curie: ClassVar[str] = "dpv:OralNotice"
    class_name: ClassVar[str] = "OralNotice"
    class_model_uri: ClassVar[URIRef] = DPV.OralNotice

    id: Union[str, OralNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OralNoticeId):
            self.id = OralNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PostedNotice(Notice):
    """
    A notice that is posted as a sign or banner
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PostedNotice"]
    class_class_curie: ClassVar[str] = "dpv:PostedNotice"
    class_name: ClassVar[str] = "PostedNotice"
    class_model_uri: ClassVar[URIRef] = DPV.PostedNotice

    id: Union[str, PostedNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PostedNoticeId):
            self.id = PostedNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrintedNotice(Notice):
    """
    A notice that is provided in a printed form on or along with a device
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PrintedNotice"]
    class_class_curie: ClassVar[str] = "dpv:PrintedNotice"
    class_name: ClassVar[str] = "PrintedNotice"
    class_model_uri: ClassVar[URIRef] = DPV.PrintedNotice

    id: Union[str, PrintedNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrintedNoticeId):
            self.id = PrintedNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrivacyNotice(Notice):
    """
    Represents a notice or document outlining information regarding privacy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PrivacyNotice"]
    class_class_curie: ClassVar[str] = "dpv:PrivacyNotice"
    class_name: ClassVar[str] = "PrivacyNotice"
    class_model_uri: ClassVar[URIRef] = DPV.PrivacyNotice

    id: Union[str, PrivacyNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrivacyNoticeId):
            self.id = PrivacyNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentNotice(PrivacyNotice):
    """
    A Notice for information provision associated with Consent
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentNotice"]
    class_class_curie: ClassVar[str] = "dpv:ConsentNotice"
    class_name: ClassVar[str] = "ConsentNotice"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentNotice

    id: Union[str, ConsentNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentNoticeId):
            self.id = ConsentNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskAssessment(Assessment):
    """
    Assessment involving identification, analysis, and evaluation of risk
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RiskAssessment"]
    class_class_curie: ClassVar[str] = "dpv:RiskAssessment"
    class_name: ClassVar[str] = "RiskAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.RiskAssessment

    id: Union[str, RiskAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RiskAssessmentId):
            self.id = RiskAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImpactAssessment(RiskAssessment):
    """
    Calculating or determining the likelihood of impact of an existing or
    proposed process, which can involve risks or detriments.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ImpactAssessment"]
    class_class_curie: ClassVar[str] = "dpv:ImpactAssessment"
    class_name: ClassVar[str] = "ImpactAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.ImpactAssessment

    id: Union[str, ImpactAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImpactAssessmentId):
            self.id = ImpactAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReviewImpactAssessment(ImpactAssessment):
    """
    Procedures to review impact assessments in terms of continued validity,
    adequacy for intended purposes, and conformance of processes with
    findings
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ReviewImpactAssessment"]
    class_class_curie: ClassVar[str] = "dpv:ReviewImpactAssessment"
    class_name: ClassVar[str] = "ReviewImpactAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.ReviewImpactAssessment

    id: Union[str, ReviewImpactAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReviewImpactAssessmentId):
            self.id = ReviewImpactAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataTransferImpactAssessment(ImpactAssessment):
    """
    Impact Assessment for conducting data transfers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataTransferImpactAssessment"]
    class_class_curie: ClassVar[str] = "dpv:DataTransferImpactAssessment"
    class_name: ClassVar[str] = "DataTransferImpactAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.DataTransferImpactAssessment

    id: Union[str, DataTransferImpactAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataTransferImpactAssessmentId):
            self.id = DataTransferImpactAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PIA(ImpactAssessment):
    """
    Impact assessment regarding privacy risks
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PIA"]
    class_class_curie: ClassVar[str] = "dpv:PIA"
    class_name: ClassVar[str] = "PIA"
    class_model_uri: ClassVar[URIRef] = DPV.PIA

    id: Union[str, PIAId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PIAId):
            self.id = PIAId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RightsImpactAssessment(ImpactAssessment):
    """
    Impact assessment which involves determining the impact on rights and
    freedoms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RightsImpactAssessment"]
    class_class_curie: ClassVar[str] = "dpv:RightsImpactAssessment"
    class_name: ClassVar[str] = "RightsImpactAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.RightsImpactAssessment

    id: Union[str, RightsImpactAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RightsImpactAssessmentId):
            self.id = RightsImpactAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DPIA(RightsImpactAssessment):
    """
    Impact assessment determining the potential and actual impact of
    processing activities on individuals or groups of individuals and taking
    into account the impacts of activities on their rights and freedoms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DPIA"]
    class_class_curie: ClassVar[str] = "dpv:DPIA"
    class_name: ClassVar[str] = "DPIA"
    class_model_uri: ClassVar[URIRef] = DPV.DPIA

    id: Union[str, DPIAId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DPIAId):
            self.id = DPIAId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataBreachImpactAssessment(RightsImpactAssessment):
    """
    Impact Assessment concerning the consequences and impacts of a data
    breach
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataBreachImpactAssessment"]
    class_class_curie: ClassVar[str] = "dpv:DataBreachImpactAssessment"
    class_name: ClassVar[str] = "DataBreachImpactAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.DataBreachImpactAssessment

    id: Union[str, DataBreachImpactAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataBreachImpactAssessmentId):
            self.id = DataBreachImpactAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FRIA(RightsImpactAssessment):
    """
    Impact assessment which assesses the potential and actual impact on
    fundamental rights occurring due to processing activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FRIA"]
    class_class_curie: ClassVar[str] = "dpv:FRIA"
    class_name: ClassVar[str] = "FRIA"
    class_model_uri: ClassVar[URIRef] = DPV.FRIA

    id: Union[str, FRIAId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FRIAId):
            self.id = FRIAId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskConcept(DpvThing):
    """
    Parent concept for combining concepts associated with risk assessment
    such as actual and potential Risk, Risk Source, Consequences, and
    Impacts
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RiskConcept"]
    class_class_curie: ClassVar[str] = "dpv:RiskConcept"
    class_name: ClassVar[str] = "RiskConcept"
    class_model_uri: ClassVar[URIRef] = DPV.RiskConcept

    id: Union[str, RiskConceptId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RiskConceptId):
            self.id = RiskConceptId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Consequence(RiskConcept):
    """
    The consequence(s) possible or arising from specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Consequence"]
    class_class_curie: ClassVar[str] = "dpv:Consequence"
    class_name: ClassVar[str] = "Consequence"
    class_model_uri: ClassVar[URIRef] = DPV.Consequence

    id: Union[str, ConsequenceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsequenceId):
            self.id = ConsequenceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsequenceAsSideEffect(Consequence):
    """
    The consequence(s) possible or arising as a side-effect of specified
    context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsequenceAsSideEffect"]
    class_class_curie: ClassVar[str] = "dpv:ConsequenceAsSideEffect"
    class_name: ClassVar[str] = "ConsequenceAsSideEffect"
    class_model_uri: ClassVar[URIRef] = DPV.ConsequenceAsSideEffect

    id: Union[str, ConsequenceAsSideEffectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsequenceAsSideEffectId):
            self.id = ConsequenceAsSideEffectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsequenceOfFailure(Consequence):
    """
    The consequence(s) possible or arising from failure of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsequenceOfFailure"]
    class_class_curie: ClassVar[str] = "dpv:ConsequenceOfFailure"
    class_name: ClassVar[str] = "ConsequenceOfFailure"
    class_model_uri: ClassVar[URIRef] = DPV.ConsequenceOfFailure

    id: Union[str, ConsequenceOfFailureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsequenceOfFailureId):
            self.id = ConsequenceOfFailureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsequenceOfSuccess(Consequence):
    """
    The consequence(s) possible or arising from success of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsequenceOfSuccess"]
    class_class_curie: ClassVar[str] = "dpv:ConsequenceOfSuccess"
    class_name: ClassVar[str] = "ConsequenceOfSuccess"
    class_model_uri: ClassVar[URIRef] = DPV.ConsequenceOfSuccess

    id: Union[str, ConsequenceOfSuccessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsequenceOfSuccessId):
            self.id = ConsequenceOfSuccessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Impact(Consequence):
    """
    The impact(s) possible or arising as a consequence from specified
    context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Impact"]
    class_class_curie: ClassVar[str] = "dpv:Impact"
    class_name: ClassVar[str] = "Impact"
    class_model_uri: ClassVar[URIRef] = DPV.Impact

    id: Union[str, ImpactId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImpactId):
            self.id = ImpactId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Risk(RiskConcept):
    """
    A risk or possibility or uncertainty of negative effects, impacts, or
    consequences
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Risk"]
    class_class_curie: ClassVar[str] = "dpv:Risk"
    class_name: ClassVar[str] = "Risk"
    class_model_uri: ClassVar[URIRef] = DPV.Risk

    id: Union[str, RiskId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RiskId):
            self.id = RiskId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResidualRisk(Risk):
    """
    Risk remaining after treatment or mitigation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ResidualRisk"]
    class_class_curie: ClassVar[str] = "dpv:ResidualRisk"
    class_name: ClassVar[str] = "ResidualRisk"
    class_model_uri: ClassVar[URIRef] = DPV.ResidualRisk

    id: Union[str, ResidualRiskId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResidualRiskId):
            self.id = ResidualRiskId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskLevel(DpvThing):
    """
    The magnitude of a risk expressed as an indication to aid in its
    management
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RiskLevel"]
    class_class_curie: ClassVar[str] = "dpv:RiskLevel"
    class_name: ClassVar[str] = "RiskLevel"
    class_model_uri: ClassVar[URIRef] = DPV.RiskLevel

    id: Union[str, RiskLevelId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RiskLevelId):
            self.id = RiskLevelId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskMitigationMeasure(TechnicalOrganisationalMeasure):
    """
    Measures intended to mitigate, minimise, or prevent risk.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RiskMitigationMeasure"]
    class_class_curie: ClassVar[str] = "dpv:RiskMitigationMeasure"
    class_name: ClassVar[str] = "RiskMitigationMeasure"
    class_model_uri: ClassVar[URIRef] = DPV.RiskMitigationMeasure

    id: Union[str, RiskMitigationMeasureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RiskMitigationMeasureId):
            self.id = RiskMitigationMeasureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecurityAssessment(RiskAssessment):
    """
    Assessment of security intended to identify gaps, vulnerabilities,
    risks, and effectiveness of controls
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SecurityAssessment"]
    class_class_curie: ClassVar[str] = "dpv:SecurityAssessment"
    class_name: ClassVar[str] = "SecurityAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.SecurityAssessment

    id: Union[str, SecurityAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecurityAssessmentId):
            self.id = SecurityAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CybersecurityAssessment(SecurityAssessment):
    """
    Assessment of cybersecurity capabilities in terms of vulnerabilities and
    effectiveness of controls
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["CybersecurityAssessment"]
    class_class_curie: ClassVar[str] = "dpv:CybersecurityAssessment"
    class_name: ClassVar[str] = "CybersecurityAssessment"
    class_model_uri: ClassVar[URIRef] = DPV.CybersecurityAssessment

    id: Union[str, CybersecurityAssessmentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CybersecurityAssessmentId):
            self.id = CybersecurityAssessmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecurityIncidentNotice(Notice):
    """
    A notice providing information about security incident(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SecurityIncidentNotice"]
    class_class_curie: ClassVar[str] = "dpv:SecurityIncidentNotice"
    class_name: ClassVar[str] = "SecurityIncidentNotice"
    class_model_uri: ClassVar[URIRef] = DPV.SecurityIncidentNotice

    id: Union[str, SecurityIncidentNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecurityIncidentNoticeId):
            self.id = SecurityIncidentNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataBreachNotice(SecurityIncidentNotice):
    """
    A notice providing information about data breach(es) i.e. unauthorised
    transfer, access, use, or modification of data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataBreachNotice"]
    class_class_curie: ClassVar[str] = "dpv:DataBreachNotice"
    class_name: ClassVar[str] = "DataBreachNotice"
    class_model_uri: ClassVar[URIRef] = DPV.DataBreachNotice

    id: Union[str, DataBreachNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataBreachNoticeId):
            self.id = DataBreachNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Severity(DpvThing):
    """
    The magnitude of being unwanted or having negative effects such as
    harmful impacts
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Severity"]
    class_class_curie: ClassVar[str] = "dpv:Severity"
    class_name: ClassVar[str] = "Severity"
    class_model_uri: ClassVar[URIRef] = DPV.Severity

    id: Union[str, SeverityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SeverityId):
            self.id = SeverityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SensitivityLevel(Severity):
    """
    Sensitivity' reflects the risk of impact if not secured or utilised with
    appropriate measures and controls e.g. for sensitive data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SensitivityLevel"]
    class_class_curie: ClassVar[str] = "dpv:SensitivityLevel"
    class_name: ClassVar[str] = "SensitivityLevel"
    class_model_uri: ClassVar[URIRef] = DPV.SensitivityLevel

    id: Union[str, SensitivityLevelId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SensitivityLevelId):
            self.id = SensitivityLevelId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Right(DpvThing):
    """
    The right(s) applicable, provided, or expected
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Right"]
    class_class_curie: ClassVar[str] = "dpv:Right"
    class_name: ClassVar[str] = "Right"
    class_model_uri: ClassVar[URIRef] = DPV.Right

    id: Union[str, RightId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RightId):
            self.id = RightId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActiveRight(Right):
    """
    The right(s) applicable, provided, or expected that need to be
    (actively) exercised
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ActiveRight"]
    class_class_curie: ClassVar[str] = "dpv:ActiveRight"
    class_name: ClassVar[str] = "ActiveRight"
    class_model_uri: ClassVar[URIRef] = DPV.ActiveRight

    id: Union[str, ActiveRightId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActiveRightId):
            self.id = ActiveRightId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSubjectRight(Right):
    """
    The rights applicable or provided to a Data Subject
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSubjectRight"]
    class_class_curie: ClassVar[str] = "dpv:DataSubjectRight"
    class_name: ClassVar[str] = "DataSubjectRight"
    class_model_uri: ClassVar[URIRef] = DPV.DataSubjectRight

    id: Union[str, DataSubjectRightId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSubjectRightId):
            self.id = DataSubjectRightId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PassiveRight(Right):
    """
    The right(s) applicable, provided, or expected that are always
    (passively) applicable
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PassiveRight"]
    class_class_curie: ClassVar[str] = "dpv:PassiveRight"
    class_name: ClassVar[str] = "PassiveRight"
    class_model_uri: ClassVar[URIRef] = DPV.PassiveRight

    id: Union[str, PassiveRightId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PassiveRightId):
            self.id = PassiveRightId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RightExerciseActivity(OrganisationalMeasure):
    """
    An activity representing an exercising of an active right
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RightExerciseActivity"]
    class_class_curie: ClassVar[str] = "dpv:RightExerciseActivity"
    class_name: ClassVar[str] = "RightExerciseActivity"
    class_model_uri: ClassVar[URIRef] = DPV.RightExerciseActivity

    id: Union[str, RightExerciseActivityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RightExerciseActivityId):
            self.id = RightExerciseActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RightExerciseRecord(RecordsOfActivities):
    """
    Record of a Right being exercised
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RightExerciseRecord"]
    class_class_curie: ClassVar[str] = "dpv:RightExerciseRecord"
    class_name: ClassVar[str] = "RightExerciseRecord"
    class_model_uri: ClassVar[URIRef] = DPV.RightExerciseRecord

    id: Union[str, RightExerciseRecordId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RightExerciseRecordId):
            self.id = RightExerciseRecordId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RightNotice(Notice):
    """
    Information associated with rights, such as which rights exist, when and
    where they are applicable, and other relevant information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RightNotice"]
    class_class_curie: ClassVar[str] = "dpv:RightNotice"
    class_name: ClassVar[str] = "RightNotice"
    class_model_uri: ClassVar[URIRef] = DPV.RightNotice

    id: Union[str, RightNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RightNoticeId):
            self.id = RightNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RightExerciseNotice(RightNotice):
    """
    Information associated with exercising of an active right such as where
    and how to exercise the right, information required for it, or updates
    on an exercised rights request
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RightExerciseNotice"]
    class_class_curie: ClassVar[str] = "dpv:RightExerciseNotice"
    class_name: ClassVar[str] = "RightExerciseNotice"
    class_model_uri: ClassVar[URIRef] = DPV.RightExerciseNotice

    id: Union[str, RightExerciseNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RightExerciseNoticeId):
            self.id = RightExerciseNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RightFulfilmentNotice(RightExerciseNotice):
    """
    Notice provided regarding fulfilment of a right
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RightFulfilmentNotice"]
    class_class_curie: ClassVar[str] = "dpv:RightFulfilmentNotice"
    class_name: ClassVar[str] = "RightFulfilmentNotice"
    class_model_uri: ClassVar[URIRef] = DPV.RightFulfilmentNotice

    id: Union[str, RightFulfilmentNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RightFulfilmentNoticeId):
            self.id = RightFulfilmentNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RightNonFulfilmentNotice(RightExerciseNotice):
    """
    Notice provided regarding non-fulfilment of a right
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RightNonFulfilmentNotice"]
    class_class_curie: ClassVar[str] = "dpv:RightNonFulfilmentNotice"
    class_name: ClassVar[str] = "RightNonFulfilmentNotice"
    class_model_uri: ClassVar[URIRef] = DPV.RightNonFulfilmentNotice

    id: Union[str, RightNonFulfilmentNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RightNonFulfilmentNoticeId):
            self.id = RightNonFulfilmentNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentControl(EntityInvolvement):
    """
    The control or activity associated with obtaining, providing,
    withdrawing, or reaffirming consent
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentControl"]
    class_class_curie: ClassVar[str] = "dpv:ConsentControl"
    class_name: ClassVar[str] = "ConsentControl"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentControl

    id: Union[str, ConsentControlId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentControlId):
            self.id = ConsentControlId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentStatus(Status):
    """
    The state or status of 'consent' that provides information reflecting
    its operational status and validity for processing data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentStatus"]
    class_class_curie: ClassVar[str] = "dpv:ConsentStatus"
    class_name: ClassVar[str] = "ConsentStatus"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentStatus

    id: Union[str, ConsentStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentStatusId):
            self.id = ConsentStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentStatusInvalidForProcessing(ConsentStatus):
    """
    States of consent that cannot be used as valid justifications for
    processing data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentStatusInvalidForProcessing"]
    class_class_curie: ClassVar[str] = "dpv:ConsentStatusInvalidForProcessing"
    class_name: ClassVar[str] = "ConsentStatusInvalidForProcessing"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentStatusInvalidForProcessing

    id: Union[str, ConsentStatusInvalidForProcessingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentStatusInvalidForProcessingId):
            self.id = ConsentStatusInvalidForProcessingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentExpired(ConsentStatusInvalidForProcessing):
    """
    The state where the temporal or contextual validity of consent has
    'expired'
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentExpired"]
    class_class_curie: ClassVar[str] = "dpv:ConsentExpired"
    class_name: ClassVar[str] = "ConsentExpired"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentExpired

    id: Union[str, ConsentExpiredId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentExpiredId):
            self.id = ConsentExpiredId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentInvalidated(ConsentStatusInvalidForProcessing):
    """
    The state where consent has been deemed to be invalid
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentInvalidated"]
    class_class_curie: ClassVar[str] = "dpv:ConsentInvalidated"
    class_name: ClassVar[str] = "ConsentInvalidated"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentInvalidated

    id: Union[str, ConsentInvalidatedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentInvalidatedId):
            self.id = ConsentInvalidatedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentRefused(ConsentStatusInvalidForProcessing):
    """
    The state where consent has been refused
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentRefused"]
    class_class_curie: ClassVar[str] = "dpv:ConsentRefused"
    class_name: ClassVar[str] = "ConsentRefused"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentRefused

    id: Union[str, ConsentRefusedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentRefusedId):
            self.id = ConsentRefusedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentRequestDeferred(ConsentStatusInvalidForProcessing):
    """
    State where a request for consent has been deferred without a decision
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentRequestDeferred"]
    class_class_curie: ClassVar[str] = "dpv:ConsentRequestDeferred"
    class_name: ClassVar[str] = "ConsentRequestDeferred"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentRequestDeferred

    id: Union[str, ConsentRequestDeferredId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentRequestDeferredId):
            self.id = ConsentRequestDeferredId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentRequested(ConsentStatusInvalidForProcessing):
    """
    State where a request for consent has been made and is awaiting a
    decision
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentRequested"]
    class_class_curie: ClassVar[str] = "dpv:ConsentRequested"
    class_name: ClassVar[str] = "ConsentRequested"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentRequested

    id: Union[str, ConsentRequestedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentRequestedId):
            self.id = ConsentRequestedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentRevoked(ConsentStatusInvalidForProcessing):
    """
    The state where the consent is revoked by an entity other than the data
    subject and which prevents it from being further used as a valid state
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentRevoked"]
    class_class_curie: ClassVar[str] = "dpv:ConsentRevoked"
    class_name: ClassVar[str] = "ConsentRevoked"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentRevoked

    id: Union[str, ConsentRevokedId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentRevokedId):
            self.id = ConsentRevokedId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentStatusValidForProcessing(ConsentStatus):
    """
    States of consent that can be used as valid justifications for
    processing data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentStatusValidForProcessing"]
    class_class_curie: ClassVar[str] = "dpv:ConsentStatusValidForProcessing"
    class_name: ClassVar[str] = "ConsentStatusValidForProcessing"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentStatusValidForProcessing

    id: Union[str, ConsentStatusValidForProcessingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentStatusValidForProcessingId):
            self.id = ConsentStatusValidForProcessingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentGiven(ConsentStatusValidForProcessing):
    """
    The state where consent has been given
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentGiven"]
    class_class_curie: ClassVar[str] = "dpv:ConsentGiven"
    class_name: ClassVar[str] = "ConsentGiven"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentGiven

    id: Union[str, ConsentGivenId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentGivenId):
            self.id = ConsentGivenId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentUnknown(ConsentStatusInvalidForProcessing):
    """
    State where information about consent is not available or is unknown
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentUnknown"]
    class_class_curie: ClassVar[str] = "dpv:ConsentUnknown"
    class_name: ClassVar[str] = "ConsentUnknown"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentUnknown

    id: Union[str, ConsentUnknownId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentUnknownId):
            self.id = ConsentUnknownId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConsentWithdrawn(ConsentStatusInvalidForProcessing):
    """
    The state where the consent is withdrawn or revoked specifically by the
    data subject and which prevents it from being further used as a valid
    state
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentWithdrawn"]
    class_class_curie: ClassVar[str] = "dpv:ConsentWithdrawn"
    class_name: ClassVar[str] = "ConsentWithdrawn"
    class_model_uri: ClassVar[URIRef] = DPV.ConsentWithdrawn

    id: Union[str, ConsentWithdrawnId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConsentWithdrawnId):
            self.id = ConsentWithdrawnId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InformedConsent(Consent):
    """
    Consent that is informed i.e. with the requirement to provide sufficient
    information to make a consenting decision
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InformedConsent"]
    class_class_curie: ClassVar[str] = "dpv:InformedConsent"
    class_name: ClassVar[str] = "InformedConsent"
    class_model_uri: ClassVar[URIRef] = DPV.InformedConsent

    id: Union[str, InformedConsentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformedConsentId):
            self.id = InformedConsentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExpressedConsent(InformedConsent):
    """
    Consent that is expressed through an action intended to convey a
    consenting decision
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ExpressedConsent"]
    class_class_curie: ClassVar[str] = "dpv:ExpressedConsent"
    class_name: ClassVar[str] = "ExpressedConsent"
    class_model_uri: ClassVar[URIRef] = DPV.ExpressedConsent

    id: Union[str, ExpressedConsentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExpressedConsentId):
            self.id = ExpressedConsentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExplicitlyExpressedConsent(ExpressedConsent):
    """
    Consent that is expressed through an explicit action solely conveying a
    consenting decision
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ExplicitlyExpressedConsent"]
    class_class_curie: ClassVar[str] = "dpv:ExplicitlyExpressedConsent"
    class_name: ClassVar[str] = "ExplicitlyExpressedConsent"
    class_model_uri: ClassVar[URIRef] = DPV.ExplicitlyExpressedConsent

    id: Union[str, ExplicitlyExpressedConsentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExplicitlyExpressedConsentId):
            self.id = ExplicitlyExpressedConsentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImpliedConsent(InformedConsent):
    """
    Consent that is implied indirectly through an action not associated
    solely with conveying a consenting decision
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ImpliedConsent"]
    class_class_curie: ClassVar[str] = "dpv:ImpliedConsent"
    class_name: ClassVar[str] = "ImpliedConsent"
    class_model_uri: ClassVar[URIRef] = DPV.ImpliedConsent

    id: Union[str, ImpliedConsentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImpliedConsentId):
            self.id = ImpliedConsentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ObtainConsent(ConsentControl):
    """
    Control for obtaining consent
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ObtainConsent"]
    class_class_curie: ClassVar[str] = "dpv:ObtainConsent"
    class_name: ClassVar[str] = "ObtainConsent"
    class_model_uri: ClassVar[URIRef] = DPV.ObtainConsent

    id: Union[str, ObtainConsentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ObtainConsentId):
            self.id = ObtainConsentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProvideConsent(ConsentControl):
    """
    Control for providing consent
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProvideConsent"]
    class_class_curie: ClassVar[str] = "dpv:ProvideConsent"
    class_name: ClassVar[str] = "ProvideConsent"
    class_model_uri: ClassVar[URIRef] = DPV.ProvideConsent

    id: Union[str, ProvideConsentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProvideConsentId):
            self.id = ProvideConsentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ManageConsent(ProvideConsent):
    """
    Control for managing a given consent in terms of providing, reaffirming,
    or withdrawing it
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ManageConsent"]
    class_class_curie: ClassVar[str] = "dpv:ManageConsent"
    class_name: ClassVar[str] = "ManageConsent"
    class_model_uri: ClassVar[URIRef] = DPV.ManageConsent

    id: Union[str, ManageConsentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ManageConsentId):
            self.id = ManageConsentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReaffirmConsent(ConsentControl):
    """
    Control for affirming consent
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ReaffirmConsent"]
    class_class_curie: ClassVar[str] = "dpv:ReaffirmConsent"
    class_name: ClassVar[str] = "ReaffirmConsent"
    class_model_uri: ClassVar[URIRef] = DPV.ReaffirmConsent

    id: Union[str, ReaffirmConsentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReaffirmConsentId):
            self.id = ReaffirmConsentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RefuseConsent(ConsentControl):
    """
    Control for refusing consent
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RefuseConsent"]
    class_class_curie: ClassVar[str] = "dpv:RefuseConsent"
    class_name: ClassVar[str] = "RefuseConsent"
    class_model_uri: ClassVar[URIRef] = DPV.RefuseConsent

    id: Union[str, RefuseConsentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RefuseConsentId):
            self.id = RefuseConsentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RenewedConsentGiven(ConsentStatusValidForProcessing):
    """
    The state where a previously given consent has been 'renewed' or
    'refreshed' or 'reaffirmed' to form a new instance of given consent
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RenewedConsentGiven"]
    class_class_curie: ClassVar[str] = "dpv:RenewedConsentGiven"
    class_name: ClassVar[str] = "RenewedConsentGiven"
    class_model_uri: ClassVar[URIRef] = DPV.RenewedConsentGiven

    id: Union[str, RenewedConsentGivenId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RenewedConsentGivenId):
            self.id = RenewedConsentGivenId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UninformedConsent(Consent):
    """
    Consent that is uninformed i.e. without requirement to provide
    sufficient information to make a consenting decision
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["UninformedConsent"]
    class_class_curie: ClassVar[str] = "dpv:UninformedConsent"
    class_name: ClassVar[str] = "UninformedConsent"
    class_model_uri: ClassVar[URIRef] = DPV.UninformedConsent

    id: Union[str, UninformedConsentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UninformedConsentId):
            self.id = UninformedConsentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WithdrawConsent(ConsentControl):
    """
    Control for withdrawing consent
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["WithdrawConsent"]
    class_class_curie: ClassVar[str] = "dpv:WithdrawConsent"
    class_name: ClassVar[str] = "WithdrawConsent"
    class_model_uri: ClassVar[URIRef] = DPV.WithdrawConsent

    id: Union[str, WithdrawConsentId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WithdrawConsentId):
            self.id = WithdrawConsentId(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.has_activity_status = Slot(uri=DPV.has_activity_status, name="has_activity_status", curie=DPV.curie('has_activity_status'),
                   model_uri=DPV.has_activity_status, domain=None, range=Optional[Union[str, list[str]]])

slots.has_applicability = Slot(uri=DPV.has_applicability, name="has_applicability", curie=DPV.curie('has_applicability'),
                   model_uri=DPV.has_applicability, domain=None, range=Optional[Union[str, list[str]]])

slots.has_assessment = Slot(uri=DPV.has_assessment, name="has_assessment", curie=DPV.curie('has_assessment'),
                   model_uri=DPV.has_assessment, domain=None, range=Optional[Union[str, list[str]]])

slots.has_audit_status = Slot(uri=DPV.has_audit_status, name="has_audit_status", curie=DPV.curie('has_audit_status'),
                   model_uri=DPV.has_audit_status, domain=None, range=Optional[Union[str, list[str]]])

slots.has_compliance_status = Slot(uri=DPV.has_compliance_status, name="has_compliance_status", curie=DPV.curie('has_compliance_status'),
                   model_uri=DPV.has_compliance_status, domain=None, range=Optional[Union[str, list[str]]])

slots.has_conformance_status = Slot(uri=DPV.has_conformance_status, name="has_conformance_status", curie=DPV.curie('has_conformance_status'),
                   model_uri=DPV.has_conformance_status, domain=None, range=Optional[Union[str, list[str]]])

slots.has_context = Slot(uri=DPV.has_context, name="has_context", curie=DPV.curie('has_context'),
                   model_uri=DPV.has_context, domain=None, range=Optional[Union[str, list[str]]])

slots.has_deterrence = Slot(uri=DPV.has_deterrence, name="has_deterrence", curie=DPV.curie('has_deterrence'),
                   model_uri=DPV.has_deterrence, domain=None, range=Optional[Union[str, list[str]]])

slots.has_duration = Slot(uri=DPV.has_duration, name="has_duration", curie=DPV.curie('has_duration'),
                   model_uri=DPV.has_duration, domain=None, range=Optional[Union[str, list[str]]])

slots.has_entity_control = Slot(uri=DPV.has_entity_control, name="has_entity_control", curie=DPV.curie('has_entity_control'),
                   model_uri=DPV.has_entity_control, domain=None, range=Optional[Union[str, list[str]]])

slots.has_expectation = Slot(uri=DPV.has_expectation, name="has_expectation", curie=DPV.curie('has_expectation'),
                   model_uri=DPV.has_expectation, domain=None, range=Optional[Union[str, list[str]]])

slots.has_fee = Slot(uri=DPV.has_fee, name="has_fee", curie=DPV.curie('has_fee'),
                   model_uri=DPV.has_fee, domain=None, range=Optional[Union[str, list[str]]])

slots.has_frequency = Slot(uri=DPV.has_frequency, name="has_frequency", curie=DPV.curie('has_frequency'),
                   model_uri=DPV.has_frequency, domain=None, range=Optional[Union[str, list[str]]])

slots.has_fulfilment_status = Slot(uri=DPV.has_fulfilment_status, name="has_fulfilment_status", curie=DPV.curie('has_fulfilment_status'),
                   model_uri=DPV.has_fulfilment_status, domain=None, range=Optional[Union[str, list[str]]])

slots.has_identifier = Slot(uri=DPV.has_identifier, name="has_identifier", curie=DPV.curie('has_identifier'),
                   model_uri=DPV.has_identifier, domain=None, range=Optional[Union[str, list[str]]])

slots.has_importance = Slot(uri=DPV.has_importance, name="has_importance", curie=DPV.curie('has_importance'),
                   model_uri=DPV.has_importance, domain=None, range=Optional[Union[str, list[str]]])

slots.has_informed_status = Slot(uri=DPV.has_informed_status, name="has_informed_status", curie=DPV.curie('has_informed_status'),
                   model_uri=DPV.has_informed_status, domain=None, range=Optional[Union[str, list[str]]])

slots.has_intention = Slot(uri=DPV.has_intention, name="has_intention", curie=DPV.curie('has_intention'),
                   model_uri=DPV.has_intention, domain=None, range=Optional[Union[str, list[str]]])

slots.has_involvement = Slot(uri=DPV.has_involvement, name="has_involvement", curie=DPV.curie('has_involvement'),
                   model_uri=DPV.has_involvement, domain=None, range=Optional[Union[str, list[str]]])

slots.has_justification = Slot(uri=DPV.has_justification, name="has_justification", curie=DPV.curie('has_justification'),
                   model_uri=DPV.has_justification, domain=None, range=Optional[Union[str, list[str]]])

slots.has_lawfulness = Slot(uri=DPV.has_lawfulness, name="has_lawfulness", curie=DPV.curie('has_lawfulness'),
                   model_uri=DPV.has_lawfulness, domain=None, range=Optional[Union[str, list[str]]])

slots.has_legal_measure = Slot(uri=DPV.has_legal_measure, name="has_legal_measure", curie=DPV.curie('has_legal_measure'),
                   model_uri=DPV.has_legal_measure, domain=None, range=Optional[Union[str, list[str]]])

slots.has_necessity = Slot(uri=DPV.has_necessity, name="has_necessity", curie=DPV.curie('has_necessity'),
                   model_uri=DPV.has_necessity, domain=None, range=Optional[Union[str, list[str]]])

slots.has_notification_status = Slot(uri=DPV.has_notification_status, name="has_notification_status", curie=DPV.curie('has_notification_status'),
                   model_uri=DPV.has_notification_status, domain=None, range=Optional[Union[str, list[str]]])

slots.has_obligation = Slot(uri=DPV.has_obligation, name="has_obligation", curie=DPV.curie('has_obligation'),
                   model_uri=DPV.has_obligation, domain=None, range=Optional[Union[str, list[str]]])

slots.has_organisational_measure = Slot(uri=DPV.has_organisational_measure, name="has_organisational_measure", curie=DPV.curie('has_organisational_measure'),
                   model_uri=DPV.has_organisational_measure, domain=None, range=Optional[Union[str, list[str]]])

slots.has_outcome = Slot(uri=DPV.has_outcome, name="has_outcome", curie=DPV.curie('has_outcome'),
                   model_uri=DPV.has_outcome, domain=None, range=Optional[Union[str, list[str]]])

slots.has_permission = Slot(uri=DPV.has_permission, name="has_permission", curie=DPV.curie('has_permission'),
                   model_uri=DPV.has_permission, domain=None, range=Optional[Union[str, list[str]]])

slots.has_physical_measure = Slot(uri=DPV.has_physical_measure, name="has_physical_measure", curie=DPV.curie('has_physical_measure'),
                   model_uri=DPV.has_physical_measure, domain=None, range=Optional[Union[str, list[str]]])

slots.has_policy = Slot(uri=DPV.has_policy, name="has_policy", curie=DPV.curie('has_policy'),
                   model_uri=DPV.has_policy, domain=None, range=Optional[Union[str, list[str]]])

slots.has_prohibition = Slot(uri=DPV.has_prohibition, name="has_prohibition", curie=DPV.curie('has_prohibition'),
                   model_uri=DPV.has_prohibition, domain=None, range=Optional[Union[str, list[str]]])

slots.has_recommendation = Slot(uri=DPV.has_recommendation, name="has_recommendation", curie=DPV.curie('has_recommendation'),
                   model_uri=DPV.has_recommendation, domain=None, range=Optional[Union[str, list[str]]])

slots.has_record_of_activity = Slot(uri=DPV.has_record_of_activity, name="has_record_of_activity", curie=DPV.curie('has_record_of_activity'),
                   model_uri=DPV.has_record_of_activity, domain=None, range=Optional[Union[str, list[str]]])

slots.has_request_status = Slot(uri=DPV.has_request_status, name="has_request_status", curie=DPV.curie('has_request_status'),
                   model_uri=DPV.has_request_status, domain=None, range=Optional[Union[str, list[str]]])

slots.has_reuse_compatibility = Slot(uri=DPV.has_reuse_compatibility, name="has_reuse_compatibility", curie=DPV.curie('has_reuse_compatibility'),
                   model_uri=DPV.has_reuse_compatibility, domain=None, range=Optional[Union[str, list[str]]])

slots.has_rule = Slot(uri=DPV.has_rule, name="has_rule", curie=DPV.curie('has_rule'),
                   model_uri=DPV.has_rule, domain=None, range=Optional[Union[str, list[str]]])

slots.has_scope = Slot(uri=DPV.has_scope, name="has_scope", curie=DPV.curie('has_scope'),
                   model_uri=DPV.has_scope, domain=None, range=Optional[Union[str, list[str]]])

slots.has_technical_measure = Slot(uri=DPV.has_technical_measure, name="has_technical_measure", curie=DPV.curie('has_technical_measure'),
                   model_uri=DPV.has_technical_measure, domain=None, range=Optional[Union[str, list[str]]])

slots.has_technical_organisational_measure = Slot(uri=DPV.has_technical_organisational_measure, name="has_technical_organisational_measure", curie=DPV.curie('has_technical_organisational_measure'),
                   model_uri=DPV.has_technical_organisational_measure, domain=None, range=Optional[Union[str, list[str]]])

slots.id = Slot(uri=DPV.id, name="id", curie=DPV.curie('id'),
                   model_uri=DPV.id, domain=None, range=URIRef)

slots.is_after = Slot(uri=DPV.is_after, name="is_after", curie=DPV.curie('is_after'),
                   model_uri=DPV.is_after, domain=None, range=Optional[Union[str, list[str]]])

slots.is_applicable_for = Slot(uri=DPV.is_applicable_for, name="is_applicable_for", curie=DPV.curie('is_applicable_for'),
                   model_uri=DPV.is_applicable_for, domain=None, range=Optional[Union[str, list[str]]])

slots.is_before = Slot(uri=DPV.is_before, name="is_before", curie=DPV.curie('is_before'),
                   model_uri=DPV.is_before, domain=None, range=Optional[Union[str, list[str]]])

slots.is_during = Slot(uri=DPV.is_during, name="is_during", curie=DPV.curie('is_during'),
                   model_uri=DPV.is_during, domain=None, range=Optional[Union[str, list[str]]])

slots.is_not_applicable_for = Slot(uri=DPV.is_not_applicable_for, name="is_not_applicable_for", curie=DPV.curie('is_not_applicable_for'),
                   model_uri=DPV.is_not_applicable_for, domain=None, range=Optional[Union[str, list[str]]])

slots.is_policy_for = Slot(uri=DPV.is_policy_for, name="is_policy_for", curie=DPV.curie('is_policy_for'),
                   model_uri=DPV.is_policy_for, domain=None, range=Optional[Union[str, list[str]]])

slots.supports_compliance_with = Slot(uri=DPV.supports_compliance_with, name="supports_compliance_with", curie=DPV.curie('supports_compliance_with'),
                   model_uri=DPV.supports_compliance_with, domain=None, range=Optional[Union[str, list[str]]])

slots.has_applicable_law = Slot(uri=DPV.has_applicable_law, name="has_applicable_law", curie=DPV.curie('has_applicable_law'),
                   model_uri=DPV.has_applicable_law, domain=None, range=Optional[Union[str, list[str]]])

slots.has_contract_control = Slot(uri=DPV.has_contract_control, name="has_contract_control", curie=DPV.curie('has_contract_control'),
                   model_uri=DPV.has_contract_control, domain=None, range=Optional[Union[str, list[str]]])

slots.has_contract_status = Slot(uri=DPV.has_contract_status, name="has_contract_status", curie=DPV.curie('has_contract_status'),
                   model_uri=DPV.has_contract_status, domain=None, range=Optional[Union[str, list[str]]])

slots.has_contractual_clause = Slot(uri=DPV.has_contractual_clause, name="has_contractual_clause", curie=DPV.curie('has_contractual_clause'),
                   model_uri=DPV.has_contractual_clause, domain=None, range=Optional[Union[str, list[str]]])

slots.has_contractual_fulfilment_status = Slot(uri=DPV.has_contractual_fulfilment_status, name="has_contractual_fulfilment_status", curie=DPV.curie('has_contractual_fulfilment_status'),
                   model_uri=DPV.has_contractual_fulfilment_status, domain=None, range=Optional[Union[str, list[str]]])

slots.has_country = Slot(uri=DPV.has_country, name="has_country", curie=DPV.curie('has_country'),
                   model_uri=DPV.has_country, domain=None, range=Optional[Union[str, list[str]]])

slots.has_indication_method = Slot(uri=DPV.has_indication_method, name="has_indication_method", curie=DPV.curie('has_indication_method'),
                   model_uri=DPV.has_indication_method, domain=None, range=Optional[Union[str, list[str]]])

slots.has_inverse_jurisdiction = Slot(uri=DPV.has_inverse_jurisdiction, name="has_inverse_jurisdiction", curie=DPV.curie('has_inverse_jurisdiction'),
                   model_uri=DPV.has_inverse_jurisdiction, domain=None, range=Optional[Union[str, list[str]]])

slots.has_jurisdiction = Slot(uri=DPV.has_jurisdiction, name="has_jurisdiction", curie=DPV.curie('has_jurisdiction'),
                   model_uri=DPV.has_jurisdiction, domain=None, range=Optional[Union[str, list[str]]])

slots.has_legal_basis = Slot(uri=DPV.has_legal_basis, name="has_legal_basis", curie=DPV.curie('has_legal_basis'),
                   model_uri=DPV.has_legal_basis, domain=None, range=Optional[Union[str, list[str]]])

slots.has_location = Slot(uri=DPV.has_location, name="has_location", curie=DPV.curie('has_location'),
                   model_uri=DPV.has_location, domain=None, range=Optional[Union[str, list[str]]])

slots.has_party = Slot(uri=DPV.has_party, name="has_party", curie=DPV.curie('has_party'),
                   model_uri=DPV.has_party, domain=None, range=Optional[Union[str, list[str]]])

slots.has_third_country = Slot(uri=DPV.has_third_country, name="has_third_country", curie=DPV.curie('has_third_country'),
                   model_uri=DPV.has_third_country, domain=None, range=Optional[Union[str, list[str]]])

slots.is_indicated_at_time = Slot(uri=DPV.is_indicated_at_time, name="is_indicated_at_time", curie=DPV.curie('is_indicated_at_time'),
                   model_uri=DPV.is_indicated_at_time, domain=None, range=Optional[Union[str, list[str]]])

slots.is_indicated_by = Slot(uri=DPV.is_indicated_by, name="is_indicated_by", curie=DPV.curie('is_indicated_by'),
                   model_uri=DPV.is_indicated_by, domain=None, range=Optional[Union[str, list[str]]])

slots.is_outside_of_location = Slot(uri=DPV.is_outside_of_location, name="is_outside_of_location", curie=DPV.curie('is_outside_of_location'),
                   model_uri=DPV.is_outside_of_location, domain=None, range=Optional[Union[str, list[str]]])

slots.has_address = Slot(uri=DPV.has_address, name="has_address", curie=DPV.curie('has_address'),
                   model_uri=DPV.has_address, domain=None, range=Optional[Union[str, list[str]]])

slots.has_authority = Slot(uri=DPV.has_authority, name="has_authority", curie=DPV.curie('has_authority'),
                   model_uri=DPV.has_authority, domain=None, range=Optional[Union[str, list[str]]])

slots.has_contact = Slot(uri=DPV.has_contact, name="has_contact", curie=DPV.curie('has_contact'),
                   model_uri=DPV.has_contact, domain=None, range=Optional[Union[str, list[str]]])

slots.has_data_controller = Slot(uri=DPV.has_data_controller, name="has_data_controller", curie=DPV.curie('has_data_controller'),
                   model_uri=DPV.has_data_controller, domain=None, range=Optional[Union[str, list[str]]])

slots.has_data_exporter = Slot(uri=DPV.has_data_exporter, name="has_data_exporter", curie=DPV.curie('has_data_exporter'),
                   model_uri=DPV.has_data_exporter, domain=None, range=Optional[Union[str, list[str]]])

slots.has_data_importer = Slot(uri=DPV.has_data_importer, name="has_data_importer", curie=DPV.curie('has_data_importer'),
                   model_uri=DPV.has_data_importer, domain=None, range=Optional[Union[str, list[str]]])

slots.has_data_processor = Slot(uri=DPV.has_data_processor, name="has_data_processor", curie=DPV.curie('has_data_processor'),
                   model_uri=DPV.has_data_processor, domain=None, range=Optional[Union[str, list[str]]])

slots.has_data_protection_officer = Slot(uri=DPV.has_data_protection_officer, name="has_data_protection_officer", curie=DPV.curie('has_data_protection_officer'),
                   model_uri=DPV.has_data_protection_officer, domain=None, range=Optional[Union[str, list[str]]])

slots.has_data_subject = Slot(uri=DPV.has_data_subject, name="has_data_subject", curie=DPV.curie('has_data_subject'),
                   model_uri=DPV.has_data_subject, domain=None, range=Optional[Union[str, list[str]]])

slots.has_entity = Slot(uri=DPV.has_entity, name="has_entity", curie=DPV.curie('has_entity'),
                   model_uri=DPV.has_entity, domain=None, range=Optional[Union[str, list[str]]])

slots.has_human_subject = Slot(uri=DPV.has_human_subject, name="has_human_subject", curie=DPV.curie('has_human_subject'),
                   model_uri=DPV.has_human_subject, domain=None, range=Optional[Union[str, list[str]]])

slots.has_joint_data_controllers = Slot(uri=DPV.has_joint_data_controllers, name="has_joint_data_controllers", curie=DPV.curie('has_joint_data_controllers'),
                   model_uri=DPV.has_joint_data_controllers, domain=None, range=Optional[Union[str, list[str]]])

slots.has_name = Slot(uri=DPV.has_name, name="has_name", curie=DPV.curie('has_name'),
                   model_uri=DPV.has_name, domain=None, range=Optional[Union[str, list[str]]])

slots.has_organisational_unit = Slot(uri=DPV.has_organisational_unit, name="has_organisational_unit", curie=DPV.curie('has_organisational_unit'),
                   model_uri=DPV.has_organisational_unit, domain=None, range=Optional[Union[str, list[str]]])

slots.has_recipient = Slot(uri=DPV.has_recipient, name="has_recipient", curie=DPV.curie('has_recipient'),
                   model_uri=DPV.has_recipient, domain=None, range=Optional[Union[str, list[str]]])

slots.has_recipient_data_controller = Slot(uri=DPV.has_recipient_data_controller, name="has_recipient_data_controller", curie=DPV.curie('has_recipient_data_controller'),
                   model_uri=DPV.has_recipient_data_controller, domain=None, range=Optional[Union[str, list[str]]])

slots.has_recipient_third_party = Slot(uri=DPV.has_recipient_third_party, name="has_recipient_third_party", curie=DPV.curie('has_recipient_third_party'),
                   model_uri=DPV.has_recipient_third_party, domain=None, range=Optional[Union[str, list[str]]])

slots.has_relation_with_data_subject = Slot(uri=DPV.has_relation_with_data_subject, name="has_relation_with_data_subject", curie=DPV.curie('has_relation_with_data_subject'),
                   model_uri=DPV.has_relation_with_data_subject, domain=None, range=Optional[Union[str, list[str]]])

slots.has_representative = Slot(uri=DPV.has_representative, name="has_representative", curie=DPV.curie('has_representative'),
                   model_uri=DPV.has_representative, domain=None, range=Optional[Union[str, list[str]]])

slots.has_responsible_entity = Slot(uri=DPV.has_responsible_entity, name="has_responsible_entity", curie=DPV.curie('has_responsible_entity'),
                   model_uri=DPV.has_responsible_entity, domain=None, range=Optional[Union[str, list[str]]])

slots.has_service_consumer = Slot(uri=DPV.has_service_consumer, name="has_service_consumer", curie=DPV.curie('has_service_consumer'),
                   model_uri=DPV.has_service_consumer, domain=None, range=Optional[Union[str, list[str]]])

slots.has_service_provider = Slot(uri=DPV.has_service_provider, name="has_service_provider", curie=DPV.curie('has_service_provider'),
                   model_uri=DPV.has_service_provider, domain=None, range=Optional[Union[str, list[str]]])

slots.has_subsidiary = Slot(uri=DPV.has_subsidiary, name="has_subsidiary", curie=DPV.curie('has_subsidiary'),
                   model_uri=DPV.has_subsidiary, domain=None, range=Optional[Union[str, list[str]]])

slots.has_third_party = Slot(uri=DPV.has_third_party, name="has_third_party", curie=DPV.curie('has_third_party'),
                   model_uri=DPV.has_third_party, domain=None, range=Optional[Union[str, list[str]]])

slots.is_authority_for = Slot(uri=DPV.is_authority_for, name="is_authority_for", curie=DPV.curie('is_authority_for'),
                   model_uri=DPV.is_authority_for, domain=None, range=Optional[Union[str, list[str]]])

slots.is_organisational_unit_of = Slot(uri=DPV.is_organisational_unit_of, name="is_organisational_unit_of", curie=DPV.curie('is_organisational_unit_of'),
                   model_uri=DPV.is_organisational_unit_of, domain=None, range=Optional[Union[str, list[str]]])

slots.is_representative_for = Slot(uri=DPV.is_representative_for, name="is_representative_for", curie=DPV.curie('is_representative_for'),
                   model_uri=DPV.is_representative_for, domain=None, range=Optional[Union[str, list[str]]])

slots.is_subsidiary_of = Slot(uri=DPV.is_subsidiary_of, name="is_subsidiary_of", curie=DPV.curie('is_subsidiary_of'),
                   model_uri=DPV.is_subsidiary_of, domain=None, range=Optional[Union[str, list[str]]])

slots.has_data = Slot(uri=DPV.has_data, name="has_data", curie=DPV.curie('has_data'),
                   model_uri=DPV.has_data, domain=None, range=Optional[Union[str, list[str]]])

slots.has_personal_data = Slot(uri=DPV.has_personal_data, name="has_personal_data", curie=DPV.curie('has_personal_data'),
                   model_uri=DPV.has_personal_data, domain=None, range=Optional[Union[str, list[str]]])

slots.has_uncategorised_data = Slot(uri=DPV.has_uncategorised_data, name="has_uncategorised_data", curie=DPV.curie('has_uncategorised_data'),
                   model_uri=DPV.has_uncategorised_data, domain=None, range=Optional[Union[str, list[str]]])

slots.has_unstructured_data = Slot(uri=DPV.has_unstructured_data, name="has_unstructured_data", curie=DPV.curie('has_unstructured_data'),
                   model_uri=DPV.has_unstructured_data, domain=None, range=Optional[Union[str, list[str]]])

slots.has_active_entity = Slot(uri=DPV.has_active_entity, name="has_active_entity", curie=DPV.curie('has_active_entity'),
                   model_uri=DPV.has_active_entity, domain=None, range=Optional[Union[str, list[str]]])

slots.has_algorithmic_logic = Slot(uri=DPV.has_algorithmic_logic, name="has_algorithmic_logic", curie=DPV.curie('has_algorithmic_logic'),
                   model_uri=DPV.has_algorithmic_logic, domain=None, range=Optional[Union[str, list[str]]])

slots.has_automation_level = Slot(uri=DPV.has_automation_level, name="has_automation_level", curie=DPV.curie('has_automation_level'),
                   model_uri=DPV.has_automation_level, domain=None, range=Optional[Union[str, list[str]]])

slots.has_data_source = Slot(uri=DPV.has_data_source, name="has_data_source", curie=DPV.curie('has_data_source'),
                   model_uri=DPV.has_data_source, domain=None, range=Optional[Union[str, list[str]]])

slots.has_data_subject_scale = Slot(uri=DPV.has_data_subject_scale, name="has_data_subject_scale", curie=DPV.curie('has_data_subject_scale'),
                   model_uri=DPV.has_data_subject_scale, domain=None, range=Optional[Union[str, list[str]]])

slots.has_data_volume = Slot(uri=DPV.has_data_volume, name="has_data_volume", curie=DPV.curie('has_data_volume'),
                   model_uri=DPV.has_data_volume, domain=None, range=Optional[Union[str, list[str]]])

slots.has_entity_involvement = Slot(uri=DPV.has_entity_involvement, name="has_entity_involvement", curie=DPV.curie('has_entity_involvement'),
                   model_uri=DPV.has_entity_involvement, domain=None, range=Optional[Union[str, list[str]]])

slots.has_geographic_coverage = Slot(uri=DPV.has_geographic_coverage, name="has_geographic_coverage", curie=DPV.curie('has_geographic_coverage'),
                   model_uri=DPV.has_geographic_coverage, domain=None, range=Optional[Union[str, list[str]]])

slots.has_human_involvement = Slot(uri=DPV.has_human_involvement, name="has_human_involvement", curie=DPV.curie('has_human_involvement'),
                   model_uri=DPV.has_human_involvement, domain=None, range=Optional[Union[str, list[str]]])

slots.has_non_involved_entity = Slot(uri=DPV.has_non_involved_entity, name="has_non_involved_entity", curie=DPV.curie('has_non_involved_entity'),
                   model_uri=DPV.has_non_involved_entity, domain=None, range=Optional[Union[str, list[str]]])

slots.has_non_personal_data_process = Slot(uri=DPV.has_non_personal_data_process, name="has_non_personal_data_process", curie=DPV.curie('has_non_personal_data_process'),
                   model_uri=DPV.has_non_personal_data_process, domain=None, range=Optional[Union[str, list[str]]])

slots.has_passive_entity = Slot(uri=DPV.has_passive_entity, name="has_passive_entity", curie=DPV.curie('has_passive_entity'),
                   model_uri=DPV.has_passive_entity, domain=None, range=Optional[Union[str, list[str]]])

slots.has_personal_data_handling = Slot(uri=DPV.has_personal_data_handling, name="has_personal_data_handling", curie=DPV.curie('has_personal_data_handling'),
                   model_uri=DPV.has_personal_data_handling, domain=None, range=Optional[Union[str, list[str]]])

slots.has_personal_data_process = Slot(uri=DPV.has_personal_data_process, name="has_personal_data_process", curie=DPV.curie('has_personal_data_process'),
                   model_uri=DPV.has_personal_data_process, domain=None, range=Optional[Union[str, list[str]]])

slots.has_process = Slot(uri=DPV.has_process, name="has_process", curie=DPV.curie('has_process'),
                   model_uri=DPV.has_process, domain=None, range=Optional[Union[str, list[str]]])

slots.has_processing = Slot(uri=DPV.has_processing, name="has_processing", curie=DPV.curie('has_processing'),
                   model_uri=DPV.has_processing, domain=None, range=Optional[Union[str, list[str]]])

slots.has_processing_condition = Slot(uri=DPV.has_processing_condition, name="has_processing_condition", curie=DPV.curie('has_processing_condition'),
                   model_uri=DPV.has_processing_condition, domain=None, range=Optional[Union[str, list[str]]])

slots.has_processing_scale = Slot(uri=DPV.has_processing_scale, name="has_processing_scale", curie=DPV.curie('has_processing_scale'),
                   model_uri=DPV.has_processing_scale, domain=None, range=Optional[Union[str, list[str]]])

slots.has_purpose = Slot(uri=DPV.has_purpose, name="has_purpose", curie=DPV.curie('has_purpose'),
                   model_uri=DPV.has_purpose, domain=None, range=Optional[Union[str, list[str]]])

slots.has_scale = Slot(uri=DPV.has_scale, name="has_scale", curie=DPV.curie('has_scale'),
                   model_uri=DPV.has_scale, domain=None, range=Optional[Union[str, list[str]]])

slots.has_sector = Slot(uri=DPV.has_sector, name="has_sector", curie=DPV.curie('has_sector'),
                   model_uri=DPV.has_sector, domain=None, range=Optional[Union[str, list[str]]])

slots.has_service = Slot(uri=DPV.has_service, name="has_service", curie=DPV.curie('has_service'),
                   model_uri=DPV.has_service, domain=None, range=Optional[Union[str, list[str]]])

slots.has_storage_condition = Slot(uri=DPV.has_storage_condition, name="has_storage_condition", curie=DPV.curie('has_storage_condition'),
                   model_uri=DPV.has_storage_condition, domain=None, range=Optional[Union[str, list[str]]])

slots.is_determined_by_entity = Slot(uri=DPV.is_determined_by_entity, name="is_determined_by_entity", curie=DPV.curie('is_determined_by_entity'),
                   model_uri=DPV.is_determined_by_entity, domain=None, range=Optional[Union[str, list[str]]])

slots.is_implemented_by_entity = Slot(uri=DPV.is_implemented_by_entity, name="is_implemented_by_entity", curie=DPV.curie('is_implemented_by_entity'),
                   model_uri=DPV.is_implemented_by_entity, domain=None, range=Optional[Union[str, list[str]]])

slots.is_implemented_using_technology = Slot(uri=DPV.is_implemented_using_technology, name="is_implemented_using_technology", curie=DPV.curie('is_implemented_using_technology'),
                   model_uri=DPV.is_implemented_using_technology, domain=None, range=Optional[Union[str, list[str]]])

slots.has_consequence = Slot(uri=DPV.has_consequence, name="has_consequence", curie=DPV.curie('has_consequence'),
                   model_uri=DPV.has_consequence, domain=None, range=Optional[Union[str, list[str]]])

slots.has_consequence_on = Slot(uri=DPV.has_consequence_on, name="has_consequence_on", curie=DPV.curie('has_consequence_on'),
                   model_uri=DPV.has_consequence_on, domain=None, range=Optional[Union[str, list[str]]])

slots.has_impact = Slot(uri=DPV.has_impact, name="has_impact", curie=DPV.curie('has_impact'),
                   model_uri=DPV.has_impact, domain=None, range=Optional[Union[str, list[str]]])

slots.has_impact_assessment = Slot(uri=DPV.has_impact_assessment, name="has_impact_assessment", curie=DPV.curie('has_impact_assessment'),
                   model_uri=DPV.has_impact_assessment, domain=None, range=Optional[Union[str, list[str]]])

slots.has_impact_on = Slot(uri=DPV.has_impact_on, name="has_impact_on", curie=DPV.curie('has_impact_on'),
                   model_uri=DPV.has_impact_on, domain=None, range=Optional[Union[str, list[str]]])

slots.has_likelihood = Slot(uri=DPV.has_likelihood, name="has_likelihood", curie=DPV.curie('has_likelihood'),
                   model_uri=DPV.has_likelihood, domain=None, range=Optional[Union[str, list[str]]])

slots.has_notice = Slot(uri=DPV.has_notice, name="has_notice", curie=DPV.curie('has_notice'),
                   model_uri=DPV.has_notice, domain=None, range=Optional[Union[str, list[str]]])

slots.has_notice_icon = Slot(uri=DPV.has_notice_icon, name="has_notice_icon", curie=DPV.curie('has_notice_icon'),
                   model_uri=DPV.has_notice_icon, domain=None, range=Optional[Union[str, list[str]]])

slots.has_notice_layer = Slot(uri=DPV.has_notice_layer, name="has_notice_layer", curie=DPV.curie('has_notice_layer'),
                   model_uri=DPV.has_notice_layer, domain=None, range=Optional[Union[str, list[str]]])

slots.has_notice_status = Slot(uri=DPV.has_notice_status, name="has_notice_status", curie=DPV.curie('has_notice_status'),
                   model_uri=DPV.has_notice_status, domain=None, range=Optional[Union[str, list[str]]])

slots.has_residual_risk = Slot(uri=DPV.has_residual_risk, name="has_residual_risk", curie=DPV.curie('has_residual_risk'),
                   model_uri=DPV.has_residual_risk, domain=None, range=Optional[Union[str, list[str]]])

slots.has_risk = Slot(uri=DPV.has_risk, name="has_risk", curie=DPV.curie('has_risk'),
                   model_uri=DPV.has_risk, domain=None, range=Optional[Union[str, list[str]]])

slots.has_risk_assessment = Slot(uri=DPV.has_risk_assessment, name="has_risk_assessment", curie=DPV.curie('has_risk_assessment'),
                   model_uri=DPV.has_risk_assessment, domain=None, range=Optional[Union[str, list[str]]])

slots.has_risk_level = Slot(uri=DPV.has_risk_level, name="has_risk_level", curie=DPV.curie('has_risk_level'),
                   model_uri=DPV.has_risk_level, domain=None, range=Optional[Union[str, list[str]]])

slots.has_sensitivity_level = Slot(uri=DPV.has_sensitivity_level, name="has_sensitivity_level", curie=DPV.curie('has_sensitivity_level'),
                   model_uri=DPV.has_sensitivity_level, domain=None, range=Optional[Union[str, list[str]]])

slots.has_severity = Slot(uri=DPV.has_severity, name="has_severity", curie=DPV.curie('has_severity'),
                   model_uri=DPV.has_severity, domain=None, range=Optional[Union[str, list[str]]])

slots.is_mitigated_by_measure = Slot(uri=DPV.is_mitigated_by_measure, name="is_mitigated_by_measure", curie=DPV.curie('is_mitigated_by_measure'),
                   model_uri=DPV.is_mitigated_by_measure, domain=None, range=Optional[Union[str, list[str]]])

slots.is_residual_risk_of = Slot(uri=DPV.is_residual_risk_of, name="is_residual_risk_of", curie=DPV.curie('is_residual_risk_of'),
                   model_uri=DPV.is_residual_risk_of, domain=None, range=Optional[Union[str, list[str]]])

slots.mitigates_risk = Slot(uri=DPV.mitigates_risk, name="mitigates_risk", curie=DPV.curie('mitigates_risk'),
                   model_uri=DPV.mitigates_risk, domain=None, range=Optional[Union[str, list[str]]])

slots.has_right = Slot(uri=DPV.has_right, name="has_right", curie=DPV.curie('has_right'),
                   model_uri=DPV.has_right, domain=None, range=Optional[Union[str, list[str]]])

slots.has_status = Slot(uri=DPV.has_status, name="has_status", curie=DPV.curie('has_status'),
                   model_uri=DPV.has_status, domain=None, range=Optional[Union[str, list[str]]])

slots.is_exercised_at = Slot(uri=DPV.is_exercised_at, name="is_exercised_at", curie=DPV.curie('is_exercised_at'),
                   model_uri=DPV.is_exercised_at, domain=None, range=Optional[Union[str, list[str]]])

slots.has_consent_control = Slot(uri=DPV.has_consent_control, name="has_consent_control", curie=DPV.curie('has_consent_control'),
                   model_uri=DPV.has_consent_control, domain=None, range=Optional[Union[str, list[str]]])

slots.has_consent_status = Slot(uri=DPV.has_consent_status, name="has_consent_status", curie=DPV.curie('has_consent_status'),
                   model_uri=DPV.has_consent_status, domain=None, range=Optional[Union[str, list[str]]])
