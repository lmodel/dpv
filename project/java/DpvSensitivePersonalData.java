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
  Personal data that is considered 'sensitive' in terms of privacy and/or impact, and therefore requires additional considerations and/or protection
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DpvSensitivePersonalData extends DpvPersonalData {



}