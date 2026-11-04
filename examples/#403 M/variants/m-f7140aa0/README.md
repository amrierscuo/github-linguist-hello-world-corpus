# 0403: M: `.m`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#403 M/hello.mumps.

Required toolchain: YottaDB o GT.M con routine M abilitata. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.m; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: stdout Hello, World! and LF.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.m`: `a81e922a3255f5fc417d51cccd5a5748f19bc14fdbb4df8440dcee68c9a9ea39`

Primary sources:

- https://docs.yottadb.com/ProgrammersGuide/langfeat.html
