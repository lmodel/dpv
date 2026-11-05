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
  A property DPV states, with the classes it names as its usual subjects and values. Every property is also a slot of DpvResource.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DpvProperty extends DpvTerm {

  private List<DpvTerm> subPropertyOf;
  private List<DpvTerm> domainIncludes;
  private List<DpvTerm> rangeIncludes;


}