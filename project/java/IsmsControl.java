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
  A control the organization has determined it needs to treat its risks: what it does in the organization's words, which Annex A controls it answers to, who owns it, how far it is in place and how well it works.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsControl  {

  private List<IsmsControl> relevantControls;
  private String implementationState;
  private List<String> controlAnnexAControls;
  private String controlTheme;
  private String controlText;
  private String controlGuidance;
  private List<String> controlThreats;
  private List<String> controlAssetTypes;
  private String controlOwner;
  private LocalDate controlImplementationDate;
  private String controlEffectiveness;
  private LocalDate controlLastTested;
  private List<String> controlEvidence;
  private URI ismsId;
  private String title;
  private String description;


}