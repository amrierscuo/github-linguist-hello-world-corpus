# 0468: NewLisp: `.lisp`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#468 NewLisp/hello.nl.

Required toolchain: newLISP10.7.5 Linux ufficiale Ubuntu. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.lisp; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: Hello, World! followed by newline; exit0.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.lisp`: `5fd420fcf931cfee86b0d3736f9b709ec15b8c07e22e4ca9220c5d7d04e34d10`

Primary sources:

- https://www.newlisp.org/downloads/newlisp_manual.html
