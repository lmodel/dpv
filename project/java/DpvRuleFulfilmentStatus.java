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
  Status associated with a rule for indicating whether it is applicable, or has been utilised, and whether the requirements of the rule have been fulfilled or violated
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DpvRuleFulfilmentStatus extends DpvStatus {



}