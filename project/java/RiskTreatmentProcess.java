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
  The documented risk treatment process per Clause 6.1.3, defining how treatment options are selected and controls determined.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class RiskTreatmentProcess extends DocumentedInformation {

  private String treatmentOptionsGuidance;
  private String controlSelectionCriteria;
  private String annexAOmissionVerification;
  private String soaTemplate;
  private String approvalWorkflow;


}