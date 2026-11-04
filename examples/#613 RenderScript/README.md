# #613 RenderScript

Voce canonica `RenderScript`, tipo `programming`, language_id `323`.

Write greetings via rsDebug in a kernel/script Android RenderScript.

## Toolchain and reproduction

Required genuine llvm-rs-cc compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires historical toolchain Android RenderScript and rs_debug.rsh, Java package org.corpus.greeting.

Comando/procedura from the directory of the example, unless explicit indications:

```text
llvm-rs-cc -I /path/to/renderscript/include -o build hello.rs; caricare il relativo ScriptC_hello ed eseguire invoke_hello in un progetto Android compatibile.
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Sorgente originale con pragma version/java package e funzione hello. Toolchain storica e Android runtime non configurati.

Remaining requirements:

- Required llvm-rs-cc compiler/runtime and matching host resources are not available/configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://developer.android.com/guide/topics/renderscript/reference/rs_debug](https://developer.android.com/guide/topics/renderscript/reference/rs_debug)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rs` | [hello.rs](hello.rs), [main.rs](variants/rsh-e00ceaaf/main.rs) created; verification pending |
| `.rsh` | [hello.rsh](variants/rsh-e00ceaaf/hello.rsh) created; verification pending |
