# 0540: PlantUML: `.plantuml`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#540 PlantUML/hello.puml.

Required toolchain: Official PlantUML MIT Light sequence-diagram parser/renderer, PlantUML version 1.2026.8 / 149874a [2026-09-05 15:59:17 UTC]. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.plantuml; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.plantuml`: `2bf9c506da220ed07b52a992b480af135eb7f9852dde165255630713d602f75f`

Primary sources:

- https://plantuml.com/sequence-diagram
