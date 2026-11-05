package example;

/* metamodel_version: 1.12.0 */
/* version: 2.3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A term DPV states as a concept and a class. Its rdf_type names the concepts it is an instance of, each a class of this schema, where DPV states one.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DpvConcept extends DpvTerm {

  private List<DpvTerm> euAiactHasRiskLevel;
  private List<DpvTerm> hasApplicableLaw;
  private List<DpvTerm> hasAuthority;
  private List<String> hasHumanDescription;
  private List<DpvTerm> hasInverseJurisdiction;
  private List<DpvTerm> hasJurisdiction;
  private List<DpvTerm> hasJustification;
  private List<DpvTerm> hasLikelihood;
  private List<DpvTerm> hasObligation;
  private List<DpvTerm> hasPermission;
  private List<DpvTerm> hasProhibition;
  private List<DpvTerm> hasRight;
  private List<DpvTerm> hasRiskLevel;
  private List<DpvTerm> hasSeverity;
  private List<String> isoAlpha2;
  private List<String> isoAlpha3;
  private List<String> isoNumeric;
  private List<String> unM49;


}