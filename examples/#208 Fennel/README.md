# #208 Fennel

Voce canonica `Fennel`, tipo `programming`, language_id `239946126`.

Fill out a Fennel program in Lua and concatenare/stampare the recipient.

## Toolchain and reproduction

Official Fennel compiler/interpreter CLI with Lua 5.4 — Fennel 1.6.0; Lua 5.4.6  Copyright (C) 1994-2023 Lua.org, PUC-Rio. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

Compiler/CLI Fennel official 1.6.0 and Lua 5.4.6. fennel-1.6.0 is the original compiler script, placed in an instrument directory external to the corpus.

Comando/procedura from the directory of the example, unless explicit indications:

```text
lua5.4 fennel-1.6.0 --compile hello.fnl; lua5.4 fennel-1.6.0 hello.fnl
```

Expected result: Successful Compilation; execution exit 0 and exact greeting.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The first invocation produces the real Lua compiled; the second one performs the same source with the authentic runtime.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://fennel-lang.org/](https://fennel-lang.org/)
- [https://fennel-lang.org/downloads/fennel-1.6.0](https://fennel-lang.org/downloads/fennel-1.6.0)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.fnl` | [hello.fnl](hello.fnl) verified |
