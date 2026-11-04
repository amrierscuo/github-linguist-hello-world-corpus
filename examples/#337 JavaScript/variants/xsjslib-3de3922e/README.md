# 0337: JavaScript: `.xsjslib`

Ruolo: Libreria SAP HANA XS classic esportabile con funzione greeting.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Node.js 22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
SAP HANA XS classic: importare la libreria e chiamare greeting()
```

Expected result: Hello, World! in log/valore/risposta or geometry according to the role; PAC returns DIRECT without network.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.xsjslib`: `781946f10e485a7dbb8a9b0b8b5d3fe4b610a05e113f1c6e789973eb107a6602`

Primary sources:

- https://help.sap.com/docs/PRODUCT_ID/52715f71adba4aaeb480d946c742d1f6/649ff83a7da04762a02e3dad8be01c8b.html
- https://nodejs.org/api/console.html#consolelogdata-args
