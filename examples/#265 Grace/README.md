# #265 Grace

Voce canonica `Grace`, tipo `programming`, language_id `135`.

Interpolate an unchangeable binding in Grace and print the result with the standard dialect.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

The self-hosted compiler generates JavaScript; fill in a work copy to store the clean source.

Comando/procedura from the directory of the example, unless explicit indications:

```text
minigrace-js hello.grace
```

Expected result: Filling and running the source produce Hello, World!.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The syntax of print without brackets and interpolation {name} follows Grace. The compiler and modules are not configured, so the flags remain false.

Remaining requirements:

- Minigrace compiler and standard dialect modules are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/gracelang/minigrace](https://github.com/gracelang/minigrace)
- [https://github.com/gracelang/language](https://github.com/gracelang/language)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.grace` | [hello.grace](hello.grace) created; verification pending |
