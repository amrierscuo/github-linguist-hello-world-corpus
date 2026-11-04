# 0337: JavaScript: `.jake`

Role: Jake Task DSL, not main JavaScript generic.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Node.js 22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
jake -f hello.jake hello
```

Expected result: Hello, World! in log/valore/risposta or geometry according to the role; PAC returns DIRECT without network.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.jake`: `dfdc8e6f6117faa5f8b3e8df876bf2e2c573aded23959c5797e8a6937e2ec99e`

Primary sources:

- https://jakejs.com/
- https://nodejs.org/api/console.html#consolelogdata-args
