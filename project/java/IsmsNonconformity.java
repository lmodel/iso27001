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
  A nonconformity: a requirement not met, how it was found and contained, its consequences and cause, and how it was closed.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsNonconformity extends IsmsRecord {

  private String nonconformitySource;
  private LocalDate nonconformityDetectedOn;
  private String nonconformityDetectedBy;
  private String nonconformityRequirement;
  private List<String> nonconformityImmediateActions;
  private String nonconformityConsequences;
  private String nonconformityRootCause;
  private String nonconformitySimilarCheck;
  private String nonconformityStatus;
  private LocalDate nonconformityClosureDate;
  private String nonconformityClosureEvidence;


}