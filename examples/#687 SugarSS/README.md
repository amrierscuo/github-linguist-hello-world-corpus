# #687 SugarSS

Voce canonica `SugarSS`, tipo `markup`, language_id `826404698`.

Leggere SugarSS e serializzare la dichiarazione content in CSS.

## Toolchain and reproduction

Official sugarss compiler/parser, 5.0.2. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Parser SugarSS e PostCSS originali, versioni loggate.

Comando/procedura from the directory of the example, unless explicit indications:

```text
npm install --prefix .tools sugarss postcss; node verify.cjs .tools build
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The authentic parser produces a AST content declaration with exact value; PostCSS serializes CSS valid. Scope: modello/stile compiled.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/postcss/sugarss](https://github.com/postcss/sugarss)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sss` | [hello.sss](hello.sss) verified |
