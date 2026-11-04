# #618 Riot

Voce canonica `Riot`, tipo `markup`, language_id `878396783`.

Fill and make a parameter Riot component.

## Toolchain and reproduction

Official Riot component compiler and official SSR runtime, 9.4.6 / SSR 9. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Compiler Riot 9.4.6 and SSR official 9, precise versions in the log; Node 22.20.0.

Comando/procedura from the directory of the example, unless explicit indications:

```text
npm install --prefix .tools @riotjs/compiler@9.4.6 @riotjs/ssr@9; node verify.cjs .tools build
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Il vero compiler emette ESM, SSR monta/rende World e Reader con il risultato p esatto. Il goal verificato eÌ€ server rendering; nessun browser richiesto.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://riot.js.org/compiler/](https://riot.js.org/compiler/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.riot` | [corpus-greeting.riot](corpus-greeting.riot) verified |
