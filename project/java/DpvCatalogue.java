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
  One part of a DPV release: one namespace family's vocabularies and terms, its contributors or its examples.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DpvCatalogue  {

  private List<DpvConcept> concepts;
  private String edition;
  private String family;
  private List<DpvVocabulary> vocabularies;
  private List<DpvConceptScheme> conceptSchemes;
  private List<DpvProperty> properties;
  private List<DpvAgent> agents;
  private List<DpvExample> examples;


}