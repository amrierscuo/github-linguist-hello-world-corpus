# 0414: MUF: `.m`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#414 MUF/hello.muf.

Required toolchain: Fuzzball MUCK con compilatore/interprete MUF. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.m; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: compiled program; the user who performs it receives Hello, World!.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.m`: `fca9bc311b87a87fd9e8a0733cd22a9603816483aec68f307287a2cb0ec36f2b`

Primary sources:

- https://www.fuzzball.org/docs/mufman.html
