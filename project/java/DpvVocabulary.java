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
  One of DPV's vocabularies, as its own Turtle file's header describes it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DpvVocabulary  {

  private URI id;
  private String title;
  private String description;
  private String identifier;
  private String bibliographicCitation;
  private List<String> conformsTo;
  private List<LocalDate> created;
  private LocalDate issued;
  private LocalDate modified;
  private List<DpvAgent> creator;
  private List<DpvAgent> contributor;
  private URI publisher;
  private URI license;
  private List<String> source;
  private String doi;
  private String biboStatus;
  private String preferredNamespacePrefix;
  private String preferredNamespaceUri;
  private String rdfsLabel;
  private URI versionIRI;
  private String versionInfo;
  private String schemaVersion;
  private List<URI> isProfileOf;
  private URI logo;


}