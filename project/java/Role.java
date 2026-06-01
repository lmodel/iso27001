package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An information security role with defined responsibilities and authorities per Clause 5.3.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Role extends NamedEntity {

  private String roleType;
  private List<String> responsibilities;
  private List<String> authorities;
  private String accountability;
  private List<String> assignedTo;
  private String delegationRules;
  private String reportingLine;


}