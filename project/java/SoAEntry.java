package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  A single entry in the Statement of Applicability, documenting the applicability and implementation status of one control.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SoAEntry  {

  private SecurityControl controlReference;
  private boolean isApplicable;
  private String inclusionJustification;
  private String exclusionJustification;
  private String implementationStatus;
  private String implementationEvidence;
  private Role responsibleRole;
  private LocalDate targetImplementationDate;

}