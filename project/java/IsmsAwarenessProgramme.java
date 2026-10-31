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
  The programme that makes people working for the organization aware of the policy, their part in the ISMS and what failing it would mean.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsAwarenessProgramme  {

  private List<String> awarenessTopics;
  private List<String> awarenessMethods;
  private String awarenessAudience;
  private String awarenessFrequency;
  private String awarenessCompletionTracking;
  private String awarenessEffectiveness;
  private URI ismsId;
  private String title;
  private String description;
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