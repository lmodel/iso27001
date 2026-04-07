package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  A security control from Annex A of ISO/IEC 27001:2022, derived from ISO/IEC 27002:2022. Represents a measure that modifies risk.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SecurityControl extends NamedEntity {

  private String controlId;
  private String controlTitle;
  private String controlCategory;
  private String controlText;
  private String implementationGuidance;
  private List<SecurityControl> relatedControls;
  private List<String> applicableThreats;
  private List<String> applicableAssets;
  private String controlOwner;
  private String implementationStatus;
  private LocalDate implementationDate;
  private String effectivenessRating;
  private LocalDate lastTestDate;
  private List<String> evidenceReferences;

}