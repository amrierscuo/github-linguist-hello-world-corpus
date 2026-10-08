import java.nio.file.*;
import java.io.*;
import org.apache.velocity.*;
import org.apache.velocity.app.*;
public class Verify {
 public static void main(String[] args) throws Exception {
  VelocityEngine engine=new VelocityEngine();engine.init();
  VelocityContext context=new VelocityContext();context.put("target","World");
  StringWriter output=new StringWriter();
  if(!engine.evaluate(context,output,"corpus",Files.readString(Path.of("hello.vtl")))) throw new AssertionError("render failed");
  if(!output.toString().equals("Hello, World!\n")) throw new AssertionError(output);
  System.out.print(output);
 }
}
