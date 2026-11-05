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
  One of DPV's examples: what it shows, and the statements its Turtle file makes, as one resource per subject.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DpvExample  {

  private URI id;
  private String title;
  private String description;
  private List<String> format;
  private List<String> source;
  private List<DpvTerm> subject;
  private List<LocalDate> created;
  private LocalDate modified;
  private DpvInterval temporal;
  private List<DpvAgent> contributor;
  private String termStatus;
  private String turtleFault;
  private List<DpvResource> resources;


}