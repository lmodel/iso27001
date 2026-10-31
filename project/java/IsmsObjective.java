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
  An information security objective: a measurable result the organization aims for, with how it plans to reach it and how it measures progress.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsObjective  {

  private IsmsRole responsibleRole;
  private List<IsmsControl> relevantControls;
  private String objectiveStatement;
  private String objectiveTarget;
  private String objectiveCurrentValue;
  private String objectiveMetric;
  private String objectiveMeasurementMethod;
  private String objectiveMeasurementFrequency;
  private LocalDate objectiveTargetDate;
  private String objectiveAchievement;
  private List<IsmsRisk> objectiveRisks;
  private String objectiveActionPlan;
  private String objectiveResources;
  private URI ismsId;
  private String title;
  private String description;


}