# #333 Java

Fill and run a Java class with main method.

Canonical type `programming`, language_id `181`.

Suggested toolchain: Microsoft OpenJDK 21.

From the example directory:

```sh
javac -d build Hello.java
java -cp build Hello
```

Expected result: stdout Hello, World! and LF, 0. output

The control executes the bytecode compiled with javac.

Recorded status: syntax verified; behavior verified. Toolchain: OpenJDK 21.0.12. [Log](verification/result.json).

Sources:

- [Oracle — Java main e primo programma](https://docs.oracle.com/javase/tutorial/getStarted/cupojava/win32.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.java` | [Hello.java](Hello.java) verified |
| `.jav` | [hello.jav](variants/jav-220a15e8/hello.jav) syntax and behavior verified |
| `.jsh` | [hello.jsh](variants/jsh-e38b41dc/hello.jsh) syntax and behavior verified |

## Additional extension verification

- `.jav`: verified on November 4, 2026. [Evidence](verification/native_20261104_333_variants_result.json).
- `.jsh`: verified on November 4, 2026. [Evidence](verification/native_20261104_333_variants_result.json).
