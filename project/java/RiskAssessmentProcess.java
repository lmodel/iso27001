package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  The documented risk assessment process per Clause 6.1.2, defining criteria and methodology for identifying, analyzing, and evaluating risks.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RiskAssessmentProcess extends DocumentedInformation {

  private String riskAcceptanceCriteria;
  private String assessmentCriteria;
  private String assessmentMethodology;
  private String likelihoodScale;
  private String impactScale;
  private String riskMatrix;
  private String assessmentFrequency;
  private List<String> triggerEvents;

}