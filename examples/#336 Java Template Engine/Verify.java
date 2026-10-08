import gg.jte.*;
import gg.jte.output.StringOutput;
import gg.jte.resolve.DirectoryCodeResolver;
import java.nio.file.*;
import java.util.*;
public class Verify {
    public static void main(String[] args) {
        TemplateEngine engine = TemplateEngine.create(new DirectoryCodeResolver(Path.of(".")), Path.of(args[0]), ContentType.Plain);
        StringOutput output = new StringOutput();
        engine.render("hello.jte", Map.of("target", "World"), output);
        String text = output.toString();
        if (!text.equals("Hello, World!\n")) throw new AssertionError(text);
        System.out.print(text);
    }
}
