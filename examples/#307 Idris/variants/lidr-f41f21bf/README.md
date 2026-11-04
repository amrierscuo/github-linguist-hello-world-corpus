# 0307: Idris: `.lidr`

Ruolo: Sorgente Idris literate in stile Bird: codice preceduto da >.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Idris; scegliere/registrare una versione compatibile con .idr. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
idris hello.lidr -o hello; ./hello
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.lidr`: `de05f69112435185e1513371061d8ec0fd732209d7264f1e341d243960372b70`

Primary sources:

- https://docs.idris-lang.org/en/latest/tutorial/miscellany.html#literate-programming
- https://docs.idris-lang.org/en/latest/tutorial/introduction.html
- https://docs.idris-lang.org/en/latest/tutorial/starting.html
