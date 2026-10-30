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
  Anything the ISMS keeps a record of that other records can refer to: it has an identifier, a title and a description.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class IsmsRecord  {

  private URI ismsId;
  private String title;
  private String description;


}