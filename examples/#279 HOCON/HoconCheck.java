import com.typesafe.config.ConfigFactory;
import java.io.File;

public final class HoconCheck {
    public static void main(String[] args) {
        var config = ConfigFactory.parseFile(new File(args[0])).resolve();
        if (!config.getString("message").equals("Hello, World!")) throw new AssertionError(config);
        if (!config.getString("target").equals("World")) throw new AssertionError(config);
        System.out.println(config.getString("message"));
        System.out.println("PASS: official HOCON parser, concatenation and substitution resolution");
    }
}
