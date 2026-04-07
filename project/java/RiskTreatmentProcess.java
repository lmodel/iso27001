package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  The documented risk treatment process per Clause 6.1.3, defining how treatment options are selected and controls determined.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RiskTreatmentProcess extends DocumentedInformation {

  private String treatmentOptionsGuidance;
  private String controlSelectionCriteria;
  private String soaTemplate;
  private String approvalWorkflow;

}