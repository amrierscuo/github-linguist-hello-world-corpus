# #345 Jsonnet

## Latest recorded verification

Latest extension checks:
- `.jsonnet`: The original Jsonnet C++ evaluator loaded and evaluated the exact source and its declared library import; emitted JSON contains the greeting value Hello, World!. [Evidence](verification/native_20261105_batch_2e6a736f6e6e6574.json).
- `.libsonnet`: The original Jsonnet C++ evaluator loaded and evaluated the exact source and its declared library import; emitted JSON contains the greeting value Hello, World!. [Evidence](verification/native_20261105_batch_2e6c6962736f6e6e6574.json).

Voce canonica `Jsonnet`, tipo `programming`, language_id `664885656`.

Evaluate a Jsonnet object with local binding and chained string.

## Toolchain and reproduction

Official Jsonnet C++ compiler/evaluator, Jsonnet commandline interpreter v0.20.0. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Jsonnet C++ 0.20.0 official from the Ubuntu package, extracted under work without global installation.

Comando/procedura from the directory of the example, unless explicit indications:

```text
jsonnet hello.jsonnet
```

Expected result: JSON exact { "message": "Hello, World!" }; exit 0.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The true assessor produces JSON; the verification reads that product and compares exactly the message field.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://jsonnet.org/learning/tutorial.html](https://jsonnet.org/learning/tutorial.html)
- [https://jsonnet.org/ref/spec.html](https://jsonnet.org/ref/spec.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.jsonnet` | [hello.jsonnet](hello.jsonnet), [driver.jsonnet](variants/libsonnet-cf82fe81/driver.jsonnet) syntax and behavior verified |
| `.libsonnet` | [hello.libsonnet](variants/libsonnet-cf82fe81/hello.libsonnet) syntax and behavior verified |