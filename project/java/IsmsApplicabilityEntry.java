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
  One entry of the Statement of Applicability, which either includes a control or excludes an Annex A control, and says why.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class IsmsApplicabilityEntry  {

  private String entryAnnexAControl;
  private String entryType;
  private String entryJustification;


}