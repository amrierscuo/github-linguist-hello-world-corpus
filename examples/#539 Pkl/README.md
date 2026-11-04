# #539 Pkl

Voce canonica `Pkl`, tipo `programming`, language_id `288822799`.

Evaluate a Pkl configuration with interpolation string and serialize it in JSON.

## Toolchain and reproduction

Official Pkl Javascriptor, Pkl 0.32.1 (Windows 10.0, Java 21.0.12.1 ). Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Pkl Java CLI 0.32.1 official, checksum corresponding to the jpkl axis of the Apple release.

Comando/procedura from the directory of the example, unless explicit indications:

```text
java -jar /path/to/pkl-0.32.1.jar eval --format json hello.pkl
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The real evaluator reads Pkl and produces name/message with exact values. The Pickle format of the 0534 voice is distinct even if the extension coincides.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://pkl-lang.org/main/current/pkl-cli/index.html](https://pkl-lang.org/main/current/pkl-cli/index.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pkl` | [hello.pkl](hello.pkl) verified |
