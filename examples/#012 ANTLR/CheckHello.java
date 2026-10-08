import java.nio.file.Files;
import java.nio.file.Path;
import org.antlr.v4.runtime.*;

public final class CheckHello {
    private static int errors;
    private static final BaseErrorListener LISTENER = new BaseErrorListener() {
        @Override
        public void syntaxError(Recognizer<?, ?> recognizer, Object symbol,
                int line, int column, String message, RecognitionException cause) {
            errors++;
        }
    };

    private static String parse(String source) {
        errors = 0;
        HelloLexer lexer = new HelloLexer(CharStreams.fromString(source));
        lexer.removeErrorListeners();
        lexer.addErrorListener(LISTENER);
        HelloParser parser = new HelloParser(new CommonTokenStream(lexer));
        parser.removeErrorListeners();
        parser.addErrorListener(LISTENER);
        return parser.message().toStringTree(parser);
    }

    public static void main(String[] args) throws Exception {
        String tree = parse(Files.readString(Path.of(args[0])));
        if (errors != 0 || !tree.equals("(message Hello, World! <EOF>)")) {
            throw new AssertionError("Expected greeting was not recognized: " + tree);
        }
        System.out.println(tree);
        for (String rejected : new String[] { "Goodbye!", "Hello, World! extra", "" }) {
            parse(rejected);
            if (errors == 0) throw new AssertionError("Unexpected acceptance: " + rejected);
        }
        System.out.println("Negative controls rejected: wrong greeting, trailing text, empty input");
    }
}
