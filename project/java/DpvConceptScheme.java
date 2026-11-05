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
  A list of terms DPV keeps within a vocabulary. DPV states nothing else about one.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DpvConceptScheme  {

  private URI id;


}