# #775 Wolfram Language

Voce canonica `Wolfram Language`, tipo `programming`, language_id `224`.

Original Wolfram Language Expressions that assign the recipient, make up the string with StringJoin and print it with Print.

## Toolchain and reproduction

Mathics3 (compatible Wolfram Language evaluator) — Mathics3 10.0.1; Running on win32 CPython 3.13.9 | packaged by Anaconda, Inc. | (main, Oct 21 2025, 19:09:58) [MSC v.1929 64 bit (AMD64)]; using SymPy 1.14.0, mpmath 1.3.0, numpy 2.3.5, cython Not installed, scipy 1.16.3, skimage 0.25.2. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python 3.13.9 and Mathics3 10.0.1, Mathics3-Scanner 10.0.1, SymPy 1.14.0; install Mathics3 dependencies in an isolated environment. The driver initializes the builtin and the original engine session.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python verify.py
```

Expected result: Hello, World! from the output Print and PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Il sorgente .wl è interpretato realmente da Mathics3, motore open source compatibile con questo sottoinsieme Wolfram Language. Il driver controlla l’output Print della sessione. Non viene dichiarata una verifica con Wolfram Kernel proprietario.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://reference.wolfram.com/language/ref/Print.html](https://reference.wolfram.com/language/ref/Print.html)
- [https://reference.wolfram.com/language/ref/StringJoin.html](https://reference.wolfram.com/language/ref/StringJoin.html)
- [https://mathics.org/](https://mathics.org/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mathematica` | [hello.mathematica](variants/mathematica-ce2c0b75/hello.mathematica) created; verification pending |
| `.cdf` | [hello.cdf](variants/cdf-cfab4dd6/hello.cdf) created; verification pending |
| `.m` | [hello.m](variants/m-f7140aa0/hello.m) created; verification pending |
| `.ma` | [hello.ma](variants/ma-bf225f29/hello.ma) created; verification pending |
| `.mt` | [hello.mt](variants/mt-d80ef8fe/hello.mt) created; verification pending |
| `.nb` | [hello.nb](variants/nb-af372417/hello.nb) created; verification pending |
| `.nbp` | artefatto da generare Formato Wolfram Player/proprietario: richiede un export/conversione reale del frontend compatibile. Non viene rinominato il codice .wl come documento serializzato. |
| `.wl` | [hello.wl](hello.wl) verified |
| `.wls` | [hello.wls](variants/wls-852bcca4/hello.wls) created; verification pending |
| `.wlt` | [hello.wlt](variants/wlt-5420c4e1/hello.wlt) created; verification pending |
