# #323 JFlex

Generate a Java lexer with JFlex and recognize World to print Hello, World!.

Canonical type `programming`, language_id `173`.

Toolchain provided: JFlex 1.9.1, java-cup-runtime and JDK 21.

From the example directory:

```sh
java -cp "$JFLEX_CLASSPATH" jflex.Main -d build hello.jflex
javac -d build build/GreetingLexer.java
java -cp build GreetingLexer input.txt
```

Expected result: 0 output; stdout Hello, World! followed by newline.

The word World is the input of the generated lexer: the output comes from the action of the rule, not from an ad hoc test parser.

Recorded status: syntax verified; behavior verified. Toolchain: JFlex 1.9.1 + CUP runtime 11b-20160615-3 + OpenJDK 21.0.12. [Log](verification/result.json).

Sources:

- [JFlex — manuale originale](https://jflex.de/manual.html)

Classpath required: `jflex-1.9.1.jar`, `java-cup-runtime-11b-20160615-3.jar`. The original JAR are available from [Maven Central](https://repo.maven.apache.org/maven2/). Set the command classpath variable; `;` separator on Windows, `:` on Unix.

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.flex` | [hello.flex](variants/flex-1e75c1a3/hello.flex) created; verification pending |
| `.jflex` | [hello.jflex](hello.jflex) verified |
