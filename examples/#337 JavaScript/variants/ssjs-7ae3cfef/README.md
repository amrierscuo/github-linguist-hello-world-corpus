# 0337: JavaScript: `.ssjs`

Ruolo: Marketing Cloud SSJS con funzione host Write.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Node.js 22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Marketing Cloud SSJS: eseguire hello.ssjs in contenuto di test
```

Expected result: Hello, World! in log/valore/risposta or geometry according to the role; PAC returns DIRECT without network.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.ssjs`: `5f6705ea8cd589e45b1d91b4fdca9f63dc9d48b0a9c2b5135f978d818fbe0454`

Primary sources:

- https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/ssjs_utilitiesWrite.html
- https://nodejs.org/api/console.html#consolelogdata-args
