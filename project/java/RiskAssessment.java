package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  An instance of risk assessment performed per Clause 8.2, identifying and evaluating information security risks.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RiskAssessment extends DocumentedInformation {

  private String assessmentScope;
  private LocalDate assessmentDate;
  private String assessor;
  private String methodologyUsed;
  private List<Risk> risksIdentified;
  private String summaryFindings;
  private List<String> recommendations;
  private LocalDate nextAssessmentDate;

}