# 0337: JavaScript: `.sjs`

Role: CommonJS JavaScript server module for compatible host; export value instead of imposing consoles.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Node.js 22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Host .sjs compatibile: importare hello.sjs e chiamare hello()
```

Expected result: Hello, World! in log/valore/risposta or geometry according to the role; PAC returns DIRECT without network.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.sjs`: `9358232ad0fd0753a9c25200d334bfa2017c8e402eef88537e5389fdf917ed08`

Primary sources:

- https://www.marklogic.com/
- https://nodejs.org/api/console.html#consolelogdata-args
