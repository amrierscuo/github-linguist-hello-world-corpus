# 0485: OCaml: `.eliomi`

Ruolo: Interfaccia Eliom lato server; implementazione corrispondente inclusa.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: OCaml 4.14.1. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Eliom originale: compilare greeting.eliomi e greeting.eliom lato server
```

Expected result: Server interface with greeting string

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `greeting.eliom`: `c8aec92538be01f759c17a68e8eafe4cffec465ccb682b8c2da08204b53dc3ef`
- `greeting.eliomi`: `9a65e001a8ddb6bff30297a3bb312f4aac0c4dd4913170e2fbc5edb1429fb058`

Primary sources:

- https://ocsigen.org/eliom/latest/manual/clientserver-language
- https://ocaml.org/manual/5.4/programs.html
