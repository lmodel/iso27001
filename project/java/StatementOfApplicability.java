package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  The Statement of Applicability (SoA) per 6.1.3 d), listing necessary controls with justification and implementation status.
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