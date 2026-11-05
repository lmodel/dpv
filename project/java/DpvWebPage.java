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
  A web page DPV names as a term's source.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DpvWebPage  {

  private String pageName;
  private String url;


}