# #601 ReScript

Voce canonica `ReScript`, tipo `programming`, language_id `501875647`.

Fill ReScript with local binding and Js.log, then run the genuine JavaScript.

## Toolchain and reproduction

Original BuckleScript ReScript/Reason compiler with standard library, BuckleScript 9.0.2 (Using OCaml: 4.06.1+BS ). Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

BuckleScript/ReScript 9.0.2 autentico con libreria OCaml della stessa distribuzione. Progetto bsconfig.json originale.

Comando/procedura from the directory of the example, unless explicit indications:

```text
bsc -I /path/to/bs-platform/lib/ocaml -bs-package-name corpus-greeting -bs-package-output commonjs:. -o Hello.cmj Hello.res; node Hello.js
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Il frontend .res autentico compila in JS, eseguito da Node. La prova usa il binario Linux con cwd di progetto per la risoluzione bsconfig.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://rescript-lang.org/docs/manual/v9.0.0/overview](https://rescript-lang.org/docs/manual/v9.0.0/overview)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.res` | [Hello.res](Hello.res), [Hello.res](variants/resi-1bac9c18/Hello.res) created; verification pending |
| `.resi` | [Hello.resi](variants/resi-1bac9c18/Hello.resi) created; verification pending |
