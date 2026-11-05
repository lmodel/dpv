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
  Data that is not Personal Data
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DpvNonPersonalData extends DpvConcept {



}