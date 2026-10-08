import java.nio.file.*;
import org.stringtemplate.v4.ST;
public class Verify {
 public static void main(String[] args)throws Exception {
  String input=Files.readString(Path.of("hello.st"));
  String world=new ST(input).add("name","World").render();
  String reader=new ST(input).add("name","Reader").render();
  if(!world.strip().equals("Hello, World!")||!reader.strip().equals("Hello, Reader!"))throw new AssertionError("render mismatch");
  System.out.println("StringTemplate "+ST.VERSION);
  System.out.println(world);System.out.println("PASS: actual ST compiler and parameter rendering");
 }
}
