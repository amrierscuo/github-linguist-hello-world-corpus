# 0558: Prolog: `.yap`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#558 Prolog/hello.pl.

Required toolchain: SWI-Prolog9.0.4 ufficiale Ubuntu. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.yap; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Hello, World! followed by newline; exit0.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.yap`: `087467ce1818250c527ca4d9e1e9e661dd740297135a4c1d59e6536a0f74f3c0`

Primary sources:

- https://www.swi-prolog.org/pldoc/doc_for?object=atomic_list_concat/2
- https://www.swi-prolog.org/pldoc/doc_for?object=initialization/2
