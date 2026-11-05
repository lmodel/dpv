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
  One statement of a resource that its keys cannot hold: a predicate with no slot, or a value not in the form its slot takes.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DpvStatement  {

  private URI predicate;
  private URI reference;
  private String literal;
  private URI datatype;
  private String language;


}