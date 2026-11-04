# 0337: JavaScript: `.jscad`

Role: OpenJSCAD: segments of the converted letters into path2 geometries.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Node.js 22.20.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
OpenJSCAD/modeling: caricare hello.jscad e chiamare main
```

Expected result: Hello, World! in log/valore/risposta or geometry according to the role; PAC returns DIRECT without network.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.jscad`: `4f65f03e95787496ce4454f3b553e4c642e3863d5374d0814f73e148e41daa6d`

Primary sources:

- https://openjscad.xyz/docs/module-modeling_text.html
- https://nodejs.org/api/console.html#consolelogdata-args
