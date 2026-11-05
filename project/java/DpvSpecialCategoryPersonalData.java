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
  Sensitive Personal Data whose use requires specific additional legal permission or justification
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DpvSpecialCategoryPersonalData extends DpvSensitivePersonalData {



}