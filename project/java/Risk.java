package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  An identified information security risk that may affect information security properties within the ISMS scope.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Risk extends NamedEntity {

  private String riskSource;
  private String threatDescription;
  private String vulnerabilityDescription;
  private List<Asset> affectedAssets;
  private List<String> affectedCiaProperties;
  private String riskOwner;
  private String likelihood;
  private String impact;
  private String inherentRiskLevel;
  private List<SecurityControl> existingControls;
  private String residualRiskLevel;
  private String riskTreatmentOption;
  private String treatmentPriority;
  private RiskTreatmentPlan relatedTreatmentPlan;

}