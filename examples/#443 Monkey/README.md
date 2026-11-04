# #443 Monkey

Voce canonica `Monkey`, tipo `programming`, language_id `236`.

Run Main with Print in the original Monkey X language.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires Monkey X transcc and backend StdCpp/C++ of the same distribution.

Comando/procedura from the directory of the example, unless explicit indications:

```text
transcc -target=StdCpp -run hello.monkey
```

Expected result: Hello, World!

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Monkey X and Monkey C are distinct voices; the program uses Strict, Main:Int and Print. Toolchain absent.

Remaining requirements:

- Monkey X transcc compiler/backend is not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/blitz-research/monkey](https://github.com/blitz-research/monkey)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.monkey` | [hello.monkey](hello.monkey) created; verification pending |
| `.monkey2` | [hello.monkey2](variants/monkey2-f16dc421/hello.monkey2) created; verification pending |
