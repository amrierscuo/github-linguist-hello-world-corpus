# 0337: JavaScript: `.jsfl`

Ruolo: Script Adobe Animate JSFL; log tramite host fl.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Node.js 22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Adobe Animate: eseguire hello.jsfl come command
```

Expected result: Hello, World! in log/valore/risposta or geometry according to the role; PAC returns DIRECT without network.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.jsfl`: `156978da52aa831d15d70f73aa03ac4d8323ddc148c028bcb6ef95338aef40c3`

Primary sources:

- https://help.adobe.com/en_US/flash/cs/extend/flash_cs5_extending.pdf
- https://nodejs.org/api/console.html#consolelogdata-args
