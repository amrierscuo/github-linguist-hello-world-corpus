# 0364: Kotlin: `.kts`

Role: Kotlin Script with top-level instructions; not main function not invoked.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Kotlin2.4.21, OpenJDK21 Microsoft. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
kotlinc -script hello.kts
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.kts`: `f80efc3925d937e1d8b2cacbfbd6f830a2778b5ca4ff31f2caa8782723861c95`

Primary sources:

- https://kotlinlang.org/docs/command-line.html
- https://github.com/JetBrains/kotlin/releases/tag/v2.4.21
