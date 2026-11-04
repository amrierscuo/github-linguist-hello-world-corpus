# #540 PlantUML

Voce canonica `PlantUML`, tipo `data`, language_id `833504686`.

Render a PlantUML sequence diagram with greeting on the message.

## Toolchain and reproduction

Official PlantUML MIT Light sequence-diagram parser/renderer — PlantUML version 1.2026.8 / 149874a [2026-09-05 15:59:17 UTC]. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

PlantUML 1.2026.8 MIT Official Light and Java 21; sequence does not require Graphviz for rendering.

Comando/procedura from the directory of the example, unless explicit indications:

```text
java -jar /path/to/plantuml-1.2026.8.jar -tsvg hello.puml
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The real maker produces SVG and the verification reads the node text of the arrow, with Hello, World! exact. SVG compiled remains in work.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://plantuml.com/sequence-diagram](https://plantuml.com/sequence-diagram)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.puml` | [hello.puml](hello.puml), [driver.puml](variants/iuml-91e3fc09/driver.puml) created; verification pending |
| `.iuml` | [hello.iuml](variants/iuml-91e3fc09/hello.iuml) created; verification pending |
| `.plantuml` | [hello.plantuml](variants/plantuml-b52e863a/hello.plantuml) created; verification pending |
