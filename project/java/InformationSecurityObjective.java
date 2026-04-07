package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  A measurable information security objective per Clause 6.2, established at relevant functions and levels of the organization.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class InformationSecurityObjective extends NamedEntity {

  private String objectiveStatement;
  private String targetValue;
  private String currentValue;
  private String metricDefinition;
  private String measurementMethod;
  private String measurementFrequency;
  private Role responsibleRole;
  private LocalDate targetDate;
  private String achievementStatus;
  private List<Risk> relatedRisks;
  private List<SecurityControl> relatedControls;
  private String actionPlan;

}