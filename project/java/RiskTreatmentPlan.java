package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  A risk treatment plan documenting planned actions to address identified risks through selected controls.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RiskTreatmentPlan extends DocumentedInformation {

  private String planScope;
  private List<Risk> risksAddressed;
  private List<String> treatmentActions;
  private List<SecurityControl> controlsToImplement;
  private String resourcesRequired;
  private List<String> responsibleParties;
  private String implementationTimeline;
  private String riskOwnerApproval;
  private String residualRiskAcceptance;
  private String implementationStatus;
  private LocalDate completionDate;

}