# #617 Ring

## Latest recorded verification

**Syntax and behavior verified** on November 5, 2026.

The official Ring1.27 console VM compiled the unchanged source and executed see/concatenation, emitting the exact greeting and LF. Only ANSI-C language/VM/standard-function sources were built; no GUI extensions, IDE or system installation.

[Native commands, versions, outputs and SHA-256](verification/native_20261105_target546_main.json). [Earlier evidence](verification/native.json).

Current native command or procedure: `ring hello.ring`.

## Extension results

- `.ring`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Voce canonica `Ring`, tipo `programming`, language_id `431`.

Run a Ring program with see and concatenation.

## Toolchain and reproduction

Required genuine ring compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires official ring and compatible librerie/runtime.

Comando/procedura from the directory of the example, unless explicit indications:

```text
ring hello.ring
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Programma originale; interpreter non configurato.

Remaining requirements:

- Required ring compiler/runtime and matching host resources are not available/configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://ring-lang.github.io/doc1.25/introduction.html](https://ring-lang.github.io/doc1.25/introduction.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ring` | [hello.ring](hello.ring) syntax and behavior verified |

</details>
