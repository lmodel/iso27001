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
  The evidence of one person's competence for work that affects information security, and what is done to close any gap.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsCompetenceRecord extends IsmsRecord {

  private String competencePerson;
  private IsmsRole competenceRole;
  private List<String> competenceRequired;
  private List<String> competenceEducation;
  private List<String> competenceTraining;
  private List<String> competenceExperience;
  private LocalDate competenceAssessmentDate;
  private List<String> competenceGaps;
  private List<String> competenceActions;
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