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
  The Statement of Applicability (SoA) recording which controls apply, their rationale, and current implementation state.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StatementOfApplicability extends DocumentedInformation {

  private List<SoAEntry> soaEntries;
  private String totalControls;
  private String implementedCount;
  private String plannedCount;
  private String notApplicableCount;
  private LocalDate lastReviewDate;


}