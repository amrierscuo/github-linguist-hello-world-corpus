# #528 Parrot Internal Representation

Voce canonica `Parrot Internal Representation`, tipo `programming`, language_id `280`.

Perform a main PIR with local binding and concatenation via print/say.

## Toolchain and reproduction

Required genuine compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

It requires Parrot VM with frontend PIR.

Comando/procedura from the directory of the example, unless explicit indications:

```text
parrot hello.pir
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

La subroutine:main è originale; interpreter unavailable. PIR usa dichiarazioni e astrazioni proprie rispetto a PASM.

Remaining requirements:

- Required parrot compiler/interpreter and matching host libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://parrot.github.io/html/docs/user/pir/intro.pod.html](https://parrot.github.io/html/docs/user/pir/intro.pod.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pir` | [hello.pir](hello.pir) created; verification pending |
