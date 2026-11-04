# #356 KerboScript

Voce canonica `KerboScript`, tipo `programming`, language_id `59716426`.

Run a KerboScript program that concatenates a variable and prints greetings on the kOS console.

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede Kerbal Space Program con il mod kOS e una CPU di bordo. Copiare il file nel volume disponibile. Il programma non pilota un veicolo o modifica controlli di volo.

Comando/procedura from the directory of the example, unless explicit indications:

```text
Nel terminale kOS di KSP: RUNPATH("hello.ks").
```

Expected result: Console kOS emette Hello, World!.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

SET/TO and PRINT with terminators. are KerboScript source. gioco/runtime is not available, so the flags remain hanging.

Remaining requirements:

- Kerbal Space Program with the kOS mod/runtime is not available.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://ksp-kos.github.io/KOS/language/variables.html](https://ksp-kos.github.io/KOS/language/variables.html)
- [https://ksp-kos.github.io/KOS/language/flow.html](https://ksp-kos.github.io/KOS/language/flow.html)
- [https://github.com/KSP-KOS/KOS](https://github.com/KSP-KOS/KOS)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ks` | [hello.ks](hello.ks) created; verification pending |
