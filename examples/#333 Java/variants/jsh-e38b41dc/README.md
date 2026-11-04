# 0333: Java: `.jsh`

## Recorded verification

**Syntax and behavior verified** on November 4, 2026. Copy .jav byte-identically as Hello.java, compile and execute; run the original .jsh as JShell input with local execution engine. [Evidence](../../verification/native_20261104_333_variants_result.json).

Ruolo: Script JShell con istruzione top-level, distinto da classe Java compilabile.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: OpenJDK 21.0.12. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
jshell hello.jsh
```

Expected result: Hello, World!

Earlier status (before this check): Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.jsh`: `40c7451ecae69a32ad31a09b931c43d2ee15570efac83d6d59f9ed5f8771f238`

Primary sources:

- https://docs.oracle.com/en/java/javase/21/jshell/introduction-jshell.html
- https://docs.oracle.com/javase/tutorial/getStarted/cupojava/win32.html
