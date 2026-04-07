package None;

/* metamodel_version: 1.7.0 */
/* version: 1.0.0 */
import java.util.List;
import lombok.*;

/**
  Evidence of competence for personnel affecting information security performance per Clause 7.2 d).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CompetenceRecord extends DocumentedInformation {

  private String personName;
  private String personRole;
  private List<String> requiredCompetencies;
  private List<String> educationRecords;
  private List<String> trainingRecords;
  private List<String> experienceRecords;
  private LocalDate competencyAssessmentDate;
  private List<String> competencyGaps;
  private List<String> developmentActions;

}