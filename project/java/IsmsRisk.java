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
  An information security risk in the risk register: where it comes from, what it threatens, who owns it, how it is rated before and after controls, and how it is treated.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsRisk extends IsmsRecord {

  private List<IsmsAsset> affectedAssets;
  private List<String> affectedSecurityProperties;
  private String riskSource;
  private String riskThreat;
  private String riskVulnerability;
  private String riskOwner;
  private String riskLikelihood;
  private String riskImpact;
  private String riskInherentLevel;
  private List<IsmsControl> riskExistingControls;
  private String riskResidualLevel;
  private String riskTreatmentOption;
  private String riskTreatmentPriority;


}