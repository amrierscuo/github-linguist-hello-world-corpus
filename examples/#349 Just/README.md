# #349 Just

Voce canonica `Just`, tipo `programming`, language_id `128447695`.

Analyze a justfile and run the hello recipe with a explicitly declared Windows shell.

## Toolchain and reproduction

Official Just recipe parser and runner, just 1.58.0. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Just official 1.58.0 portable Windows x64. justfile configures windows-shell with powershell.exe -NoLogo -NoProfile -Command. The recipe does not change file or system.

Comando/procedura from the directory of the example, unless explicit indications:

```text
just --list; just hello
```

Expected result: Listed recipe; exit 0; exact greeting.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The real parser lists hello and the runner performs the original recipe. echo in the indicated shell produces stdout compared exactly.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://just.systems/man/en/](https://just.systems/man/en/)
- [https://github.com/casey/just](https://github.com/casey/just)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.just` | [hello.just](variants/just-45047af7/hello.just) created; verification pending |
