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
  A documented procedure for operational planning and control per Clause 8.1.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OperationalProcedure extends DocumentedInformation {

  private String procedureScope;
  private String processCriteria;
  private List<String> controlMeasures;
  private List<Role> responsibleRoles;
  private List<SecurityControl> relatedControls;
  private String changeControlRequirements;


}