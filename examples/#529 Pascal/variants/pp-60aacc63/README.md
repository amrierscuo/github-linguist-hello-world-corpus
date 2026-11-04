# 0529: Pascal: `.pp`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#529 Pascal/hello.pas.

Required toolchain: Genuine Free Pascal compiler, 3.2.2. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.pp; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.pp`: `61390bec262f49020edd581463d7747ae45794775aeab6fad686b6241c28f082`

Primary sources:

- https://www.freepascal.org/docs.html
