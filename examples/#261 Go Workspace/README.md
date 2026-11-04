# #261 Go Workspace

Voce canonica `Go Workspace`, tipo `data`, language_id `934546256`.

Define a workspace Go with two local modules: app import greeting and print the result.

## Toolchain and reproduction

Official Go toolchain workspace loader and compiler, go version go1.27.1 windows/amd64. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Go 1.27.1 portable Windows x64. go.work elenca app e greeting; app richiede example.org/corpus/greeting v0.0.0. Il workspace risolve quella dipendenza alla directory locale. La prova usa GOPROXY=off, GOSUMDB=off, GOTOOLCHAIN=local e cache sotto work.

Comando/procedura from the directory of the example, unless explicit indications:

```text
go work edit -json; go run ./app
```

Expected result: Workspace with two Uses; exit program 0 and exact stdout Hello, World!.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The true loader Go analyzes go.work and the compiler builds both modules before the execution. No replace or downloaded module is necessary.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://go.dev/doc/tutorial/workspaces](https://go.dev/doc/tutorial/workspaces)
- [https://go.dev/ref/mod#workspaces](https://go.dev/ref/mod#workspaces)
