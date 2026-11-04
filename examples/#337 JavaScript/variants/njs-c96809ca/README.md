# 0337: JavaScript: `.njs`

Role: Nginx njs module exporting handler HTTP; use only loopback if executed.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Node.js 22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
njs -c o nginx -t con js_import hello.njs; chiamare handler solo su 127.0.0.1 e arrestare server
```

Expected result: Hello, World! in log/valore/risposta or geometry according to the role; PAC returns DIRECT without network.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.njs`: `4559a47913cb7303394866afd2679e82699081d7fc29b704a7535e944fe574da`

Primary sources:

- https://nginx.org/en/docs/njs/
- https://nodejs.org/api/console.html#consolelogdata-args
