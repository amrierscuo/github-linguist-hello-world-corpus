import x10.io.Console;

public class Hello {
    public static def main(args: Rail[String]): void {
        val audience: String = "World";
        Console.OUT.println("Hello, " + audience + "!");
    }
}
