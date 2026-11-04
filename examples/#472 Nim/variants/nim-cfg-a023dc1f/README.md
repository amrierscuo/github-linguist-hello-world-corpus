# 0472: Nim: `.nim.cfg`

Role: Nim compiler options, not a Nim program.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Nim1.6.14 Ubuntu, backend C/GCC. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
nim c --out:build/hello hello.nim; ./build/hello (Nim carica hello.nim.cfg associato)
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.nim`: `076562c4b011aa8f2efd2cbc2dc88d3afb525f4e5666e8e97ccbe7c94315c002`
- `hello.nim.cfg`: `06851203890f5cddb3ccafc38ddbe8b28c3bd825ec38fb5b8ce5725667ea0619`

Primary sources:

- https://nim-lang.org/docs/nimc.html#compiler-usage-configuration-files
- https://nim-lang.org/docs/tut1.html
