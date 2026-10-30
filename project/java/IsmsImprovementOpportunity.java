package example;

/* metamodel_version: 1.12.0 */
/* version: 2022/Amd 1:2024 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An opportunity to improve the ISMS's suitability, adequacy or effectiveness, and what came of it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsImprovementOpportunity extends IsmsRecord {

  private IsmsRole responsibleRole;
  private String improvementSource;
  private LocalDate improvementIdentifiedOn;
  private String improvementIdentifiedBy;
  private String improvementBenefit;
  private String improvementPriority;
  private String improvementPlan;
  private LocalDate improvementTargetDate;
  private LocalDate improvementCompletionDate;
  private String improvementOutcome;
  private String improvementStatus;


}