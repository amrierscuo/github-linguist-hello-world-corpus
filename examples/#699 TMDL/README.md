# #699 TMDL

Voce canonica `TMDL`, tipo `data`, language_id `769162295`.

Describe a tabular TMDL model with an original DAX size that returns greeting.

## Toolchain and reproduction

Required genuine Microsoft.AnalysisServices.Tabular TmdlSerializer compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires Microsoft.AnalysisServices.Tabular TOM/TmdlSerializer and tabular engine for DAX.

Comando/procedura from the directory of the example, unless explicit indications:

```text
TmdlSerializer.DeserializeModelFromFolder(directory); in un motore tabulare compatibile valutare la misura Greeting[Hello].
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Model and table original sources; parser/engine not available. No Power BI service or remote account required for future local verification.

Remaining requirements:

- Required Microsoft.AnalysisServices.Tabular TmdlSerializer toolchain and matching execution/format resources are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://learn.microsoft.com/en-us/analysis-services/tmdl/tmdl-overview?view=asallproducts-allversions](https://learn.microsoft.com/en-us/analysis-services/tmdl/tmdl-overview?view=asallproducts-allversions)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.tmdl` | [model.tmdl](model.tmdl), [Greeting.tmdl](tables/Greeting.tmdl) created; verification pending |
