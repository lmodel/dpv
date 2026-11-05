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
  An inverse jurisdiction for a specific jurisdiction is the set of all other jurisdictions that are not part of the specific jurisdiction
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DpvInverseJurisdiction extends DpvJurisdiction {



}