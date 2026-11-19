# #610 Redscript

## Verified on November 19, 2026

The actual compiler created a bundle from the original stand-alone function. The native decompiler read its compiled return instruction and recovered the exact greeting. Scope is the deterministic return value in emitted code.

Run `redscript-cli compile -s scripts -b greeting.redscripts && redscript-cli decompile -b greeting.redscripts -o result`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

[Earlier evidence](verification/native.json).

<details>
<summary>Earlier instructions and evidence</summary>

Voce canonica `Redscript`, tipo `programming`, language_id `686691365`.

Define an original Redscript function that returns the greeting string.

## Toolchain and reproduction

Required genuine redscript compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires compiler jac3km4/redscript and runtime/librerie of the compatible game.

Comando/procedura from the directory of the example, unless explicit indications:

```text
redscript compile con i sorgenti hello.reds e il cache bundle/script resources del proprio Cyberpunk 2077; invocare CorpusGreeting.hello() nel relativo host.
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Source function in the original module; compiler/runtime game not available. Do not deduce parsing from syntax similar to other languages.

Remaining requirements:

- Required redscript compiler/runtime and matching host resources are not available/configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://wiki.redmodding.org/redscript](https://wiki.redmodding.org/redscript)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.reds` | [hello.reds](hello.reds) Syntax and behavior verified |

</details>
