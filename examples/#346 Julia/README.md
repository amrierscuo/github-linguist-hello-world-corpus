# #346 Julia

Voce canonica `Julia`, tipo `programming`, language_id `184`.

Perform a Julia source that concatenates greeting through the topics of println.

## Toolchain and reproduction

Official Julia native runtime, julia version 1.13.1. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Julia ufficiale portable 1.13.1 Windows x64. L’archivio è verificato contro SHA-256 del versions.json ufficiale. JULIA_DEPOT_PATH è isolata nella directory di lavoro.

Comando/procedura from the directory of the example, unless explicit indications:

```text
julia --startup-file=no --history-file=no hello.jl
```

Exit 0; exact greeting followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Il runtime nativo legge ed esegue il vero sorgente .jl e stdout viene confrontato esattamente. La voce Julia REPL registra separatamente prompt e visualizzazione interattiva.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://docs.julialang.org/en/v1/manual/command-line-interface/](https://docs.julialang.org/en/v1/manual/command-line-interface/)
- [https://docs.julialang.org/en/v1/manual/strings/](https://docs.julialang.org/en/v1/manual/strings/)
- [https://julialang-s3.julialang.org/bin/versions.json](https://julialang-s3.julialang.org/bin/versions.json)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.jl` | [hello.jl](hello.jl) verified |
