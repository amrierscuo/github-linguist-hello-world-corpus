# #350 KCL

Voce canonica `KCL`, tipo `programming`, language_id `1052003890`.

Define a KCL scheme with typified attributes and evaluate a configuration that interpolates name.

## Toolchain and reproduction

Official KCL configuration language compiler/evaluator, kcl version 0.13.0-windows-amd64. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

CLI KCL official 0.13.0 portable Windows x64 from kcl-lang/cli. repository This is KCL of kcl-lang, CNCF configuration language.

Comando/procedura from the directory of the example, unless explicit indications:

```text
kcl run hello.k
```

Expected result: Configuration evaluated with the two exact attributes; exit 0.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The authentic compiler controls diagram and types and produces YAML with greeting.name =World and greeting.message = Hello, World!. An existing YAML reader only serves to compare the product of true KCL execution.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.kcl-lang.io/docs/reference/lang/spec/schema](https://www.kcl-lang.io/docs/reference/lang/spec/schema)
- [https://github.com/kcl-lang/cli](https://github.com/kcl-lang/cli)
- [https://www.kcl-lang.io/](https://www.kcl-lang.io/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.k` | [hello.k](hello.k) verified |
