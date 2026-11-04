# 0485: OCaml: `.eliom`

Role: Module Eliom server/client delimited: server-side function without starting network.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: OCaml 4.14.1. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Eliom originale con ppx_eliom: compilare il modulo lato server
```

Expected result: Hello, World! in the local server log

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.eliom`: `35c4d4d155d8ba4273d15f2480275c54c5741f160cfa881064b09792a55224f7`

Primary sources:

- https://ocsigen.org/eliom/latest/manual/clientserver-language
- https://ocaml.org/manual/5.4/programs.html
