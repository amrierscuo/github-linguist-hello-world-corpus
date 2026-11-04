# #336 Java Template Engine

Fill out a JTE Java template with target parameter and make greetings.

Canonical type `programming`, language_id `599494012`.

Suggested toolchain: JDK 21, jte and jte-runtime 3.1.16.

From the example directory:

```sh
java -cp "$JTE_CLASSPATH" Verify.java build/jte
```

Expected result: stdout Hello, World! and LF, 0. output

The engine compiles the template in Java with the JDK toolchain, then renders the constant parameter.

Recorded status: syntax verified; behavior verified. Toolchain: OpenJDK 21.0.12 + jte/jte-runtime 3.1.16. [Log](verification/result.json).

Sources:

- [JTE — sintassi](https://jte.gg/syntax/)
- [JTE — implementazione](https://github.com/casid/jte)

Classpath required: `jte-3.1.16.jar`, `jte-runtime-3.1.16.jar`, `jte-extension-api-3.1.16.jar`. The original JAR are available from [Maven Central](https://repo.maven.apache.org/maven2/). Set the command classpath variable; `;` separator on Windows, `:` on Unix.

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.jte` | [hello.jte](hello.jte) verified |
