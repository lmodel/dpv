# Auto generated from dpv.yaml by pythongen.py version: 0.0.1
# Schema: dpv
#
# id: https://w3id.org/lmodel/dpv
# description: A LinkML model of the Data Privacy Vocabulary (DPV) 2.3 of the W3C Data Privacy Vocabularies and Controls Community Group. DPV states each concept as a class and as an instance of a broader concept, so the model holds its terms as records: each concept that terms are instances of is a class, each property is a slot under its own IRI, and every term of DPV's vocabularies is a record that validates against them.
# license: Apache-2.0

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

from linkml_runtime.linkml_model.types import Decimal, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Decimal, URIorCURIE

metamodel_version = "1.12.0"
version = "2.3"

# Namespaces
AI = CurieNamespace('ai', 'https://w3id.org/dpv/ai#')
BIBO = CurieNamespace('bibo', 'http://purl.org/ontology/bibo/')
DCAM = CurieNamespace('dcam', 'http://purl.org/dc/dcam/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DE_GDNG = CurieNamespace('de-gdng', 'https://w3id.org/dpv/legal/de/gdng#')
DEX = CurieNamespace('dex', 'https://w3id.org/dpv/examples#')
DPV = CurieNamespace('dpv', 'https://w3id.org/dpv#')
DPV_AGENT = CurieNamespace('dpv_agent', 'https://w3id.org/lmodel/dpv/agents/')
DPV_LINKML = CurieNamespace('dpv_linkml', 'https://w3id.org/lmodel/dpv/')
EU_AIACT = CurieNamespace('eu-aiact', 'https://w3id.org/dpv/legal/eu/aiact#')
EU_DGA = CurieNamespace('eu-dga', 'https://w3id.org/dpv/legal/eu/dga#')
EU_EHDS = CurieNamespace('eu-ehds', 'https://w3id.org/dpv/legal/eu/ehds#')
EU_GDPR = CurieNamespace('eu-gdpr', 'https://w3id.org/dpv/legal/eu/gdpr#')
EU_NIS2 = CurieNamespace('eu-nis2', 'https://w3id.org/dpv/legal/eu/nis2#')
EU_RIGHTS = CurieNamespace('eu-rights', 'https://w3id.org/dpv/rights/eu#')
EX = CurieNamespace('ex', 'http://example.com#')
EXA = CurieNamespace('exA', 'http://example.com/exA#')
EXB = CurieNamespace('exB', 'http://example.com/exB#')
EXD = CurieNamespace('exd', 'http://example.com/default#')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
IEEE_7012 = CurieNamespace('ieee-7012', 'https://w3id.org/dpv/standards/ieee/7012#')
JUSTIFICATIONS = CurieNamespace('justifications', 'https://w3id.org/dpv/justifications#')
LEGAL = CurieNamespace('legal', 'https://w3id.org/dpv/legal#')
LEGAL_AT = CurieNamespace('legal-at', 'https://w3id.org/dpv/legal/at#')
LEGAL_BE = CurieNamespace('legal-be', 'https://w3id.org/dpv/legal/be#')
LEGAL_BG = CurieNamespace('legal-bg', 'https://w3id.org/dpv/legal/bg#')
LEGAL_CY = CurieNamespace('legal-cy', 'https://w3id.org/dpv/legal/cy#')
LEGAL_CZ = CurieNamespace('legal-cz', 'https://w3id.org/dpv/legal/cz#')
LEGAL_DE = CurieNamespace('legal-de', 'https://w3id.org/dpv/legal/de#')
LEGAL_DK = CurieNamespace('legal-dk', 'https://w3id.org/dpv/legal/dk#')
LEGAL_EE = CurieNamespace('legal-ee', 'https://w3id.org/dpv/legal/ee#')
LEGAL_ES = CurieNamespace('legal-es', 'https://w3id.org/dpv/legal/es#')
LEGAL_EU = CurieNamespace('legal-eu', 'https://w3id.org/dpv/legal/eu#')
LEGAL_FI = CurieNamespace('legal-fi', 'https://w3id.org/dpv/legal/fi#')
LEGAL_FR = CurieNamespace('legal-fr', 'https://w3id.org/dpv/legal/fr#')
LEGAL_GB = CurieNamespace('legal-gb', 'https://w3id.org/dpv/legal/gb#')
LEGAL_GR = CurieNamespace('legal-gr', 'https://w3id.org/dpv/legal/gr#')
LEGAL_HK = CurieNamespace('legal-hk', 'https://w3id.org/dpv/legal/hk#')
LEGAL_HR = CurieNamespace('legal-hr', 'https://w3id.org/dpv/legal/hr#')
LEGAL_HU = CurieNamespace('legal-hu', 'https://w3id.org/dpv/legal/hu#')
LEGAL_IE = CurieNamespace('legal-ie', 'https://w3id.org/dpv/legal/ie#')
LEGAL_IN = CurieNamespace('legal-in', 'https://w3id.org/dpv/legal/in#')
LEGAL_IS = CurieNamespace('legal-is', 'https://w3id.org/dpv/legal/is#')
LEGAL_IT = CurieNamespace('legal-it', 'https://w3id.org/dpv/legal/it#')
LEGAL_JP = CurieNamespace('legal-jp', 'https://w3id.org/dpv/legal/jp#')
LEGAL_KR = CurieNamespace('legal-kr', 'https://w3id.org/dpv/legal/kr#')
LEGAL_LI = CurieNamespace('legal-li', 'https://w3id.org/dpv/legal/li#')
LEGAL_LT = CurieNamespace('legal-lt', 'https://w3id.org/dpv/legal/lt#')
LEGAL_LU = CurieNamespace('legal-lu', 'https://w3id.org/dpv/legal/lu#')
LEGAL_LV = CurieNamespace('legal-lv', 'https://w3id.org/dpv/legal/lv#')
LEGAL_MO = CurieNamespace('legal-mo', 'https://w3id.org/dpv/legal/mo#')
LEGAL_MT = CurieNamespace('legal-mt', 'https://w3id.org/dpv/legal/mt#')
LEGAL_MY = CurieNamespace('legal-my', 'https://w3id.org/dpv/legal/my#')
LEGAL_NL = CurieNamespace('legal-nl', 'https://w3id.org/dpv/legal/nl#')
LEGAL_NO = CurieNamespace('legal-no', 'https://w3id.org/dpv/legal/no#')
LEGAL_PH = CurieNamespace('legal-ph', 'https://w3id.org/dpv/legal/ph#')
LEGAL_PL = CurieNamespace('legal-pl', 'https://w3id.org/dpv/legal/pl#')
LEGAL_PT = CurieNamespace('legal-pt', 'https://w3id.org/dpv/legal/pt#')
LEGAL_RO = CurieNamespace('legal-ro', 'https://w3id.org/dpv/legal/ro#')
LEGAL_SE = CurieNamespace('legal-se', 'https://w3id.org/dpv/legal/se#')
LEGAL_SG = CurieNamespace('legal-sg', 'https://w3id.org/dpv/legal/sg#')
LEGAL_SI = CurieNamespace('legal-si', 'https://w3id.org/dpv/legal/si#')
LEGAL_SK = CurieNamespace('legal-sk', 'https://w3id.org/dpv/legal/sk#')
LEGAL_TH = CurieNamespace('legal-th', 'https://w3id.org/dpv/legal/th#')
LEGAL_TW = CurieNamespace('legal-tw', 'https://w3id.org/dpv/legal/tw#')
LEGAL_US = CurieNamespace('legal-us', 'https://w3id.org/dpv/legal/us#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LOC = CurieNamespace('loc', 'https://w3id.org/dpv/loc#')
NACE = CurieNamespace('nace', 'http://data.europa.eu/ux2/nace2.1/')
ODRL = CurieNamespace('odrl', 'http://www.w3.org/ns/odrl/2/')
ORG = CurieNamespace('org', 'http://www.w3.org/ns/org#')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PD = CurieNamespace('pd', 'https://w3id.org/dpv/pd#')
PROF = CurieNamespace('prof', 'http://www.w3.org/ns/dx/prof/')
PROFILE = CurieNamespace('profile', 'http://www.w3.org/ns/dx/prof/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RISK = CurieNamespace('risk', 'https://w3id.org/dpv/risk#')
ROLE = CurieNamespace('role', 'http://www.w3.org/ns/dx/prof/role/')
SCORO = CurieNamespace('scoro', 'http://purl.org/spar/scoro/')
SDO = CurieNamespace('sdo', 'https://schema.org/')
SECTOR = CurieNamespace('sector', 'https://w3id.org/dpv/sector#')
SECTOR_EDUCATION = CurieNamespace('sector-education', 'https://w3id.org/dpv/sector/education#')
SECTOR_FINANCE = CurieNamespace('sector-finance', 'https://w3id.org/dpv/sector/finance#')
SECTOR_HEALTH = CurieNamespace('sector-health', 'https://w3id.org/dpv/sector/health#')
SECTOR_INFRA = CurieNamespace('sector-infra', 'https://w3id.org/dpv/sector/infra#')
SECTOR_LAW = CurieNamespace('sector-law', 'https://w3id.org/dpv/sector/law#')
SECTOR_PUBLICSERVICES = CurieNamespace('sector-publicservices', 'https://w3id.org/dpv/sector/publicservices#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SPL = CurieNamespace('spl', 'https://specialprivacy.ercim.eu/langs/usage-policy#')
SVD = CurieNamespace('svd', 'https://specialprivacy.ercim.eu/vocabs/data#')
SVPR = CurieNamespace('svpr', 'https://specialprivacy.ercim.eu/vocabs/processing#')
SVPU = CurieNamespace('svpu', 'https://specialprivacy.ercim.eu/vocabs/purposes#')
SW = CurieNamespace('sw', 'http://www.w3.org/2003/06/sw-vocab-status/ns#')
TECH = CurieNamespace('tech', 'https://w3id.org/dpv/tech#')
TIME = CurieNamespace('time', 'http://www.w3.org/2006/time#')
VANN = CurieNamespace('vann', 'http://purl.org/vocab/vann/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = DPV_LINKML


# Types
class DpvDate(String):
    """ A date as DPV writes it, year first. """
    type_class_uri = XSD["date"]
    type_class_curie = "xsd:date"
    type_name = "dpv_date"
    type_model_uri = DPV_LINKML.DpvDate


class DpvUri(String):
    """ An address as DPV writes it, typed xsd:anyURI. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "dpv_uri"
    type_model_uri = DPV_LINKML.DpvUri


# Class references
class DpvVocabularyId(URIorCURIE):
    pass


class DpvConceptSchemeId(URIorCURIE):
    pass


class DpvAgentId(URIorCURIE):
    pass


class DpvTermId(URIorCURIE):
    pass


class DpvConceptId(DpvTermId):
    pass


class DpvPropertyId(DpvTermId):
    pass


class DpvResourceId(DpvTermId):
    pass


class DpvExampleId(URIorCURIE):
    pass


class DpvAggregatedDataId(DpvConceptId):
    pass


class DpvApplicabilityId(DpvConceptId):
    pass


class DpvContractualClauseId(DpvConceptId):
    pass


class DpvDurationId(DpvConceptId):
    pass


class DpvExpectationStatusId(DpvConceptId):
    pass


class DpvFeeRequirementId(DpvConceptId):
    pass


class DpvFrequencyId(DpvConceptId):
    pass


class DpvImportanceId(DpvConceptId):
    pass


class DpvJustificationId(DpvConceptId):
    pass


class DpvLawId(DpvConceptId):
    pass


class DpvLegalBasisId(DpvConceptId):
    pass


class DpvLegalEntityId(DpvConceptId):
    pass


class DpvAuthorityId(DpvLegalEntityId):
    pass


class DpvDataProtectionAuthorityId(DpvAuthorityId):
    pass


class DpvHumanSubjectId(DpvLegalEntityId):
    pass


class DpvLegalMeasureId(DpvConceptId):
    pass


class DpvLikelihoodId(DpvConceptId):
    pass


class DpvLocationId(DpvConceptId):
    pass


class DpvJurisdictionId(DpvLocationId):
    pass


class DpvCountryId(DpvJurisdictionId):
    pass


class DpvInverseJurisdictionId(DpvJurisdictionId):
    pass


class DpvLocationFixtureId(DpvConceptId):
    pass


class DpvNecessityId(DpvConceptId):
    pass


class DpvNonPersonalDataId(DpvConceptId):
    pass


class DpvOrganisationalMeasureId(DpvConceptId):
    pass


class DpvPersonalDataId(DpvConceptId):
    pass


class DpvPhysicalMeasureId(DpvConceptId):
    pass


class DpvProcessingId(DpvConceptId):
    pass


class DpvProcessingContextId(DpvConceptId):
    pass


class DpvAutomationLevelId(DpvProcessingContextId):
    pass


class DpvDataSourceId(DpvProcessingContextId):
    pass


class DpvDataSubjectDataSourceId(DpvDataSourceId):
    pass


class DpvDataSubjectScaleId(DpvProcessingContextId):
    pass


class DpvDataVolumeId(DpvProcessingContextId):
    pass


class DpvEntityNonPermissiveInvolvementId(DpvProcessingContextId):
    pass


class DpvEntityPermissiveInvolvementId(DpvProcessingContextId):
    pass


class DpvEvaluationScoringId(DpvProcessingContextId):
    pass


class DpvGeographicCoverageId(DpvProcessingContextId):
    pass


class DpvHumanInvolvementId(DpvProcessingContextId):
    pass


class DpvInnovativeUseOfTechnologyId(DpvProcessingContextId):
    pass


class DpvProcessingScaleId(DpvProcessingContextId):
    pass


class DpvPublicRegisterOfEntitiesId(DpvConceptId):
    pass


class DpvPurposeId(DpvConceptId):
    pass


class DpvRegionId(DpvCountryId):
    pass


class DpvRightId(DpvConceptId):
    pass


class DpvRiskConceptId(DpvConceptId):
    pass


class DpvRiskLevelId(DpvConceptId):
    pass


class DpvRuleId(DpvConceptId):
    pass


class DpvObligationId(DpvRuleId):
    pass


class DpvPermissionId(DpvRuleId):
    pass


class DpvProhibitionId(DpvRuleId):
    pass


class DpvScoringOfIndividualsId(DpvEvaluationScoringId):
    pass


class DpvSectorId(DpvConceptId):
    pass


class DpvSensitivePersonalDataId(DpvPersonalDataId):
    pass


class DpvSeverityId(DpvConceptId):
    pass


class DpvSpecialCategoryPersonalDataId(DpvSensitivePersonalDataId):
    pass


class DpvStatusId(DpvConceptId):
    pass


class DpvActivityStatusId(DpvStatusId):
    pass


class DpvAuditStatusId(DpvStatusId):
    pass


class DpvComplianceStatusId(DpvStatusId):
    pass


class DpvConformanceStatusId(DpvStatusId):
    pass


class DpvConsentStatusId(DpvStatusId):
    pass


class DpvContractActivationStatusId(DpvStatusId):
    pass


class DpvContractExecutionStatusId(DpvStatusId):
    pass


class DpvContractFulfilmentStatusId(DpvStatusId):
    pass


class DpvContractPerformanceStatusId(DpvStatusId):
    pass


class DpvContractPreparationStatusId(DpvStatusId):
    pass


class DpvContractTerminationStatusId(DpvStatusId):
    pass


class DpvContractualClauseFulfilmentStatusId(DpvStatusId):
    pass


class DpvEntityInformedStatusId(DpvStatusId):
    pass


class DpvEntityInvolvementStatusId(DpvStatusId):
    pass


class DpvIntentionStatusId(DpvStatusId):
    pass


class DpvInvolvementStatusId(DpvStatusId):
    pass


class DpvLawfulnessId(DpvComplianceStatusId):
    pass


class DpvLegalObligationStatusId(DpvStatusId):
    pass


class DpvLegitimateInterestStatusId(DpvStatusId):
    pass


class DpvNoticeStatusId(DpvStatusId):
    pass


class DpvNotificationStatusId(DpvStatusId):
    pass


class DpvOfficialAuthorityExerciseStatusId(DpvStatusId):
    pass


class DpvPublicInterestStatusId(DpvStatusId):
    pass


class DpvRequestStatusId(DpvStatusId):
    pass


class DpvReuseCompatibilityId(DpvStatusId):
    pass


class DpvRuleFulfilmentStatusId(DpvStatusId):
    pass


class DpvSupraNationalUnionId(DpvJurisdictionId):
    pass


class DpvTechnicalMeasureId(DpvConceptId):
    pass


class DpvTechnologyId(DpvConceptId):
    pass


class DpvVitalInterestStatusId(DpvStatusId):
    pass


class DpvPdPersonalDataId(DpvConceptId):
    pass


class DpvActorId(DpvConceptId):
    pass


class DpvCommunicationMechanismId(DpvTechnologyId):
    pass


class DpvDocumentationId(DpvConceptId):
    pass


class DpvProvisionMethodId(DpvTechnologyId):
    pass


class DpvProvisionStatusId(DpvStatusId):
    pass


class DpvTechCapabilityId(DpvConceptId):
    pass


class DpvTechMarketAvailabilityStatusId(DpvStatusId):
    pass


class DpvAiCapabilityId(DpvTechnologyId):
    pass


class DpvLifecycleStageId(DpvConceptId):
    pass


class DpvTechniqueId(DpvTechnologyId):
    pass


class DpvTrainingTechniqueId(DpvProcessingId):
    pass


class DpvAvailabilityConceptId(DpvRiskConceptId):
    pass


class DpvConfidentialityConceptId(DpvRiskConceptId):
    pass


class DpvIncidentInvestigationStatusId(DpvStatusId):
    pass


class DpvIncidentNoticeId(DpvOrganisationalMeasureId):
    pass


class DpvIncidentStatusId(DpvStatusId):
    pass


class DpvIntegrityConceptId(DpvRiskConceptId):
    pass


class DpvPotentialConsequenceId(DpvRiskConceptId):
    pass


class DpvPotentialImpactId(DpvRiskConceptId):
    pass


class DpvPotentialRiskId(DpvRiskConceptId):
    pass


class DpvPotentialRiskSourceId(DpvRiskConceptId):
    pass


class DpvRiskAnalysisId(DpvConceptId):
    pass


class DpvRiskControlId(DpvConceptId):
    pass


class DpvAISystemId(DpvTechnologyId):
    pass


class DpvAdequacyDecisionId(DpvLegalBasisId):
    pass


class DpvChangeCategoryId(DpvConceptId):
    pass


class DpvDBIARiskStatusId(DpvAuditStatusId):
    pass


class DpvDPIAConformityId(DpvConformanceStatusId):
    pass


class DpvDPIANecessityStatusId(DpvAuditStatusId):
    pass


class DpvDPIAOutcomeStatusId(DpvAuditStatusId):
    pass


class DpvDPIAProcessingRecommendationId(DpvAuditStatusId):
    pass


class DpvDPIARiskStatusId(DpvAuditStatusId):
    pass


class DpvDataBreachNoticeId(DpvOrganisationalMeasureId):
    pass


class DpvDataBreachNoticeRequirementId(DpvAuditStatusId):
    pass


class DpvEuAiactMarketAvailabilityStatusId(DpvTechMarketAvailabilityStatusId):
    pass


class DpvEuAiactRiskLevelId(DpvRiskLevelId):
    pass


class DpvEuGdprDataProtectionAuthorityId(DpvDataProtectionAuthorityId):
    pass


class DpvEuGdprProcessingId(DpvProcessingId):
    pass


class DpvHighRiskAISystemId(DpvAISystemId):
    pass


class DpvMarketPlacementStatusId(DpvTechMarketAvailabilityStatusId):
    pass


class DpvProhibitedAISystemId(DpvAISystemId):
    pass


class DpvProportionalityStatusId(DpvStatusId):
    pass


class DpvRegulatedHealthDataHolderId(DpvConceptId):
    pass


class DpvServiceSupplyStatusId(DpvProvisionStatusId):
    pass


class DpvSectorHealthReuseCompatibilityId(DpvReuseCompatibilityId):
    pass


class DpvAgentNegotiationBehaviourId(DpvContractualClauseId):
    pass


class DpvAgentRequestBehaviourId(DpvContractualClauseId):
    pass


class DpvAgreementId(DpvContractualClauseId):
    pass


class DpvAgreementNegotiationStatusId(DpvStatusId):
    pass


class DpvConflictResolutionTermId(DpvContractualClauseId):
    pass


class DpvDataDeletionTermId(DpvContractualClauseId):
    pass


class DpvDataSharingTermId(DpvContractualClauseId):
    pass


class DpvDeonticInterpretationTermId(DpvContractualClauseId):
    pass


class DpvPortabilityTermId(DpvContractualClauseId):
    pass


class DpvPreferenceApplicabilityId(DpvContractualClauseId):
    pass


class DpvProfilingTermId(DpvContractualClauseId):
    pass


class DpvTrackingTermId(DpvContractualClauseId):
    pass


class DpvTransparencyTermId(DpvContractualClauseId):
    pass


class DpvDataTransparencyTermId(DpvTransparencyTermId):
    pass


class DpvPartyTransparencyTermId(DpvTransparencyTermId):
    pass


class DpvPurposeTransparencyTermId(DpvTransparencyTermId):
    pass


@dataclass(repr=False)
class DpvCatalogue(YAMLRoot):
    """
    One part of a DPV release: one namespace family's vocabularies and terms, its contributors or its examples.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV_LINKML["DpvCatalogue"]
    class_class_curie: ClassVar[str] = "dpv_linkml:DpvCatalogue"
    class_name: ClassVar[str] = "DpvCatalogue"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvCatalogue

    edition: str = None
    family: Union[str, "DpvFamily"] = None
    concepts: Optional[Union[dict[Union[str, DpvConceptId], Union[dict, "DpvConcept"]], list[Union[dict, "DpvConcept"]]]] = empty_dict()
    vocabularies: Optional[Union[dict[Union[str, DpvVocabularyId], Union[dict, "DpvVocabulary"]], list[Union[dict, "DpvVocabulary"]]]] = empty_dict()
    concept_schemes: Optional[Union[list[Union[str, DpvConceptSchemeId]], dict[Union[str, DpvConceptSchemeId], Union[dict, "DpvConceptScheme"]]]] = empty_dict()
    properties: Optional[Union[dict[Union[str, DpvPropertyId], Union[dict, "DpvProperty"]], list[Union[dict, "DpvProperty"]]]] = empty_dict()
    agents: Optional[Union[dict[Union[str, DpvAgentId], Union[dict, "DpvAgent"]], list[Union[dict, "DpvAgent"]]]] = empty_dict()
    examples: Optional[Union[dict[Union[str, DpvExampleId], Union[dict, "DpvExample"]], list[Union[dict, "DpvExample"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.edition):
            self.MissingRequiredField("edition")
        if not isinstance(self.edition, str):
            self.edition = str(self.edition)

        if self._is_empty(self.family):
            self.MissingRequiredField("family")
        if not isinstance(self.family, DpvFamily):
            self.family = DpvFamily(self.family)

        self._normalize_inlined_as_list(slot_name="concepts", slot_type=DpvConcept, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="vocabularies", slot_type=DpvVocabulary, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="concept_schemes", slot_type=DpvConceptScheme, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="properties", slot_type=DpvProperty, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="agents", slot_type=DpvAgent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="examples", slot_type=DpvExample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvVocabulary(YAMLRoot):
    """
    One of DPV's vocabularies, as its own Turtle file's header describes it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL["Ontology"]
    class_class_curie: ClassVar[str] = "owl:Ontology"
    class_name: ClassVar[str] = "DpvVocabulary"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvVocabulary

    id: Union[str, DpvVocabularyId] = None
    versionInfo: str = None
    title: Optional[str] = None
    description: Optional[str] = None
    identifier: Optional[str] = None
    bibliographicCitation: Optional[str] = None
    conformsTo: Optional[Union[str, list[str]]] = empty_list()
    created: Optional[Union[Union[str, DpvDate], list[Union[str, DpvDate]]]] = empty_list()
    issued: Optional[Union[str, DpvDate]] = None
    modified: Optional[Union[str, DpvDate]] = None
    creator: Optional[Union[Union[str, DpvAgentId], list[Union[str, DpvAgentId]]]] = empty_list()
    contributor: Optional[Union[Union[str, DpvAgentId], list[Union[str, DpvAgentId]]]] = empty_list()
    publisher: Optional[Union[str, DpvUri]] = None
    license: Optional[Union[str, DpvUri]] = None
    source: Optional[Union[str, list[str]]] = empty_list()
    doi: Optional[str] = None
    bibo_status: Optional[str] = None
    preferredNamespacePrefix: Optional[str] = None
    preferredNamespaceUri: Optional[str] = None
    rdfs_Label: Optional[str] = None
    versionIRI: Optional[Union[str, DpvUri]] = None
    schema_version: Optional[str] = None
    isProfileOf: Optional[Union[Union[str, DpvUri], list[Union[str, DpvUri]]]] = empty_list()
    logo: Optional[Union[str, DpvUri]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvVocabularyId):
            self.id = DpvVocabularyId(self.id)

        if self._is_empty(self.versionInfo):
            self.MissingRequiredField("versionInfo")
        if not isinstance(self.versionInfo, str):
            self.versionInfo = str(self.versionInfo)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.bibliographicCitation is not None and not isinstance(self.bibliographicCitation, str):
            self.bibliographicCitation = str(self.bibliographicCitation)

        if not isinstance(self.conformsTo, list):
            self.conformsTo = [self.conformsTo] if self.conformsTo is not None else []
        self.conformsTo = [v if isinstance(v, str) else str(v) for v in self.conformsTo]

        if not isinstance(self.created, list):
            self.created = [self.created] if self.created is not None else []
        self.created = [v if isinstance(v, DpvDate) else DpvDate(v) for v in self.created]

        if self.issued is not None and not isinstance(self.issued, DpvDate):
            self.issued = DpvDate(self.issued)

        if self.modified is not None and not isinstance(self.modified, DpvDate):
            self.modified = DpvDate(self.modified)

        if not isinstance(self.creator, list):
            self.creator = [self.creator] if self.creator is not None else []
        self.creator = [v if isinstance(v, DpvAgentId) else DpvAgentId(v) for v in self.creator]

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, DpvAgentId) else DpvAgentId(v) for v in self.contributor]

        if self.publisher is not None and not isinstance(self.publisher, DpvUri):
            self.publisher = DpvUri(self.publisher)

        if self.license is not None and not isinstance(self.license, DpvUri):
            self.license = DpvUri(self.license)

        if not isinstance(self.source, list):
            self.source = [self.source] if self.source is not None else []
        self.source = [v if isinstance(v, str) else str(v) for v in self.source]

        if self.doi is not None and not isinstance(self.doi, str):
            self.doi = str(self.doi)

        if self.bibo_status is not None and not isinstance(self.bibo_status, str):
            self.bibo_status = str(self.bibo_status)

        if self.preferredNamespacePrefix is not None and not isinstance(self.preferredNamespacePrefix, str):
            self.preferredNamespacePrefix = str(self.preferredNamespacePrefix)

        if self.preferredNamespaceUri is not None and not isinstance(self.preferredNamespaceUri, str):
            self.preferredNamespaceUri = str(self.preferredNamespaceUri)

        if self.rdfs_Label is not None and not isinstance(self.rdfs_Label, str):
            self.rdfs_Label = str(self.rdfs_Label)

        if self.versionIRI is not None and not isinstance(self.versionIRI, DpvUri):
            self.versionIRI = DpvUri(self.versionIRI)

        if self.schema_version is not None and not isinstance(self.schema_version, str):
            self.schema_version = str(self.schema_version)

        if not isinstance(self.isProfileOf, list):
            self.isProfileOf = [self.isProfileOf] if self.isProfileOf is not None else []
        self.isProfileOf = [v if isinstance(v, DpvUri) else DpvUri(v) for v in self.isProfileOf]

        if self.logo is not None and not isinstance(self.logo, DpvUri):
            self.logo = DpvUri(self.logo)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvConceptScheme(YAMLRoot):
    """
    A list of terms DPV keeps within a vocabulary. DPV states nothing else about one.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["ConceptScheme"]
    class_class_curie: ClassVar[str] = "skos:ConceptScheme"
    class_name: ClassVar[str] = "DpvConceptScheme"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvConceptScheme

    id: Union[str, DpvConceptSchemeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvConceptSchemeId):
            self.id = DpvConceptSchemeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvAgent(YAMLRoot):
    """
    A person or an organization DPV names as a contributor, as DPV's files describe them.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["Agent"]
    class_class_curie: ClassVar[str] = "dcterms:Agent"
    class_name: ClassVar[str] = "DpvAgent"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvAgent

    id: Union[str, DpvAgentId] = None
    name: str = None
    homepage: Optional[str] = None
    memberOf: Optional[Union[Union[str, DpvAgentId], list[Union[str, DpvAgentId]]]] = empty_list()
    hasORCID: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvAgentId):
            self.id = DpvAgentId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.homepage is not None and not isinstance(self.homepage, str):
            self.homepage = str(self.homepage)

        if not isinstance(self.memberOf, list):
            self.memberOf = [self.memberOf] if self.memberOf is not None else []
        self.memberOf = [v if isinstance(v, DpvAgentId) else DpvAgentId(v) for v in self.memberOf]

        if self.hasORCID is not None and not isinstance(self.hasORCID, str):
            self.hasORCID = str(self.hasORCID)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvWebPage(YAMLRoot):
    """
    A web page DPV names as a term's source.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SDO["WebPage"]
    class_class_curie: ClassVar[str] = "sdo:WebPage"
    class_name: ClassVar[str] = "DpvWebPage"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvWebPage

    page_name: str = None
    url: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.page_name):
            self.MissingRequiredField("page_name")
        if not isinstance(self.page_name, str):
            self.page_name = str(self.page_name)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvInterval(YAMLRoot):
    """
    A period of time, with the dates that start and end it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TIME["ProperInterval"]
    class_class_curie: ClassVar[str] = "time:ProperInterval"
    class_name: ClassVar[str] = "DpvInterval"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvInterval

    hasBeginning: Optional[Union[str, DpvDate]] = None
    hasEnd: Optional[Union[str, DpvDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.hasBeginning is not None and not isinstance(self.hasBeginning, DpvDate):
            self.hasBeginning = DpvDate(self.hasBeginning)

        if self.hasEnd is not None and not isinstance(self.hasEnd, DpvDate):
            self.hasEnd = DpvDate(self.hasEnd)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvTerm(YAMLRoot):
    """
    One thing DPV's vocabularies state, or a thing a use case describes with them, as a record under its own IRI.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV_LINKML["DpvTerm"]
    class_class_curie: ClassVar[str] = "dpv_linkml:DpvTerm"
    class_name: ClassVar[str] = "DpvTerm"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvTerm

    id: Union[str, DpvTermId] = None
    rdf_type: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    prefLabel: Optional[str] = None
    prefLabel_de: Optional[str] = None
    definition: Optional[str] = None
    definition_de: Optional[str] = None
    scopeNote: Optional[Union[str, list[str]]] = empty_list()
    broader: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    related: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    inScheme: Optional[Union[Union[str, DpvConceptSchemeId], list[Union[str, DpvConceptSchemeId]]]] = empty_list()
    sameAs: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isDefinedBy: Optional[Union[Union[str, DpvVocabularyId], list[Union[str, DpvVocabularyId]]]] = empty_list()
    subClassOf: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    example: Optional[Union[Union[str, DpvExampleId], list[Union[str, DpvExampleId]]]] = empty_list()
    exactMatch: Optional[Union[Union[str, DpvUri], list[Union[str, DpvUri]]]] = empty_list()
    term_status: Optional[Union[str, "DpvTermStatus"]] = None
    created: Optional[Union[Union[str, DpvDate], list[Union[str, DpvDate]]]] = empty_list()
    modified: Optional[Union[str, DpvDate]] = None
    contributor: Optional[Union[Union[str, DpvAgentId], list[Union[str, DpvAgentId]]]] = empty_list()
    source: Optional[Union[str, list[str]]] = empty_list()
    source_page: Optional[Union[Union[dict, DpvWebPage], list[Union[dict, DpvWebPage]]]] = empty_list()
    homepage: Optional[str] = None
    value: Optional[Decimal] = None
    temporal: Optional[Union[dict, DpvInterval]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvTermId):
            self.id = DpvTermId(self.id)

        if not isinstance(self.rdf_type, list):
            self.rdf_type = [self.rdf_type] if self.rdf_type is not None else []
        self.rdf_type = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.rdf_type]

        if self.prefLabel is not None and not isinstance(self.prefLabel, str):
            self.prefLabel = str(self.prefLabel)

        if self.prefLabel_de is not None and not isinstance(self.prefLabel_de, str):
            self.prefLabel_de = str(self.prefLabel_de)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.definition_de is not None and not isinstance(self.definition_de, str):
            self.definition_de = str(self.definition_de)

        if not isinstance(self.scopeNote, list):
            self.scopeNote = [self.scopeNote] if self.scopeNote is not None else []
        self.scopeNote = [v if isinstance(v, str) else str(v) for v in self.scopeNote]

        if not isinstance(self.broader, list):
            self.broader = [self.broader] if self.broader is not None else []
        self.broader = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.broader]

        if not isinstance(self.related, list):
            self.related = [self.related] if self.related is not None else []
        self.related = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.related]

        if not isinstance(self.inScheme, list):
            self.inScheme = [self.inScheme] if self.inScheme is not None else []
        self.inScheme = [v if isinstance(v, DpvConceptSchemeId) else DpvConceptSchemeId(v) for v in self.inScheme]

        if not isinstance(self.sameAs, list):
            self.sameAs = [self.sameAs] if self.sameAs is not None else []
        self.sameAs = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.sameAs]

        if not isinstance(self.isDefinedBy, list):
            self.isDefinedBy = [self.isDefinedBy] if self.isDefinedBy is not None else []
        self.isDefinedBy = [v if isinstance(v, DpvVocabularyId) else DpvVocabularyId(v) for v in self.isDefinedBy]

        if not isinstance(self.subClassOf, list):
            self.subClassOf = [self.subClassOf] if self.subClassOf is not None else []
        self.subClassOf = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.subClassOf]

        if not isinstance(self.example, list):
            self.example = [self.example] if self.example is not None else []
        self.example = [v if isinstance(v, DpvExampleId) else DpvExampleId(v) for v in self.example]

        if not isinstance(self.exactMatch, list):
            self.exactMatch = [self.exactMatch] if self.exactMatch is not None else []
        self.exactMatch = [v if isinstance(v, DpvUri) else DpvUri(v) for v in self.exactMatch]

        if self.term_status is not None and not isinstance(self.term_status, DpvTermStatus):
            self.term_status = DpvTermStatus(self.term_status)

        if not isinstance(self.created, list):
            self.created = [self.created] if self.created is not None else []
        self.created = [v if isinstance(v, DpvDate) else DpvDate(v) for v in self.created]

        if self.modified is not None and not isinstance(self.modified, DpvDate):
            self.modified = DpvDate(self.modified)

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, DpvAgentId) else DpvAgentId(v) for v in self.contributor]

        if not isinstance(self.source, list):
            self.source = [self.source] if self.source is not None else []
        self.source = [v if isinstance(v, str) else str(v) for v in self.source]

        self._normalize_inlined_as_list(slot_name="source_page", slot_type=DpvWebPage, key_name="page_name", keyed=False)

        if self.homepage is not None and not isinstance(self.homepage, str):
            self.homepage = str(self.homepage)

        if self.value is not None and not isinstance(self.value, Decimal):
            self.value = Decimal(self.value)

        if self.temporal is not None and not isinstance(self.temporal, DpvInterval):
            self.temporal = DpvInterval(**as_dict(self.temporal))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvConcept(DpvTerm):
    """
    A term DPV states as a concept and a class. Its rdf_type names the concepts it is an instance of, each a class of
    this schema, where DPV states one.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["Concept"]
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "DpvConcept"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvConcept

    id: Union[str, DpvConceptId] = None
    eu_aiact_hasRiskLevel: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasApplicableLaw: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasAuthority: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasHumanDescription: Optional[Union[str, list[str]]] = empty_list()
    hasInverseJurisdiction: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasJurisdiction: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasJustification: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasLikelihood: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasObligation: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasPermission: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasProhibition: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRight: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRiskLevel: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasSeverity: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    iso_alpha2: Optional[Union[str, list[str]]] = empty_list()
    iso_alpha3: Optional[Union[str, list[str]]] = empty_list()
    iso_numeric: Optional[Union[str, list[str]]] = empty_list()
    un_m49: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvConceptId):
            self.id = DpvConceptId(self.id)

        if not isinstance(self.eu_aiact_hasRiskLevel, list):
            self.eu_aiact_hasRiskLevel = [self.eu_aiact_hasRiskLevel] if self.eu_aiact_hasRiskLevel is not None else []
        self.eu_aiact_hasRiskLevel = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.eu_aiact_hasRiskLevel]

        if not isinstance(self.hasApplicableLaw, list):
            self.hasApplicableLaw = [self.hasApplicableLaw] if self.hasApplicableLaw is not None else []
        self.hasApplicableLaw = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasApplicableLaw]

        if not isinstance(self.hasAuthority, list):
            self.hasAuthority = [self.hasAuthority] if self.hasAuthority is not None else []
        self.hasAuthority = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAuthority]

        if not isinstance(self.hasHumanDescription, list):
            self.hasHumanDescription = [self.hasHumanDescription] if self.hasHumanDescription is not None else []
        self.hasHumanDescription = [v if isinstance(v, str) else str(v) for v in self.hasHumanDescription]

        if not isinstance(self.hasInverseJurisdiction, list):
            self.hasInverseJurisdiction = [self.hasInverseJurisdiction] if self.hasInverseJurisdiction is not None else []
        self.hasInverseJurisdiction = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasInverseJurisdiction]

        if not isinstance(self.hasJurisdiction, list):
            self.hasJurisdiction = [self.hasJurisdiction] if self.hasJurisdiction is not None else []
        self.hasJurisdiction = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasJurisdiction]

        if not isinstance(self.hasJustification, list):
            self.hasJustification = [self.hasJustification] if self.hasJustification is not None else []
        self.hasJustification = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasJustification]

        if not isinstance(self.hasLikelihood, list):
            self.hasLikelihood = [self.hasLikelihood] if self.hasLikelihood is not None else []
        self.hasLikelihood = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasLikelihood]

        if not isinstance(self.hasObligation, list):
            self.hasObligation = [self.hasObligation] if self.hasObligation is not None else []
        self.hasObligation = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasObligation]

        if not isinstance(self.hasPermission, list):
            self.hasPermission = [self.hasPermission] if self.hasPermission is not None else []
        self.hasPermission = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasPermission]

        if not isinstance(self.hasProhibition, list):
            self.hasProhibition = [self.hasProhibition] if self.hasProhibition is not None else []
        self.hasProhibition = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasProhibition]

        if not isinstance(self.hasRight, list):
            self.hasRight = [self.hasRight] if self.hasRight is not None else []
        self.hasRight = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRight]

        if not isinstance(self.hasRiskLevel, list):
            self.hasRiskLevel = [self.hasRiskLevel] if self.hasRiskLevel is not None else []
        self.hasRiskLevel = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRiskLevel]

        if not isinstance(self.hasSeverity, list):
            self.hasSeverity = [self.hasSeverity] if self.hasSeverity is not None else []
        self.hasSeverity = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasSeverity]

        if not isinstance(self.iso_alpha2, list):
            self.iso_alpha2 = [self.iso_alpha2] if self.iso_alpha2 is not None else []
        self.iso_alpha2 = [v if isinstance(v, str) else str(v) for v in self.iso_alpha2]

        if not isinstance(self.iso_alpha3, list):
            self.iso_alpha3 = [self.iso_alpha3] if self.iso_alpha3 is not None else []
        self.iso_alpha3 = [v if isinstance(v, str) else str(v) for v in self.iso_alpha3]

        if not isinstance(self.iso_numeric, list):
            self.iso_numeric = [self.iso_numeric] if self.iso_numeric is not None else []
        self.iso_numeric = [v if isinstance(v, str) else str(v) for v in self.iso_numeric]

        if not isinstance(self.un_m49, list):
            self.un_m49 = [self.un_m49] if self.un_m49 is not None else []
        self.un_m49 = [v if isinstance(v, str) else str(v) for v in self.un_m49]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvProperty(DpvTerm):
    """
    A property DPV states, with the classes it names as its usual subjects and values. Every property is also a slot
    of DpvResource.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF["Property"]
    class_class_curie: ClassVar[str] = "rdf:Property"
    class_name: ClassVar[str] = "DpvProperty"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvProperty

    id: Union[str, DpvPropertyId] = None
    subPropertyOf: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    domainIncludes: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    rangeIncludes: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPropertyId):
            self.id = DpvPropertyId(self.id)

        if not isinstance(self.subPropertyOf, list):
            self.subPropertyOf = [self.subPropertyOf] if self.subPropertyOf is not None else []
        self.subPropertyOf = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.subPropertyOf]

        if not isinstance(self.domainIncludes, list):
            self.domainIncludes = [self.domainIncludes] if self.domainIncludes is not None else []
        self.domainIncludes = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.domainIncludes]

        if not isinstance(self.rangeIncludes, list):
            self.rangeIncludes = [self.rangeIncludes] if self.rangeIncludes is not None else []
        self.rangeIncludes = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.rangeIncludes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvResource(DpvTerm):
    """
    A thing a use case describes with DPV, such as a process, holding any DPV property, because DPV states none as
    limited to a class.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS["Resource"]
    class_class_curie: ClassVar[str] = "rdfs:Resource"
    class_name: ClassVar[str] = "DpvResource"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvResource

    id: Union[str, DpvResourceId] = None
    accessRights: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    ai_hasCapability: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    ai_hasData: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    ai_hasModel: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    avoids: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    causedByThreat: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    causedByVulnerability: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    conformsTo: Optional[Union[str, list[str]]] = empty_list()
    contains: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    controls: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    coverage: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    dateAccepted: Optional[Union[str, list[str]]] = empty_list()
    dateSubmitted: Optional[Union[str, list[str]]] = empty_list()
    de_gdng_hasDataHolder: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    description: Optional[str] = None
    detects: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    eliminates: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    eu_aiact_hasRiskLevel: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    eu_dga_hasDataHolder: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    exploitsVulnerability: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    format: Optional[Union[str, list[str]]] = empty_list()
    hasAI: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasAISystem: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasAPI: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasActiveEntity: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasActivityStatus: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasActor: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasAddress: Optional[Union[str, list[str]]] = empty_list()
    hasAgent: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasAgentBehaviour: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasAgreement: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasAgreementPreference: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasAgreementRegistry: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasAlgorithm: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasAlgorithmicLogic: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasApplicability: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasApplicableLaw: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasApplication: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasAssessment: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasAuditStatus: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasAuditor: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasAuthority: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasAutomationLevel: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasChangeCategory: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasChangeDescription: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasCommunicationMechanism: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasComplianceStatus: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasComponent: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasConcernedSA: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasConflictResolution: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasConformanceStatus: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasConsentControl: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasConsentStatus: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasConsequence: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasConsequenceOn: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasContact: Optional[Union[str, list[str]]] = empty_list()
    hasContext: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasContractControl: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasContractStatus: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasContractualClause: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasContractualFulfilmentStatus: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasControl: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasCountry: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasCustomer: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDAO: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDISP: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasData: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDataController: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDataExporter: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDataImporter: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDataProcessor: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDataProtectionOfficer: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDataReuseAssistant: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDataSharingTerm: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDataSource: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDataSubject: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDataSubjectScale: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDataUser: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDataVolume: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDeonticInterpretation: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDeployer: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDeploymentLocation: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDesigner: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDeterrence: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDeveloper: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDevice: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDocumentation: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasDuration: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasEndpoint: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasEntity: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasEntityControl: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasEntityInvolvement: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasEstablishment: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasEvaluator: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasExpectation: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasFee: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasFirstParty: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasFrequency: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasFulfilmentStatus: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasFunction: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasGPAIModel: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasGeographicCoverage: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasHardware: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasHumanDescription: Optional[Union[str, list[str]]] = empty_list()
    hasHumanInvolvement: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasHumanReadableFormat: Optional[Union[str, list[str]]] = empty_list()
    hasHumanSubject: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasIdentifier: Optional[Union[str, list[str]]] = empty_list()
    hasImpact: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasImpactAssessment: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasImpactOn: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasImportance: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasIncident: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasIndicationMethod: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasInformedStatus: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasInfrastructure: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasInput: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasInputAction: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasInputData: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasInstaller: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasIntendedUse: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasIntention: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasInverseJurisdiction: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasInvolvement: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasJointDataControllers: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasJurisdiction: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasJustification: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasLawfulness: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasLeadSA: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasLegalBasis: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasLegalMeasure: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasLicense: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasLifecycleStage: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasLikelihood: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasLocalSA: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasLocation: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasMachineReadableFormat: Optional[Union[str, list[str]]] = empty_list()
    hasMainEstablishment: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasMaintainer: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasManufacturer: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasMarketAvailabilityStatus: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasName: Optional[Union[str, list[str]]] = empty_list()
    hasNecessity: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasNonInvolvedEntity: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasNonPersonalDataProcess: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasNotice: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasNoticeIcon: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasNoticeLayer: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasNoticeStatus: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasNotificationStatus: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasObligation: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasOperatingEnvironment: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasOperatingFactor: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasOrganisationalMeasure: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasOrganisationalUnit: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasOutcome: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasOutput: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasOutputAction: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasOutputData: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasOwner: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasPart: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasPartner: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasParty: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasPassiveEntity: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasPermission: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasPersonalData: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasPersonalDataHandling: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasPersonalDataProcess: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasPhysicalMeasure: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasPlatform: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasPolicy: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasPortabilityTerm: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasPreferenceApplicability: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasProcess: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasProcessing: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasProcessingCondition: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasProcessingScale: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasProducer: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasProfilingTerm: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasProhibition: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasProvider: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasProvisionMethod: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasProvisionStatus: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasPurchaser: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasPurpose: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRecipient: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRecipientDataController: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRecipientThirdParty: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRecommendation: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRecordOfActivity: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRelationWithDataSubject: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRepresentative: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRequestStatus: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasResidualRisk: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasResponsibleEntity: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasReuseCompatibility: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRight: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRisk: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRiskAcceptance: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRiskAnalysis: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRiskAssessment: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRiskCriteria: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRiskEvaluation: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRiskIdentification: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRiskLevel: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRiskManagement: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRiskOwner: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRiskPerception: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRiskSource: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRiskTreatment: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasRule: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasScale: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasScope: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasSecondParty: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasSector: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasSensitivityLevel: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasService: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasServiceConsumer: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasServiceProvider: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasSeverity: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasSoftware: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasStatus: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasStorageCondition: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasSubject: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasSubsidiary: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasSupplier: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasSystem: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasSystemIntegrator: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasTRL: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasTechnicalMeasure: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasTechnicalOrganisationalMeasure: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasTechnique: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasTestingData: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasThirdCountry: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasThirdParty: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasThreatSource: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasTrackingTerm: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasTrainingData: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasTransparencyTerm: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasUncategorisedData: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasUnstructuredData: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasUser: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasValidationData: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    hasVulnerability: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    identifier: Optional[str] = None
    identifies: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    ieee_7012_hasParty: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    ieee_7012_hasThirdParty: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    interrupts: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    intervenes: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    investigates: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isAfter: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isApplicableFor: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isAuthorityFor: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isBefore: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isComponentOf: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isDeterminedByEntity: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isDuring: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isExercisedAt: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isExploitedBy: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isImplementedByEntity: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isImplementedUsingTechnology: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isIndicatedAtTime: Optional[Union[str, list[str]]] = empty_list()
    isIndicatedBy: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isMainEstablishmentFor: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isMitigatedByMeasure: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isNotApplicableFor: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isOrganisationalUnitOf: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isOutsideOfLocation: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isPartOf: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isPolicyFor: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isRepresentativeFor: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isResidualRiskOf: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isSubsidiaryOf: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isVersionOf: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    isVulnerabilityOf: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    iso_alpha2: Optional[Union[str, list[str]]] = empty_list()
    iso_alpha3: Optional[Union[str, list[str]]] = empty_list()
    iso_numeric: Optional[Union[str, list[str]]] = empty_list()
    logs: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    mitigates: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    mitigatesRisk: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    modifies: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    monitors: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    overrides: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    page: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    recovers: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    reduces: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    refersToRisk: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    remedies: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    resolves: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    reverses: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    risk_hasRiskAssessment: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    shares: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    subject: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    substitutes: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    supportsComplianceWith: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    tech_hasCapability: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    tech_hasModel: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    tech_hasService: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    title: Optional[str] = None
    transfers: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    un_m49: Optional[Union[str, list[str]]] = empty_list()
    valid: Optional[Union[str, list[str]]] = empty_list()
    statements: Optional[Union[Union[dict, "DpvStatement"], list[Union[dict, "DpvStatement"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvResourceId):
            self.id = DpvResourceId(self.id)

        if not isinstance(self.accessRights, list):
            self.accessRights = [self.accessRights] if self.accessRights is not None else []
        self.accessRights = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.accessRights]

        if not isinstance(self.ai_hasCapability, list):
            self.ai_hasCapability = [self.ai_hasCapability] if self.ai_hasCapability is not None else []
        self.ai_hasCapability = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.ai_hasCapability]

        if not isinstance(self.ai_hasData, list):
            self.ai_hasData = [self.ai_hasData] if self.ai_hasData is not None else []
        self.ai_hasData = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.ai_hasData]

        if not isinstance(self.ai_hasModel, list):
            self.ai_hasModel = [self.ai_hasModel] if self.ai_hasModel is not None else []
        self.ai_hasModel = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.ai_hasModel]

        if not isinstance(self.avoids, list):
            self.avoids = [self.avoids] if self.avoids is not None else []
        self.avoids = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.avoids]

        if not isinstance(self.causedByThreat, list):
            self.causedByThreat = [self.causedByThreat] if self.causedByThreat is not None else []
        self.causedByThreat = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.causedByThreat]

        if not isinstance(self.causedByVulnerability, list):
            self.causedByVulnerability = [self.causedByVulnerability] if self.causedByVulnerability is not None else []
        self.causedByVulnerability = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.causedByVulnerability]

        if not isinstance(self.conformsTo, list):
            self.conformsTo = [self.conformsTo] if self.conformsTo is not None else []
        self.conformsTo = [v if isinstance(v, str) else str(v) for v in self.conformsTo]

        if not isinstance(self.contains, list):
            self.contains = [self.contains] if self.contains is not None else []
        self.contains = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.contains]

        if not isinstance(self.controls, list):
            self.controls = [self.controls] if self.controls is not None else []
        self.controls = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.controls]

        if not isinstance(self.coverage, list):
            self.coverage = [self.coverage] if self.coverage is not None else []
        self.coverage = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.coverage]

        if not isinstance(self.dateAccepted, list):
            self.dateAccepted = [self.dateAccepted] if self.dateAccepted is not None else []
        self.dateAccepted = [v if isinstance(v, str) else str(v) for v in self.dateAccepted]

        if not isinstance(self.dateSubmitted, list):
            self.dateSubmitted = [self.dateSubmitted] if self.dateSubmitted is not None else []
        self.dateSubmitted = [v if isinstance(v, str) else str(v) for v in self.dateSubmitted]

        if not isinstance(self.de_gdng_hasDataHolder, list):
            self.de_gdng_hasDataHolder = [self.de_gdng_hasDataHolder] if self.de_gdng_hasDataHolder is not None else []
        self.de_gdng_hasDataHolder = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.de_gdng_hasDataHolder]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.detects, list):
            self.detects = [self.detects] if self.detects is not None else []
        self.detects = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.detects]

        if not isinstance(self.eliminates, list):
            self.eliminates = [self.eliminates] if self.eliminates is not None else []
        self.eliminates = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.eliminates]

        if not isinstance(self.eu_aiact_hasRiskLevel, list):
            self.eu_aiact_hasRiskLevel = [self.eu_aiact_hasRiskLevel] if self.eu_aiact_hasRiskLevel is not None else []
        self.eu_aiact_hasRiskLevel = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.eu_aiact_hasRiskLevel]

        if not isinstance(self.eu_dga_hasDataHolder, list):
            self.eu_dga_hasDataHolder = [self.eu_dga_hasDataHolder] if self.eu_dga_hasDataHolder is not None else []
        self.eu_dga_hasDataHolder = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.eu_dga_hasDataHolder]

        if not isinstance(self.exploitsVulnerability, list):
            self.exploitsVulnerability = [self.exploitsVulnerability] if self.exploitsVulnerability is not None else []
        self.exploitsVulnerability = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.exploitsVulnerability]

        if not isinstance(self.format, list):
            self.format = [self.format] if self.format is not None else []
        self.format = [v if isinstance(v, str) else str(v) for v in self.format]

        if not isinstance(self.hasAI, list):
            self.hasAI = [self.hasAI] if self.hasAI is not None else []
        self.hasAI = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAI]

        if not isinstance(self.hasAISystem, list):
            self.hasAISystem = [self.hasAISystem] if self.hasAISystem is not None else []
        self.hasAISystem = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAISystem]

        if not isinstance(self.hasAPI, list):
            self.hasAPI = [self.hasAPI] if self.hasAPI is not None else []
        self.hasAPI = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAPI]

        if not isinstance(self.hasActiveEntity, list):
            self.hasActiveEntity = [self.hasActiveEntity] if self.hasActiveEntity is not None else []
        self.hasActiveEntity = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasActiveEntity]

        if not isinstance(self.hasActivityStatus, list):
            self.hasActivityStatus = [self.hasActivityStatus] if self.hasActivityStatus is not None else []
        self.hasActivityStatus = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasActivityStatus]

        if not isinstance(self.hasActor, list):
            self.hasActor = [self.hasActor] if self.hasActor is not None else []
        self.hasActor = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasActor]

        if not isinstance(self.hasAddress, list):
            self.hasAddress = [self.hasAddress] if self.hasAddress is not None else []
        self.hasAddress = [v if isinstance(v, str) else str(v) for v in self.hasAddress]

        if not isinstance(self.hasAgent, list):
            self.hasAgent = [self.hasAgent] if self.hasAgent is not None else []
        self.hasAgent = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAgent]

        if not isinstance(self.hasAgentBehaviour, list):
            self.hasAgentBehaviour = [self.hasAgentBehaviour] if self.hasAgentBehaviour is not None else []
        self.hasAgentBehaviour = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAgentBehaviour]

        if not isinstance(self.hasAgreement, list):
            self.hasAgreement = [self.hasAgreement] if self.hasAgreement is not None else []
        self.hasAgreement = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAgreement]

        if not isinstance(self.hasAgreementPreference, list):
            self.hasAgreementPreference = [self.hasAgreementPreference] if self.hasAgreementPreference is not None else []
        self.hasAgreementPreference = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAgreementPreference]

        if not isinstance(self.hasAgreementRegistry, list):
            self.hasAgreementRegistry = [self.hasAgreementRegistry] if self.hasAgreementRegistry is not None else []
        self.hasAgreementRegistry = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAgreementRegistry]

        if not isinstance(self.hasAlgorithm, list):
            self.hasAlgorithm = [self.hasAlgorithm] if self.hasAlgorithm is not None else []
        self.hasAlgorithm = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAlgorithm]

        if not isinstance(self.hasAlgorithmicLogic, list):
            self.hasAlgorithmicLogic = [self.hasAlgorithmicLogic] if self.hasAlgorithmicLogic is not None else []
        self.hasAlgorithmicLogic = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAlgorithmicLogic]

        if not isinstance(self.hasApplicability, list):
            self.hasApplicability = [self.hasApplicability] if self.hasApplicability is not None else []
        self.hasApplicability = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasApplicability]

        if not isinstance(self.hasApplicableLaw, list):
            self.hasApplicableLaw = [self.hasApplicableLaw] if self.hasApplicableLaw is not None else []
        self.hasApplicableLaw = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasApplicableLaw]

        if not isinstance(self.hasApplication, list):
            self.hasApplication = [self.hasApplication] if self.hasApplication is not None else []
        self.hasApplication = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasApplication]

        if not isinstance(self.hasAssessment, list):
            self.hasAssessment = [self.hasAssessment] if self.hasAssessment is not None else []
        self.hasAssessment = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAssessment]

        if not isinstance(self.hasAuditStatus, list):
            self.hasAuditStatus = [self.hasAuditStatus] if self.hasAuditStatus is not None else []
        self.hasAuditStatus = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAuditStatus]

        if not isinstance(self.hasAuditor, list):
            self.hasAuditor = [self.hasAuditor] if self.hasAuditor is not None else []
        self.hasAuditor = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAuditor]

        if not isinstance(self.hasAuthority, list):
            self.hasAuthority = [self.hasAuthority] if self.hasAuthority is not None else []
        self.hasAuthority = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAuthority]

        if not isinstance(self.hasAutomationLevel, list):
            self.hasAutomationLevel = [self.hasAutomationLevel] if self.hasAutomationLevel is not None else []
        self.hasAutomationLevel = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasAutomationLevel]

        if not isinstance(self.hasChangeCategory, list):
            self.hasChangeCategory = [self.hasChangeCategory] if self.hasChangeCategory is not None else []
        self.hasChangeCategory = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasChangeCategory]

        if not isinstance(self.hasChangeDescription, list):
            self.hasChangeDescription = [self.hasChangeDescription] if self.hasChangeDescription is not None else []
        self.hasChangeDescription = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasChangeDescription]

        if not isinstance(self.hasCommunicationMechanism, list):
            self.hasCommunicationMechanism = [self.hasCommunicationMechanism] if self.hasCommunicationMechanism is not None else []
        self.hasCommunicationMechanism = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasCommunicationMechanism]

        if not isinstance(self.hasComplianceStatus, list):
            self.hasComplianceStatus = [self.hasComplianceStatus] if self.hasComplianceStatus is not None else []
        self.hasComplianceStatus = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasComplianceStatus]

        if not isinstance(self.hasComponent, list):
            self.hasComponent = [self.hasComponent] if self.hasComponent is not None else []
        self.hasComponent = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasComponent]

        if not isinstance(self.hasConcernedSA, list):
            self.hasConcernedSA = [self.hasConcernedSA] if self.hasConcernedSA is not None else []
        self.hasConcernedSA = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasConcernedSA]

        if not isinstance(self.hasConflictResolution, list):
            self.hasConflictResolution = [self.hasConflictResolution] if self.hasConflictResolution is not None else []
        self.hasConflictResolution = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasConflictResolution]

        if not isinstance(self.hasConformanceStatus, list):
            self.hasConformanceStatus = [self.hasConformanceStatus] if self.hasConformanceStatus is not None else []
        self.hasConformanceStatus = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasConformanceStatus]

        if not isinstance(self.hasConsentControl, list):
            self.hasConsentControl = [self.hasConsentControl] if self.hasConsentControl is not None else []
        self.hasConsentControl = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasConsentControl]

        if not isinstance(self.hasConsentStatus, list):
            self.hasConsentStatus = [self.hasConsentStatus] if self.hasConsentStatus is not None else []
        self.hasConsentStatus = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasConsentStatus]

        if not isinstance(self.hasConsequence, list):
            self.hasConsequence = [self.hasConsequence] if self.hasConsequence is not None else []
        self.hasConsequence = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasConsequence]

        if not isinstance(self.hasConsequenceOn, list):
            self.hasConsequenceOn = [self.hasConsequenceOn] if self.hasConsequenceOn is not None else []
        self.hasConsequenceOn = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasConsequenceOn]

        if not isinstance(self.hasContact, list):
            self.hasContact = [self.hasContact] if self.hasContact is not None else []
        self.hasContact = [v if isinstance(v, str) else str(v) for v in self.hasContact]

        if not isinstance(self.hasContext, list):
            self.hasContext = [self.hasContext] if self.hasContext is not None else []
        self.hasContext = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasContext]

        if not isinstance(self.hasContractControl, list):
            self.hasContractControl = [self.hasContractControl] if self.hasContractControl is not None else []
        self.hasContractControl = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasContractControl]

        if not isinstance(self.hasContractStatus, list):
            self.hasContractStatus = [self.hasContractStatus] if self.hasContractStatus is not None else []
        self.hasContractStatus = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasContractStatus]

        if not isinstance(self.hasContractualClause, list):
            self.hasContractualClause = [self.hasContractualClause] if self.hasContractualClause is not None else []
        self.hasContractualClause = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasContractualClause]

        if not isinstance(self.hasContractualFulfilmentStatus, list):
            self.hasContractualFulfilmentStatus = [self.hasContractualFulfilmentStatus] if self.hasContractualFulfilmentStatus is not None else []
        self.hasContractualFulfilmentStatus = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasContractualFulfilmentStatus]

        if not isinstance(self.hasControl, list):
            self.hasControl = [self.hasControl] if self.hasControl is not None else []
        self.hasControl = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasControl]

        if not isinstance(self.hasCountry, list):
            self.hasCountry = [self.hasCountry] if self.hasCountry is not None else []
        self.hasCountry = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasCountry]

        if not isinstance(self.hasCustomer, list):
            self.hasCustomer = [self.hasCustomer] if self.hasCustomer is not None else []
        self.hasCustomer = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasCustomer]

        if not isinstance(self.hasDAO, list):
            self.hasDAO = [self.hasDAO] if self.hasDAO is not None else []
        self.hasDAO = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDAO]

        if not isinstance(self.hasDISP, list):
            self.hasDISP = [self.hasDISP] if self.hasDISP is not None else []
        self.hasDISP = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDISP]

        if not isinstance(self.hasData, list):
            self.hasData = [self.hasData] if self.hasData is not None else []
        self.hasData = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasData]

        if not isinstance(self.hasDataController, list):
            self.hasDataController = [self.hasDataController] if self.hasDataController is not None else []
        self.hasDataController = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDataController]

        if not isinstance(self.hasDataExporter, list):
            self.hasDataExporter = [self.hasDataExporter] if self.hasDataExporter is not None else []
        self.hasDataExporter = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDataExporter]

        if not isinstance(self.hasDataImporter, list):
            self.hasDataImporter = [self.hasDataImporter] if self.hasDataImporter is not None else []
        self.hasDataImporter = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDataImporter]

        if not isinstance(self.hasDataProcessor, list):
            self.hasDataProcessor = [self.hasDataProcessor] if self.hasDataProcessor is not None else []
        self.hasDataProcessor = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDataProcessor]

        if not isinstance(self.hasDataProtectionOfficer, list):
            self.hasDataProtectionOfficer = [self.hasDataProtectionOfficer] if self.hasDataProtectionOfficer is not None else []
        self.hasDataProtectionOfficer = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDataProtectionOfficer]

        if not isinstance(self.hasDataReuseAssistant, list):
            self.hasDataReuseAssistant = [self.hasDataReuseAssistant] if self.hasDataReuseAssistant is not None else []
        self.hasDataReuseAssistant = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDataReuseAssistant]

        if not isinstance(self.hasDataSharingTerm, list):
            self.hasDataSharingTerm = [self.hasDataSharingTerm] if self.hasDataSharingTerm is not None else []
        self.hasDataSharingTerm = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDataSharingTerm]

        if not isinstance(self.hasDataSource, list):
            self.hasDataSource = [self.hasDataSource] if self.hasDataSource is not None else []
        self.hasDataSource = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDataSource]

        if not isinstance(self.hasDataSubject, list):
            self.hasDataSubject = [self.hasDataSubject] if self.hasDataSubject is not None else []
        self.hasDataSubject = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDataSubject]

        if not isinstance(self.hasDataSubjectScale, list):
            self.hasDataSubjectScale = [self.hasDataSubjectScale] if self.hasDataSubjectScale is not None else []
        self.hasDataSubjectScale = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDataSubjectScale]

        if not isinstance(self.hasDataUser, list):
            self.hasDataUser = [self.hasDataUser] if self.hasDataUser is not None else []
        self.hasDataUser = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDataUser]

        if not isinstance(self.hasDataVolume, list):
            self.hasDataVolume = [self.hasDataVolume] if self.hasDataVolume is not None else []
        self.hasDataVolume = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDataVolume]

        if not isinstance(self.hasDeonticInterpretation, list):
            self.hasDeonticInterpretation = [self.hasDeonticInterpretation] if self.hasDeonticInterpretation is not None else []
        self.hasDeonticInterpretation = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDeonticInterpretation]

        if not isinstance(self.hasDeployer, list):
            self.hasDeployer = [self.hasDeployer] if self.hasDeployer is not None else []
        self.hasDeployer = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDeployer]

        if not isinstance(self.hasDeploymentLocation, list):
            self.hasDeploymentLocation = [self.hasDeploymentLocation] if self.hasDeploymentLocation is not None else []
        self.hasDeploymentLocation = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDeploymentLocation]

        if not isinstance(self.hasDesigner, list):
            self.hasDesigner = [self.hasDesigner] if self.hasDesigner is not None else []
        self.hasDesigner = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDesigner]

        if not isinstance(self.hasDeterrence, list):
            self.hasDeterrence = [self.hasDeterrence] if self.hasDeterrence is not None else []
        self.hasDeterrence = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDeterrence]

        if not isinstance(self.hasDeveloper, list):
            self.hasDeveloper = [self.hasDeveloper] if self.hasDeveloper is not None else []
        self.hasDeveloper = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDeveloper]

        if not isinstance(self.hasDevice, list):
            self.hasDevice = [self.hasDevice] if self.hasDevice is not None else []
        self.hasDevice = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDevice]

        if not isinstance(self.hasDocumentation, list):
            self.hasDocumentation = [self.hasDocumentation] if self.hasDocumentation is not None else []
        self.hasDocumentation = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDocumentation]

        if not isinstance(self.hasDuration, list):
            self.hasDuration = [self.hasDuration] if self.hasDuration is not None else []
        self.hasDuration = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasDuration]

        if not isinstance(self.hasEndpoint, list):
            self.hasEndpoint = [self.hasEndpoint] if self.hasEndpoint is not None else []
        self.hasEndpoint = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasEndpoint]

        if not isinstance(self.hasEntity, list):
            self.hasEntity = [self.hasEntity] if self.hasEntity is not None else []
        self.hasEntity = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasEntity]

        if not isinstance(self.hasEntityControl, list):
            self.hasEntityControl = [self.hasEntityControl] if self.hasEntityControl is not None else []
        self.hasEntityControl = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasEntityControl]

        if not isinstance(self.hasEntityInvolvement, list):
            self.hasEntityInvolvement = [self.hasEntityInvolvement] if self.hasEntityInvolvement is not None else []
        self.hasEntityInvolvement = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasEntityInvolvement]

        if not isinstance(self.hasEstablishment, list):
            self.hasEstablishment = [self.hasEstablishment] if self.hasEstablishment is not None else []
        self.hasEstablishment = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasEstablishment]

        if not isinstance(self.hasEvaluator, list):
            self.hasEvaluator = [self.hasEvaluator] if self.hasEvaluator is not None else []
        self.hasEvaluator = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasEvaluator]

        if not isinstance(self.hasExpectation, list):
            self.hasExpectation = [self.hasExpectation] if self.hasExpectation is not None else []
        self.hasExpectation = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasExpectation]

        if not isinstance(self.hasFee, list):
            self.hasFee = [self.hasFee] if self.hasFee is not None else []
        self.hasFee = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasFee]

        if not isinstance(self.hasFirstParty, list):
            self.hasFirstParty = [self.hasFirstParty] if self.hasFirstParty is not None else []
        self.hasFirstParty = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasFirstParty]

        if not isinstance(self.hasFrequency, list):
            self.hasFrequency = [self.hasFrequency] if self.hasFrequency is not None else []
        self.hasFrequency = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasFrequency]

        if not isinstance(self.hasFulfilmentStatus, list):
            self.hasFulfilmentStatus = [self.hasFulfilmentStatus] if self.hasFulfilmentStatus is not None else []
        self.hasFulfilmentStatus = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasFulfilmentStatus]

        if not isinstance(self.hasFunction, list):
            self.hasFunction = [self.hasFunction] if self.hasFunction is not None else []
        self.hasFunction = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasFunction]

        if not isinstance(self.hasGPAIModel, list):
            self.hasGPAIModel = [self.hasGPAIModel] if self.hasGPAIModel is not None else []
        self.hasGPAIModel = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasGPAIModel]

        if not isinstance(self.hasGeographicCoverage, list):
            self.hasGeographicCoverage = [self.hasGeographicCoverage] if self.hasGeographicCoverage is not None else []
        self.hasGeographicCoverage = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasGeographicCoverage]

        if not isinstance(self.hasHardware, list):
            self.hasHardware = [self.hasHardware] if self.hasHardware is not None else []
        self.hasHardware = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasHardware]

        if not isinstance(self.hasHumanDescription, list):
            self.hasHumanDescription = [self.hasHumanDescription] if self.hasHumanDescription is not None else []
        self.hasHumanDescription = [v if isinstance(v, str) else str(v) for v in self.hasHumanDescription]

        if not isinstance(self.hasHumanInvolvement, list):
            self.hasHumanInvolvement = [self.hasHumanInvolvement] if self.hasHumanInvolvement is not None else []
        self.hasHumanInvolvement = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasHumanInvolvement]

        if not isinstance(self.hasHumanReadableFormat, list):
            self.hasHumanReadableFormat = [self.hasHumanReadableFormat] if self.hasHumanReadableFormat is not None else []
        self.hasHumanReadableFormat = [v if isinstance(v, str) else str(v) for v in self.hasHumanReadableFormat]

        if not isinstance(self.hasHumanSubject, list):
            self.hasHumanSubject = [self.hasHumanSubject] if self.hasHumanSubject is not None else []
        self.hasHumanSubject = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasHumanSubject]

        if not isinstance(self.hasIdentifier, list):
            self.hasIdentifier = [self.hasIdentifier] if self.hasIdentifier is not None else []
        self.hasIdentifier = [v if isinstance(v, str) else str(v) for v in self.hasIdentifier]

        if not isinstance(self.hasImpact, list):
            self.hasImpact = [self.hasImpact] if self.hasImpact is not None else []
        self.hasImpact = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasImpact]

        if not isinstance(self.hasImpactAssessment, list):
            self.hasImpactAssessment = [self.hasImpactAssessment] if self.hasImpactAssessment is not None else []
        self.hasImpactAssessment = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasImpactAssessment]

        if not isinstance(self.hasImpactOn, list):
            self.hasImpactOn = [self.hasImpactOn] if self.hasImpactOn is not None else []
        self.hasImpactOn = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasImpactOn]

        if not isinstance(self.hasImportance, list):
            self.hasImportance = [self.hasImportance] if self.hasImportance is not None else []
        self.hasImportance = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasImportance]

        if not isinstance(self.hasIncident, list):
            self.hasIncident = [self.hasIncident] if self.hasIncident is not None else []
        self.hasIncident = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasIncident]

        if not isinstance(self.hasIndicationMethod, list):
            self.hasIndicationMethod = [self.hasIndicationMethod] if self.hasIndicationMethod is not None else []
        self.hasIndicationMethod = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasIndicationMethod]

        if not isinstance(self.hasInformedStatus, list):
            self.hasInformedStatus = [self.hasInformedStatus] if self.hasInformedStatus is not None else []
        self.hasInformedStatus = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasInformedStatus]

        if not isinstance(self.hasInfrastructure, list):
            self.hasInfrastructure = [self.hasInfrastructure] if self.hasInfrastructure is not None else []
        self.hasInfrastructure = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasInfrastructure]

        if not isinstance(self.hasInput, list):
            self.hasInput = [self.hasInput] if self.hasInput is not None else []
        self.hasInput = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasInput]

        if not isinstance(self.hasInputAction, list):
            self.hasInputAction = [self.hasInputAction] if self.hasInputAction is not None else []
        self.hasInputAction = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasInputAction]

        if not isinstance(self.hasInputData, list):
            self.hasInputData = [self.hasInputData] if self.hasInputData is not None else []
        self.hasInputData = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasInputData]

        if not isinstance(self.hasInstaller, list):
            self.hasInstaller = [self.hasInstaller] if self.hasInstaller is not None else []
        self.hasInstaller = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasInstaller]

        if not isinstance(self.hasIntendedUse, list):
            self.hasIntendedUse = [self.hasIntendedUse] if self.hasIntendedUse is not None else []
        self.hasIntendedUse = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasIntendedUse]

        if not isinstance(self.hasIntention, list):
            self.hasIntention = [self.hasIntention] if self.hasIntention is not None else []
        self.hasIntention = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasIntention]

        if not isinstance(self.hasInverseJurisdiction, list):
            self.hasInverseJurisdiction = [self.hasInverseJurisdiction] if self.hasInverseJurisdiction is not None else []
        self.hasInverseJurisdiction = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasInverseJurisdiction]

        if not isinstance(self.hasInvolvement, list):
            self.hasInvolvement = [self.hasInvolvement] if self.hasInvolvement is not None else []
        self.hasInvolvement = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasInvolvement]

        if not isinstance(self.hasJointDataControllers, list):
            self.hasJointDataControllers = [self.hasJointDataControllers] if self.hasJointDataControllers is not None else []
        self.hasJointDataControllers = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasJointDataControllers]

        if not isinstance(self.hasJurisdiction, list):
            self.hasJurisdiction = [self.hasJurisdiction] if self.hasJurisdiction is not None else []
        self.hasJurisdiction = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasJurisdiction]

        if not isinstance(self.hasJustification, list):
            self.hasJustification = [self.hasJustification] if self.hasJustification is not None else []
        self.hasJustification = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasJustification]

        if not isinstance(self.hasLawfulness, list):
            self.hasLawfulness = [self.hasLawfulness] if self.hasLawfulness is not None else []
        self.hasLawfulness = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasLawfulness]

        if not isinstance(self.hasLeadSA, list):
            self.hasLeadSA = [self.hasLeadSA] if self.hasLeadSA is not None else []
        self.hasLeadSA = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasLeadSA]

        if not isinstance(self.hasLegalBasis, list):
            self.hasLegalBasis = [self.hasLegalBasis] if self.hasLegalBasis is not None else []
        self.hasLegalBasis = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasLegalBasis]

        if not isinstance(self.hasLegalMeasure, list):
            self.hasLegalMeasure = [self.hasLegalMeasure] if self.hasLegalMeasure is not None else []
        self.hasLegalMeasure = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasLegalMeasure]

        if not isinstance(self.hasLicense, list):
            self.hasLicense = [self.hasLicense] if self.hasLicense is not None else []
        self.hasLicense = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasLicense]

        if not isinstance(self.hasLifecycleStage, list):
            self.hasLifecycleStage = [self.hasLifecycleStage] if self.hasLifecycleStage is not None else []
        self.hasLifecycleStage = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasLifecycleStage]

        if not isinstance(self.hasLikelihood, list):
            self.hasLikelihood = [self.hasLikelihood] if self.hasLikelihood is not None else []
        self.hasLikelihood = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasLikelihood]

        if not isinstance(self.hasLocalSA, list):
            self.hasLocalSA = [self.hasLocalSA] if self.hasLocalSA is not None else []
        self.hasLocalSA = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasLocalSA]

        if not isinstance(self.hasLocation, list):
            self.hasLocation = [self.hasLocation] if self.hasLocation is not None else []
        self.hasLocation = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasLocation]

        if not isinstance(self.hasMachineReadableFormat, list):
            self.hasMachineReadableFormat = [self.hasMachineReadableFormat] if self.hasMachineReadableFormat is not None else []
        self.hasMachineReadableFormat = [v if isinstance(v, str) else str(v) for v in self.hasMachineReadableFormat]

        if not isinstance(self.hasMainEstablishment, list):
            self.hasMainEstablishment = [self.hasMainEstablishment] if self.hasMainEstablishment is not None else []
        self.hasMainEstablishment = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasMainEstablishment]

        if not isinstance(self.hasMaintainer, list):
            self.hasMaintainer = [self.hasMaintainer] if self.hasMaintainer is not None else []
        self.hasMaintainer = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasMaintainer]

        if not isinstance(self.hasManufacturer, list):
            self.hasManufacturer = [self.hasManufacturer] if self.hasManufacturer is not None else []
        self.hasManufacturer = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasManufacturer]

        if not isinstance(self.hasMarketAvailabilityStatus, list):
            self.hasMarketAvailabilityStatus = [self.hasMarketAvailabilityStatus] if self.hasMarketAvailabilityStatus is not None else []
        self.hasMarketAvailabilityStatus = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasMarketAvailabilityStatus]

        if not isinstance(self.hasName, list):
            self.hasName = [self.hasName] if self.hasName is not None else []
        self.hasName = [v if isinstance(v, str) else str(v) for v in self.hasName]

        if not isinstance(self.hasNecessity, list):
            self.hasNecessity = [self.hasNecessity] if self.hasNecessity is not None else []
        self.hasNecessity = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasNecessity]

        if not isinstance(self.hasNonInvolvedEntity, list):
            self.hasNonInvolvedEntity = [self.hasNonInvolvedEntity] if self.hasNonInvolvedEntity is not None else []
        self.hasNonInvolvedEntity = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasNonInvolvedEntity]

        if not isinstance(self.hasNonPersonalDataProcess, list):
            self.hasNonPersonalDataProcess = [self.hasNonPersonalDataProcess] if self.hasNonPersonalDataProcess is not None else []
        self.hasNonPersonalDataProcess = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasNonPersonalDataProcess]

        if not isinstance(self.hasNotice, list):
            self.hasNotice = [self.hasNotice] if self.hasNotice is not None else []
        self.hasNotice = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasNotice]

        if not isinstance(self.hasNoticeIcon, list):
            self.hasNoticeIcon = [self.hasNoticeIcon] if self.hasNoticeIcon is not None else []
        self.hasNoticeIcon = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasNoticeIcon]

        if not isinstance(self.hasNoticeLayer, list):
            self.hasNoticeLayer = [self.hasNoticeLayer] if self.hasNoticeLayer is not None else []
        self.hasNoticeLayer = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasNoticeLayer]

        if not isinstance(self.hasNoticeStatus, list):
            self.hasNoticeStatus = [self.hasNoticeStatus] if self.hasNoticeStatus is not None else []
        self.hasNoticeStatus = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasNoticeStatus]

        if not isinstance(self.hasNotificationStatus, list):
            self.hasNotificationStatus = [self.hasNotificationStatus] if self.hasNotificationStatus is not None else []
        self.hasNotificationStatus = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasNotificationStatus]

        if not isinstance(self.hasObligation, list):
            self.hasObligation = [self.hasObligation] if self.hasObligation is not None else []
        self.hasObligation = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasObligation]

        if not isinstance(self.hasOperatingEnvironment, list):
            self.hasOperatingEnvironment = [self.hasOperatingEnvironment] if self.hasOperatingEnvironment is not None else []
        self.hasOperatingEnvironment = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasOperatingEnvironment]

        if not isinstance(self.hasOperatingFactor, list):
            self.hasOperatingFactor = [self.hasOperatingFactor] if self.hasOperatingFactor is not None else []
        self.hasOperatingFactor = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasOperatingFactor]

        if not isinstance(self.hasOrganisationalMeasure, list):
            self.hasOrganisationalMeasure = [self.hasOrganisationalMeasure] if self.hasOrganisationalMeasure is not None else []
        self.hasOrganisationalMeasure = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasOrganisationalMeasure]

        if not isinstance(self.hasOrganisationalUnit, list):
            self.hasOrganisationalUnit = [self.hasOrganisationalUnit] if self.hasOrganisationalUnit is not None else []
        self.hasOrganisationalUnit = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasOrganisationalUnit]

        if not isinstance(self.hasOutcome, list):
            self.hasOutcome = [self.hasOutcome] if self.hasOutcome is not None else []
        self.hasOutcome = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasOutcome]

        if not isinstance(self.hasOutput, list):
            self.hasOutput = [self.hasOutput] if self.hasOutput is not None else []
        self.hasOutput = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasOutput]

        if not isinstance(self.hasOutputAction, list):
            self.hasOutputAction = [self.hasOutputAction] if self.hasOutputAction is not None else []
        self.hasOutputAction = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasOutputAction]

        if not isinstance(self.hasOutputData, list):
            self.hasOutputData = [self.hasOutputData] if self.hasOutputData is not None else []
        self.hasOutputData = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasOutputData]

        if not isinstance(self.hasOwner, list):
            self.hasOwner = [self.hasOwner] if self.hasOwner is not None else []
        self.hasOwner = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasOwner]

        if not isinstance(self.hasPart, list):
            self.hasPart = [self.hasPart] if self.hasPart is not None else []
        self.hasPart = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasPart]

        if not isinstance(self.hasPartner, list):
            self.hasPartner = [self.hasPartner] if self.hasPartner is not None else []
        self.hasPartner = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasPartner]

        if not isinstance(self.hasParty, list):
            self.hasParty = [self.hasParty] if self.hasParty is not None else []
        self.hasParty = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasParty]

        if not isinstance(self.hasPassiveEntity, list):
            self.hasPassiveEntity = [self.hasPassiveEntity] if self.hasPassiveEntity is not None else []
        self.hasPassiveEntity = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasPassiveEntity]

        if not isinstance(self.hasPermission, list):
            self.hasPermission = [self.hasPermission] if self.hasPermission is not None else []
        self.hasPermission = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasPermission]

        if not isinstance(self.hasPersonalData, list):
            self.hasPersonalData = [self.hasPersonalData] if self.hasPersonalData is not None else []
        self.hasPersonalData = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasPersonalData]

        if not isinstance(self.hasPersonalDataHandling, list):
            self.hasPersonalDataHandling = [self.hasPersonalDataHandling] if self.hasPersonalDataHandling is not None else []
        self.hasPersonalDataHandling = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasPersonalDataHandling]

        if not isinstance(self.hasPersonalDataProcess, list):
            self.hasPersonalDataProcess = [self.hasPersonalDataProcess] if self.hasPersonalDataProcess is not None else []
        self.hasPersonalDataProcess = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasPersonalDataProcess]

        if not isinstance(self.hasPhysicalMeasure, list):
            self.hasPhysicalMeasure = [self.hasPhysicalMeasure] if self.hasPhysicalMeasure is not None else []
        self.hasPhysicalMeasure = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasPhysicalMeasure]

        if not isinstance(self.hasPlatform, list):
            self.hasPlatform = [self.hasPlatform] if self.hasPlatform is not None else []
        self.hasPlatform = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasPlatform]

        if not isinstance(self.hasPolicy, list):
            self.hasPolicy = [self.hasPolicy] if self.hasPolicy is not None else []
        self.hasPolicy = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasPolicy]

        if not isinstance(self.hasPortabilityTerm, list):
            self.hasPortabilityTerm = [self.hasPortabilityTerm] if self.hasPortabilityTerm is not None else []
        self.hasPortabilityTerm = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasPortabilityTerm]

        if not isinstance(self.hasPreferenceApplicability, list):
            self.hasPreferenceApplicability = [self.hasPreferenceApplicability] if self.hasPreferenceApplicability is not None else []
        self.hasPreferenceApplicability = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasPreferenceApplicability]

        if not isinstance(self.hasProcess, list):
            self.hasProcess = [self.hasProcess] if self.hasProcess is not None else []
        self.hasProcess = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasProcess]

        if not isinstance(self.hasProcessing, list):
            self.hasProcessing = [self.hasProcessing] if self.hasProcessing is not None else []
        self.hasProcessing = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasProcessing]

        if not isinstance(self.hasProcessingCondition, list):
            self.hasProcessingCondition = [self.hasProcessingCondition] if self.hasProcessingCondition is not None else []
        self.hasProcessingCondition = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasProcessingCondition]

        if not isinstance(self.hasProcessingScale, list):
            self.hasProcessingScale = [self.hasProcessingScale] if self.hasProcessingScale is not None else []
        self.hasProcessingScale = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasProcessingScale]

        if not isinstance(self.hasProducer, list):
            self.hasProducer = [self.hasProducer] if self.hasProducer is not None else []
        self.hasProducer = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasProducer]

        if not isinstance(self.hasProfilingTerm, list):
            self.hasProfilingTerm = [self.hasProfilingTerm] if self.hasProfilingTerm is not None else []
        self.hasProfilingTerm = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasProfilingTerm]

        if not isinstance(self.hasProhibition, list):
            self.hasProhibition = [self.hasProhibition] if self.hasProhibition is not None else []
        self.hasProhibition = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasProhibition]

        if not isinstance(self.hasProvider, list):
            self.hasProvider = [self.hasProvider] if self.hasProvider is not None else []
        self.hasProvider = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasProvider]

        if not isinstance(self.hasProvisionMethod, list):
            self.hasProvisionMethod = [self.hasProvisionMethod] if self.hasProvisionMethod is not None else []
        self.hasProvisionMethod = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasProvisionMethod]

        if not isinstance(self.hasProvisionStatus, list):
            self.hasProvisionStatus = [self.hasProvisionStatus] if self.hasProvisionStatus is not None else []
        self.hasProvisionStatus = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasProvisionStatus]

        if not isinstance(self.hasPurchaser, list):
            self.hasPurchaser = [self.hasPurchaser] if self.hasPurchaser is not None else []
        self.hasPurchaser = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasPurchaser]

        if not isinstance(self.hasPurpose, list):
            self.hasPurpose = [self.hasPurpose] if self.hasPurpose is not None else []
        self.hasPurpose = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasPurpose]

        if not isinstance(self.hasRecipient, list):
            self.hasRecipient = [self.hasRecipient] if self.hasRecipient is not None else []
        self.hasRecipient = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRecipient]

        if not isinstance(self.hasRecipientDataController, list):
            self.hasRecipientDataController = [self.hasRecipientDataController] if self.hasRecipientDataController is not None else []
        self.hasRecipientDataController = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRecipientDataController]

        if not isinstance(self.hasRecipientThirdParty, list):
            self.hasRecipientThirdParty = [self.hasRecipientThirdParty] if self.hasRecipientThirdParty is not None else []
        self.hasRecipientThirdParty = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRecipientThirdParty]

        if not isinstance(self.hasRecommendation, list):
            self.hasRecommendation = [self.hasRecommendation] if self.hasRecommendation is not None else []
        self.hasRecommendation = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRecommendation]

        if not isinstance(self.hasRecordOfActivity, list):
            self.hasRecordOfActivity = [self.hasRecordOfActivity] if self.hasRecordOfActivity is not None else []
        self.hasRecordOfActivity = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRecordOfActivity]

        if not isinstance(self.hasRelationWithDataSubject, list):
            self.hasRelationWithDataSubject = [self.hasRelationWithDataSubject] if self.hasRelationWithDataSubject is not None else []
        self.hasRelationWithDataSubject = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRelationWithDataSubject]

        if not isinstance(self.hasRepresentative, list):
            self.hasRepresentative = [self.hasRepresentative] if self.hasRepresentative is not None else []
        self.hasRepresentative = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRepresentative]

        if not isinstance(self.hasRequestStatus, list):
            self.hasRequestStatus = [self.hasRequestStatus] if self.hasRequestStatus is not None else []
        self.hasRequestStatus = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRequestStatus]

        if not isinstance(self.hasResidualRisk, list):
            self.hasResidualRisk = [self.hasResidualRisk] if self.hasResidualRisk is not None else []
        self.hasResidualRisk = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasResidualRisk]

        if not isinstance(self.hasResponsibleEntity, list):
            self.hasResponsibleEntity = [self.hasResponsibleEntity] if self.hasResponsibleEntity is not None else []
        self.hasResponsibleEntity = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasResponsibleEntity]

        if not isinstance(self.hasReuseCompatibility, list):
            self.hasReuseCompatibility = [self.hasReuseCompatibility] if self.hasReuseCompatibility is not None else []
        self.hasReuseCompatibility = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasReuseCompatibility]

        if not isinstance(self.hasRight, list):
            self.hasRight = [self.hasRight] if self.hasRight is not None else []
        self.hasRight = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRight]

        if not isinstance(self.hasRisk, list):
            self.hasRisk = [self.hasRisk] if self.hasRisk is not None else []
        self.hasRisk = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRisk]

        if not isinstance(self.hasRiskAcceptance, list):
            self.hasRiskAcceptance = [self.hasRiskAcceptance] if self.hasRiskAcceptance is not None else []
        self.hasRiskAcceptance = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRiskAcceptance]

        if not isinstance(self.hasRiskAnalysis, list):
            self.hasRiskAnalysis = [self.hasRiskAnalysis] if self.hasRiskAnalysis is not None else []
        self.hasRiskAnalysis = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRiskAnalysis]

        if not isinstance(self.hasRiskAssessment, list):
            self.hasRiskAssessment = [self.hasRiskAssessment] if self.hasRiskAssessment is not None else []
        self.hasRiskAssessment = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRiskAssessment]

        if not isinstance(self.hasRiskCriteria, list):
            self.hasRiskCriteria = [self.hasRiskCriteria] if self.hasRiskCriteria is not None else []
        self.hasRiskCriteria = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRiskCriteria]

        if not isinstance(self.hasRiskEvaluation, list):
            self.hasRiskEvaluation = [self.hasRiskEvaluation] if self.hasRiskEvaluation is not None else []
        self.hasRiskEvaluation = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRiskEvaluation]

        if not isinstance(self.hasRiskIdentification, list):
            self.hasRiskIdentification = [self.hasRiskIdentification] if self.hasRiskIdentification is not None else []
        self.hasRiskIdentification = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRiskIdentification]

        if not isinstance(self.hasRiskLevel, list):
            self.hasRiskLevel = [self.hasRiskLevel] if self.hasRiskLevel is not None else []
        self.hasRiskLevel = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRiskLevel]

        if not isinstance(self.hasRiskManagement, list):
            self.hasRiskManagement = [self.hasRiskManagement] if self.hasRiskManagement is not None else []
        self.hasRiskManagement = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRiskManagement]

        if not isinstance(self.hasRiskOwner, list):
            self.hasRiskOwner = [self.hasRiskOwner] if self.hasRiskOwner is not None else []
        self.hasRiskOwner = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRiskOwner]

        if not isinstance(self.hasRiskPerception, list):
            self.hasRiskPerception = [self.hasRiskPerception] if self.hasRiskPerception is not None else []
        self.hasRiskPerception = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRiskPerception]

        if not isinstance(self.hasRiskSource, list):
            self.hasRiskSource = [self.hasRiskSource] if self.hasRiskSource is not None else []
        self.hasRiskSource = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRiskSource]

        if not isinstance(self.hasRiskTreatment, list):
            self.hasRiskTreatment = [self.hasRiskTreatment] if self.hasRiskTreatment is not None else []
        self.hasRiskTreatment = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRiskTreatment]

        if not isinstance(self.hasRule, list):
            self.hasRule = [self.hasRule] if self.hasRule is not None else []
        self.hasRule = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasRule]

        if not isinstance(self.hasScale, list):
            self.hasScale = [self.hasScale] if self.hasScale is not None else []
        self.hasScale = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasScale]

        if not isinstance(self.hasScope, list):
            self.hasScope = [self.hasScope] if self.hasScope is not None else []
        self.hasScope = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasScope]

        if not isinstance(self.hasSecondParty, list):
            self.hasSecondParty = [self.hasSecondParty] if self.hasSecondParty is not None else []
        self.hasSecondParty = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasSecondParty]

        if not isinstance(self.hasSector, list):
            self.hasSector = [self.hasSector] if self.hasSector is not None else []
        self.hasSector = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasSector]

        if not isinstance(self.hasSensitivityLevel, list):
            self.hasSensitivityLevel = [self.hasSensitivityLevel] if self.hasSensitivityLevel is not None else []
        self.hasSensitivityLevel = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasSensitivityLevel]

        if not isinstance(self.hasService, list):
            self.hasService = [self.hasService] if self.hasService is not None else []
        self.hasService = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasService]

        if not isinstance(self.hasServiceConsumer, list):
            self.hasServiceConsumer = [self.hasServiceConsumer] if self.hasServiceConsumer is not None else []
        self.hasServiceConsumer = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasServiceConsumer]

        if not isinstance(self.hasServiceProvider, list):
            self.hasServiceProvider = [self.hasServiceProvider] if self.hasServiceProvider is not None else []
        self.hasServiceProvider = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasServiceProvider]

        if not isinstance(self.hasSeverity, list):
            self.hasSeverity = [self.hasSeverity] if self.hasSeverity is not None else []
        self.hasSeverity = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasSeverity]

        if not isinstance(self.hasSoftware, list):
            self.hasSoftware = [self.hasSoftware] if self.hasSoftware is not None else []
        self.hasSoftware = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasSoftware]

        if not isinstance(self.hasStatus, list):
            self.hasStatus = [self.hasStatus] if self.hasStatus is not None else []
        self.hasStatus = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasStatus]

        if not isinstance(self.hasStorageCondition, list):
            self.hasStorageCondition = [self.hasStorageCondition] if self.hasStorageCondition is not None else []
        self.hasStorageCondition = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasStorageCondition]

        if not isinstance(self.hasSubject, list):
            self.hasSubject = [self.hasSubject] if self.hasSubject is not None else []
        self.hasSubject = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasSubject]

        if not isinstance(self.hasSubsidiary, list):
            self.hasSubsidiary = [self.hasSubsidiary] if self.hasSubsidiary is not None else []
        self.hasSubsidiary = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasSubsidiary]

        if not isinstance(self.hasSupplier, list):
            self.hasSupplier = [self.hasSupplier] if self.hasSupplier is not None else []
        self.hasSupplier = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasSupplier]

        if not isinstance(self.hasSystem, list):
            self.hasSystem = [self.hasSystem] if self.hasSystem is not None else []
        self.hasSystem = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasSystem]

        if not isinstance(self.hasSystemIntegrator, list):
            self.hasSystemIntegrator = [self.hasSystemIntegrator] if self.hasSystemIntegrator is not None else []
        self.hasSystemIntegrator = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasSystemIntegrator]

        if not isinstance(self.hasTRL, list):
            self.hasTRL = [self.hasTRL] if self.hasTRL is not None else []
        self.hasTRL = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasTRL]

        if not isinstance(self.hasTechnicalMeasure, list):
            self.hasTechnicalMeasure = [self.hasTechnicalMeasure] if self.hasTechnicalMeasure is not None else []
        self.hasTechnicalMeasure = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasTechnicalMeasure]

        if not isinstance(self.hasTechnicalOrganisationalMeasure, list):
            self.hasTechnicalOrganisationalMeasure = [self.hasTechnicalOrganisationalMeasure] if self.hasTechnicalOrganisationalMeasure is not None else []
        self.hasTechnicalOrganisationalMeasure = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasTechnicalOrganisationalMeasure]

        if not isinstance(self.hasTechnique, list):
            self.hasTechnique = [self.hasTechnique] if self.hasTechnique is not None else []
        self.hasTechnique = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasTechnique]

        if not isinstance(self.hasTestingData, list):
            self.hasTestingData = [self.hasTestingData] if self.hasTestingData is not None else []
        self.hasTestingData = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasTestingData]

        if not isinstance(self.hasThirdCountry, list):
            self.hasThirdCountry = [self.hasThirdCountry] if self.hasThirdCountry is not None else []
        self.hasThirdCountry = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasThirdCountry]

        if not isinstance(self.hasThirdParty, list):
            self.hasThirdParty = [self.hasThirdParty] if self.hasThirdParty is not None else []
        self.hasThirdParty = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasThirdParty]

        if not isinstance(self.hasThreatSource, list):
            self.hasThreatSource = [self.hasThreatSource] if self.hasThreatSource is not None else []
        self.hasThreatSource = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasThreatSource]

        if not isinstance(self.hasTrackingTerm, list):
            self.hasTrackingTerm = [self.hasTrackingTerm] if self.hasTrackingTerm is not None else []
        self.hasTrackingTerm = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasTrackingTerm]

        if not isinstance(self.hasTrainingData, list):
            self.hasTrainingData = [self.hasTrainingData] if self.hasTrainingData is not None else []
        self.hasTrainingData = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasTrainingData]

        if not isinstance(self.hasTransparencyTerm, list):
            self.hasTransparencyTerm = [self.hasTransparencyTerm] if self.hasTransparencyTerm is not None else []
        self.hasTransparencyTerm = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasTransparencyTerm]

        if not isinstance(self.hasUncategorisedData, list):
            self.hasUncategorisedData = [self.hasUncategorisedData] if self.hasUncategorisedData is not None else []
        self.hasUncategorisedData = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasUncategorisedData]

        if not isinstance(self.hasUnstructuredData, list):
            self.hasUnstructuredData = [self.hasUnstructuredData] if self.hasUnstructuredData is not None else []
        self.hasUnstructuredData = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasUnstructuredData]

        if not isinstance(self.hasUser, list):
            self.hasUser = [self.hasUser] if self.hasUser is not None else []
        self.hasUser = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasUser]

        if not isinstance(self.hasValidationData, list):
            self.hasValidationData = [self.hasValidationData] if self.hasValidationData is not None else []
        self.hasValidationData = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasValidationData]

        if not isinstance(self.hasVulnerability, list):
            self.hasVulnerability = [self.hasVulnerability] if self.hasVulnerability is not None else []
        self.hasVulnerability = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.hasVulnerability]

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if not isinstance(self.identifies, list):
            self.identifies = [self.identifies] if self.identifies is not None else []
        self.identifies = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.identifies]

        if not isinstance(self.ieee_7012_hasParty, list):
            self.ieee_7012_hasParty = [self.ieee_7012_hasParty] if self.ieee_7012_hasParty is not None else []
        self.ieee_7012_hasParty = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.ieee_7012_hasParty]

        if not isinstance(self.ieee_7012_hasThirdParty, list):
            self.ieee_7012_hasThirdParty = [self.ieee_7012_hasThirdParty] if self.ieee_7012_hasThirdParty is not None else []
        self.ieee_7012_hasThirdParty = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.ieee_7012_hasThirdParty]

        if not isinstance(self.interrupts, list):
            self.interrupts = [self.interrupts] if self.interrupts is not None else []
        self.interrupts = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.interrupts]

        if not isinstance(self.intervenes, list):
            self.intervenes = [self.intervenes] if self.intervenes is not None else []
        self.intervenes = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.intervenes]

        if not isinstance(self.investigates, list):
            self.investigates = [self.investigates] if self.investigates is not None else []
        self.investigates = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.investigates]

        if not isinstance(self.isAfter, list):
            self.isAfter = [self.isAfter] if self.isAfter is not None else []
        self.isAfter = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isAfter]

        if not isinstance(self.isApplicableFor, list):
            self.isApplicableFor = [self.isApplicableFor] if self.isApplicableFor is not None else []
        self.isApplicableFor = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isApplicableFor]

        if not isinstance(self.isAuthorityFor, list):
            self.isAuthorityFor = [self.isAuthorityFor] if self.isAuthorityFor is not None else []
        self.isAuthorityFor = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isAuthorityFor]

        if not isinstance(self.isBefore, list):
            self.isBefore = [self.isBefore] if self.isBefore is not None else []
        self.isBefore = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isBefore]

        if not isinstance(self.isComponentOf, list):
            self.isComponentOf = [self.isComponentOf] if self.isComponentOf is not None else []
        self.isComponentOf = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isComponentOf]

        if not isinstance(self.isDeterminedByEntity, list):
            self.isDeterminedByEntity = [self.isDeterminedByEntity] if self.isDeterminedByEntity is not None else []
        self.isDeterminedByEntity = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isDeterminedByEntity]

        if not isinstance(self.isDuring, list):
            self.isDuring = [self.isDuring] if self.isDuring is not None else []
        self.isDuring = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isDuring]

        if not isinstance(self.isExercisedAt, list):
            self.isExercisedAt = [self.isExercisedAt] if self.isExercisedAt is not None else []
        self.isExercisedAt = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isExercisedAt]

        if not isinstance(self.isExploitedBy, list):
            self.isExploitedBy = [self.isExploitedBy] if self.isExploitedBy is not None else []
        self.isExploitedBy = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isExploitedBy]

        if not isinstance(self.isImplementedByEntity, list):
            self.isImplementedByEntity = [self.isImplementedByEntity] if self.isImplementedByEntity is not None else []
        self.isImplementedByEntity = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isImplementedByEntity]

        if not isinstance(self.isImplementedUsingTechnology, list):
            self.isImplementedUsingTechnology = [self.isImplementedUsingTechnology] if self.isImplementedUsingTechnology is not None else []
        self.isImplementedUsingTechnology = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isImplementedUsingTechnology]

        if not isinstance(self.isIndicatedAtTime, list):
            self.isIndicatedAtTime = [self.isIndicatedAtTime] if self.isIndicatedAtTime is not None else []
        self.isIndicatedAtTime = [v if isinstance(v, str) else str(v) for v in self.isIndicatedAtTime]

        if not isinstance(self.isIndicatedBy, list):
            self.isIndicatedBy = [self.isIndicatedBy] if self.isIndicatedBy is not None else []
        self.isIndicatedBy = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isIndicatedBy]

        if not isinstance(self.isMainEstablishmentFor, list):
            self.isMainEstablishmentFor = [self.isMainEstablishmentFor] if self.isMainEstablishmentFor is not None else []
        self.isMainEstablishmentFor = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isMainEstablishmentFor]

        if not isinstance(self.isMitigatedByMeasure, list):
            self.isMitigatedByMeasure = [self.isMitigatedByMeasure] if self.isMitigatedByMeasure is not None else []
        self.isMitigatedByMeasure = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isMitigatedByMeasure]

        if not isinstance(self.isNotApplicableFor, list):
            self.isNotApplicableFor = [self.isNotApplicableFor] if self.isNotApplicableFor is not None else []
        self.isNotApplicableFor = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isNotApplicableFor]

        if not isinstance(self.isOrganisationalUnitOf, list):
            self.isOrganisationalUnitOf = [self.isOrganisationalUnitOf] if self.isOrganisationalUnitOf is not None else []
        self.isOrganisationalUnitOf = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isOrganisationalUnitOf]

        if not isinstance(self.isOutsideOfLocation, list):
            self.isOutsideOfLocation = [self.isOutsideOfLocation] if self.isOutsideOfLocation is not None else []
        self.isOutsideOfLocation = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isOutsideOfLocation]

        if not isinstance(self.isPartOf, list):
            self.isPartOf = [self.isPartOf] if self.isPartOf is not None else []
        self.isPartOf = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isPartOf]

        if not isinstance(self.isPolicyFor, list):
            self.isPolicyFor = [self.isPolicyFor] if self.isPolicyFor is not None else []
        self.isPolicyFor = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isPolicyFor]

        if not isinstance(self.isRepresentativeFor, list):
            self.isRepresentativeFor = [self.isRepresentativeFor] if self.isRepresentativeFor is not None else []
        self.isRepresentativeFor = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isRepresentativeFor]

        if not isinstance(self.isResidualRiskOf, list):
            self.isResidualRiskOf = [self.isResidualRiskOf] if self.isResidualRiskOf is not None else []
        self.isResidualRiskOf = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isResidualRiskOf]

        if not isinstance(self.isSubsidiaryOf, list):
            self.isSubsidiaryOf = [self.isSubsidiaryOf] if self.isSubsidiaryOf is not None else []
        self.isSubsidiaryOf = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isSubsidiaryOf]

        if not isinstance(self.isVersionOf, list):
            self.isVersionOf = [self.isVersionOf] if self.isVersionOf is not None else []
        self.isVersionOf = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isVersionOf]

        if not isinstance(self.isVulnerabilityOf, list):
            self.isVulnerabilityOf = [self.isVulnerabilityOf] if self.isVulnerabilityOf is not None else []
        self.isVulnerabilityOf = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.isVulnerabilityOf]

        if not isinstance(self.iso_alpha2, list):
            self.iso_alpha2 = [self.iso_alpha2] if self.iso_alpha2 is not None else []
        self.iso_alpha2 = [v if isinstance(v, str) else str(v) for v in self.iso_alpha2]

        if not isinstance(self.iso_alpha3, list):
            self.iso_alpha3 = [self.iso_alpha3] if self.iso_alpha3 is not None else []
        self.iso_alpha3 = [v if isinstance(v, str) else str(v) for v in self.iso_alpha3]

        if not isinstance(self.iso_numeric, list):
            self.iso_numeric = [self.iso_numeric] if self.iso_numeric is not None else []
        self.iso_numeric = [v if isinstance(v, str) else str(v) for v in self.iso_numeric]

        if not isinstance(self.logs, list):
            self.logs = [self.logs] if self.logs is not None else []
        self.logs = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.logs]

        if not isinstance(self.mitigates, list):
            self.mitigates = [self.mitigates] if self.mitigates is not None else []
        self.mitigates = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.mitigates]

        if not isinstance(self.mitigatesRisk, list):
            self.mitigatesRisk = [self.mitigatesRisk] if self.mitigatesRisk is not None else []
        self.mitigatesRisk = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.mitigatesRisk]

        if not isinstance(self.modifies, list):
            self.modifies = [self.modifies] if self.modifies is not None else []
        self.modifies = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.modifies]

        if not isinstance(self.monitors, list):
            self.monitors = [self.monitors] if self.monitors is not None else []
        self.monitors = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.monitors]

        if not isinstance(self.overrides, list):
            self.overrides = [self.overrides] if self.overrides is not None else []
        self.overrides = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.overrides]

        if not isinstance(self.page, list):
            self.page = [self.page] if self.page is not None else []
        self.page = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.page]

        if not isinstance(self.recovers, list):
            self.recovers = [self.recovers] if self.recovers is not None else []
        self.recovers = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.recovers]

        if not isinstance(self.reduces, list):
            self.reduces = [self.reduces] if self.reduces is not None else []
        self.reduces = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.reduces]

        if not isinstance(self.refersToRisk, list):
            self.refersToRisk = [self.refersToRisk] if self.refersToRisk is not None else []
        self.refersToRisk = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.refersToRisk]

        if not isinstance(self.remedies, list):
            self.remedies = [self.remedies] if self.remedies is not None else []
        self.remedies = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.remedies]

        if not isinstance(self.resolves, list):
            self.resolves = [self.resolves] if self.resolves is not None else []
        self.resolves = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.resolves]

        if not isinstance(self.reverses, list):
            self.reverses = [self.reverses] if self.reverses is not None else []
        self.reverses = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.reverses]

        if not isinstance(self.risk_hasRiskAssessment, list):
            self.risk_hasRiskAssessment = [self.risk_hasRiskAssessment] if self.risk_hasRiskAssessment is not None else []
        self.risk_hasRiskAssessment = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.risk_hasRiskAssessment]

        if not isinstance(self.shares, list):
            self.shares = [self.shares] if self.shares is not None else []
        self.shares = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.shares]

        if not isinstance(self.subject, list):
            self.subject = [self.subject] if self.subject is not None else []
        self.subject = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.subject]

        if not isinstance(self.substitutes, list):
            self.substitutes = [self.substitutes] if self.substitutes is not None else []
        self.substitutes = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.substitutes]

        if not isinstance(self.supportsComplianceWith, list):
            self.supportsComplianceWith = [self.supportsComplianceWith] if self.supportsComplianceWith is not None else []
        self.supportsComplianceWith = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.supportsComplianceWith]

        if not isinstance(self.tech_hasCapability, list):
            self.tech_hasCapability = [self.tech_hasCapability] if self.tech_hasCapability is not None else []
        self.tech_hasCapability = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.tech_hasCapability]

        if not isinstance(self.tech_hasModel, list):
            self.tech_hasModel = [self.tech_hasModel] if self.tech_hasModel is not None else []
        self.tech_hasModel = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.tech_hasModel]

        if not isinstance(self.tech_hasService, list):
            self.tech_hasService = [self.tech_hasService] if self.tech_hasService is not None else []
        self.tech_hasService = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.tech_hasService]

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.transfers, list):
            self.transfers = [self.transfers] if self.transfers is not None else []
        self.transfers = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.transfers]

        if not isinstance(self.un_m49, list):
            self.un_m49 = [self.un_m49] if self.un_m49 is not None else []
        self.un_m49 = [v if isinstance(v, str) else str(v) for v in self.un_m49]

        if not isinstance(self.valid, list):
            self.valid = [self.valid] if self.valid is not None else []
        self.valid = [v if isinstance(v, str) else str(v) for v in self.valid]

        self._normalize_inlined_as_list(slot_name="statements", slot_type=DpvStatement, key_name="predicate", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvExample(YAMLRoot):
    """
    One of DPV's examples: what it shows, and the statements its Turtle file makes, as one resource per subject.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DEX["Example"]
    class_class_curie: ClassVar[str] = "dex:Example"
    class_name: ClassVar[str] = "DpvExample"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvExample

    id: Union[str, DpvExampleId] = None
    title: str = None
    description: Optional[str] = None
    format: Optional[Union[str, list[str]]] = empty_list()
    source: Optional[Union[str, list[str]]] = empty_list()
    subject: Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]] = empty_list()
    created: Optional[Union[Union[str, DpvDate], list[Union[str, DpvDate]]]] = empty_list()
    modified: Optional[Union[str, DpvDate]] = None
    temporal: Optional[Union[dict, DpvInterval]] = None
    contributor: Optional[Union[Union[str, DpvAgentId], list[Union[str, DpvAgentId]]]] = empty_list()
    term_status: Optional[Union[str, "DpvTermStatus"]] = None
    turtle_fault: Optional[str] = None
    resources: Optional[Union[dict[Union[str, DpvResourceId], Union[dict, DpvResource]], list[Union[dict, DpvResource]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvExampleId):
            self.id = DpvExampleId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.format, list):
            self.format = [self.format] if self.format is not None else []
        self.format = [v if isinstance(v, str) else str(v) for v in self.format]

        if not isinstance(self.source, list):
            self.source = [self.source] if self.source is not None else []
        self.source = [v if isinstance(v, str) else str(v) for v in self.source]

        if not isinstance(self.subject, list):
            self.subject = [self.subject] if self.subject is not None else []
        self.subject = [v if isinstance(v, DpvTermId) else DpvTermId(v) for v in self.subject]

        if not isinstance(self.created, list):
            self.created = [self.created] if self.created is not None else []
        self.created = [v if isinstance(v, DpvDate) else DpvDate(v) for v in self.created]

        if self.modified is not None and not isinstance(self.modified, DpvDate):
            self.modified = DpvDate(self.modified)

        if self.temporal is not None and not isinstance(self.temporal, DpvInterval):
            self.temporal = DpvInterval(**as_dict(self.temporal))

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, DpvAgentId) else DpvAgentId(v) for v in self.contributor]

        if self.term_status is not None and not isinstance(self.term_status, DpvTermStatus):
            self.term_status = DpvTermStatus(self.term_status)

        if self.turtle_fault is not None and not isinstance(self.turtle_fault, str):
            self.turtle_fault = str(self.turtle_fault)

        self._normalize_inlined_as_list(slot_name="resources", slot_type=DpvResource, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvStatement(YAMLRoot):
    """
    One statement of a resource that its keys cannot hold: a predicate with no slot, or a value not in the form its
    slot takes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV_LINKML["DpvStatement"]
    class_class_curie: ClassVar[str] = "dpv_linkml:DpvStatement"
    class_name: ClassVar[str] = "DpvStatement"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvStatement

    predicate: Union[str, URIorCURIE] = None
    datatype: Optional[Union[str, URIorCURIE]] = None
    reference: Optional[Union[str, URIorCURIE]] = None
    literal: Optional[str] = None
    language: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.predicate):
            self.MissingRequiredField("predicate")
        if not isinstance(self.predicate, URIorCURIE):
            self.predicate = URIorCURIE(self.predicate)

        if self.datatype is not None and not isinstance(self.datatype, URIorCURIE):
            self.datatype = URIorCURIE(self.datatype)

        if self.reference is not None and not isinstance(self.reference, URIorCURIE):
            self.reference = URIorCURIE(self.reference)

        if self.literal is not None and not isinstance(self.literal, str):
            self.literal = str(self.literal)

        if self.language is not None and not isinstance(self.language, str):
            self.language = str(self.language)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvAggregatedData(DpvConcept):
    """
    A kind of term DPV names as dpv:AggregatedData and does not define.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AggregatedData"]
    class_class_curie: ClassVar[str] = "dpv:AggregatedData"
    class_name: ClassVar[str] = "DpvAggregatedData"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvAggregatedData

    id: Union[str, DpvAggregatedDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvAggregatedDataId):
            self.id = DpvAggregatedDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvApplicability(DpvConcept):
    """
    Concept provided to represent indication of cases where the information or context is not applicable (N/A) or not
    available or this is not known or determined yet. If the information is applicable and available, this concept
    should not be used.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Applicability"]
    class_class_curie: ClassVar[str] = "dpv:Applicability"
    class_name: ClassVar[str] = "DpvApplicability"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvApplicability

    id: Union[str, DpvApplicabilityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvApplicabilityId):
            self.id = DpvApplicabilityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvContractualClause(DpvConcept):
    """
    A part or component within a contract that outlines its specifics
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractualClause"]
    class_class_curie: ClassVar[str] = "dpv:ContractualClause"
    class_name: ClassVar[str] = "DpvContractualClause"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvContractualClause

    id: Union[str, DpvContractualClauseId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvContractualClauseId):
            self.id = DpvContractualClauseId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDuration(DpvConcept):
    """
    The duration or temporal limitation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Duration"]
    class_class_curie: ClassVar[str] = "dpv:Duration"
    class_name: ClassVar[str] = "DpvDuration"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDuration

    id: Union[str, DpvDurationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDurationId):
            self.id = DpvDurationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvExpectationStatus(DpvConcept):
    """
    Status indicating whether the specified context was intended or unintended
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ExpectationStatus"]
    class_class_curie: ClassVar[str] = "dpv:ExpectationStatus"
    class_name: ClassVar[str] = "DpvExpectationStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvExpectationStatus

    id: Union[str, DpvExpectationStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvExpectationStatusId):
            self.id = DpvExpectationStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvFeeRequirement(DpvConcept):
    """
    Concept indicating whether a fee is required
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["FeeRequirement"]
    class_class_curie: ClassVar[str] = "dpv:FeeRequirement"
    class_name: ClassVar[str] = "DpvFeeRequirement"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvFeeRequirement

    id: Union[str, DpvFeeRequirementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvFeeRequirementId):
            self.id = DpvFeeRequirementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvFrequency(DpvConcept):
    """
    The frequency or information about periods and repetitions in terms of recurrence.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Frequency"]
    class_class_curie: ClassVar[str] = "dpv:Frequency"
    class_name: ClassVar[str] = "DpvFrequency"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvFrequency

    id: Union[str, DpvFrequencyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvFrequencyId):
            self.id = DpvFrequencyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvImportance(DpvConcept):
    """
    An indication of 'importance' within a context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Importance"]
    class_class_curie: ClassVar[str] = "dpv:Importance"
    class_name: ClassVar[str] = "DpvImportance"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvImportance

    id: Union[str, DpvImportanceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvImportanceId):
            self.id = DpvImportanceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvJustification(DpvConcept):
    """
    A form of documentation providing reasons, explanations, or justifications
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Justification"]
    class_class_curie: ClassVar[str] = "dpv:Justification"
    class_name: ClassVar[str] = "DpvJustification"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvJustification

    id: Union[str, DpvJustificationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvJustificationId):
            self.id = DpvJustificationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvLaw(DpvConcept):
    """
    A law is a set of rules created by government or authorities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Law"]
    class_class_curie: ClassVar[str] = "dpv:Law"
    class_name: ClassVar[str] = "DpvLaw"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvLaw

    id: Union[str, DpvLawId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvLawId):
            self.id = DpvLawId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvLegalBasis(DpvConcept):
    """
    Legal basis used to justify processing of data or use of technology in accordance with a law
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalBasis"]
    class_class_curie: ClassVar[str] = "dpv:LegalBasis"
    class_name: ClassVar[str] = "DpvLegalBasis"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvLegalBasis

    id: Union[str, DpvLegalBasisId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvLegalBasisId):
            self.id = DpvLegalBasisId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvLegalEntity(DpvConcept):
    """
    A human or non-human 'thing' that constitutes as an entity and which is recognised and defined in law
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalEntity"]
    class_class_curie: ClassVar[str] = "dpv:LegalEntity"
    class_name: ClassVar[str] = "DpvLegalEntity"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvLegalEntity

    id: Union[str, DpvLegalEntityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvLegalEntityId):
            self.id = DpvLegalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvAuthority(DpvLegalEntity):
    """
    An authority with the power to create or enforce laws, or determine their compliance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Authority"]
    class_class_curie: ClassVar[str] = "dpv:Authority"
    class_name: ClassVar[str] = "DpvAuthority"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvAuthority

    id: Union[str, DpvAuthorityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvAuthorityId):
            self.id = DpvAuthorityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDataProtectionAuthority(DpvAuthority):
    """
    An authority tasked with overseeing legal compliance regarding privacy and data protection laws.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataProtectionAuthority"]
    class_class_curie: ClassVar[str] = "dpv:DataProtectionAuthority"
    class_name: ClassVar[str] = "DpvDataProtectionAuthority"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDataProtectionAuthority

    id: Union[str, DpvDataProtectionAuthorityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDataProtectionAuthorityId):
            self.id = DpvDataProtectionAuthorityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvHumanSubject(DpvLegalEntity):
    """
    The individual (or category of individuals) that is the subject within some context such as personal data
    (dpv:DataSubject) or technology (tech:Subject)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HumanSubject"]
    class_class_curie: ClassVar[str] = "dpv:HumanSubject"
    class_name: ClassVar[str] = "DpvHumanSubject"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvHumanSubject

    id: Union[str, DpvHumanSubjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvHumanSubjectId):
            self.id = DpvHumanSubjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvLegalMeasure(DpvConcept):
    """
    Legal measures used to safeguard and ensure good practices in connection with data and technologies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalMeasure"]
    class_class_curie: ClassVar[str] = "dpv:LegalMeasure"
    class_name: ClassVar[str] = "DpvLegalMeasure"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvLegalMeasure

    id: Union[str, DpvLegalMeasureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvLegalMeasureId):
            self.id = DpvLegalMeasureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvLikelihood(DpvConcept):
    """
    The likelihood or probability or chance of something taking place or occurring
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Likelihood"]
    class_class_curie: ClassVar[str] = "dpv:Likelihood"
    class_name: ClassVar[str] = "DpvLikelihood"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvLikelihood

    id: Union[str, DpvLikelihoodId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvLikelihoodId):
            self.id = DpvLikelihoodId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvLocation(DpvConcept):
    """
    A location is a position, site, or area where something is located
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Location"]
    class_class_curie: ClassVar[str] = "dpv:Location"
    class_name: ClassVar[str] = "DpvLocation"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvLocation

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
    A jurisdiction represents the locations that define the extent of authority (or control) claimed, granted, or
    asserted by a legal entity (in particular a legal authority) to govern or enforce rules
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Jurisdiction"]
    class_class_curie: ClassVar[str] = "dpv:Jurisdiction"
    class_name: ClassVar[str] = "DpvJurisdiction"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvJurisdiction

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
    A political entity indicative of a sovereign or non-sovereign territorial state comprising of distinct
    geographical areas
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Country"]
    class_class_curie: ClassVar[str] = "dpv:Country"
    class_name: ClassVar[str] = "DpvCountry"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvCountry

    id: Union[str, DpvCountryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvCountryId):
            self.id = DpvCountryId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvInverseJurisdiction(DpvJurisdiction):
    """
    An inverse jurisdiction for a specific jurisdiction is the set of all other jurisdictions that are not part of the
    specific jurisdiction
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InverseJurisdiction"]
    class_class_curie: ClassVar[str] = "dpv:InverseJurisdiction"
    class_name: ClassVar[str] = "DpvInverseJurisdiction"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvInverseJurisdiction

    id: Union[str, DpvInverseJurisdictionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvInverseJurisdictionId):
            self.id = DpvInverseJurisdictionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvLocationFixture(DpvConcept):
    """
    The fixture of location refers to whether the location is fixed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LocationFixture"]
    class_class_curie: ClassVar[str] = "dpv:LocationFixture"
    class_name: ClassVar[str] = "DpvLocationFixture"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvLocationFixture

    id: Union[str, DpvLocationFixtureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvLocationFixtureId):
            self.id = DpvLocationFixtureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvNecessity(DpvConcept):
    """
    An indication of 'necessity' within a context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Necessity"]
    class_class_curie: ClassVar[str] = "dpv:Necessity"
    class_name: ClassVar[str] = "DpvNecessity"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvNecessity

    id: Union[str, DpvNecessityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvNecessityId):
            self.id = DpvNecessityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvNonPersonalData(DpvConcept):
    """
    Data that is not Personal Data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NonPersonalData"]
    class_class_curie: ClassVar[str] = "dpv:NonPersonalData"
    class_name: ClassVar[str] = "DpvNonPersonalData"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvNonPersonalData

    id: Union[str, DpvNonPersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvNonPersonalDataId):
            self.id = DpvNonPersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvOrganisationalMeasure(DpvConcept):
    """
    Organisational measures used to safeguard and ensure good practices in connection with data and technologies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OrganisationalMeasure"]
    class_class_curie: ClassVar[str] = "dpv:OrganisationalMeasure"
    class_name: ClassVar[str] = "DpvOrganisationalMeasure"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvOrganisationalMeasure

    id: Union[str, DpvOrganisationalMeasureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvOrganisationalMeasureId):
            self.id = DpvOrganisationalMeasureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvPersonalData(DpvConcept):
    """
    Data directly or indirectly associated or related to an individual
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PersonalData"]
    class_class_curie: ClassVar[str] = "dpv:PersonalData"
    class_name: ClassVar[str] = "DpvPersonalData"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvPersonalData

    id: Union[str, DpvPersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPersonalDataId):
            self.id = DpvPersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvPhysicalMeasure(DpvConcept):
    """
    Physical measures used to safeguard and ensure good practices in connection with data and technologies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PhysicalMeasure"]
    class_class_curie: ClassVar[str] = "dpv:PhysicalMeasure"
    class_name: ClassVar[str] = "DpvPhysicalMeasure"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvPhysicalMeasure

    id: Union[str, DpvPhysicalMeasureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPhysicalMeasureId):
            self.id = DpvPhysicalMeasureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvProcessing(DpvConcept):
    """
    Operations or 'processing' performed on data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Processing"]
    class_class_curie: ClassVar[str] = "dpv:Processing"
    class_name: ClassVar[str] = "DpvProcessing"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvProcessing

    id: Union[str, DpvProcessingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvProcessingId):
            self.id = DpvProcessingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvProcessingContext(DpvConcept):
    """
    Context or conditions within which processing takes place
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProcessingContext"]
    class_class_curie: ClassVar[str] = "dpv:ProcessingContext"
    class_name: ClassVar[str] = "DpvProcessingContext"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvProcessingContext

    id: Union[str, DpvProcessingContextId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvProcessingContextId):
            self.id = DpvProcessingContextId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvAutomationLevel(DpvProcessingContext):
    """
    Indication of degree or level of automation associated with specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AutomationLevel"]
    class_class_curie: ClassVar[str] = "dpv:AutomationLevel"
    class_name: ClassVar[str] = "DpvAutomationLevel"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvAutomationLevel

    id: Union[str, DpvAutomationLevelId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvAutomationLevelId):
            self.id = DpvAutomationLevelId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDataSource(DpvProcessingContext):
    """
    The source or origin of data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSource"]
    class_class_curie: ClassVar[str] = "dpv:DataSource"
    class_name: ClassVar[str] = "DpvDataSource"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDataSource

    id: Union[str, DpvDataSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDataSourceId):
            self.id = DpvDataSourceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDataSubjectDataSource(DpvDataSource):
    """
    Data Sourced from Data Subject(s), e.g. when data is collected via a form or observed from their activities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSubjectDataSource"]
    class_class_curie: ClassVar[str] = "dpv:DataSubjectDataSource"
    class_name: ClassVar[str] = "DpvDataSubjectDataSource"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDataSubjectDataSource

    id: Union[str, DpvDataSubjectDataSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDataSubjectDataSourceId):
            self.id = DpvDataSubjectDataSourceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDataSubjectScale(DpvProcessingContext):
    """
    Scale of Data Subject(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataSubjectScale"]
    class_class_curie: ClassVar[str] = "dpv:DataSubjectScale"
    class_name: ClassVar[str] = "DpvDataSubjectScale"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDataSubjectScale

    id: Union[str, DpvDataSubjectScaleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDataSubjectScaleId):
            self.id = DpvDataSubjectScaleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDataVolume(DpvProcessingContext):
    """
    Volume or Scale of Data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["DataVolume"]
    class_class_curie: ClassVar[str] = "dpv:DataVolume"
    class_name: ClassVar[str] = "DpvDataVolume"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDataVolume

    id: Union[str, DpvDataVolumeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDataVolumeId):
            self.id = DpvDataVolumeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvEntityNonPermissiveInvolvement(DpvProcessingContext):
    """
    Involvement of an entity in specific context where it is not permitted or able to do something
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityNonPermissiveInvolvement"]
    class_class_curie: ClassVar[str] = "dpv:EntityNonPermissiveInvolvement"
    class_name: ClassVar[str] = "DpvEntityNonPermissiveInvolvement"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvEntityNonPermissiveInvolvement

    id: Union[str, DpvEntityNonPermissiveInvolvementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvEntityNonPermissiveInvolvementId):
            self.id = DpvEntityNonPermissiveInvolvementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvEntityPermissiveInvolvement(DpvProcessingContext):
    """
    Involvement of an entity in specific context where it is permitted or able to do something
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityPermissiveInvolvement"]
    class_class_curie: ClassVar[str] = "dpv:EntityPermissiveInvolvement"
    class_name: ClassVar[str] = "DpvEntityPermissiveInvolvement"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvEntityPermissiveInvolvement

    id: Union[str, DpvEntityPermissiveInvolvementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvEntityPermissiveInvolvementId):
            self.id = DpvEntityPermissiveInvolvementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvEvaluationScoring(DpvProcessingContext):
    """
    Processing that involves evaluation and scoring of individuals
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EvaluationScoring"]
    class_class_curie: ClassVar[str] = "dpv:EvaluationScoring"
    class_name: ClassVar[str] = "DpvEvaluationScoring"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvEvaluationScoring

    id: Union[str, DpvEvaluationScoringId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvEvaluationScoringId):
            self.id = DpvEvaluationScoringId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvGeographicCoverage(DpvProcessingContext):
    """
    Indicate of scale in terms of geographic coverage
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["GeographicCoverage"]
    class_class_curie: ClassVar[str] = "dpv:GeographicCoverage"
    class_name: ClassVar[str] = "DpvGeographicCoverage"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvGeographicCoverage

    id: Union[str, DpvGeographicCoverageId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvGeographicCoverageId):
            self.id = DpvGeographicCoverageId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvHumanInvolvement(DpvProcessingContext):
    """
    The involvement of humans in specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["HumanInvolvement"]
    class_class_curie: ClassVar[str] = "dpv:HumanInvolvement"
    class_name: ClassVar[str] = "DpvHumanInvolvement"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvHumanInvolvement

    id: Union[str, DpvHumanInvolvementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvHumanInvolvementId):
            self.id = DpvHumanInvolvementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvInnovativeUseOfTechnology(DpvProcessingContext):
    """
    Indicates that technology is being used in an innovative manner
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InnovativeUseOfTechnology"]
    class_class_curie: ClassVar[str] = "dpv:InnovativeUseOfTechnology"
    class_name: ClassVar[str] = "DpvInnovativeUseOfTechnology"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvInnovativeUseOfTechnology

    id: Union[str, DpvInnovativeUseOfTechnologyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvInnovativeUseOfTechnologyId):
            self.id = DpvInnovativeUseOfTechnologyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvProcessingScale(DpvProcessingContext):
    """
    Scale of Processing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ProcessingScale"]
    class_class_curie: ClassVar[str] = "dpv:ProcessingScale"
    class_name: ClassVar[str] = "DpvProcessingScale"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvProcessingScale

    id: Union[str, DpvProcessingScaleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvProcessingScaleId):
            self.id = DpvProcessingScaleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvPublicRegisterOfEntities(DpvConcept):
    """
    A publicly available list of entities e.g. to indicate which entities perform a certain activity within a certain
    location or jurisdiction
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicRegisterOfEntities"]
    class_class_curie: ClassVar[str] = "dpv:PublicRegisterOfEntities"
    class_name: ClassVar[str] = "DpvPublicRegisterOfEntities"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvPublicRegisterOfEntities

    id: Union[str, DpvPublicRegisterOfEntitiesId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPublicRegisterOfEntitiesId):
            self.id = DpvPublicRegisterOfEntitiesId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvPurpose(DpvConcept):
    """
    Purpose or (broader) Goal associated with data or technology
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Purpose"]
    class_class_curie: ClassVar[str] = "dpv:Purpose"
    class_name: ClassVar[str] = "DpvPurpose"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvPurpose

    id: Union[str, DpvPurposeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPurposeId):
            self.id = DpvPurposeId(self.id)

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
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvRegion

    id: Union[str, DpvRegionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvRegionId):
            self.id = DpvRegionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvRight(DpvConcept):
    """
    The right(s) applicable, provided, or expected
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Right"]
    class_class_curie: ClassVar[str] = "dpv:Right"
    class_name: ClassVar[str] = "DpvRight"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvRight

    id: Union[str, DpvRightId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvRightId):
            self.id = DpvRightId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvRiskConcept(DpvConcept):
    """
    Parent concept for combining concepts associated with risk assessment such as actual and potential Risk, Risk
    Source, Consequences, and Impacts
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RiskConcept"]
    class_class_curie: ClassVar[str] = "dpv:RiskConcept"
    class_name: ClassVar[str] = "DpvRiskConcept"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvRiskConcept

    id: Union[str, DpvRiskConceptId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvRiskConceptId):
            self.id = DpvRiskConceptId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvRiskLevel(DpvConcept):
    """
    The magnitude of a risk expressed as an indication to aid in its management
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RiskLevel"]
    class_class_curie: ClassVar[str] = "dpv:RiskLevel"
    class_name: ClassVar[str] = "DpvRiskLevel"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvRiskLevel

    id: Union[str, DpvRiskLevelId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvRiskLevelId):
            self.id = DpvRiskLevelId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvRule(DpvConcept):
    """
    A rule describing a process or control that directs or determines if and how an activity should be conducted
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Rule"]
    class_class_curie: ClassVar[str] = "dpv:Rule"
    class_name: ClassVar[str] = "DpvRule"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvRule

    id: Union[str, DpvRuleId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvRuleId):
            self.id = DpvRuleId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvObligation(DpvRule):
    """
    A rule describing an obligation for performing an activity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Obligation"]
    class_class_curie: ClassVar[str] = "dpv:Obligation"
    class_name: ClassVar[str] = "DpvObligation"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvObligation

    id: Union[str, DpvObligationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvObligationId):
            self.id = DpvObligationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvPermission(DpvRule):
    """
    A rule describing a permission to perform an activity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Permission"]
    class_class_curie: ClassVar[str] = "dpv:Permission"
    class_name: ClassVar[str] = "DpvPermission"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvPermission

    id: Union[str, DpvPermissionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPermissionId):
            self.id = DpvPermissionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvProhibition(DpvRule):
    """
    A rule describing a prohibition to perform an activity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Prohibition"]
    class_class_curie: ClassVar[str] = "dpv:Prohibition"
    class_name: ClassVar[str] = "DpvProhibition"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvProhibition

    id: Union[str, DpvProhibitionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvProhibitionId):
            self.id = DpvProhibitionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvScoringOfIndividuals(DpvEvaluationScoring):
    """
    Processing that involves scoring of individuals
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ScoringOfIndividuals"]
    class_class_curie: ClassVar[str] = "dpv:ScoringOfIndividuals"
    class_name: ClassVar[str] = "DpvScoringOfIndividuals"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvScoringOfIndividuals

    id: Union[str, DpvScoringOfIndividualsId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvScoringOfIndividualsId):
            self.id = DpvScoringOfIndividualsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvSector(DpvConcept):
    """
    Sector describes the area of application or domain that indicates or restricts scope for interpretation and
    application of purpose e.g. Agriculture, Banking
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Sector"]
    class_class_curie: ClassVar[str] = "dpv:Sector"
    class_name: ClassVar[str] = "DpvSector"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvSector

    id: Union[str, DpvSectorId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvSectorId):
            self.id = DpvSectorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvSensitivePersonalData(DpvPersonalData):
    """
    Personal data that is considered 'sensitive' in terms of privacy and/or impact, and therefore requires additional
    considerations and/or protection
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SensitivePersonalData"]
    class_class_curie: ClassVar[str] = "dpv:SensitivePersonalData"
    class_name: ClassVar[str] = "DpvSensitivePersonalData"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvSensitivePersonalData

    id: Union[str, DpvSensitivePersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvSensitivePersonalDataId):
            self.id = DpvSensitivePersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvSeverity(DpvConcept):
    """
    The magnitude of being unwanted or having negative effects such as harmful impacts
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Severity"]
    class_class_curie: ClassVar[str] = "dpv:Severity"
    class_name: ClassVar[str] = "DpvSeverity"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvSeverity

    id: Union[str, DpvSeverityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvSeverityId):
            self.id = DpvSeverityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvSpecialCategoryPersonalData(DpvSensitivePersonalData):
    """
    Sensitive Personal Data whose use requires specific additional legal permission or justification
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SpecialCategoryPersonalData"]
    class_class_curie: ClassVar[str] = "dpv:SpecialCategoryPersonalData"
    class_name: ClassVar[str] = "DpvSpecialCategoryPersonalData"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvSpecialCategoryPersonalData

    id: Union[str, DpvSpecialCategoryPersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvSpecialCategoryPersonalDataId):
            self.id = DpvSpecialCategoryPersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvStatus(DpvConcept):
    """
    The status or state of something
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Status"]
    class_class_curie: ClassVar[str] = "dpv:Status"
    class_name: ClassVar[str] = "DpvStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvStatus

    id: Union[str, DpvStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvStatusId):
            self.id = DpvStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvActivityStatus(DpvStatus):
    """
    Status associated with activity operations and lifecycles
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ActivityStatus"]
    class_class_curie: ClassVar[str] = "dpv:ActivityStatus"
    class_name: ClassVar[str] = "DpvActivityStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvActivityStatus

    id: Union[str, DpvActivityStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvActivityStatusId):
            self.id = DpvActivityStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvAuditStatus(DpvStatus):
    """
    Status associated with Auditing or Investigation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["AuditStatus"]
    class_class_curie: ClassVar[str] = "dpv:AuditStatus"
    class_name: ClassVar[str] = "DpvAuditStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvAuditStatus

    id: Union[str, DpvAuditStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvAuditStatusId):
            self.id = DpvAuditStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvComplianceStatus(DpvStatus):
    """
    Status associated with Compliance with some norms, objectives, or requirements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ComplianceStatus"]
    class_class_curie: ClassVar[str] = "dpv:ComplianceStatus"
    class_name: ClassVar[str] = "DpvComplianceStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvComplianceStatus

    id: Union[str, DpvComplianceStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvComplianceStatusId):
            self.id = DpvComplianceStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvConformanceStatus(DpvStatus):
    """
    Status associated with conformance to a standard, guideline, code, or recommendation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConformanceStatus"]
    class_class_curie: ClassVar[str] = "dpv:ConformanceStatus"
    class_name: ClassVar[str] = "DpvConformanceStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvConformanceStatus

    id: Union[str, DpvConformanceStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvConformanceStatusId):
            self.id = DpvConformanceStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvConsentStatus(DpvStatus):
    """
    The state or status of 'consent' that provides information reflecting its operational status and validity for
    processing data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ConsentStatus"]
    class_class_curie: ClassVar[str] = "dpv:ConsentStatus"
    class_name: ClassVar[str] = "DpvConsentStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvConsentStatus

    id: Union[str, DpvConsentStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvConsentStatusId):
            self.id = DpvConsentStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvContractActivationStatus(DpvStatus):
    """
    Status associated with activation of a contract i.e. whether its terms are active and are required to be performed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractActivationStatus"]
    class_class_curie: ClassVar[str] = "dpv:ContractActivationStatus"
    class_name: ClassVar[str] = "DpvContractActivationStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvContractActivationStatus

    id: Union[str, DpvContractActivationStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvContractActivationStatusId):
            self.id = DpvContractActivationStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvContractExecutionStatus(DpvStatus):
    """
    Status associated with execution of a contract (i.e. signing and procedural aspects before the contract terms come
    in to effect)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractExecutionStatus"]
    class_class_curie: ClassVar[str] = "dpv:ContractExecutionStatus"
    class_name: ClassVar[str] = "DpvContractExecutionStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvContractExecutionStatus

    id: Union[str, DpvContractExecutionStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvContractExecutionStatusId):
            self.id = DpvContractExecutionStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvContractFulfilmentStatus(DpvStatus):
    """
    Status associated with fulfilment of a contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractFulfilmentStatus"]
    class_class_curie: ClassVar[str] = "dpv:ContractFulfilmentStatus"
    class_name: ClassVar[str] = "DpvContractFulfilmentStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvContractFulfilmentStatus

    id: Union[str, DpvContractFulfilmentStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvContractFulfilmentStatusId):
            self.id = DpvContractFulfilmentStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvContractPerformanceStatus(DpvStatus):
    """
    Status associated with performance of a contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractPerformanceStatus"]
    class_class_curie: ClassVar[str] = "dpv:ContractPerformanceStatus"
    class_name: ClassVar[str] = "DpvContractPerformanceStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvContractPerformanceStatus

    id: Union[str, DpvContractPerformanceStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvContractPerformanceStatusId):
            self.id = DpvContractPerformanceStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvContractPreparationStatus(DpvStatus):
    """
    Status associated with preparation of contracts before they are signed or accepted or executed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractPreparationStatus"]
    class_class_curie: ClassVar[str] = "dpv:ContractPreparationStatus"
    class_name: ClassVar[str] = "DpvContractPreparationStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvContractPreparationStatus

    id: Union[str, DpvContractPreparationStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvContractPreparationStatusId):
            self.id = DpvContractPreparationStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvContractTerminationStatus(DpvStatus):
    """
    Status associated with termination of a contract
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractTerminationStatus"]
    class_class_curie: ClassVar[str] = "dpv:ContractTerminationStatus"
    class_name: ClassVar[str] = "DpvContractTerminationStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvContractTerminationStatus

    id: Union[str, DpvContractTerminationStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvContractTerminationStatusId):
            self.id = DpvContractTerminationStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvContractualClauseFulfilmentStatus(DpvStatus):
    """
    Status associated with fulfilment of a contractual clause
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ContractualClauseFulfilmentStatus"]
    class_class_curie: ClassVar[str] = "dpv:ContractualClauseFulfilmentStatus"
    class_name: ClassVar[str] = "DpvContractualClauseFulfilmentStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvContractualClauseFulfilmentStatus

    id: Union[str, DpvContractualClauseFulfilmentStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvContractualClauseFulfilmentStatusId):
            self.id = DpvContractualClauseFulfilmentStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvEntityInformedStatus(DpvStatus):
    """
    Status indicating whether an entity is informed or uninformed about specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityInformedStatus"]
    class_class_curie: ClassVar[str] = "dpv:EntityInformedStatus"
    class_name: ClassVar[str] = "DpvEntityInformedStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvEntityInformedStatus

    id: Union[str, DpvEntityInformedStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvEntityInformedStatusId):
            self.id = DpvEntityInformedStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvEntityInvolvementStatus(DpvStatus):
    """
    Status indicating whether an entity is involved
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["EntityInvolvementStatus"]
    class_class_curie: ClassVar[str] = "dpv:EntityInvolvementStatus"
    class_name: ClassVar[str] = "DpvEntityInvolvementStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvEntityInvolvementStatus

    id: Union[str, DpvEntityInvolvementStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvEntityInvolvementStatusId):
            self.id = DpvEntityInvolvementStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvIntentionStatus(DpvStatus):
    """
    Status indicating whether the specified context was intended or unintended
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["IntentionStatus"]
    class_class_curie: ClassVar[str] = "dpv:IntentionStatus"
    class_name: ClassVar[str] = "DpvIntentionStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvIntentionStatus

    id: Union[str, DpvIntentionStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvIntentionStatusId):
            self.id = DpvIntentionStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvInvolvementStatus(DpvStatus):
    """
    Status indicating whether the involvement of specified context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["InvolvementStatus"]
    class_class_curie: ClassVar[str] = "dpv:InvolvementStatus"
    class_name: ClassVar[str] = "DpvInvolvementStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvInvolvementStatus

    id: Union[str, DpvInvolvementStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvInvolvementStatusId):
            self.id = DpvInvolvementStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvLawfulness(DpvComplianceStatus):
    """
    Status associated with expressing lawfulness or legal compliance
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Lawfulness"]
    class_class_curie: ClassVar[str] = "dpv:Lawfulness"
    class_name: ClassVar[str] = "DpvLawfulness"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvLawfulness

    id: Union[str, DpvLawfulnessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvLawfulnessId):
            self.id = DpvLawfulnessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvLegalObligationStatus(DpvStatus):
    """
    Status associated with use of Legal Obligation as a legal basis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegalObligationStatus"]
    class_class_curie: ClassVar[str] = "dpv:LegalObligationStatus"
    class_name: ClassVar[str] = "DpvLegalObligationStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvLegalObligationStatus

    id: Union[str, DpvLegalObligationStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvLegalObligationStatusId):
            self.id = DpvLegalObligationStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvLegitimateInterestStatus(DpvStatus):
    """
    Status associated with use of Legitimate Interest as a legal basis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["LegitimateInterestStatus"]
    class_class_curie: ClassVar[str] = "dpv:LegitimateInterestStatus"
    class_name: ClassVar[str] = "DpvLegitimateInterestStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvLegitimateInterestStatus

    id: Union[str, DpvLegitimateInterestStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvLegitimateInterestStatusId):
            self.id = DpvLegitimateInterestStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvNoticeStatus(DpvStatus):
    """
    Status associated with notice provision, use, and management
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NoticeStatus"]
    class_class_curie: ClassVar[str] = "dpv:NoticeStatus"
    class_name: ClassVar[str] = "DpvNoticeStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvNoticeStatus

    id: Union[str, DpvNoticeStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvNoticeStatusId):
            self.id = DpvNoticeStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvNotificationStatus(DpvStatus):
    """
    Status indicating whether notification(s) are planned, completed, or failed
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["NotificationStatus"]
    class_class_curie: ClassVar[str] = "dpv:NotificationStatus"
    class_name: ClassVar[str] = "DpvNotificationStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvNotificationStatus

    id: Union[str, DpvNotificationStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvNotificationStatusId):
            self.id = DpvNotificationStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvOfficialAuthorityExerciseStatus(DpvStatus):
    """
    Status associated with use of Official Authority as a legal basis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["OfficialAuthorityExerciseStatus"]
    class_class_curie: ClassVar[str] = "dpv:OfficialAuthorityExerciseStatus"
    class_name: ClassVar[str] = "DpvOfficialAuthorityExerciseStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvOfficialAuthorityExerciseStatus

    id: Union[str, DpvOfficialAuthorityExerciseStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvOfficialAuthorityExerciseStatusId):
            self.id = DpvOfficialAuthorityExerciseStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvPublicInterestStatus(DpvStatus):
    """
    Status associated with use of Public Interest as a legal basis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["PublicInterestStatus"]
    class_class_curie: ClassVar[str] = "dpv:PublicInterestStatus"
    class_name: ClassVar[str] = "DpvPublicInterestStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvPublicInterestStatus

    id: Union[str, DpvPublicInterestStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPublicInterestStatusId):
            self.id = DpvPublicInterestStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvRequestStatus(DpvStatus):
    """
    Status associated with requests
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RequestStatus"]
    class_class_curie: ClassVar[str] = "dpv:RequestStatus"
    class_name: ClassVar[str] = "DpvRequestStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvRequestStatus

    id: Union[str, DpvRequestStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvRequestStatusId):
            self.id = DpvRequestStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvReuseCompatibility(DpvStatus):
    """
    Status indicating whether the specified context is compatible with another earlier context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["ReuseCompatibility"]
    class_class_curie: ClassVar[str] = "dpv:ReuseCompatibility"
    class_name: ClassVar[str] = "DpvReuseCompatibility"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvReuseCompatibility

    id: Union[str, DpvReuseCompatibilityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvReuseCompatibilityId):
            self.id = DpvReuseCompatibilityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvRuleFulfilmentStatus(DpvStatus):
    """
    Status associated with a rule for indicating whether it is applicable, or has been utilised, and whether the
    requirements of the rule have been fulfilled or violated
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["RuleFulfilmentStatus"]
    class_class_curie: ClassVar[str] = "dpv:RuleFulfilmentStatus"
    class_name: ClassVar[str] = "DpvRuleFulfilmentStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvRuleFulfilmentStatus

    id: Union[str, DpvRuleFulfilmentStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvRuleFulfilmentStatusId):
            self.id = DpvRuleFulfilmentStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvSupraNationalUnion(DpvJurisdiction):
    """
    A political union of two or more countries with an establishment of common authority
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["SupraNationalUnion"]
    class_class_curie: ClassVar[str] = "dpv:SupraNationalUnion"
    class_name: ClassVar[str] = "DpvSupraNationalUnion"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvSupraNationalUnion

    id: Union[str, DpvSupraNationalUnionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvSupraNationalUnionId):
            self.id = DpvSupraNationalUnionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvTechnicalMeasure(DpvConcept):
    """
    Technical measures used to safeguard and ensure good practices in connection with data and technologies
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["TechnicalMeasure"]
    class_class_curie: ClassVar[str] = "dpv:TechnicalMeasure"
    class_name: ClassVar[str] = "DpvTechnicalMeasure"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvTechnicalMeasure

    id: Union[str, DpvTechnicalMeasureId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvTechnicalMeasureId):
            self.id = DpvTechnicalMeasureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvTechnology(DpvConcept):
    """
    The technology, technological implementation, or any techniques, skills, methods, and processes used or applied
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["Technology"]
    class_class_curie: ClassVar[str] = "dpv:Technology"
    class_name: ClassVar[str] = "DpvTechnology"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvTechnology

    id: Union[str, DpvTechnologyId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvTechnologyId):
            self.id = DpvTechnologyId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvVitalInterestStatus(DpvStatus):
    """
    Status associated with use of Vital Interest as a legal basis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DPV["VitalInterestStatus"]
    class_class_curie: ClassVar[str] = "dpv:VitalInterestStatus"
    class_name: ClassVar[str] = "DpvVitalInterestStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvVitalInterestStatus

    id: Union[str, DpvVitalInterestStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvVitalInterestStatusId):
            self.id = DpvVitalInterestStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvPdPersonalData(DpvConcept):
    """
    A kind of term DPV names as pd:PersonalData and does not define.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PD["PersonalData"]
    class_class_curie: ClassVar[str] = "pd:PersonalData"
    class_name: ClassVar[str] = "DpvPdPersonalData"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvPdPersonalData

    id: Union[str, DpvPdPersonalDataId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPdPersonalDataId):
            self.id = DpvPdPersonalDataId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvActor(DpvConcept):
    """
    Actors and Entities involved in provision, use, and management of Technology
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TECH["Actor"]
    class_class_curie: ClassVar[str] = "tech:Actor"
    class_name: ClassVar[str] = "DpvActor"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvActor

    id: Union[str, DpvActorId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvActorId):
            self.id = DpvActorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvCommunicationMechanism(DpvTechnology):
    """
    Communication mechanism used or provided by Technology
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TECH["CommunicationMechanism"]
    class_class_curie: ClassVar[str] = "tech:CommunicationMechanism"
    class_name: ClassVar[str] = "DpvCommunicationMechanism"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvCommunicationMechanism

    id: Union[str, DpvCommunicationMechanismId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvCommunicationMechanismId):
            self.id = DpvCommunicationMechanismId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDocumentation(DpvConcept):
    """
    Information describing use, functionality, design, or other technical aspects of the Technology
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TECH["Documentation"]
    class_class_curie: ClassVar[str] = "tech:Documentation"
    class_name: ClassVar[str] = "DpvDocumentation"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDocumentation

    id: Union[str, DpvDocumentationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDocumentationId):
            self.id = DpvDocumentationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvProvisionMethod(DpvTechnology):
    """
    Method associated with provision or use of technology
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TECH["ProvisionMethod"]
    class_class_curie: ClassVar[str] = "tech:ProvisionMethod"
    class_name: ClassVar[str] = "DpvProvisionMethod"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvProvisionMethod

    id: Union[str, DpvProvisionMethodId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvProvisionMethodId):
            self.id = DpvProvisionMethodId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvProvisionStatus(DpvStatus):
    """
    Status indicating whether Technology has been provided
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TECH["ProvisionStatus"]
    class_class_curie: ClassVar[str] = "tech:ProvisionStatus"
    class_name: ClassVar[str] = "DpvProvisionStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvProvisionStatus

    id: Union[str, DpvProvisionStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvProvisionStatusId):
            self.id = DpvProvisionStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvTechCapability(DpvConcept):
    """
    Expression of what the technology is capable of achieving or providing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TECH["Capability"]
    class_class_curie: ClassVar[str] = "tech:Capability"
    class_name: ClassVar[str] = "DpvTechCapability"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvTechCapability

    id: Union[str, DpvTechCapabilityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvTechCapabilityId):
            self.id = DpvTechCapabilityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvTechMarketAvailabilityStatus(DpvStatus):
    """
    Status indicating whether Technology is available on the market
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TECH["MarketAvailabilityStatus"]
    class_class_curie: ClassVar[str] = "tech:MarketAvailabilityStatus"
    class_name: ClassVar[str] = "DpvTechMarketAvailabilityStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvTechMarketAvailabilityStatus

    id: Union[str, DpvTechMarketAvailabilityStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvTechMarketAvailabilityStatusId):
            self.id = DpvTechMarketAvailabilityStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvAiCapability(DpvTechnology):
    """
    Capability or use of AI to achieve a technical goal or objective
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI["Capability"]
    class_class_curie: ClassVar[str] = "ai:Capability"
    class_name: ClassVar[str] = "DpvAiCapability"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvAiCapability

    id: Union[str, DpvAiCapabilityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvAiCapabilityId):
            self.id = DpvAiCapabilityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvLifecycleStage(DpvConcept):
    """
    A stage in the lifecycle of AI
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI["LifecycleStage"]
    class_class_curie: ClassVar[str] = "ai:LifecycleStage"
    class_name: ClassVar[str] = "DpvLifecycleStage"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvLifecycleStage

    id: Union[str, DpvLifecycleStageId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvLifecycleStageId):
            self.id = DpvLifecycleStageId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvTechnique(DpvTechnology):
    """
    The underlying technological algorithm, method, or process that forms the technique for using or applying AI
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI["Technique"]
    class_class_curie: ClassVar[str] = "ai:Technique"
    class_name: ClassVar[str] = "DpvTechnique"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvTechnique

    id: Union[str, DpvTechniqueId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvTechniqueId):
            self.id = DpvTechniqueId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvTrainingTechnique(DpvProcessing):
    """
    Process to determine or to improve the parameters of a machine learning model based on a machine learning
    algorithm by using training data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AI["TrainingTechnique"]
    class_class_curie: ClassVar[str] = "ai:TrainingTechnique"
    class_name: ClassVar[str] = "DpvTrainingTechnique"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvTrainingTechnique

    id: Union[str, DpvTrainingTechniqueId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvTrainingTechniqueId):
            self.id = DpvTrainingTechniqueId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvAvailabilityConcept(DpvRiskConcept):
    """
    Indicates a concept is relevant to 'Availability' in CIA InfoSec model
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RISK["AvailabilityConcept"]
    class_class_curie: ClassVar[str] = "risk:AvailabilityConcept"
    class_name: ClassVar[str] = "DpvAvailabilityConcept"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvAvailabilityConcept

    id: Union[str, DpvAvailabilityConceptId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvAvailabilityConceptId):
            self.id = DpvAvailabilityConceptId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvConfidentialityConcept(DpvRiskConcept):
    """
    Indicates a concept is relevant to 'Confidentiality' in CIA InfoSec model
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RISK["ConfidentialityConcept"]
    class_class_curie: ClassVar[str] = "risk:ConfidentialityConcept"
    class_name: ClassVar[str] = "DpvConfidentialityConcept"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvConfidentialityConcept

    id: Union[str, DpvConfidentialityConceptId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvConfidentialityConceptId):
            self.id = DpvConfidentialityConceptId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvIncidentInvestigationStatus(DpvStatus):
    """
    Status associated with investigation of an incident
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RISK["IncidentInvestigationStatus"]
    class_class_curie: ClassVar[str] = "risk:IncidentInvestigationStatus"
    class_name: ClassVar[str] = "DpvIncidentInvestigationStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvIncidentInvestigationStatus

    id: Union[str, DpvIncidentInvestigationStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvIncidentInvestigationStatusId):
            self.id = DpvIncidentInvestigationStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvIncidentNotice(DpvOrganisationalMeasure):
    """
    Notice associated with an incident
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RISK["IncidentNotice"]
    class_class_curie: ClassVar[str] = "risk:IncidentNotice"
    class_name: ClassVar[str] = "DpvIncidentNotice"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvIncidentNotice

    id: Union[str, DpvIncidentNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvIncidentNoticeId):
            self.id = DpvIncidentNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvIncidentStatus(DpvStatus):
    """
    Status associated with an incident
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RISK["IncidentStatus"]
    class_class_curie: ClassVar[str] = "risk:IncidentStatus"
    class_name: ClassVar[str] = "DpvIncidentStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvIncidentStatus

    id: Union[str, DpvIncidentStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvIncidentStatusId):
            self.id = DpvIncidentStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvIntegrityConcept(DpvRiskConcept):
    """
    Indicates a concept is relevant to 'Integrity' in CIA InfoSec model
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RISK["IntegrityConcept"]
    class_class_curie: ClassVar[str] = "risk:IntegrityConcept"
    class_name: ClassVar[str] = "DpvIntegrityConcept"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvIntegrityConcept

    id: Union[str, DpvIntegrityConceptId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvIntegrityConceptId):
            self.id = DpvIntegrityConceptId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvPotentialConsequence(DpvRiskConcept):
    """
    Indicates a concept can potentially be a 'consequence concept within an use-case
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RISK["PotentialConsequence"]
    class_class_curie: ClassVar[str] = "risk:PotentialConsequence"
    class_name: ClassVar[str] = "DpvPotentialConsequence"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvPotentialConsequence

    id: Union[str, DpvPotentialConsequenceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPotentialConsequenceId):
            self.id = DpvPotentialConsequenceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvPotentialImpact(DpvRiskConcept):
    """
    Indicates a concept can potentially be a 'impact' concept within an use-case
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RISK["PotentialImpact"]
    class_class_curie: ClassVar[str] = "risk:PotentialImpact"
    class_name: ClassVar[str] = "DpvPotentialImpact"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvPotentialImpact

    id: Union[str, DpvPotentialImpactId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPotentialImpactId):
            self.id = DpvPotentialImpactId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvPotentialRisk(DpvRiskConcept):
    """
    Indicates a concept can potentially be a 'risk' concept within an use-case
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RISK["PotentialRisk"]
    class_class_curie: ClassVar[str] = "risk:PotentialRisk"
    class_name: ClassVar[str] = "DpvPotentialRisk"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvPotentialRisk

    id: Union[str, DpvPotentialRiskId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPotentialRiskId):
            self.id = DpvPotentialRiskId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvPotentialRiskSource(DpvRiskConcept):
    """
    Indicates a concept can potentially be a 'risk source' concept within an use-case
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RISK["PotentialRiskSource"]
    class_class_curie: ClassVar[str] = "risk:PotentialRiskSource"
    class_name: ClassVar[str] = "DpvPotentialRiskSource"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvPotentialRiskSource

    id: Union[str, DpvPotentialRiskSourceId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPotentialRiskSourceId):
            self.id = DpvPotentialRiskSourceId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvRiskAnalysis(DpvConcept):
    """
    A technique or method used to analyse and identify risk levels, sources, likelihoods, severities, and other
    necessary information required to conduct risk management procedures
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RISK["RiskAnalysis"]
    class_class_curie: ClassVar[str] = "risk:RiskAnalysis"
    class_name: ClassVar[str] = "DpvRiskAnalysis"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvRiskAnalysis

    id: Union[str, DpvRiskAnalysisId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvRiskAnalysisId):
            self.id = DpvRiskAnalysisId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvRiskControl(DpvConcept):
    """
    Control that modifies risk
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RISK["RiskControl"]
    class_class_curie: ClassVar[str] = "risk:RiskControl"
    class_name: ClassVar[str] = "DpvRiskControl"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvRiskControl

    id: Union[str, DpvRiskControlId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvRiskControlId):
            self.id = DpvRiskControlId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvAISystem(DpvTechnology):
    """
    A machine-based system designed to operate with varying levels of autonomy and that may exhibit adaptiveness after
    deployment and that, for explicit or implicit objectives, infers, from the input it receives, how to generate
    outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual
    environments.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_AIACT["AISystem"]
    class_class_curie: ClassVar[str] = "eu-aiact:AISystem"
    class_name: ClassVar[str] = "DpvAISystem"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvAISystem

    id: Union[str, DpvAISystemId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvAISystemId):
            self.id = DpvAISystemId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvAdequacyDecision(DpvLegalBasis):
    """
    An adequacy decision as per GDPR Art.45(3) for the transfer of data to a third country or an international
    organisation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_GDPR["AdequacyDecision"]
    class_class_curie: ClassVar[str] = "eu-gdpr:AdequacyDecision"
    class_name: ClassVar[str] = "DpvAdequacyDecision"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvAdequacyDecision

    id: Union[str, DpvAdequacyDecisionId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvAdequacyDecisionId):
            self.id = DpvAdequacyDecisionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvChangeCategory(DpvConcept):
    """
    A categorisation of the change associated with the AI system
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_AIACT["ChangeCategory"]
    class_class_curie: ClassVar[str] = "eu-aiact:ChangeCategory"
    class_name: ClassVar[str] = "DpvChangeCategory"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvChangeCategory

    id: Union[str, DpvChangeCategoryId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvChangeCategoryId):
            self.id = DpvChangeCategoryId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDBIARiskStatus(DpvAuditStatus):
    """
    Status reflecting the status of risk associated with a DBIA regarding rights and freedoms of natural persons
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_GDPR["DBIARiskStatus"]
    class_class_curie: ClassVar[str] = "eu-gdpr:DBIARiskStatus"
    class_name: ClassVar[str] = "DpvDBIARiskStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDBIARiskStatus

    id: Union[str, DpvDBIARiskStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDBIARiskStatusId):
            self.id = DpvDBIARiskStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDPIAConformity(DpvConformanceStatus):
    """
    Conformity of a process with a DPIA
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_GDPR["DPIAConformity"]
    class_class_curie: ClassVar[str] = "eu-gdpr:DPIAConformity"
    class_name: ClassVar[str] = "DpvDPIAConformity"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDPIAConformity

    id: Union[str, DpvDPIAConformityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDPIAConformityId):
            self.id = DpvDPIAConformityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDPIANecessityStatus(DpvAuditStatus):
    """
    Status reflecting whether a DPIA is necessary
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_GDPR["DPIANecessityStatus"]
    class_class_curie: ClassVar[str] = "eu-gdpr:DPIANecessityStatus"
    class_name: ClassVar[str] = "DpvDPIANecessityStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDPIANecessityStatus

    id: Union[str, DpvDPIANecessityStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDPIANecessityStatusId):
            self.id = DpvDPIANecessityStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDPIAOutcomeStatus(DpvAuditStatus):
    """
    Status reflecting the outcomes of a DPIA
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_GDPR["DPIAOutcomeStatus"]
    class_class_curie: ClassVar[str] = "eu-gdpr:DPIAOutcomeStatus"
    class_name: ClassVar[str] = "DpvDPIAOutcomeStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDPIAOutcomeStatus

    id: Union[str, DpvDPIAOutcomeStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDPIAOutcomeStatusId):
            self.id = DpvDPIAOutcomeStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDPIAProcessingRecommendation(DpvAuditStatus):
    """
    Recommendation from the DPIA regarding processing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_GDPR["DPIAProcessingRecommendation"]
    class_class_curie: ClassVar[str] = "eu-gdpr:DPIAProcessingRecommendation"
    class_name: ClassVar[str] = "DpvDPIAProcessingRecommendation"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDPIAProcessingRecommendation

    id: Union[str, DpvDPIAProcessingRecommendationId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDPIAProcessingRecommendationId):
            self.id = DpvDPIAProcessingRecommendationId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDPIARiskStatus(DpvAuditStatus):
    """
    Status reflecting the status of risk associated with a DPIA
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_GDPR["DPIARiskStatus"]
    class_class_curie: ClassVar[str] = "eu-gdpr:DPIARiskStatus"
    class_name: ClassVar[str] = "DpvDPIARiskStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDPIARiskStatus

    id: Union[str, DpvDPIARiskStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDPIARiskStatusId):
            self.id = DpvDPIARiskStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDataBreachNotice(DpvOrganisationalMeasure):
    """
    Notice associated with data breach providing information in compliance with GDPR
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_GDPR["DataBreachNotice"]
    class_class_curie: ClassVar[str] = "eu-gdpr:DataBreachNotice"
    class_name: ClassVar[str] = "DpvDataBreachNotice"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDataBreachNotice

    id: Union[str, DpvDataBreachNoticeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDataBreachNoticeId):
            self.id = DpvDataBreachNoticeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDataBreachNoticeRequirement(DpvAuditStatus):
    """
    Whether a Data Breach notification is required
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_GDPR["DataBreachNoticeRequirement"]
    class_class_curie: ClassVar[str] = "eu-gdpr:DataBreachNoticeRequirement"
    class_name: ClassVar[str] = "DpvDataBreachNoticeRequirement"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDataBreachNoticeRequirement

    id: Union[str, DpvDataBreachNoticeRequirementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDataBreachNoticeRequirementId):
            self.id = DpvDataBreachNoticeRequirementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvEuAiactMarketAvailabilityStatus(DpvTechMarketAvailabilityStatus):
    """
    Status associated with whether the AI system or GPAI Model is available for distribution or use on the market in
    the course of a commercial activity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_AIACT["MarketAvailabilityStatus"]
    class_class_curie: ClassVar[str] = "eu-aiact:MarketAvailabilityStatus"
    class_name: ClassVar[str] = "DpvEuAiactMarketAvailabilityStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvEuAiactMarketAvailabilityStatus

    id: Union[str, DpvEuAiactMarketAvailabilityStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvEuAiactMarketAvailabilityStatusId):
            self.id = DpvEuAiactMarketAvailabilityStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvEuAiactRiskLevel(DpvRiskLevel):
    """
    Enumeration of AI Act's risk-based categorisation which determines the prohibitions and obligations for AI systems
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_AIACT["RiskLevel"]
    class_class_curie: ClassVar[str] = "eu-aiact:RiskLevel"
    class_name: ClassVar[str] = "DpvEuAiactRiskLevel"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvEuAiactRiskLevel

    id: Union[str, DpvEuAiactRiskLevelId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvEuAiactRiskLevelId):
            self.id = DpvEuAiactRiskLevelId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvEuGdprDataProtectionAuthority(DpvDataProtectionAuthority):
    """
    ‘Supervisory Authority’ or 'Data Protection Authority' means an independent public authority which is established
    by a Member State pursuant to Article 51
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_GDPR["DataProtectionAuthority"]
    class_class_curie: ClassVar[str] = "eu-gdpr:DataProtectionAuthority"
    class_name: ClassVar[str] = "DpvEuGdprDataProtectionAuthority"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvEuGdprDataProtectionAuthority

    id: Union[str, DpvEuGdprDataProtectionAuthorityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvEuGdprDataProtectionAuthorityId):
            self.id = DpvEuGdprDataProtectionAuthorityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvEuGdprProcessing(DpvProcessing):
    """
    ‘Processing’ means any operation or set of operations which is performed on personal data or on sets of personal
    data, whether or not by automated means, such as collection, recording, organisation, structuring, storage,
    adaptation or alteration, retrieval, consultation, use, disclosure by transmission, dissemination or otherwise
    making available, alignment or combination, restriction, erasure or destruction
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_GDPR["Processing"]
    class_class_curie: ClassVar[str] = "eu-gdpr:Processing"
    class_name: ClassVar[str] = "DpvEuGdprProcessing"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvEuGdprProcessing

    id: Union[str, DpvEuGdprProcessingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvEuGdprProcessingId):
            self.id = DpvEuGdprProcessingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvHighRiskAISystem(DpvAISystem):
    """
    High-risk AI system according to the AI Act
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_AIACT["HighRiskAISystem"]
    class_class_curie: ClassVar[str] = "eu-aiact:HighRiskAISystem"
    class_name: ClassVar[str] = "DpvHighRiskAISystem"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvHighRiskAISystem

    id: Union[str, DpvHighRiskAISystemId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvHighRiskAISystemId):
            self.id = DpvHighRiskAISystemId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvMarketPlacementStatus(DpvTechMarketAvailabilityStatus):
    """
    Status associated with whether the AI system or GPAI Model has been 'first' made available on the market
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_AIACT["MarketPlacementStatus"]
    class_class_curie: ClassVar[str] = "eu-aiact:MarketPlacementStatus"
    class_name: ClassVar[str] = "DpvMarketPlacementStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvMarketPlacementStatus

    id: Union[str, DpvMarketPlacementStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvMarketPlacementStatusId):
            self.id = DpvMarketPlacementStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvProhibitedAISystem(DpvAISystem):
    """
    Prohibited AI system according to Article 5, AI Act
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_AIACT["ProhibitedAISystem"]
    class_class_curie: ClassVar[str] = "eu-aiact:ProhibitedAISystem"
    class_name: ClassVar[str] = "DpvProhibitedAISystem"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvProhibitedAISystem

    id: Union[str, DpvProhibitedAISystemId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvProhibitedAISystemId):
            self.id = DpvProhibitedAISystemId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvProportionalityStatus(DpvStatus):
    """
    Status indicating whether the specific activity or context is proportionate
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_GDPR["ProportionalityStatus"]
    class_class_curie: ClassVar[str] = "eu-gdpr:ProportionalityStatus"
    class_name: ClassVar[str] = "DpvProportionalityStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvProportionalityStatus

    id: Union[str, DpvProportionalityStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvProportionalityStatusId):
            self.id = DpvProportionalityStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvRegulatedHealthDataHolder(DpvConcept):
    """
    Solche datenhaltenden Stellen, die gesetzlich geregelt sind, wie das Forschungsdatenzentrum Gesundheit, das
    Zentrum für Krebregisterdaten beim RKI und die Plattform nach §64e Abs.9 des fünften Buches Sozialgesetzbuch
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DE_GDNG["RegulatedHealthDataHolder"]
    class_class_curie: ClassVar[str] = "de-gdng:RegulatedHealthDataHolder"
    class_name: ClassVar[str] = "DpvRegulatedHealthDataHolder"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvRegulatedHealthDataHolder

    id: Union[str, DpvRegulatedHealthDataHolderId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvRegulatedHealthDataHolderId):
            self.id = DpvRegulatedHealthDataHolderId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvServiceSupplyStatus(DpvProvisionStatus):
    """
    Status associated with whether the AI system has been supplied for use or put in to service or been recalled or
    withdrawn
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EU_AIACT["ServiceSupplyStatus"]
    class_class_curie: ClassVar[str] = "eu-aiact:ServiceSupplyStatus"
    class_name: ClassVar[str] = "DpvServiceSupplyStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvServiceSupplyStatus

    id: Union[str, DpvServiceSupplyStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvServiceSupplyStatusId):
            self.id = DpvServiceSupplyStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvSectorHealthReuseCompatibility(DpvReuseCompatibility):
    """
    Status indicating whether the reuse of health data is compatible for given context
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SECTOR_HEALTH["ReuseCompatibility"]
    class_class_curie: ClassVar[str] = "sector-health:ReuseCompatibility"
    class_name: ClassVar[str] = "DpvSectorHealthReuseCompatibility"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvSectorHealthReuseCompatibility

    id: Union[str, DpvSectorHealthReuseCompatibilityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvSectorHealthReuseCompatibilityId):
            self.id = DpvSectorHealthReuseCompatibilityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvAgentNegotiationBehaviour(DpvContractualClause):
    """
    Term that indicates the behaviour of the Agent in relation to negotiations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["AgentNegotiationBehaviour"]
    class_class_curie: ClassVar[str] = "ieee-7012:AgentNegotiationBehaviour"
    class_name: ClassVar[str] = "DpvAgentNegotiationBehaviour"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvAgentNegotiationBehaviour

    id: Union[str, DpvAgentNegotiationBehaviourId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvAgentNegotiationBehaviourId):
            self.id = DpvAgentNegotiationBehaviourId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvAgentRequestBehaviour(DpvContractualClause):
    """
    Term that indicates the behaviour of the Agent in relation to requests
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["AgentRequestBehaviour"]
    class_class_curie: ClassVar[str] = "ieee-7012:AgentRequestBehaviour"
    class_name: ClassVar[str] = "DpvAgentRequestBehaviour"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvAgentRequestBehaviour

    id: Union[str, DpvAgentRequestBehaviourId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvAgentRequestBehaviourId):
            self.id = DpvAgentRequestBehaviourId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvAgreement(DpvContractualClause):
    """
    A compound set of terms or clauses, proposed and offered before a formal contract between parties, and also
    referred to as a "proposal" pr "proposed agreement"
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["Agreement"]
    class_class_curie: ClassVar[str] = "ieee-7012:Agreement"
    class_name: ClassVar[str] = "DpvAgreement"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvAgreement

    id: Union[str, DpvAgreementId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvAgreementId):
            self.id = DpvAgreementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvAgreementNegotiationStatus(DpvStatus):
    """
    Status associated with the Agreement Negotiation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["AgreementNegotiationStatus"]
    class_class_curie: ClassVar[str] = "ieee-7012:AgreementNegotiationStatus"
    class_name: ClassVar[str] = "DpvAgreementNegotiationStatus"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvAgreementNegotiationStatus

    id: Union[str, DpvAgreementNegotiationStatusId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvAgreementNegotiationStatusId):
            self.id = DpvAgreementNegotiationStatusId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvConflictResolutionTerm(DpvContractualClause):
    """
    Term related to resolving conflicts in Term(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["ConflictResolutionTerm"]
    class_class_curie: ClassVar[str] = "ieee-7012:ConflictResolutionTerm"
    class_name: ClassVar[str] = "DpvConflictResolutionTerm"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvConflictResolutionTerm

    id: Union[str, DpvConflictResolutionTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvConflictResolutionTermId):
            self.id = DpvConflictResolutionTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDataDeletionTerm(DpvContractualClause):
    """
    Term that indicates deletion regarding data as an obligation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["DataDeletionTerm"]
    class_class_curie: ClassVar[str] = "ieee-7012:DataDeletionTerm"
    class_name: ClassVar[str] = "DpvDataDeletionTerm"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDataDeletionTerm

    id: Union[str, DpvDataDeletionTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDataDeletionTermId):
            self.id = DpvDataDeletionTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDataSharingTerm(DpvContractualClause):
    """
    Term related to Data Sharing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["DataSharingTerm"]
    class_class_curie: ClassVar[str] = "ieee-7012:DataSharingTerm"
    class_name: ClassVar[str] = "DpvDataSharingTerm"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDataSharingTerm

    id: Union[str, DpvDataSharingTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDataSharingTermId):
            self.id = DpvDataSharingTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDeonticInterpretationTerm(DpvContractualClause):
    """
    Term related to interpretation of the Term(s) using deontic logic
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["DeonticInterpretationTerm"]
    class_class_curie: ClassVar[str] = "ieee-7012:DeonticInterpretationTerm"
    class_name: ClassVar[str] = "DpvDeonticInterpretationTerm"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDeonticInterpretationTerm

    id: Union[str, DpvDeonticInterpretationTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDeonticInterpretationTermId):
            self.id = DpvDeonticInterpretationTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvPortabilityTerm(DpvContractualClause):
    """
    Term that indicates portability of data from service provider to individual
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["PortabilityTerm"]
    class_class_curie: ClassVar[str] = "ieee-7012:PortabilityTerm"
    class_name: ClassVar[str] = "DpvPortabilityTerm"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvPortabilityTerm

    id: Union[str, DpvPortabilityTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPortabilityTermId):
            self.id = DpvPortabilityTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvPreferenceApplicability(DpvContractualClause):
    """
    Term that indicates the applicability of Privacy Preference(s)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["PreferenceApplicability"]
    class_class_curie: ClassVar[str] = "ieee-7012:PreferenceApplicability"
    class_name: ClassVar[str] = "DpvPreferenceApplicability"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvPreferenceApplicability

    id: Union[str, DpvPreferenceApplicabilityId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPreferenceApplicabilityId):
            self.id = DpvPreferenceApplicabilityId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvProfilingTerm(DpvContractualClause):
    """
    Term related to Profiling
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["ProfilingTerm"]
    class_class_curie: ClassVar[str] = "ieee-7012:ProfilingTerm"
    class_name: ClassVar[str] = "DpvProfilingTerm"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvProfilingTerm

    id: Union[str, DpvProfilingTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvProfilingTermId):
            self.id = DpvProfilingTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvTrackingTerm(DpvContractualClause):
    """
    Term related to Tracking
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["TrackingTerm"]
    class_class_curie: ClassVar[str] = "ieee-7012:TrackingTerm"
    class_name: ClassVar[str] = "DpvTrackingTerm"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvTrackingTerm

    id: Union[str, DpvTrackingTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvTrackingTermId):
            self.id = DpvTrackingTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvTransparencyTerm(DpvContractualClause):
    """
    Term that indicates transparency as an obligation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["TransparencyTerm"]
    class_class_curie: ClassVar[str] = "ieee-7012:TransparencyTerm"
    class_name: ClassVar[str] = "DpvTransparencyTerm"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvTransparencyTerm

    id: Union[str, DpvTransparencyTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvTransparencyTermId):
            self.id = DpvTransparencyTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvDataTransparencyTerm(DpvTransparencyTerm):
    """
    Term that indicates transparency regarding data involved and its source as an obligation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["DataTransparencyTerm"]
    class_class_curie: ClassVar[str] = "ieee-7012:DataTransparencyTerm"
    class_name: ClassVar[str] = "DpvDataTransparencyTerm"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvDataTransparencyTerm

    id: Union[str, DpvDataTransparencyTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvDataTransparencyTermId):
            self.id = DpvDataTransparencyTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvPartyTransparencyTerm(DpvTransparencyTerm):
    """
    Term that indicates transparency regarding identities and involvement of parties in specific roles as an obligation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["PartyTransparencyTerm"]
    class_class_curie: ClassVar[str] = "ieee-7012:PartyTransparencyTerm"
    class_name: ClassVar[str] = "DpvPartyTransparencyTerm"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvPartyTransparencyTerm

    id: Union[str, DpvPartyTransparencyTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPartyTransparencyTermId):
            self.id = DpvPartyTransparencyTermId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DpvPurposeTransparencyTerm(DpvTransparencyTerm):
    """
    Term that indicates transparency regarding purposes involved for processing of data and technologies as an
    obligation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = IEEE_7012["PurposeTransparencyTerm"]
    class_class_curie: ClassVar[str] = "ieee-7012:PurposeTransparencyTerm"
    class_name: ClassVar[str] = "DpvPurposeTransparencyTerm"
    class_model_uri: ClassVar[URIRef] = DPV_LINKML.DpvPurposeTransparencyTerm

    id: Union[str, DpvPurposeTransparencyTermId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DpvPurposeTransparencyTermId):
            self.id = DpvPurposeTransparencyTermId(self.id)

        super().__post_init__(**kwargs)


# Enumerations
class DpvFamily(EnumDefinitionImpl):
    """
    The parts of a release, one file each.
    """
    core = PermissibleValue(
        text="core",
        title="Core",
        description="The vocabulary at https://w3id.org/dpv and the terms it adopts from others.")
    pd = PermissibleValue(
        text="pd",
        title="Personal Data",
        description="The personal data vocabulary.")
    tech = PermissibleValue(
        text="tech",
        title="Technology",
        description="The technology vocabulary.")
    ai = PermissibleValue(
        text="ai",
        title="Artificial Intelligence",
        description="The artificial intelligence vocabulary.")
    risk = PermissibleValue(
        text="risk",
        title="Risk",
        description="The risk vocabulary.")
    justifications = PermissibleValue(
        text="justifications",
        title="Justifications",
        description="The justifications vocabulary.")
    loc = PermissibleValue(
        text="loc",
        title="Locations",
        description="The locations vocabulary.")
    legal = PermissibleValue(
        text="legal",
        title="Laws and Authorities",
        description="The legal vocabularies, of each jurisdiction and each EU law.")
    sector = PermissibleValue(
        text="sector",
        title="Sectors",
        description="The sector vocabularies.")
    standards = PermissibleValue(
        text="standards",
        title="Standards",
        description="The vocabularies of other standards.")
    agents = PermissibleValue(
        text="agents",
        title="Agents",
        description="The contributors.")
    examples = PermissibleValue(
        text="examples",
        title="Examples",
        description="The examples.")

    _defn = EnumDefinition(
        name="DpvFamily",
        description="The parts of a release, one file each.",
    )

class DpvTermStatus(EnumDefinitionImpl):
    """
    How DPV's editors mark a term's standing.
    """
    accepted = PermissibleValue(
        text="accepted",
        title="Accepted",
        description="The Community Group has accepted the term.")
    modified = PermissibleValue(
        text="modified",
        title="Modified",
        description="The term changed in a recent release.")
    sunset = PermissibleValue(
        text="sunset",
        title="Sunset",
        description="The term is on its way out of the vocabulary.")

    _defn = EnumDefinition(
        name="DpvTermStatus",
        description="How DPV's editors mark a term's standing.",
    )

# Slots
class slots:
    pass

slots.concepts = Slot(uri=DPV_LINKML.concepts, name="concepts", curie=DPV_LINKML.curie('concepts'),
                   model_uri=DPV_LINKML.concepts, domain=None, range=Optional[Union[dict[Union[str, DpvConceptId], Union[dict, DpvConcept]], list[Union[dict, DpvConcept]]]])

slots.name = Slot(uri=FOAF.name, name="name", curie=FOAF.curie('name'),
                   model_uri=DPV_LINKML.name, domain=None, range=str)

slots.memberOf = Slot(uri=ORG.memberOf, name="memberOf", curie=ORG.curie('memberOf'),
                   model_uri=DPV_LINKML.memberOf, domain=None, range=Optional[Union[Union[str, DpvAgentId], list[Union[str, DpvAgentId]]]],
                   pattern=re.compile(r'^dpv_agent:(person|org)-[a-z0-9-]+$'))

slots.url = Slot(uri=SDO.url, name="url", curie=SDO.curie('url'),
                   model_uri=DPV_LINKML.url, domain=None, range=Optional[str])

slots.id = Slot(uri=DPV_LINKML.id, name="id", curie=DPV_LINKML.curie('id'),
                   model_uri=DPV_LINKML.id, domain=None, range=URIRef,
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                   model_uri=DPV_LINKML.title, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=DPV_LINKML.description, domain=None, range=Optional[str])

slots.identifier = Slot(uri=DCTERMS.identifier, name="identifier", curie=DCTERMS.curie('identifier'),
                   model_uri=DPV_LINKML.identifier, domain=None, range=Optional[str])

slots.bibliographicCitation = Slot(uri=DCTERMS.bibliographicCitation, name="bibliographicCitation", curie=DCTERMS.curie('bibliographicCitation'),
                   model_uri=DPV_LINKML.bibliographicCitation, domain=None, range=Optional[str])

slots.conformsTo = Slot(uri=DCTERMS.conformsTo, name="conformsTo", curie=DCTERMS.curie('conformsTo'),
                   model_uri=DPV_LINKML.conformsTo, domain=None, range=Optional[Union[str, list[str]]])

slots.created = Slot(uri=DCTERMS.created, name="created", curie=DCTERMS.curie('created'),
                   model_uri=DPV_LINKML.created, domain=None, range=Optional[Union[Union[str, DpvDate], list[Union[str, DpvDate]]]])

slots.issued = Slot(uri=DCTERMS.issued, name="issued", curie=DCTERMS.curie('issued'),
                   model_uri=DPV_LINKML.issued, domain=None, range=Optional[Union[str, DpvDate]])

slots.modified = Slot(uri=DCTERMS.modified, name="modified", curie=DCTERMS.curie('modified'),
                   model_uri=DPV_LINKML.modified, domain=None, range=Optional[Union[str, DpvDate]])

slots.creator = Slot(uri=DCTERMS.creator, name="creator", curie=DCTERMS.curie('creator'),
                   model_uri=DPV_LINKML.creator, domain=None, range=Optional[Union[Union[str, DpvAgentId], list[Union[str, DpvAgentId]]]],
                   pattern=re.compile(r'^dpv_agent:(person|org)-[a-z0-9-]+$'))

slots.contributor = Slot(uri=DCTERMS.contributor, name="contributor", curie=DCTERMS.curie('contributor'),
                   model_uri=DPV_LINKML.contributor, domain=None, range=Optional[Union[Union[str, DpvAgentId], list[Union[str, DpvAgentId]]]],
                   pattern=re.compile(r'^dpv_agent:(person|org)-[a-z0-9-]+$'))

slots.publisher = Slot(uri=DCTERMS.publisher, name="publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=DPV_LINKML.publisher, domain=None, range=Optional[Union[str, DpvUri]])

slots.license = Slot(uri=DCTERMS.license, name="license", curie=DCTERMS.curie('license'),
                   model_uri=DPV_LINKML.license, domain=None, range=Optional[Union[str, DpvUri]])

slots.source = Slot(uri=DCTERMS.source, name="source", curie=DCTERMS.curie('source'),
                   model_uri=DPV_LINKML.source, domain=None, range=Optional[Union[str, list[str]]])

slots.homepage = Slot(uri=FOAF.homepage, name="homepage", curie=FOAF.curie('homepage'),
                   model_uri=DPV_LINKML.homepage, domain=None, range=Optional[str])

slots.doi = Slot(uri=BIBO.doi, name="doi", curie=BIBO.curie('doi'),
                   model_uri=DPV_LINKML.doi, domain=None, range=Optional[str])

slots.bibo_status = Slot(uri=BIBO.status, name="bibo_status", curie=BIBO.curie('status'),
                   model_uri=DPV_LINKML.bibo_status, domain=None, range=Optional[str])

slots.preferredNamespacePrefix = Slot(uri=VANN.preferredNamespacePrefix, name="preferredNamespacePrefix", curie=VANN.curie('preferredNamespacePrefix'),
                   model_uri=DPV_LINKML.preferredNamespacePrefix, domain=None, range=Optional[str])

slots.preferredNamespaceUri = Slot(uri=VANN.preferredNamespaceUri, name="preferredNamespaceUri", curie=VANN.curie('preferredNamespaceUri'),
                   model_uri=DPV_LINKML.preferredNamespaceUri, domain=None, range=Optional[str])

slots.rdfs_Label = Slot(uri=RDFS.Label, name="rdfs_Label", curie=RDFS.curie('Label'),
                   model_uri=DPV_LINKML.rdfs_Label, domain=None, range=Optional[str])

slots.versionIRI = Slot(uri=OWL.versionIRI, name="versionIRI", curie=OWL.curie('versionIRI'),
                   model_uri=DPV_LINKML.versionIRI, domain=None, range=Optional[Union[str, DpvUri]])

slots.versionInfo = Slot(uri=OWL.versionInfo, name="versionInfo", curie=OWL.curie('versionInfo'),
                   model_uri=DPV_LINKML.versionInfo, domain=None, range=str)

slots.schema_version = Slot(uri=SDO.version, name="schema_version", curie=SDO.curie('version'),
                   model_uri=DPV_LINKML.schema_version, domain=None, range=Optional[str])

slots.isProfileOf = Slot(uri=PROF.isProfileOf, name="isProfileOf", curie=PROF.curie('isProfileOf'),
                   model_uri=DPV_LINKML.isProfileOf, domain=None, range=Optional[Union[Union[str, DpvUri], list[Union[str, DpvUri]]]])

slots.logo = Slot(uri=FOAF.logo, name="logo", curie=FOAF.curie('logo'),
                   model_uri=DPV_LINKML.logo, domain=None, range=Optional[Union[str, DpvUri]])

slots.accessRights = Slot(uri=DCTERMS.accessRights, name="accessRights", curie=DCTERMS.curie('accessRights'),
                   model_uri=DPV_LINKML.accessRights, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.ai_hasCapability = Slot(uri=AI.hasCapability, name="ai_hasCapability", curie=AI.curie('hasCapability'),
                   model_uri=DPV_LINKML.ai_hasCapability, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.ai_hasData = Slot(uri=AI.hasData, name="ai_hasData", curie=AI.curie('hasData'),
                   model_uri=DPV_LINKML.ai_hasData, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.ai_hasModel = Slot(uri=AI.hasModel, name="ai_hasModel", curie=AI.curie('hasModel'),
                   model_uri=DPV_LINKML.ai_hasModel, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.avoids = Slot(uri=RISK.avoids, name="avoids", curie=RISK.curie('avoids'),
                   model_uri=DPV_LINKML.avoids, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.causedByThreat = Slot(uri=RISK.causedByThreat, name="causedByThreat", curie=RISK.curie('causedByThreat'),
                   model_uri=DPV_LINKML.causedByThreat, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.causedByVulnerability = Slot(uri=RISK.causedByVulnerability, name="causedByVulnerability", curie=RISK.curie('causedByVulnerability'),
                   model_uri=DPV_LINKML.causedByVulnerability, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.contains = Slot(uri=RISK.contains, name="contains", curie=RISK.curie('contains'),
                   model_uri=DPV_LINKML.contains, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.controls = Slot(uri=RISK.controls, name="controls", curie=RISK.curie('controls'),
                   model_uri=DPV_LINKML.controls, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.coverage = Slot(uri=DCTERMS.coverage, name="coverage", curie=DCTERMS.curie('coverage'),
                   model_uri=DPV_LINKML.coverage, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.dateAccepted = Slot(uri=DCTERMS.dateAccepted, name="dateAccepted", curie=DCTERMS.curie('dateAccepted'),
                   model_uri=DPV_LINKML.dateAccepted, domain=None, range=Optional[Union[str, list[str]]])

slots.dateSubmitted = Slot(uri=DCTERMS.dateSubmitted, name="dateSubmitted", curie=DCTERMS.curie('dateSubmitted'),
                   model_uri=DPV_LINKML.dateSubmitted, domain=None, range=Optional[Union[str, list[str]]])

slots.de_gdng_hasDataHolder = Slot(uri=DE_GDNG.hasDataHolder, name="de_gdng_hasDataHolder", curie=DE_GDNG.curie('hasDataHolder'),
                   model_uri=DPV_LINKML.de_gdng_hasDataHolder, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.detects = Slot(uri=RISK.detects, name="detects", curie=RISK.curie('detects'),
                   model_uri=DPV_LINKML.detects, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.eliminates = Slot(uri=RISK.eliminates, name="eliminates", curie=RISK.curie('eliminates'),
                   model_uri=DPV_LINKML.eliminates, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.eu_aiact_hasRiskLevel = Slot(uri=EU_AIACT.hasRiskLevel, name="eu_aiact_hasRiskLevel", curie=EU_AIACT.curie('hasRiskLevel'),
                   model_uri=DPV_LINKML.eu_aiact_hasRiskLevel, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.eu_dga_hasDataHolder = Slot(uri=EU_DGA.hasDataHolder, name="eu_dga_hasDataHolder", curie=EU_DGA.curie('hasDataHolder'),
                   model_uri=DPV_LINKML.eu_dga_hasDataHolder, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.exploitsVulnerability = Slot(uri=RISK.exploitsVulnerability, name="exploitsVulnerability", curie=RISK.curie('exploitsVulnerability'),
                   model_uri=DPV_LINKML.exploitsVulnerability, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.format = Slot(uri=DCTERMS.format, name="format", curie=DCTERMS.curie('format'),
                   model_uri=DPV_LINKML.format, domain=None, range=Optional[Union[str, list[str]]])

slots.hasAI = Slot(uri=AI.hasAI, name="hasAI", curie=AI.curie('hasAI'),
                   model_uri=DPV_LINKML.hasAI, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasAISystem = Slot(uri=AI.hasAISystem, name="hasAISystem", curie=AI.curie('hasAISystem'),
                   model_uri=DPV_LINKML.hasAISystem, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasAPI = Slot(uri=TECH.hasAPI, name="hasAPI", curie=TECH.curie('hasAPI'),
                   model_uri=DPV_LINKML.hasAPI, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasActiveEntity = Slot(uri=DPV.hasActiveEntity, name="hasActiveEntity", curie=DPV.curie('hasActiveEntity'),
                   model_uri=DPV_LINKML.hasActiveEntity, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasActivityStatus = Slot(uri=DPV.hasActivityStatus, name="hasActivityStatus", curie=DPV.curie('hasActivityStatus'),
                   model_uri=DPV_LINKML.hasActivityStatus, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasActor = Slot(uri=TECH.hasActor, name="hasActor", curie=TECH.curie('hasActor'),
                   model_uri=DPV_LINKML.hasActor, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasAddress = Slot(uri=DPV.hasAddress, name="hasAddress", curie=DPV.curie('hasAddress'),
                   model_uri=DPV_LINKML.hasAddress, domain=None, range=Optional[Union[str, list[str]]])

slots.hasAgent = Slot(uri=IEEE_7012.hasAgent, name="hasAgent", curie=IEEE_7012.curie('hasAgent'),
                   model_uri=DPV_LINKML.hasAgent, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasAgentBehaviour = Slot(uri=IEEE_7012.hasAgentBehaviour, name="hasAgentBehaviour", curie=IEEE_7012.curie('hasAgentBehaviour'),
                   model_uri=DPV_LINKML.hasAgentBehaviour, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasAgreement = Slot(uri=IEEE_7012.hasAgreement, name="hasAgreement", curie=IEEE_7012.curie('hasAgreement'),
                   model_uri=DPV_LINKML.hasAgreement, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasAgreementPreference = Slot(uri=IEEE_7012.hasAgreementPreference, name="hasAgreementPreference", curie=IEEE_7012.curie('hasAgreementPreference'),
                   model_uri=DPV_LINKML.hasAgreementPreference, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasAgreementRegistry = Slot(uri=IEEE_7012.hasAgreementRegistry, name="hasAgreementRegistry", curie=IEEE_7012.curie('hasAgreementRegistry'),
                   model_uri=DPV_LINKML.hasAgreementRegistry, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasAlgorithm = Slot(uri=TECH.hasAlgorithm, name="hasAlgorithm", curie=TECH.curie('hasAlgorithm'),
                   model_uri=DPV_LINKML.hasAlgorithm, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasAlgorithmicLogic = Slot(uri=DPV.hasAlgorithmicLogic, name="hasAlgorithmicLogic", curie=DPV.curie('hasAlgorithmicLogic'),
                   model_uri=DPV_LINKML.hasAlgorithmicLogic, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasApplicability = Slot(uri=DPV.hasApplicability, name="hasApplicability", curie=DPV.curie('hasApplicability'),
                   model_uri=DPV_LINKML.hasApplicability, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasApplicableLaw = Slot(uri=DPV.hasApplicableLaw, name="hasApplicableLaw", curie=DPV.curie('hasApplicableLaw'),
                   model_uri=DPV_LINKML.hasApplicableLaw, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasApplication = Slot(uri=TECH.hasApplication, name="hasApplication", curie=TECH.curie('hasApplication'),
                   model_uri=DPV_LINKML.hasApplication, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasAssessment = Slot(uri=DPV.hasAssessment, name="hasAssessment", curie=DPV.curie('hasAssessment'),
                   model_uri=DPV_LINKML.hasAssessment, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasAuditStatus = Slot(uri=DPV.hasAuditStatus, name="hasAuditStatus", curie=DPV.curie('hasAuditStatus'),
                   model_uri=DPV_LINKML.hasAuditStatus, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasAuditor = Slot(uri=TECH.hasAuditor, name="hasAuditor", curie=TECH.curie('hasAuditor'),
                   model_uri=DPV_LINKML.hasAuditor, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasAuthority = Slot(uri=DPV.hasAuthority, name="hasAuthority", curie=DPV.curie('hasAuthority'),
                   model_uri=DPV_LINKML.hasAuthority, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasAutomationLevel = Slot(uri=DPV.hasAutomationLevel, name="hasAutomationLevel", curie=DPV.curie('hasAutomationLevel'),
                   model_uri=DPV_LINKML.hasAutomationLevel, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasChangeCategory = Slot(uri=EU_AIACT.hasChangeCategory, name="hasChangeCategory", curie=EU_AIACT.curie('hasChangeCategory'),
                   model_uri=DPV_LINKML.hasChangeCategory, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasChangeDescription = Slot(uri=EU_AIACT.hasChangeDescription, name="hasChangeDescription", curie=EU_AIACT.curie('hasChangeDescription'),
                   model_uri=DPV_LINKML.hasChangeDescription, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasCommunicationMechanism = Slot(uri=TECH.hasCommunicationMechanism, name="hasCommunicationMechanism", curie=TECH.curie('hasCommunicationMechanism'),
                   model_uri=DPV_LINKML.hasCommunicationMechanism, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasComplianceStatus = Slot(uri=DPV.hasComplianceStatus, name="hasComplianceStatus", curie=DPV.curie('hasComplianceStatus'),
                   model_uri=DPV_LINKML.hasComplianceStatus, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasComponent = Slot(uri=TECH.hasComponent, name="hasComponent", curie=TECH.curie('hasComponent'),
                   model_uri=DPV_LINKML.hasComponent, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasConcernedSA = Slot(uri=EU_GDPR.hasConcernedSA, name="hasConcernedSA", curie=EU_GDPR.curie('hasConcernedSA'),
                   model_uri=DPV_LINKML.hasConcernedSA, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasConflictResolution = Slot(uri=IEEE_7012.hasConflictResolution, name="hasConflictResolution", curie=IEEE_7012.curie('hasConflictResolution'),
                   model_uri=DPV_LINKML.hasConflictResolution, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasConformanceStatus = Slot(uri=DPV.hasConformanceStatus, name="hasConformanceStatus", curie=DPV.curie('hasConformanceStatus'),
                   model_uri=DPV_LINKML.hasConformanceStatus, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasConsentControl = Slot(uri=DPV.hasConsentControl, name="hasConsentControl", curie=DPV.curie('hasConsentControl'),
                   model_uri=DPV_LINKML.hasConsentControl, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasConsentStatus = Slot(uri=DPV.hasConsentStatus, name="hasConsentStatus", curie=DPV.curie('hasConsentStatus'),
                   model_uri=DPV_LINKML.hasConsentStatus, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasConsequence = Slot(uri=DPV.hasConsequence, name="hasConsequence", curie=DPV.curie('hasConsequence'),
                   model_uri=DPV_LINKML.hasConsequence, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasConsequenceOn = Slot(uri=DPV.hasConsequenceOn, name="hasConsequenceOn", curie=DPV.curie('hasConsequenceOn'),
                   model_uri=DPV_LINKML.hasConsequenceOn, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasContact = Slot(uri=DPV.hasContact, name="hasContact", curie=DPV.curie('hasContact'),
                   model_uri=DPV_LINKML.hasContact, domain=None, range=Optional[Union[str, list[str]]])

slots.hasContext = Slot(uri=DPV.hasContext, name="hasContext", curie=DPV.curie('hasContext'),
                   model_uri=DPV_LINKML.hasContext, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasContractControl = Slot(uri=DPV.hasContractControl, name="hasContractControl", curie=DPV.curie('hasContractControl'),
                   model_uri=DPV_LINKML.hasContractControl, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasContractStatus = Slot(uri=DPV.hasContractStatus, name="hasContractStatus", curie=DPV.curie('hasContractStatus'),
                   model_uri=DPV_LINKML.hasContractStatus, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasContractualClause = Slot(uri=DPV.hasContractualClause, name="hasContractualClause", curie=DPV.curie('hasContractualClause'),
                   model_uri=DPV_LINKML.hasContractualClause, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasContractualFulfilmentStatus = Slot(uri=DPV.hasContractualFulfilmentStatus, name="hasContractualFulfilmentStatus", curie=DPV.curie('hasContractualFulfilmentStatus'),
                   model_uri=DPV_LINKML.hasContractualFulfilmentStatus, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasControl = Slot(uri=RISK.hasControl, name="hasControl", curie=RISK.curie('hasControl'),
                   model_uri=DPV_LINKML.hasControl, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasCountry = Slot(uri=DPV.hasCountry, name="hasCountry", curie=DPV.curie('hasCountry'),
                   model_uri=DPV_LINKML.hasCountry, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasCustomer = Slot(uri=TECH.hasCustomer, name="hasCustomer", curie=TECH.curie('hasCustomer'),
                   model_uri=DPV_LINKML.hasCustomer, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDAO = Slot(uri=EU_DGA.hasDAO, name="hasDAO", curie=EU_DGA.curie('hasDAO'),
                   model_uri=DPV_LINKML.hasDAO, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDISP = Slot(uri=EU_DGA.hasDISP, name="hasDISP", curie=EU_DGA.curie('hasDISP'),
                   model_uri=DPV_LINKML.hasDISP, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasData = Slot(uri=DPV.hasData, name="hasData", curie=DPV.curie('hasData'),
                   model_uri=DPV_LINKML.hasData, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDataController = Slot(uri=DPV.hasDataController, name="hasDataController", curie=DPV.curie('hasDataController'),
                   model_uri=DPV_LINKML.hasDataController, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDataExporter = Slot(uri=DPV.hasDataExporter, name="hasDataExporter", curie=DPV.curie('hasDataExporter'),
                   model_uri=DPV_LINKML.hasDataExporter, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDataImporter = Slot(uri=DPV.hasDataImporter, name="hasDataImporter", curie=DPV.curie('hasDataImporter'),
                   model_uri=DPV_LINKML.hasDataImporter, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDataProcessor = Slot(uri=DPV.hasDataProcessor, name="hasDataProcessor", curie=DPV.curie('hasDataProcessor'),
                   model_uri=DPV_LINKML.hasDataProcessor, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDataProtectionOfficer = Slot(uri=DPV.hasDataProtectionOfficer, name="hasDataProtectionOfficer", curie=DPV.curie('hasDataProtectionOfficer'),
                   model_uri=DPV_LINKML.hasDataProtectionOfficer, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDataReuseAssistant = Slot(uri=EU_DGA.hasDataReuseAssistant, name="hasDataReuseAssistant", curie=EU_DGA.curie('hasDataReuseAssistant'),
                   model_uri=DPV_LINKML.hasDataReuseAssistant, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDataSharingTerm = Slot(uri=IEEE_7012.hasDataSharingTerm, name="hasDataSharingTerm", curie=IEEE_7012.curie('hasDataSharingTerm'),
                   model_uri=DPV_LINKML.hasDataSharingTerm, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDataSource = Slot(uri=DPV.hasDataSource, name="hasDataSource", curie=DPV.curie('hasDataSource'),
                   model_uri=DPV_LINKML.hasDataSource, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDataSubject = Slot(uri=DPV.hasDataSubject, name="hasDataSubject", curie=DPV.curie('hasDataSubject'),
                   model_uri=DPV_LINKML.hasDataSubject, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDataSubjectScale = Slot(uri=DPV.hasDataSubjectScale, name="hasDataSubjectScale", curie=DPV.curie('hasDataSubjectScale'),
                   model_uri=DPV_LINKML.hasDataSubjectScale, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDataUser = Slot(uri=EU_DGA.hasDataUser, name="hasDataUser", curie=EU_DGA.curie('hasDataUser'),
                   model_uri=DPV_LINKML.hasDataUser, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDataVolume = Slot(uri=DPV.hasDataVolume, name="hasDataVolume", curie=DPV.curie('hasDataVolume'),
                   model_uri=DPV_LINKML.hasDataVolume, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDeonticInterpretation = Slot(uri=IEEE_7012.hasDeonticInterpretation, name="hasDeonticInterpretation", curie=IEEE_7012.curie('hasDeonticInterpretation'),
                   model_uri=DPV_LINKML.hasDeonticInterpretation, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDeployer = Slot(uri=TECH.hasDeployer, name="hasDeployer", curie=TECH.curie('hasDeployer'),
                   model_uri=DPV_LINKML.hasDeployer, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDeploymentLocation = Slot(uri=TECH.hasDeploymentLocation, name="hasDeploymentLocation", curie=TECH.curie('hasDeploymentLocation'),
                   model_uri=DPV_LINKML.hasDeploymentLocation, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDesigner = Slot(uri=TECH.hasDesigner, name="hasDesigner", curie=TECH.curie('hasDesigner'),
                   model_uri=DPV_LINKML.hasDesigner, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDeterrence = Slot(uri=DPV.hasDeterrence, name="hasDeterrence", curie=DPV.curie('hasDeterrence'),
                   model_uri=DPV_LINKML.hasDeterrence, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDeveloper = Slot(uri=TECH.hasDeveloper, name="hasDeveloper", curie=TECH.curie('hasDeveloper'),
                   model_uri=DPV_LINKML.hasDeveloper, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDevice = Slot(uri=TECH.hasDevice, name="hasDevice", curie=TECH.curie('hasDevice'),
                   model_uri=DPV_LINKML.hasDevice, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDocumentation = Slot(uri=TECH.hasDocumentation, name="hasDocumentation", curie=TECH.curie('hasDocumentation'),
                   model_uri=DPV_LINKML.hasDocumentation, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasDuration = Slot(uri=DPV.hasDuration, name="hasDuration", curie=DPV.curie('hasDuration'),
                   model_uri=DPV_LINKML.hasDuration, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasEndpoint = Slot(uri=IEEE_7012.hasEndpoint, name="hasEndpoint", curie=IEEE_7012.curie('hasEndpoint'),
                   model_uri=DPV_LINKML.hasEndpoint, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasEntity = Slot(uri=DPV.hasEntity, name="hasEntity", curie=DPV.curie('hasEntity'),
                   model_uri=DPV_LINKML.hasEntity, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasEntityControl = Slot(uri=DPV.hasEntityControl, name="hasEntityControl", curie=DPV.curie('hasEntityControl'),
                   model_uri=DPV_LINKML.hasEntityControl, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasEntityInvolvement = Slot(uri=DPV.hasEntityInvolvement, name="hasEntityInvolvement", curie=DPV.curie('hasEntityInvolvement'),
                   model_uri=DPV_LINKML.hasEntityInvolvement, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasEstablishment = Slot(uri=EU_GDPR.hasEstablishment, name="hasEstablishment", curie=EU_GDPR.curie('hasEstablishment'),
                   model_uri=DPV_LINKML.hasEstablishment, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasEvaluator = Slot(uri=TECH.hasEvaluator, name="hasEvaluator", curie=TECH.curie('hasEvaluator'),
                   model_uri=DPV_LINKML.hasEvaluator, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasExpectation = Slot(uri=DPV.hasExpectation, name="hasExpectation", curie=DPV.curie('hasExpectation'),
                   model_uri=DPV_LINKML.hasExpectation, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasFee = Slot(uri=DPV.hasFee, name="hasFee", curie=DPV.curie('hasFee'),
                   model_uri=DPV_LINKML.hasFee, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasFirstParty = Slot(uri=IEEE_7012.hasFirstParty, name="hasFirstParty", curie=IEEE_7012.curie('hasFirstParty'),
                   model_uri=DPV_LINKML.hasFirstParty, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasFrequency = Slot(uri=DPV.hasFrequency, name="hasFrequency", curie=DPV.curie('hasFrequency'),
                   model_uri=DPV_LINKML.hasFrequency, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasFulfilmentStatus = Slot(uri=DPV.hasFulfilmentStatus, name="hasFulfilmentStatus", curie=DPV.curie('hasFulfilmentStatus'),
                   model_uri=DPV_LINKML.hasFulfilmentStatus, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasFunction = Slot(uri=TECH.hasFunction, name="hasFunction", curie=TECH.curie('hasFunction'),
                   model_uri=DPV_LINKML.hasFunction, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasGPAIModel = Slot(uri=AI.hasGPAIModel, name="hasGPAIModel", curie=AI.curie('hasGPAIModel'),
                   model_uri=DPV_LINKML.hasGPAIModel, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasGeographicCoverage = Slot(uri=DPV.hasGeographicCoverage, name="hasGeographicCoverage", curie=DPV.curie('hasGeographicCoverage'),
                   model_uri=DPV_LINKML.hasGeographicCoverage, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasHardware = Slot(uri=TECH.hasHardware, name="hasHardware", curie=TECH.curie('hasHardware'),
                   model_uri=DPV_LINKML.hasHardware, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasHumanDescription = Slot(uri=IEEE_7012.hasHumanDescription, name="hasHumanDescription", curie=IEEE_7012.curie('hasHumanDescription'),
                   model_uri=DPV_LINKML.hasHumanDescription, domain=None, range=Optional[Union[str, list[str]]])

slots.hasHumanInvolvement = Slot(uri=DPV.hasHumanInvolvement, name="hasHumanInvolvement", curie=DPV.curie('hasHumanInvolvement'),
                   model_uri=DPV_LINKML.hasHumanInvolvement, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasHumanReadableFormat = Slot(uri=IEEE_7012.hasHumanReadableFormat, name="hasHumanReadableFormat", curie=IEEE_7012.curie('hasHumanReadableFormat'),
                   model_uri=DPV_LINKML.hasHumanReadableFormat, domain=None, range=Optional[Union[str, list[str]]])

slots.hasHumanSubject = Slot(uri=DPV.hasHumanSubject, name="hasHumanSubject", curie=DPV.curie('hasHumanSubject'),
                   model_uri=DPV_LINKML.hasHumanSubject, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasIdentifier = Slot(uri=DPV.hasIdentifier, name="hasIdentifier", curie=DPV.curie('hasIdentifier'),
                   model_uri=DPV_LINKML.hasIdentifier, domain=None, range=Optional[Union[str, list[str]]])

slots.hasImpact = Slot(uri=DPV.hasImpact, name="hasImpact", curie=DPV.curie('hasImpact'),
                   model_uri=DPV_LINKML.hasImpact, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasImpactAssessment = Slot(uri=DPV.hasImpactAssessment, name="hasImpactAssessment", curie=DPV.curie('hasImpactAssessment'),
                   model_uri=DPV_LINKML.hasImpactAssessment, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasImpactOn = Slot(uri=DPV.hasImpactOn, name="hasImpactOn", curie=DPV.curie('hasImpactOn'),
                   model_uri=DPV_LINKML.hasImpactOn, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasImportance = Slot(uri=DPV.hasImportance, name="hasImportance", curie=DPV.curie('hasImportance'),
                   model_uri=DPV_LINKML.hasImportance, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasIncident = Slot(uri=RISK.hasIncident, name="hasIncident", curie=RISK.curie('hasIncident'),
                   model_uri=DPV_LINKML.hasIncident, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasIndicationMethod = Slot(uri=DPV.hasIndicationMethod, name="hasIndicationMethod", curie=DPV.curie('hasIndicationMethod'),
                   model_uri=DPV_LINKML.hasIndicationMethod, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasInformedStatus = Slot(uri=DPV.hasInformedStatus, name="hasInformedStatus", curie=DPV.curie('hasInformedStatus'),
                   model_uri=DPV_LINKML.hasInformedStatus, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasInfrastructure = Slot(uri=TECH.hasInfrastructure, name="hasInfrastructure", curie=TECH.curie('hasInfrastructure'),
                   model_uri=DPV_LINKML.hasInfrastructure, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasInput = Slot(uri=TECH.hasInput, name="hasInput", curie=TECH.curie('hasInput'),
                   model_uri=DPV_LINKML.hasInput, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasInputAction = Slot(uri=TECH.hasInputAction, name="hasInputAction", curie=TECH.curie('hasInputAction'),
                   model_uri=DPV_LINKML.hasInputAction, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasInputData = Slot(uri=TECH.hasInputData, name="hasInputData", curie=TECH.curie('hasInputData'),
                   model_uri=DPV_LINKML.hasInputData, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasInstaller = Slot(uri=TECH.hasInstaller, name="hasInstaller", curie=TECH.curie('hasInstaller'),
                   model_uri=DPV_LINKML.hasInstaller, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasIntendedUse = Slot(uri=TECH.hasIntendedUse, name="hasIntendedUse", curie=TECH.curie('hasIntendedUse'),
                   model_uri=DPV_LINKML.hasIntendedUse, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasIntention = Slot(uri=DPV.hasIntention, name="hasIntention", curie=DPV.curie('hasIntention'),
                   model_uri=DPV_LINKML.hasIntention, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasInverseJurisdiction = Slot(uri=DPV.hasInverseJurisdiction, name="hasInverseJurisdiction", curie=DPV.curie('hasInverseJurisdiction'),
                   model_uri=DPV_LINKML.hasInverseJurisdiction, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasInvolvement = Slot(uri=DPV.hasInvolvement, name="hasInvolvement", curie=DPV.curie('hasInvolvement'),
                   model_uri=DPV_LINKML.hasInvolvement, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasJointDataControllers = Slot(uri=DPV.hasJointDataControllers, name="hasJointDataControllers", curie=DPV.curie('hasJointDataControllers'),
                   model_uri=DPV_LINKML.hasJointDataControllers, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasJurisdiction = Slot(uri=DPV.hasJurisdiction, name="hasJurisdiction", curie=DPV.curie('hasJurisdiction'),
                   model_uri=DPV_LINKML.hasJurisdiction, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasJustification = Slot(uri=DPV.hasJustification, name="hasJustification", curie=DPV.curie('hasJustification'),
                   model_uri=DPV_LINKML.hasJustification, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasLawfulness = Slot(uri=DPV.hasLawfulness, name="hasLawfulness", curie=DPV.curie('hasLawfulness'),
                   model_uri=DPV_LINKML.hasLawfulness, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasLeadSA = Slot(uri=EU_GDPR.hasLeadSA, name="hasLeadSA", curie=EU_GDPR.curie('hasLeadSA'),
                   model_uri=DPV_LINKML.hasLeadSA, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasLegalBasis = Slot(uri=DPV.hasLegalBasis, name="hasLegalBasis", curie=DPV.curie('hasLegalBasis'),
                   model_uri=DPV_LINKML.hasLegalBasis, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasLegalMeasure = Slot(uri=DPV.hasLegalMeasure, name="hasLegalMeasure", curie=DPV.curie('hasLegalMeasure'),
                   model_uri=DPV_LINKML.hasLegalMeasure, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasLicense = Slot(uri=TECH.hasLicense, name="hasLicense", curie=TECH.curie('hasLicense'),
                   model_uri=DPV_LINKML.hasLicense, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasLifecycleStage = Slot(uri=TECH.hasLifecycleStage, name="hasLifecycleStage", curie=TECH.curie('hasLifecycleStage'),
                   model_uri=DPV_LINKML.hasLifecycleStage, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasLikelihood = Slot(uri=DPV.hasLikelihood, name="hasLikelihood", curie=DPV.curie('hasLikelihood'),
                   model_uri=DPV_LINKML.hasLikelihood, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasLocalSA = Slot(uri=EU_GDPR.hasLocalSA, name="hasLocalSA", curie=EU_GDPR.curie('hasLocalSA'),
                   model_uri=DPV_LINKML.hasLocalSA, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasLocation = Slot(uri=DPV.hasLocation, name="hasLocation", curie=DPV.curie('hasLocation'),
                   model_uri=DPV_LINKML.hasLocation, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasMachineReadableFormat = Slot(uri=IEEE_7012.hasMachineReadableFormat, name="hasMachineReadableFormat", curie=IEEE_7012.curie('hasMachineReadableFormat'),
                   model_uri=DPV_LINKML.hasMachineReadableFormat, domain=None, range=Optional[Union[str, list[str]]])

slots.hasMainEstablishment = Slot(uri=EU_GDPR.hasMainEstablishment, name="hasMainEstablishment", curie=EU_GDPR.curie('hasMainEstablishment'),
                   model_uri=DPV_LINKML.hasMainEstablishment, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasMaintainer = Slot(uri=TECH.hasMaintainer, name="hasMaintainer", curie=TECH.curie('hasMaintainer'),
                   model_uri=DPV_LINKML.hasMaintainer, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasManufacturer = Slot(uri=TECH.hasManufacturer, name="hasManufacturer", curie=TECH.curie('hasManufacturer'),
                   model_uri=DPV_LINKML.hasManufacturer, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasMarketAvailabilityStatus = Slot(uri=TECH.hasMarketAvailabilityStatus, name="hasMarketAvailabilityStatus", curie=TECH.curie('hasMarketAvailabilityStatus'),
                   model_uri=DPV_LINKML.hasMarketAvailabilityStatus, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasName = Slot(uri=DPV.hasName, name="hasName", curie=DPV.curie('hasName'),
                   model_uri=DPV_LINKML.hasName, domain=None, range=Optional[Union[str, list[str]]])

slots.hasNecessity = Slot(uri=DPV.hasNecessity, name="hasNecessity", curie=DPV.curie('hasNecessity'),
                   model_uri=DPV_LINKML.hasNecessity, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasNonInvolvedEntity = Slot(uri=DPV.hasNonInvolvedEntity, name="hasNonInvolvedEntity", curie=DPV.curie('hasNonInvolvedEntity'),
                   model_uri=DPV_LINKML.hasNonInvolvedEntity, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasNonPersonalDataProcess = Slot(uri=DPV.hasNonPersonalDataProcess, name="hasNonPersonalDataProcess", curie=DPV.curie('hasNonPersonalDataProcess'),
                   model_uri=DPV_LINKML.hasNonPersonalDataProcess, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasNotice = Slot(uri=DPV.hasNotice, name="hasNotice", curie=DPV.curie('hasNotice'),
                   model_uri=DPV_LINKML.hasNotice, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasNoticeIcon = Slot(uri=DPV.hasNoticeIcon, name="hasNoticeIcon", curie=DPV.curie('hasNoticeIcon'),
                   model_uri=DPV_LINKML.hasNoticeIcon, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasNoticeLayer = Slot(uri=DPV.hasNoticeLayer, name="hasNoticeLayer", curie=DPV.curie('hasNoticeLayer'),
                   model_uri=DPV_LINKML.hasNoticeLayer, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasNoticeStatus = Slot(uri=DPV.hasNoticeStatus, name="hasNoticeStatus", curie=DPV.curie('hasNoticeStatus'),
                   model_uri=DPV_LINKML.hasNoticeStatus, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasNotificationStatus = Slot(uri=DPV.hasNotificationStatus, name="hasNotificationStatus", curie=DPV.curie('hasNotificationStatus'),
                   model_uri=DPV_LINKML.hasNotificationStatus, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasObligation = Slot(uri=DPV.hasObligation, name="hasObligation", curie=DPV.curie('hasObligation'),
                   model_uri=DPV_LINKML.hasObligation, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasOperatingEnvironment = Slot(uri=TECH.hasOperatingEnvironment, name="hasOperatingEnvironment", curie=TECH.curie('hasOperatingEnvironment'),
                   model_uri=DPV_LINKML.hasOperatingEnvironment, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasOperatingFactor = Slot(uri=TECH.hasOperatingFactor, name="hasOperatingFactor", curie=TECH.curie('hasOperatingFactor'),
                   model_uri=DPV_LINKML.hasOperatingFactor, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasOrganisationalMeasure = Slot(uri=DPV.hasOrganisationalMeasure, name="hasOrganisationalMeasure", curie=DPV.curie('hasOrganisationalMeasure'),
                   model_uri=DPV_LINKML.hasOrganisationalMeasure, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasOrganisationalUnit = Slot(uri=DPV.hasOrganisationalUnit, name="hasOrganisationalUnit", curie=DPV.curie('hasOrganisationalUnit'),
                   model_uri=DPV_LINKML.hasOrganisationalUnit, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasOutcome = Slot(uri=DPV.hasOutcome, name="hasOutcome", curie=DPV.curie('hasOutcome'),
                   model_uri=DPV_LINKML.hasOutcome, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasOutput = Slot(uri=TECH.hasOutput, name="hasOutput", curie=TECH.curie('hasOutput'),
                   model_uri=DPV_LINKML.hasOutput, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasOutputAction = Slot(uri=TECH.hasOutputAction, name="hasOutputAction", curie=TECH.curie('hasOutputAction'),
                   model_uri=DPV_LINKML.hasOutputAction, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasOutputData = Slot(uri=TECH.hasOutputData, name="hasOutputData", curie=TECH.curie('hasOutputData'),
                   model_uri=DPV_LINKML.hasOutputData, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasOwner = Slot(uri=TECH.hasOwner, name="hasOwner", curie=TECH.curie('hasOwner'),
                   model_uri=DPV_LINKML.hasOwner, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasPart = Slot(uri=DCTERMS.hasPart, name="hasPart", curie=DCTERMS.curie('hasPart'),
                   model_uri=DPV_LINKML.hasPart, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasPartner = Slot(uri=TECH.hasPartner, name="hasPartner", curie=TECH.curie('hasPartner'),
                   model_uri=DPV_LINKML.hasPartner, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasParty = Slot(uri=DPV.hasParty, name="hasParty", curie=DPV.curie('hasParty'),
                   model_uri=DPV_LINKML.hasParty, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasPassiveEntity = Slot(uri=DPV.hasPassiveEntity, name="hasPassiveEntity", curie=DPV.curie('hasPassiveEntity'),
                   model_uri=DPV_LINKML.hasPassiveEntity, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasPermission = Slot(uri=DPV.hasPermission, name="hasPermission", curie=DPV.curie('hasPermission'),
                   model_uri=DPV_LINKML.hasPermission, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasPersonalData = Slot(uri=DPV.hasPersonalData, name="hasPersonalData", curie=DPV.curie('hasPersonalData'),
                   model_uri=DPV_LINKML.hasPersonalData, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasPersonalDataHandling = Slot(uri=DPV.hasPersonalDataHandling, name="hasPersonalDataHandling", curie=DPV.curie('hasPersonalDataHandling'),
                   model_uri=DPV_LINKML.hasPersonalDataHandling, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasPersonalDataProcess = Slot(uri=DPV.hasPersonalDataProcess, name="hasPersonalDataProcess", curie=DPV.curie('hasPersonalDataProcess'),
                   model_uri=DPV_LINKML.hasPersonalDataProcess, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasPhysicalMeasure = Slot(uri=DPV.hasPhysicalMeasure, name="hasPhysicalMeasure", curie=DPV.curie('hasPhysicalMeasure'),
                   model_uri=DPV_LINKML.hasPhysicalMeasure, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasPlatform = Slot(uri=TECH.hasPlatform, name="hasPlatform", curie=TECH.curie('hasPlatform'),
                   model_uri=DPV_LINKML.hasPlatform, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasPolicy = Slot(uri=DPV.hasPolicy, name="hasPolicy", curie=DPV.curie('hasPolicy'),
                   model_uri=DPV_LINKML.hasPolicy, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasPortabilityTerm = Slot(uri=IEEE_7012.hasPortabilityTerm, name="hasPortabilityTerm", curie=IEEE_7012.curie('hasPortabilityTerm'),
                   model_uri=DPV_LINKML.hasPortabilityTerm, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasPreferenceApplicability = Slot(uri=IEEE_7012.hasPreferenceApplicability, name="hasPreferenceApplicability", curie=IEEE_7012.curie('hasPreferenceApplicability'),
                   model_uri=DPV_LINKML.hasPreferenceApplicability, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasProcess = Slot(uri=DPV.hasProcess, name="hasProcess", curie=DPV.curie('hasProcess'),
                   model_uri=DPV_LINKML.hasProcess, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasProcessing = Slot(uri=DPV.hasProcessing, name="hasProcessing", curie=DPV.curie('hasProcessing'),
                   model_uri=DPV_LINKML.hasProcessing, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasProcessingCondition = Slot(uri=DPV.hasProcessingCondition, name="hasProcessingCondition", curie=DPV.curie('hasProcessingCondition'),
                   model_uri=DPV_LINKML.hasProcessingCondition, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasProcessingScale = Slot(uri=DPV.hasProcessingScale, name="hasProcessingScale", curie=DPV.curie('hasProcessingScale'),
                   model_uri=DPV_LINKML.hasProcessingScale, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasProducer = Slot(uri=TECH.hasProducer, name="hasProducer", curie=TECH.curie('hasProducer'),
                   model_uri=DPV_LINKML.hasProducer, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasProfilingTerm = Slot(uri=IEEE_7012.hasProfilingTerm, name="hasProfilingTerm", curie=IEEE_7012.curie('hasProfilingTerm'),
                   model_uri=DPV_LINKML.hasProfilingTerm, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasProhibition = Slot(uri=DPV.hasProhibition, name="hasProhibition", curie=DPV.curie('hasProhibition'),
                   model_uri=DPV_LINKML.hasProhibition, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasProvider = Slot(uri=TECH.hasProvider, name="hasProvider", curie=TECH.curie('hasProvider'),
                   model_uri=DPV_LINKML.hasProvider, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasProvisionMethod = Slot(uri=TECH.hasProvisionMethod, name="hasProvisionMethod", curie=TECH.curie('hasProvisionMethod'),
                   model_uri=DPV_LINKML.hasProvisionMethod, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasProvisionStatus = Slot(uri=TECH.hasProvisionStatus, name="hasProvisionStatus", curie=TECH.curie('hasProvisionStatus'),
                   model_uri=DPV_LINKML.hasProvisionStatus, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasPurchaser = Slot(uri=TECH.hasPurchaser, name="hasPurchaser", curie=TECH.curie('hasPurchaser'),
                   model_uri=DPV_LINKML.hasPurchaser, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasPurpose = Slot(uri=DPV.hasPurpose, name="hasPurpose", curie=DPV.curie('hasPurpose'),
                   model_uri=DPV_LINKML.hasPurpose, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRecipient = Slot(uri=DPV.hasRecipient, name="hasRecipient", curie=DPV.curie('hasRecipient'),
                   model_uri=DPV_LINKML.hasRecipient, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRecipientDataController = Slot(uri=DPV.hasRecipientDataController, name="hasRecipientDataController", curie=DPV.curie('hasRecipientDataController'),
                   model_uri=DPV_LINKML.hasRecipientDataController, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRecipientThirdParty = Slot(uri=DPV.hasRecipientThirdParty, name="hasRecipientThirdParty", curie=DPV.curie('hasRecipientThirdParty'),
                   model_uri=DPV_LINKML.hasRecipientThirdParty, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRecommendation = Slot(uri=DPV.hasRecommendation, name="hasRecommendation", curie=DPV.curie('hasRecommendation'),
                   model_uri=DPV_LINKML.hasRecommendation, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRecordOfActivity = Slot(uri=DPV.hasRecordOfActivity, name="hasRecordOfActivity", curie=DPV.curie('hasRecordOfActivity'),
                   model_uri=DPV_LINKML.hasRecordOfActivity, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRelationWithDataSubject = Slot(uri=DPV.hasRelationWithDataSubject, name="hasRelationWithDataSubject", curie=DPV.curie('hasRelationWithDataSubject'),
                   model_uri=DPV_LINKML.hasRelationWithDataSubject, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRepresentative = Slot(uri=DPV.hasRepresentative, name="hasRepresentative", curie=DPV.curie('hasRepresentative'),
                   model_uri=DPV_LINKML.hasRepresentative, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRequestStatus = Slot(uri=DPV.hasRequestStatus, name="hasRequestStatus", curie=DPV.curie('hasRequestStatus'),
                   model_uri=DPV_LINKML.hasRequestStatus, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasResidualRisk = Slot(uri=DPV.hasResidualRisk, name="hasResidualRisk", curie=DPV.curie('hasResidualRisk'),
                   model_uri=DPV_LINKML.hasResidualRisk, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasResponsibleEntity = Slot(uri=DPV.hasResponsibleEntity, name="hasResponsibleEntity", curie=DPV.curie('hasResponsibleEntity'),
                   model_uri=DPV_LINKML.hasResponsibleEntity, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasReuseCompatibility = Slot(uri=DPV.hasReuseCompatibility, name="hasReuseCompatibility", curie=DPV.curie('hasReuseCompatibility'),
                   model_uri=DPV_LINKML.hasReuseCompatibility, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRight = Slot(uri=DPV.hasRight, name="hasRight", curie=DPV.curie('hasRight'),
                   model_uri=DPV_LINKML.hasRight, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRisk = Slot(uri=DPV.hasRisk, name="hasRisk", curie=DPV.curie('hasRisk'),
                   model_uri=DPV_LINKML.hasRisk, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRiskAcceptance = Slot(uri=RISK.hasRiskAcceptance, name="hasRiskAcceptance", curie=RISK.curie('hasRiskAcceptance'),
                   model_uri=DPV_LINKML.hasRiskAcceptance, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRiskAnalysis = Slot(uri=RISK.hasRiskAnalysis, name="hasRiskAnalysis", curie=RISK.curie('hasRiskAnalysis'),
                   model_uri=DPV_LINKML.hasRiskAnalysis, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRiskAssessment = Slot(uri=DPV.hasRiskAssessment, name="hasRiskAssessment", curie=DPV.curie('hasRiskAssessment'),
                   model_uri=DPV_LINKML.hasRiskAssessment, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRiskCriteria = Slot(uri=RISK.hasRiskCriteria, name="hasRiskCriteria", curie=RISK.curie('hasRiskCriteria'),
                   model_uri=DPV_LINKML.hasRiskCriteria, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRiskEvaluation = Slot(uri=RISK.hasRiskEvaluation, name="hasRiskEvaluation", curie=RISK.curie('hasRiskEvaluation'),
                   model_uri=DPV_LINKML.hasRiskEvaluation, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRiskIdentification = Slot(uri=RISK.hasRiskIdentification, name="hasRiskIdentification", curie=RISK.curie('hasRiskIdentification'),
                   model_uri=DPV_LINKML.hasRiskIdentification, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRiskLevel = Slot(uri=DPV.hasRiskLevel, name="hasRiskLevel", curie=DPV.curie('hasRiskLevel'),
                   model_uri=DPV_LINKML.hasRiskLevel, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRiskManagement = Slot(uri=RISK.hasRiskManagement, name="hasRiskManagement", curie=RISK.curie('hasRiskManagement'),
                   model_uri=DPV_LINKML.hasRiskManagement, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRiskOwner = Slot(uri=RISK.hasRiskOwner, name="hasRiskOwner", curie=RISK.curie('hasRiskOwner'),
                   model_uri=DPV_LINKML.hasRiskOwner, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRiskPerception = Slot(uri=RISK.hasRiskPerception, name="hasRiskPerception", curie=RISK.curie('hasRiskPerception'),
                   model_uri=DPV_LINKML.hasRiskPerception, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRiskSource = Slot(uri=RISK.hasRiskSource, name="hasRiskSource", curie=RISK.curie('hasRiskSource'),
                   model_uri=DPV_LINKML.hasRiskSource, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRiskTreatment = Slot(uri=RISK.hasRiskTreatment, name="hasRiskTreatment", curie=RISK.curie('hasRiskTreatment'),
                   model_uri=DPV_LINKML.hasRiskTreatment, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasRule = Slot(uri=DPV.hasRule, name="hasRule", curie=DPV.curie('hasRule'),
                   model_uri=DPV_LINKML.hasRule, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasScale = Slot(uri=DPV.hasScale, name="hasScale", curie=DPV.curie('hasScale'),
                   model_uri=DPV_LINKML.hasScale, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasScope = Slot(uri=DPV.hasScope, name="hasScope", curie=DPV.curie('hasScope'),
                   model_uri=DPV_LINKML.hasScope, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasSecondParty = Slot(uri=IEEE_7012.hasSecondParty, name="hasSecondParty", curie=IEEE_7012.curie('hasSecondParty'),
                   model_uri=DPV_LINKML.hasSecondParty, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasSector = Slot(uri=DPV.hasSector, name="hasSector", curie=DPV.curie('hasSector'),
                   model_uri=DPV_LINKML.hasSector, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasSensitivityLevel = Slot(uri=DPV.hasSensitivityLevel, name="hasSensitivityLevel", curie=DPV.curie('hasSensitivityLevel'),
                   model_uri=DPV_LINKML.hasSensitivityLevel, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasService = Slot(uri=DPV.hasService, name="hasService", curie=DPV.curie('hasService'),
                   model_uri=DPV_LINKML.hasService, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasServiceConsumer = Slot(uri=DPV.hasServiceConsumer, name="hasServiceConsumer", curie=DPV.curie('hasServiceConsumer'),
                   model_uri=DPV_LINKML.hasServiceConsumer, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasServiceProvider = Slot(uri=DPV.hasServiceProvider, name="hasServiceProvider", curie=DPV.curie('hasServiceProvider'),
                   model_uri=DPV_LINKML.hasServiceProvider, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasSeverity = Slot(uri=DPV.hasSeverity, name="hasSeverity", curie=DPV.curie('hasSeverity'),
                   model_uri=DPV_LINKML.hasSeverity, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasSoftware = Slot(uri=TECH.hasSoftware, name="hasSoftware", curie=TECH.curie('hasSoftware'),
                   model_uri=DPV_LINKML.hasSoftware, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasStatus = Slot(uri=DPV.hasStatus, name="hasStatus", curie=DPV.curie('hasStatus'),
                   model_uri=DPV_LINKML.hasStatus, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasStorageCondition = Slot(uri=DPV.hasStorageCondition, name="hasStorageCondition", curie=DPV.curie('hasStorageCondition'),
                   model_uri=DPV_LINKML.hasStorageCondition, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasSubject = Slot(uri=TECH.hasSubject, name="hasSubject", curie=TECH.curie('hasSubject'),
                   model_uri=DPV_LINKML.hasSubject, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasSubsidiary = Slot(uri=DPV.hasSubsidiary, name="hasSubsidiary", curie=DPV.curie('hasSubsidiary'),
                   model_uri=DPV_LINKML.hasSubsidiary, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasSupplier = Slot(uri=TECH.hasSupplier, name="hasSupplier", curie=TECH.curie('hasSupplier'),
                   model_uri=DPV_LINKML.hasSupplier, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasSystem = Slot(uri=TECH.hasSystem, name="hasSystem", curie=TECH.curie('hasSystem'),
                   model_uri=DPV_LINKML.hasSystem, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasSystemIntegrator = Slot(uri=TECH.hasSystemIntegrator, name="hasSystemIntegrator", curie=TECH.curie('hasSystemIntegrator'),
                   model_uri=DPV_LINKML.hasSystemIntegrator, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasTRL = Slot(uri=TECH.hasTRL, name="hasTRL", curie=TECH.curie('hasTRL'),
                   model_uri=DPV_LINKML.hasTRL, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasTechnicalMeasure = Slot(uri=DPV.hasTechnicalMeasure, name="hasTechnicalMeasure", curie=DPV.curie('hasTechnicalMeasure'),
                   model_uri=DPV_LINKML.hasTechnicalMeasure, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasTechnicalOrganisationalMeasure = Slot(uri=DPV.hasTechnicalOrganisationalMeasure, name="hasTechnicalOrganisationalMeasure", curie=DPV.curie('hasTechnicalOrganisationalMeasure'),
                   model_uri=DPV_LINKML.hasTechnicalOrganisationalMeasure, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasTechnique = Slot(uri=AI.hasTechnique, name="hasTechnique", curie=AI.curie('hasTechnique'),
                   model_uri=DPV_LINKML.hasTechnique, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasTestingData = Slot(uri=AI.hasTestingData, name="hasTestingData", curie=AI.curie('hasTestingData'),
                   model_uri=DPV_LINKML.hasTestingData, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasThirdCountry = Slot(uri=DPV.hasThirdCountry, name="hasThirdCountry", curie=DPV.curie('hasThirdCountry'),
                   model_uri=DPV_LINKML.hasThirdCountry, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasThirdParty = Slot(uri=DPV.hasThirdParty, name="hasThirdParty", curie=DPV.curie('hasThirdParty'),
                   model_uri=DPV_LINKML.hasThirdParty, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasThreatSource = Slot(uri=RISK.hasThreatSource, name="hasThreatSource", curie=RISK.curie('hasThreatSource'),
                   model_uri=DPV_LINKML.hasThreatSource, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasTrackingTerm = Slot(uri=IEEE_7012.hasTrackingTerm, name="hasTrackingTerm", curie=IEEE_7012.curie('hasTrackingTerm'),
                   model_uri=DPV_LINKML.hasTrackingTerm, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasTrainingData = Slot(uri=AI.hasTrainingData, name="hasTrainingData", curie=AI.curie('hasTrainingData'),
                   model_uri=DPV_LINKML.hasTrainingData, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasTransparencyTerm = Slot(uri=IEEE_7012.hasTransparencyTerm, name="hasTransparencyTerm", curie=IEEE_7012.curie('hasTransparencyTerm'),
                   model_uri=DPV_LINKML.hasTransparencyTerm, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasUncategorisedData = Slot(uri=DPV.hasUncategorisedData, name="hasUncategorisedData", curie=DPV.curie('hasUncategorisedData'),
                   model_uri=DPV_LINKML.hasUncategorisedData, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasUnstructuredData = Slot(uri=DPV.hasUnstructuredData, name="hasUnstructuredData", curie=DPV.curie('hasUnstructuredData'),
                   model_uri=DPV_LINKML.hasUnstructuredData, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasUser = Slot(uri=TECH.hasUser, name="hasUser", curie=TECH.curie('hasUser'),
                   model_uri=DPV_LINKML.hasUser, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasValidationData = Slot(uri=AI.hasValidationData, name="hasValidationData", curie=AI.curie('hasValidationData'),
                   model_uri=DPV_LINKML.hasValidationData, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.hasVulnerability = Slot(uri=RISK.hasVulnerability, name="hasVulnerability", curie=RISK.curie('hasVulnerability'),
                   model_uri=DPV_LINKML.hasVulnerability, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.identifies = Slot(uri=RISK.identifies, name="identifies", curie=RISK.curie('identifies'),
                   model_uri=DPV_LINKML.identifies, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.ieee_7012_hasParty = Slot(uri=IEEE_7012.hasParty, name="ieee_7012_hasParty", curie=IEEE_7012.curie('hasParty'),
                   model_uri=DPV_LINKML.ieee_7012_hasParty, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.ieee_7012_hasThirdParty = Slot(uri=IEEE_7012.hasThirdParty, name="ieee_7012_hasThirdParty", curie=IEEE_7012.curie('hasThirdParty'),
                   model_uri=DPV_LINKML.ieee_7012_hasThirdParty, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.interrupts = Slot(uri=RISK.interrupts, name="interrupts", curie=RISK.curie('interrupts'),
                   model_uri=DPV_LINKML.interrupts, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.intervenes = Slot(uri=RISK.intervenes, name="intervenes", curie=RISK.curie('intervenes'),
                   model_uri=DPV_LINKML.intervenes, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.investigates = Slot(uri=RISK.investigates, name="investigates", curie=RISK.curie('investigates'),
                   model_uri=DPV_LINKML.investigates, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isAfter = Slot(uri=DPV.isAfter, name="isAfter", curie=DPV.curie('isAfter'),
                   model_uri=DPV_LINKML.isAfter, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isApplicableFor = Slot(uri=DPV.isApplicableFor, name="isApplicableFor", curie=DPV.curie('isApplicableFor'),
                   model_uri=DPV_LINKML.isApplicableFor, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isAuthorityFor = Slot(uri=DPV.isAuthorityFor, name="isAuthorityFor", curie=DPV.curie('isAuthorityFor'),
                   model_uri=DPV_LINKML.isAuthorityFor, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isBefore = Slot(uri=DPV.isBefore, name="isBefore", curie=DPV.curie('isBefore'),
                   model_uri=DPV_LINKML.isBefore, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isComponentOf = Slot(uri=TECH.isComponentOf, name="isComponentOf", curie=TECH.curie('isComponentOf'),
                   model_uri=DPV_LINKML.isComponentOf, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isDeterminedByEntity = Slot(uri=DPV.isDeterminedByEntity, name="isDeterminedByEntity", curie=DPV.curie('isDeterminedByEntity'),
                   model_uri=DPV_LINKML.isDeterminedByEntity, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isDuring = Slot(uri=DPV.isDuring, name="isDuring", curie=DPV.curie('isDuring'),
                   model_uri=DPV_LINKML.isDuring, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isExercisedAt = Slot(uri=DPV.isExercisedAt, name="isExercisedAt", curie=DPV.curie('isExercisedAt'),
                   model_uri=DPV_LINKML.isExercisedAt, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isExploitedBy = Slot(uri=RISK.isExploitedBy, name="isExploitedBy", curie=RISK.curie('isExploitedBy'),
                   model_uri=DPV_LINKML.isExploitedBy, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isImplementedByEntity = Slot(uri=DPV.isImplementedByEntity, name="isImplementedByEntity", curie=DPV.curie('isImplementedByEntity'),
                   model_uri=DPV_LINKML.isImplementedByEntity, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isImplementedUsingTechnology = Slot(uri=DPV.isImplementedUsingTechnology, name="isImplementedUsingTechnology", curie=DPV.curie('isImplementedUsingTechnology'),
                   model_uri=DPV_LINKML.isImplementedUsingTechnology, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isIndicatedAtTime = Slot(uri=DPV.isIndicatedAtTime, name="isIndicatedAtTime", curie=DPV.curie('isIndicatedAtTime'),
                   model_uri=DPV_LINKML.isIndicatedAtTime, domain=None, range=Optional[Union[str, list[str]]])

slots.isIndicatedBy = Slot(uri=DPV.isIndicatedBy, name="isIndicatedBy", curie=DPV.curie('isIndicatedBy'),
                   model_uri=DPV_LINKML.isIndicatedBy, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isMainEstablishmentFor = Slot(uri=EU_GDPR.isMainEstablishmentFor, name="isMainEstablishmentFor", curie=EU_GDPR.curie('isMainEstablishmentFor'),
                   model_uri=DPV_LINKML.isMainEstablishmentFor, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isMitigatedByMeasure = Slot(uri=DPV.isMitigatedByMeasure, name="isMitigatedByMeasure", curie=DPV.curie('isMitigatedByMeasure'),
                   model_uri=DPV_LINKML.isMitigatedByMeasure, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isNotApplicableFor = Slot(uri=DPV.isNotApplicableFor, name="isNotApplicableFor", curie=DPV.curie('isNotApplicableFor'),
                   model_uri=DPV_LINKML.isNotApplicableFor, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isOrganisationalUnitOf = Slot(uri=DPV.isOrganisationalUnitOf, name="isOrganisationalUnitOf", curie=DPV.curie('isOrganisationalUnitOf'),
                   model_uri=DPV_LINKML.isOrganisationalUnitOf, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isOutsideOfLocation = Slot(uri=DPV.isOutsideOfLocation, name="isOutsideOfLocation", curie=DPV.curie('isOutsideOfLocation'),
                   model_uri=DPV_LINKML.isOutsideOfLocation, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isPartOf = Slot(uri=DCTERMS.isPartOf, name="isPartOf", curie=DCTERMS.curie('isPartOf'),
                   model_uri=DPV_LINKML.isPartOf, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isPolicyFor = Slot(uri=DPV.isPolicyFor, name="isPolicyFor", curie=DPV.curie('isPolicyFor'),
                   model_uri=DPV_LINKML.isPolicyFor, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isRepresentativeFor = Slot(uri=DPV.isRepresentativeFor, name="isRepresentativeFor", curie=DPV.curie('isRepresentativeFor'),
                   model_uri=DPV_LINKML.isRepresentativeFor, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isResidualRiskOf = Slot(uri=DPV.isResidualRiskOf, name="isResidualRiskOf", curie=DPV.curie('isResidualRiskOf'),
                   model_uri=DPV_LINKML.isResidualRiskOf, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isSubsidiaryOf = Slot(uri=DPV.isSubsidiaryOf, name="isSubsidiaryOf", curie=DPV.curie('isSubsidiaryOf'),
                   model_uri=DPV_LINKML.isSubsidiaryOf, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isVersionOf = Slot(uri=DCTERMS.isVersionOf, name="isVersionOf", curie=DCTERMS.curie('isVersionOf'),
                   model_uri=DPV_LINKML.isVersionOf, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isVulnerabilityOf = Slot(uri=RISK.isVulnerabilityOf, name="isVulnerabilityOf", curie=RISK.curie('isVulnerabilityOf'),
                   model_uri=DPV_LINKML.isVulnerabilityOf, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.iso_alpha2 = Slot(uri=LOC.iso_alpha2, name="iso_alpha2", curie=LOC.curie('iso_alpha2'),
                   model_uri=DPV_LINKML.iso_alpha2, domain=None, range=Optional[Union[str, list[str]]])

slots.iso_alpha3 = Slot(uri=LOC.iso_alpha3, name="iso_alpha3", curie=LOC.curie('iso_alpha3'),
                   model_uri=DPV_LINKML.iso_alpha3, domain=None, range=Optional[Union[str, list[str]]])

slots.iso_numeric = Slot(uri=LOC.iso_numeric, name="iso_numeric", curie=LOC.curie('iso_numeric'),
                   model_uri=DPV_LINKML.iso_numeric, domain=None, range=Optional[Union[str, list[str]]])

slots.logs = Slot(uri=RISK.logs, name="logs", curie=RISK.curie('logs'),
                   model_uri=DPV_LINKML.logs, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.mitigates = Slot(uri=RISK.mitigates, name="mitigates", curie=RISK.curie('mitigates'),
                   model_uri=DPV_LINKML.mitigates, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.mitigatesRisk = Slot(uri=DPV.mitigatesRisk, name="mitigatesRisk", curie=DPV.curie('mitigatesRisk'),
                   model_uri=DPV_LINKML.mitigatesRisk, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.modifies = Slot(uri=RISK.modifies, name="modifies", curie=RISK.curie('modifies'),
                   model_uri=DPV_LINKML.modifies, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.monitors = Slot(uri=RISK.monitors, name="monitors", curie=RISK.curie('monitors'),
                   model_uri=DPV_LINKML.monitors, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.overrides = Slot(uri=RISK.overrides, name="overrides", curie=RISK.curie('overrides'),
                   model_uri=DPV_LINKML.overrides, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.page = Slot(uri=FOAF.page, name="page", curie=FOAF.curie('page'),
                   model_uri=DPV_LINKML.page, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.recovers = Slot(uri=RISK.recovers, name="recovers", curie=RISK.curie('recovers'),
                   model_uri=DPV_LINKML.recovers, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.reduces = Slot(uri=RISK.reduces, name="reduces", curie=RISK.curie('reduces'),
                   model_uri=DPV_LINKML.reduces, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.refersToRisk = Slot(uri=RISK.refersToRisk, name="refersToRisk", curie=RISK.curie('refersToRisk'),
                   model_uri=DPV_LINKML.refersToRisk, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.remedies = Slot(uri=RISK.remedies, name="remedies", curie=RISK.curie('remedies'),
                   model_uri=DPV_LINKML.remedies, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.resolves = Slot(uri=RISK.resolves, name="resolves", curie=RISK.curie('resolves'),
                   model_uri=DPV_LINKML.resolves, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.reverses = Slot(uri=RISK.reverses, name="reverses", curie=RISK.curie('reverses'),
                   model_uri=DPV_LINKML.reverses, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.risk_hasRiskAssessment = Slot(uri=RISK.hasRiskAssessment, name="risk_hasRiskAssessment", curie=RISK.curie('hasRiskAssessment'),
                   model_uri=DPV_LINKML.risk_hasRiskAssessment, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.shares = Slot(uri=RISK.shares, name="shares", curie=RISK.curie('shares'),
                   model_uri=DPV_LINKML.shares, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.subject = Slot(uri=DCTERMS.subject, name="subject", curie=DCTERMS.curie('subject'),
                   model_uri=DPV_LINKML.subject, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.substitutes = Slot(uri=RISK.substitutes, name="substitutes", curie=RISK.curie('substitutes'),
                   model_uri=DPV_LINKML.substitutes, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.supportsComplianceWith = Slot(uri=DPV.supportsComplianceWith, name="supportsComplianceWith", curie=DPV.curie('supportsComplianceWith'),
                   model_uri=DPV_LINKML.supportsComplianceWith, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.tech_hasCapability = Slot(uri=TECH.hasCapability, name="tech_hasCapability", curie=TECH.curie('hasCapability'),
                   model_uri=DPV_LINKML.tech_hasCapability, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.tech_hasModel = Slot(uri=TECH.hasModel, name="tech_hasModel", curie=TECH.curie('hasModel'),
                   model_uri=DPV_LINKML.tech_hasModel, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.tech_hasService = Slot(uri=TECH.hasService, name="tech_hasService", curie=TECH.curie('hasService'),
                   model_uri=DPV_LINKML.tech_hasService, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.temporal = Slot(uri=DCTERMS.temporal, name="temporal", curie=DCTERMS.curie('temporal'),
                   model_uri=DPV_LINKML.temporal, domain=None, range=Optional[Union[dict, DpvInterval]])

slots.transfers = Slot(uri=RISK.transfers, name="transfers", curie=RISK.curie('transfers'),
                   model_uri=DPV_LINKML.transfers, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.un_m49 = Slot(uri=LOC.un_m49, name="un_m49", curie=LOC.curie('un_m49'),
                   model_uri=DPV_LINKML.un_m49, domain=None, range=Optional[Union[str, list[str]]])

slots.valid = Slot(uri=DCTERMS.valid, name="valid", curie=DCTERMS.curie('valid'),
                   model_uri=DPV_LINKML.valid, domain=None, range=Optional[Union[str, list[str]]])

slots.rdf_type = Slot(uri=RDF.type, name="rdf_type", curie=RDF.curie('type'),
                   model_uri=DPV_LINKML.rdf_type, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.prefLabel = Slot(uri=SKOS.prefLabel, name="prefLabel", curie=SKOS.curie('prefLabel'),
                   model_uri=DPV_LINKML.prefLabel, domain=None, range=Optional[str])

slots.prefLabel_de = Slot(uri=SKOS.prefLabel, name="prefLabel_de", curie=SKOS.curie('prefLabel'),
                   model_uri=DPV_LINKML.prefLabel_de, domain=None, range=Optional[str])

slots.definition = Slot(uri=SKOS.definition, name="definition", curie=SKOS.curie('definition'),
                   model_uri=DPV_LINKML.definition, domain=None, range=Optional[str])

slots.definition_de = Slot(uri=SKOS.definition, name="definition_de", curie=SKOS.curie('definition'),
                   model_uri=DPV_LINKML.definition_de, domain=None, range=Optional[str])

slots.scopeNote = Slot(uri=SKOS.scopeNote, name="scopeNote", curie=SKOS.curie('scopeNote'),
                   model_uri=DPV_LINKML.scopeNote, domain=None, range=Optional[Union[str, list[str]]])

slots.broader = Slot(uri=SKOS.broader, name="broader", curie=SKOS.curie('broader'),
                   model_uri=DPV_LINKML.broader, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.related = Slot(uri=SKOS.related, name="related", curie=SKOS.curie('related'),
                   model_uri=DPV_LINKML.related, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.inScheme = Slot(uri=SKOS.inScheme, name="inScheme", curie=SKOS.curie('inScheme'),
                   model_uri=DPV_LINKML.inScheme, domain=None, range=Optional[Union[Union[str, DpvConceptSchemeId], list[Union[str, DpvConceptSchemeId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.sameAs = Slot(uri=SKOS.sameAs, name="sameAs", curie=SKOS.curie('sameAs'),
                   model_uri=DPV_LINKML.sameAs, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.isDefinedBy = Slot(uri=RDFS.isDefinedBy, name="isDefinedBy", curie=RDFS.curie('isDefinedBy'),
                   model_uri=DPV_LINKML.isDefinedBy, domain=None, range=Optional[Union[Union[str, DpvVocabularyId], list[Union[str, DpvVocabularyId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.subClassOf = Slot(uri=RDFS.subClassOf, name="subClassOf", curie=RDFS.curie('subClassOf'),
                   model_uri=DPV_LINKML.subClassOf, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.subPropertyOf = Slot(uri=RDFS.subPropertyOf, name="subPropertyOf", curie=RDFS.curie('subPropertyOf'),
                   model_uri=DPV_LINKML.subPropertyOf, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.domainIncludes = Slot(uri=DCAM.domainIncludes, name="domainIncludes", curie=DCAM.curie('domainIncludes'),
                   model_uri=DPV_LINKML.domainIncludes, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.rangeIncludes = Slot(uri=DCAM.rangeIncludes, name="rangeIncludes", curie=DCAM.curie('rangeIncludes'),
                   model_uri=DPV_LINKML.rangeIncludes, domain=None, range=Optional[Union[Union[str, DpvTermId], list[Union[str, DpvTermId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.example = Slot(uri=VANN.example, name="example", curie=VANN.curie('example'),
                   model_uri=DPV_LINKML.example, domain=None, range=Optional[Union[Union[str, DpvExampleId], list[Union[str, DpvExampleId]]]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.exactMatch = Slot(uri=SKOS.exactMatch, name="exactMatch", curie=SKOS.curie('exactMatch'),
                   model_uri=DPV_LINKML.exactMatch, domain=None, range=Optional[Union[Union[str, DpvUri], list[Union[str, DpvUri]]]])

slots.term_status = Slot(uri=SW.term_status, name="term_status", curie=SW.curie('term_status'),
                   model_uri=DPV_LINKML.term_status, domain=None, range=Optional[Union[str, "DpvTermStatus"]])

slots.value = Slot(uri=RDF.value, name="value", curie=RDF.curie('value'),
                   model_uri=DPV_LINKML.value, domain=None, range=Optional[Decimal])

slots.source_page = Slot(uri=DCTERMS.source, name="source_page", curie=DCTERMS.curie('source'),
                   model_uri=DPV_LINKML.source_page, domain=None, range=Optional[Union[Union[dict, DpvWebPage], list[Union[dict, DpvWebPage]]]])

slots.datatype = Slot(uri=DPV_LINKML.datatype, name="datatype", curie=DPV_LINKML.curie('datatype'),
                   model_uri=DPV_LINKML.datatype, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.statements = Slot(uri=DPV_LINKML.statements, name="statements", curie=DPV_LINKML.curie('statements'),
                   model_uri=DPV_LINKML.statements, domain=None, range=Optional[Union[Union[dict, DpvStatement], list[Union[dict, DpvStatement]]]])

slots.dpvCatalogue__edition = Slot(uri=DCTERMS.isVersionOf, name="dpvCatalogue__edition", curie=DCTERMS.curie('isVersionOf'),
                   model_uri=DPV_LINKML.dpvCatalogue__edition, domain=None, range=str)

slots.dpvCatalogue__family = Slot(uri=DPV_LINKML.family, name="dpvCatalogue__family", curie=DPV_LINKML.curie('family'),
                   model_uri=DPV_LINKML.dpvCatalogue__family, domain=None, range=Union[str, "DpvFamily"])

slots.dpvCatalogue__vocabularies = Slot(uri=DPV_LINKML.vocabularies, name="dpvCatalogue__vocabularies", curie=DPV_LINKML.curie('vocabularies'),
                   model_uri=DPV_LINKML.dpvCatalogue__vocabularies, domain=None, range=Optional[Union[dict[Union[str, DpvVocabularyId], Union[dict, DpvVocabulary]], list[Union[dict, DpvVocabulary]]]])

slots.dpvCatalogue__concept_schemes = Slot(uri=DPV_LINKML.concept_schemes, name="dpvCatalogue__concept_schemes", curie=DPV_LINKML.curie('concept_schemes'),
                   model_uri=DPV_LINKML.dpvCatalogue__concept_schemes, domain=None, range=Optional[Union[list[Union[str, DpvConceptSchemeId]], dict[Union[str, DpvConceptSchemeId], Union[dict, DpvConceptScheme]]]])

slots.dpvCatalogue__properties = Slot(uri=DPV_LINKML.properties, name="dpvCatalogue__properties", curie=DPV_LINKML.curie('properties'),
                   model_uri=DPV_LINKML.dpvCatalogue__properties, domain=None, range=Optional[Union[dict[Union[str, DpvPropertyId], Union[dict, DpvProperty]], list[Union[dict, DpvProperty]]]])

slots.dpvCatalogue__agents = Slot(uri=DPV_LINKML.agents, name="dpvCatalogue__agents", curie=DPV_LINKML.curie('agents'),
                   model_uri=DPV_LINKML.dpvCatalogue__agents, domain=None, range=Optional[Union[dict[Union[str, DpvAgentId], Union[dict, DpvAgent]], list[Union[dict, DpvAgent]]]])

slots.dpvCatalogue__examples = Slot(uri=DPV_LINKML.examples, name="dpvCatalogue__examples", curie=DPV_LINKML.curie('examples'),
                   model_uri=DPV_LINKML.dpvCatalogue__examples, domain=None, range=Optional[Union[dict[Union[str, DpvExampleId], Union[dict, DpvExample]], list[Union[dict, DpvExample]]]])

slots.dpvAgent__hasORCID = Slot(uri=SCORO.hasORCID, name="dpvAgent__hasORCID", curie=SCORO.curie('hasORCID'),
                   model_uri=DPV_LINKML.dpvAgent__hasORCID, domain=None, range=Optional[str])

slots.dpvWebPage__page_name = Slot(uri=SDO.name, name="dpvWebPage__page_name", curie=SDO.curie('name'),
                   model_uri=DPV_LINKML.dpvWebPage__page_name, domain=None, range=str)

slots.dpvInterval__hasBeginning = Slot(uri=TIME.hasBeginning, name="dpvInterval__hasBeginning", curie=TIME.curie('hasBeginning'),
                   model_uri=DPV_LINKML.dpvInterval__hasBeginning, domain=None, range=Optional[Union[str, DpvDate]])

slots.dpvInterval__hasEnd = Slot(uri=TIME.hasEnd, name="dpvInterval__hasEnd", curie=TIME.curie('hasEnd'),
                   model_uri=DPV_LINKML.dpvInterval__hasEnd, domain=None, range=Optional[Union[str, DpvDate]])

slots.dpvExample__turtle_fault = Slot(uri=DPV_LINKML.turtle_fault, name="dpvExample__turtle_fault", curie=DPV_LINKML.curie('turtle_fault'),
                   model_uri=DPV_LINKML.dpvExample__turtle_fault, domain=None, range=Optional[str])

slots.dpvExample__resources = Slot(uri=DPV_LINKML.resources, name="dpvExample__resources", curie=DPV_LINKML.curie('resources'),
                   model_uri=DPV_LINKML.dpvExample__resources, domain=None, range=Optional[Union[dict[Union[str, DpvResourceId], Union[dict, DpvResource]], list[Union[dict, DpvResource]]]])

slots.dpvStatement__predicate = Slot(uri=RDF.predicate, name="dpvStatement__predicate", curie=RDF.curie('predicate'),
                   model_uri=DPV_LINKML.dpvStatement__predicate, domain=None, range=Union[str, URIorCURIE],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.dpvStatement__reference = Slot(uri=RDF.object, name="dpvStatement__reference", curie=RDF.curie('object'),
                   model_uri=DPV_LINKML.dpvStatement__reference, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^[A-Za-z_][A-Za-z0-9_+.-]*:\S*$'))

slots.dpvStatement__literal = Slot(uri=RDF.value, name="dpvStatement__literal", curie=RDF.curie('value'),
                   model_uri=DPV_LINKML.dpvStatement__literal, domain=None, range=Optional[str])

slots.dpvStatement__language = Slot(uri=DPV_LINKML.language, name="dpvStatement__language", curie=DPV_LINKML.curie('language'),
                   model_uri=DPV_LINKML.dpvStatement__language, domain=None, range=Optional[str])

slots.DpvAgent_id = Slot(uri=DPV_LINKML.id, name="DpvAgent_id", curie=DPV_LINKML.curie('id'),
                   model_uri=DPV_LINKML.DpvAgent_id, domain=DpvAgent, range=Union[str, DpvAgentId],
                   pattern=re.compile(r'^dpv_agent:(person|org)-[a-z0-9-]+$'))

slots.DpvExample_title = Slot(uri=DCTERMS.title, name="DpvExample_title", curie=DCTERMS.curie('title'),
                   model_uri=DPV_LINKML.DpvExample_title, domain=DpvExample, range=str)
