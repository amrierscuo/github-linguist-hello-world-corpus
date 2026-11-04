# 0337: JavaScript: `.jsm`

Ruolo: Modulo Mozilla JSM legacy con export dichiarato; nessun console.log top-level.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Node.js 22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Firefox legacy compatibile: importare il modulo JSM e leggere greeting
```

Expected result: Hello, World! in log/valore/risposta or geometry according to the role; PAC returns DIRECT without network.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.jsm`: `2fe55cf92a1eca85af71e6940601cc9dea7409fa2b2df50708c8ac0c3c16b4a4`

Primary sources:

- https://firefox-source-docs.mozilla.org/dom/scriptloader/jsm_importer.html
- https://nodejs.org/api/console.html#consolelogdata-args
