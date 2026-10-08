import freemarker.template.Configuration;
import java.io.File;
import java.io.StringWriter;
import java.util.Map;

public final class FreeMarkerCheck {
    public static void main(String[] args) throws Exception {
        var config = new Configuration(Configuration.VERSION_2_3_34);
        config.setDirectoryForTemplateLoading(new File(args[0]));
        config.setDefaultEncoding("UTF-8");
        var template = config.getTemplate("hello.ftl");
        var result = new StringWriter();
        template.process(Map.of("name", "World"), result);
        if (!result.toString().equals("Hello, World!\n")) throw new AssertionError(result);
        var control = new StringWriter();
        template.process(Map.of("name", "Reader"), control);
        if (!control.toString().equals("Hello, Reader!\n")) throw new AssertionError(control);
        System.out.print(result);
        System.out.println("PASS: genuine FreeMarker parse/render; parameter control");
    }
}
