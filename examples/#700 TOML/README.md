# #700 TOML

## Latest recorded verification

Latest extension checks:
- `.toml.example`: CPython tomllib: exact parsed configuration and language field. [Evidence](verification/native_20261104_followup_2e746f6d6c2e6578616d706c65.json).

Voce canonica `TOML`, tipo `data`, language_id `365`.

Decode an original TOML configuration with message and language.

## Toolchain and reproduction

Python standard-library TOML parser, 3.13.9. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python3.13.9 tomllib nativo.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The true parser reconstructs an exact typed map; the message field produces greeting.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://toml.io/en/v1.0.0](https://toml.io/en/v1.0.0)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.toml` | [hello.toml](hello.toml) verified |
| `.toml.example` | [hello.toml.example](variants/toml-example-35fdb380/hello.toml.example) syntax and behavior verified |