# 0472: Nim: `.nimrod`

Role: Historical name of the Nimrod source, same syntactic subset echo/let of the Nim program; contemporary loader may require .nim.

Origin: Byte-identical copy of the original corpus source: examples/#472 Nim/hello.nim.

Required toolchain: Nim1.6.14 Ubuntu, backend C/GCC. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Copiare il sorgente in build/hello.nim; nim c -r build/hello.nim
```

Expected result: Hello, World! followed by newline; exit0.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.nimrod`: `46f0e4621c8b9d1c31674c7086f534c6a673f52a940dfbea1c9bc168f14a494f`

Primary sources:

- https://nim-lang.org/docs/tut1.html
