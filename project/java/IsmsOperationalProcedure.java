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
  A procedure by which the organization plans and controls the processes that meet its information security requirements.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsOperationalProcedure extends IsmsRecord {

  private List<IsmsControl> relevantControls;
  private String procedureScope;
  private String procedureCriteria;
  private List<String> procedureControlMeasures;
  private List<IsmsRole> procedureRoles;
  private String procedureChangeControl;
  private String documentReference;
  private String documentVersion;
  private String documentAuthor;
  private String documentOwner;
  private String documentApprover;
  private LocalDate documentApprovalDate;
  private LocalDate documentEffectiveDate;
  private LocalDate documentLastReviewDate;
  private LocalDate documentNextReviewDate;
  private String documentStatus;
  private String documentClassification;
  private String documentRetention;
  private List<String> documentDistribution;
  private String documentStorage;
  private String documentChangeControl;
  private Boolean documentExternalOrigin;
  private String documentExternalSource;


}