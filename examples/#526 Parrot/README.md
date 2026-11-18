# #526 Parrot

## Verified on November 18, 2026

The original PASM bytes were staged with the suffix selected by the Parrot VM. The native VM used the assembler frontend and the unchanged program emitted the exact greeting.

Run `cp hello.parrot hello.pasm; parrot hello.pasm`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

[Earlier evidence](verification/native.json).

<details>
<summary>Earlier instructions and evidence</summary>

Voce canonica `Parrot`, tipo `programming`, language_id `278`.

Provide an original input to the generic VM Parrot and print the greeting.

## Toolchain and reproduction

Required genuine compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Parrot and frontend PASM. The .parrot file is source text in assembly format, explicitly selected with -a; it is not invented bytecode.

Comando/procedura from the directory of the example, unless explicit indications:

```text
parrot -a hello.parrot
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Parrot is the VM common to PASM and PIR voices; this generic voice uses its canonical extension with a selection of the frontend. Toolchain absent, both flag pending.

Remaining requirements:

- Required parrot compiler/interpreter and matching host libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://parrot.github.io/html/docs/intro.pod.html](https://parrot.github.io/html/docs/intro.pod.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.parrot` | [hello.parrot](hello.parrot) Syntax and behavior verified |

</details>
