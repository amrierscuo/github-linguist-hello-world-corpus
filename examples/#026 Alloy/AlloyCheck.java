import java.nio.file.Files;
import java.nio.file.Path;
import edu.mit.csail.sdg.alloy4.A4Reporter;
import edu.mit.csail.sdg.alloy4.Err;
import edu.mit.csail.sdg.ast.Command;
import edu.mit.csail.sdg.parser.CompModule;
import edu.mit.csail.sdg.parser.CompUtil;
import edu.mit.csail.sdg.translator.A4Options;
import edu.mit.csail.sdg.translator.A4Solution;
import edu.mit.csail.sdg.translator.A4TupleSet;
import edu.mit.csail.sdg.translator.TranslateAlloyToKodkod;
import kodkod.engine.satlab.SATFactory;

class AlloyCheck {
    private static void require(boolean condition, String message) {
        if (!condition) throw new AssertionError(message);
    }

    public static void main(String[] args) throws Exception {
        Path source = Path.of(args.length > 0 ? args[0] : "hello.als");
        CompModule world = CompUtil.parseEverything_fromFile(A4Reporter.NOP, null, source.toAbsolutePath().toString());
        require(world.getAllCommands().size() == 2, "Expected two Alloy commands");
        A4Options options = new A4Options();
        options.solver = SATFactory.get("sat4j");
        int index = 0;
        for (Command command : world.getAllCommands()) {
            A4Solution solution = TranslateAlloyToKodkod.execute_command(A4Reporter.NOP, world.getAllReachableSigs(), command, options);
            if (index == 0) {
                require(!command.check && solution.satisfiable(), "showGreeting must be satisfiable");
                A4TupleSet texts = (A4TupleSet) solution.eval(CompUtil.parseOneExpression_fromString(world, "Greeting.text"));
                require(texts.size() == 1 && texts.arity() == 1, "Exactly one text atom expected");
                String text = texts.iterator().next().atom(0);
                require(text.equals("\"Hello, World!\""), "Unexpected Alloy text atom: " + text);
                System.out.println("showGreeting: SAT; Greeting.text = " + text);
            } else {
                require(command.check && !solution.satisfiable(), "GreetingIsHelloWorld must have no counterexample");
                System.out.println("GreetingIsHelloWorld: UNSAT counterexample, scope 3");
            }
            index++;
        }
        boolean rejected = false;
        try {
            CompUtil.parseEverything_fromString(A4Reporter.NOP, Files.readString(source).replace("one sig Greeting", "one sig"));
        } catch (Err expected) {
            rejected = true;
        }
        require(rejected, "Malformed signature must be rejected by Alloy parser");
        System.out.println("PASS: native Alloy parser, SAT4J instance, bounded assertion, malformed-signature negative control");
    }
}
