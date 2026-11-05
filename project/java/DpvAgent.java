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
  A person or an organization DPV names as a contributor, as DPV's files describe them.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DpvAgent  {

  private URI id;
  private String homepage;
  private String name;
  private String hasORCID;
  private List<DpvAgent> memberOf;


}