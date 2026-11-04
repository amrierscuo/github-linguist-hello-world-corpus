# 0337: JavaScript: `.xsjs`

Role: Endpoint SAP HANA XS classic with greeting response.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Node.js 22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
SAP HANA XS classic: attivare solo in progetto di test e richiedere endpoint locale
```

Expected result: Hello, World! in log/valore/risposta or geometry according to the role; PAC returns DIRECT without network.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.xsjs`: `934c760c40e8274a936ddad214fafe5f6aba4e3cef87b77ffbef148d61da4f2d`

Primary sources:

- https://help.sap.com/doc/3de842783af24336b6305a3c0223a369/2.0.05/en-US/%24.web.Body.html
- https://nodejs.org/api/console.html#consolelogdata-args
