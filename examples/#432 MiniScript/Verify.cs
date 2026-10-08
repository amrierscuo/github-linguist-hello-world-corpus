using System;
using System.IO;
using System.Text;
using Miniscript;
public class Verify {
    public static void Main() {
        StringBuilder output = new StringBuilder();
        Interpreter engine = new Interpreter(File.ReadAllText("hello.ms"));
        engine.standardOutput = (text, newline) => { output.Append(text); if (newline) output.Append("\n"); };
        engine.errorOutput = (text, newline) => { throw new Exception(text); };
        engine.Compile();
        engine.RunUntilDone();
        if (!engine.done || output.ToString() != "Hello, World!\n") throw new Exception("unexpected MiniScript output");
        Console.Write(output.ToString());
    }
}
