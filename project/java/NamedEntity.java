package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Abstract base class for all entities with an identifier, name, and description. Provides common identification and documentation slots.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class NamedEntity  {

  private URI id;
  private String name;
  private String description;
  private LocalDate createdDate;
  private LocalDate modifiedDate;
  private String version;


}