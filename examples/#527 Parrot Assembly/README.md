# #527 Parrot Assembly

Voce canonica `Parrot Assembly`, tipo `programming`, language_id `279`.

Perform PASM instructions that set the string log and invoke print.

## Toolchain and reproduction

Required genuine compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

It requires Parrot VM with frontend PASM.

Comando/procedura from the directory of the example, unless explicit indications:

```text
parrot hello.pasm
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Sorgente assembly originale; interpreter non configurato. L’estensione .pasm distingue l’assembly dalla voce generica e dal PIR.

Remaining requirements:

- Required parrot compiler/interpreter and matching host libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://parrot.github.io/html/docs/user/pasm/index.pod.html](https://parrot.github.io/html/docs/user/pasm/index.pod.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pasm` | [hello.pasm](hello.pasm) created; verification pending |
