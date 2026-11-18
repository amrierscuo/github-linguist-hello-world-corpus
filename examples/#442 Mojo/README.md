# #442 Mojo

## Verified on November 18, 2026

The official Mojo runtime evaluated the entry point after updating its declaration to def for this compiler and printed the exact greeting.

Run `mojo hello.mojo`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

[Earlier evidence](verification/native.json).

[Prior attempt](verification/native_20261118_wave736_prior_attempt.json).

<details>
<summary>Earlier instructions and evidence</summary>

Voce canonica `Mojo`, tipo `programming`, language_id `1045019587`.

Print greeting from the main fn entry point of Mojo.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires official Modular Mojo distribution with compatible runtime.

Comando/procedura from the directory of the example, unless explicit indications:

```text
mojo hello.mojo
```

Expected result: Hello, World!

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Original source; compiler/runtime not configured.

Remaining requirements:

- Mojo compiler/runtime is not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://docs.modular.com/mojo/manual/basics](https://docs.modular.com/mojo/manual/basics)
- [https://docs.modular.com/mojo/quickstart](https://docs.modular.com/mojo/quickstart)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mojo` | [hello.mojo](hello.mojo) Syntax and behavior verified |

</details>
