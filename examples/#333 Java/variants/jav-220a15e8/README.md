# 0333: Java: `.jav`

## Recorded verification

**Syntax and behavior verified** on November 4, 2026. Copy .jav byte-identically as Hello.java, compile and execute; run the original .jsh as JShell input with local execution engine. [Evidence](../../verification/native_20261104_333_variants_result.json).

Role: historical Alias of Java source; javac requires the name hello.java for the public class.

Origin: Byte-identical copy of the original corpus source: examples/#333 Java/hello.java.

Required toolchain: OpenJDK 21.0.12. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Copiare hello.jav in una directory di build come hello.java; javac hello.java; java Hello
```

Expected result: stdout Hello, World! and LF, 0. output

Earlier status (before this check): Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.jav`: `e8533e4508f5734f52cbfcf23d34a842fcce5d27f9d82b23ca2f4ff6b3bf1e32`

Primary sources:

- https://docs.oracle.com/javase/tutorial/getStarted/cupojava/win32.html
