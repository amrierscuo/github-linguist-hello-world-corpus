# #832 templ

Generate Go from templ and make the original component.

## Toolchain

v0.3.1070; go version go1.27.1 windows/amd64

## Procedure

templ generate; go mod tidy; go mod verify; go run .

## Expected result

HTML rendered contains <h1> Hello, World! </h1>.

## Status

syntax and behavior verified.

CLI/generator and runtime templ original; name is passed as parameter. Go generated and binaries remain in work, go.sum comes from true resolution.

Real check 2026-10-08T13:49:00.064965+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://templ.guide/quick-start/creating-a-simple-templ-component/](https://templ.guide/quick-start/creating-a-simple-templ-component/)
- [https://github.com/a-h/templ/releases/tag/v0.3.1070](https://github.com/a-h/templ/releases/tag/v0.3.1070)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.templ` | [hello.templ](hello.templ) verified |
