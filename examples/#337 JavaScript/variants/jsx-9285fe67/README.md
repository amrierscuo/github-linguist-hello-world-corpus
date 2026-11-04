# 0337: JavaScript: `.jsx`

Role: Script Adobe ExtendScript .jsx: JavaScript without JSX React, greeting dialogue.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Node.js 22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Host Adobe ExtendScript compatibile: eseguire hello.jsx
```

Expected result: Hello, World! in log/valore/risposta or geometry according to the role; PAC returns DIRECT without network.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.jsx`: `4cedb4294e19952cef51dfd2e310dfa71e0acd702ed27c5ad73dc2544afcc6c2`

Primary sources:

- https://extendscript.docsforadobe.dev/
- https://nodejs.org/api/console.html#consolelogdata-args
