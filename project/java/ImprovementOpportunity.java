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
  An opportunity for continual improvement per Clause 10.1, enhancing overall ISMS performance.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImprovementOpportunity extends NamedEntity {

  private String improvementSource;
  private LocalDate identificationDate;
  private String identifiedBy;
  private String improvementDescription;
  private String expectedBenefit;
  private String priority;
  private String implementationPlan;
  private String responsibleParty;
  private LocalDate targetDate;
  private LocalDate actualCompletionDate;
  private String outcomeAssessment;
  private String status;


}