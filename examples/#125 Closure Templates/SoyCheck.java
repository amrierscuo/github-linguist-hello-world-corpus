import com.google.template.soy.SoyFileSet;
import java.io.File;
import java.util.Map;

public final class SoyCheck {
    public static void main(String[] args) throws Exception {
        var tofu = SoyFileSet.builder().add(new File(args[0])).build().compileToTofu();
        String result = tofu.newRenderer("corpus.hello.greeting")
            .setData(Map.of("name", "World")).renderText();
        if (!result.equals("Hello, World!")) throw new AssertionError(result);
        String control = tofu.newRenderer("corpus.hello.greeting")
            .setData(Map.of("name", "Reader")).renderText();
        if (!control.equals("Hello, Reader!")) throw new AssertionError(control);
        System.out.println(result);
        System.out.println("PASS: official Soy compile/render and parameter control");
    }
}
