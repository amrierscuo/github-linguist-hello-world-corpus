# 0337: JavaScript: `.gs`

Ruolo: Google Apps Script, routine esplicita hello e Logger.log.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Node.js 22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Eseguire hello nell’editor Apps Script; leggere log locale del progetto
```

Expected result: Hello, World! in log/valore/risposta or geometry according to the role; PAC returns DIRECT without network.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.gs`: `0a0249c44cde6bd323ba20a7e9e04f4950bebea75064fcff5ace476ad3181f92`

Primary sources:

- https://developers.google.com/apps-script/reference/base/logger
- https://nodejs.org/api/console.html#consolelogdata-args
