# #682 Starlark

Voce canonica `Starlark`, tipo `programming`, language_id `960266174`.

Evaluate a parametric Starlark function and control print and Reader.

## Toolchain and reproduction

Authentic Google Starlark Go Evaluationor, go.starlark.net v0.0.0-20261005163335-bcb1a1a55bf9; go version go1.27.1 windows/amd64. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Google Starlark Go implementation original, exact version in go.mod / go.sum; official go 1.27.1.

Comando/procedura from the directory of the example, unless explicit indications:

```text
go run verify.go hello.star
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

ExecFile compila/esegue the real file; starlark.Call invokes greet with Reader and verify the value. Cache/build are in work.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/google/starlark-go](https://github.com/google/starlark-go)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bzl` | [hello.bzl](variants/bzl-54e0179a/hello.bzl) created; verification pending |
| `.star` | [hello.star](hello.star) verified |
