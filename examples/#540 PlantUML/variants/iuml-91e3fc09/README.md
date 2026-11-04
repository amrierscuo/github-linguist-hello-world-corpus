# 0540: PlantUML: `.iuml`

Role: Includes PlantUML with greeting variable definition, separate diagram driver.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Official PlantUML MIT Light sequence-diagram parser/renderer, PlantUML version 1.2026.8 / 149874a [2026-09-05 15:59:17 UTC]. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
java -jar plantuml.jar -tsvg driver.puml
```

Expected result: Label Hello, World! in SVG

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `driver.puml`: `25772e482c8bcabb40472dc44ba271903534187c0b00fd9039deb5caff5abee1`
- `hello.iuml`: `bf5a6ae4fb7487d784bf3f88a4f78024a4167a0cc68aa9ec84ff883b1decaeea`

Primary sources:

- https://plantuml.com/preprocessing
- https://plantuml.com/sequence-diagram
