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
  One thing DPV's vocabularies state, or a thing a use case describes with them, as a record under its own IRI.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class DpvTerm  {

  private URI id;
  private List<DpvTerm> rdfType;
  private String prefLabel;
  private String prefLabelDe;
  private String definition;
  private String definitionDe;
  private List<String> scopeNote;
  private List<DpvTerm> broader;
  private List<DpvTerm> related;
  private List<DpvConceptScheme> inScheme;
  private List<DpvTerm> sameAs;
  private List<DpvVocabulary> isDefinedBy;
  private List<DpvTerm> subClassOf;
  private List<DpvExample> example;
  private List<URI> exactMatch;
  private String termStatus;
  private List<LocalDate> created;
  private LocalDate modified;
  private List<DpvAgent> contributor;
  private List<String> source;
  private List<DpvWebPage> sourcePage;
  private String homepage;
  private BigDecimal value;
  private DpvInterval temporal;


}