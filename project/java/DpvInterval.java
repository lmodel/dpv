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
  A period of time, with the dates that start and end it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DpvInterval  {

  private LocalDate hasBeginning;
  private LocalDate hasEnd;


}