import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.jar.Manifest;
public final class VerifyManifest {
  public static void main(String[] args) throws Exception {
    try (InputStream input = Files.newInputStream(Path.of(args[0]))) {
      var attrs = new Manifest(input).getMainAttributes();
      if (!"1.0".equals(attrs.getValue("Manifest-Version")) ||
          !"Hello".equals(attrs.getValue("Main-Class")) ||
          !"Hello, World!".equals(attrs.getValue("Corpus-Greeting")))
        throw new AssertionError("Unexpected manifest attributes");
      System.out.println(attrs.getValue("Corpus-Greeting"));
    }
  }
}
