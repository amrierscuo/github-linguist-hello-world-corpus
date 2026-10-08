import java.nio.file.*;
import java.io.*;
import java.util.*;
public class Verify {
    public static void main(String[] args) throws Exception {
        Properties props = new Properties();
        try (Reader reader = Files.newBufferedReader(Path.of("hello.properties"))) { props.load(reader); }
        if (props.size() != 1 || !"Hello, World!".equals(props.getProperty("greeting"))) throw new AssertionError(props);
        System.out.println(props.getProperty("greeting"));
    }
}
