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
  An entry that leaves out an Annex A control the organization does not need, and says why.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IsmsExcludedControl extends IsmsApplicabilityEntry {



}