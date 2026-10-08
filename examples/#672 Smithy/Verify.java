import software.amazon.smithy.model.*;
import software.amazon.smithy.model.shapes.*;
public class Verify {
 public static void main(String[] args) {
  Model model = Model.assembler().addImport(java.nio.file.Path.of("hello.smithy")).assemble().unwrap();
  String value = model.expectShape(ShapeId.from("corpus#Greeting"), EnumShape.class).getEnumValues().get("HELLO");
  if (!"Hello, World!".equals(value)) throw new AssertionError(value);
  System.out.println(value);
 }
}
