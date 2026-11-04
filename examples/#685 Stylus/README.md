# #685 Stylus

Voce canonica `Stylus`, tipo `markup`, language_id `359`.

Fill Stylus in a CSS content rule that contains greeting.

## Toolchain and reproduction

Official stylus compiler/parser, 0.64.0. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Compiler Stylus 0.64.0 autentico.

Comando/procedura from the directory of the example, unless explicit indications:

```text
npm install --prefix .tools stylus@0.64.0; node verify.cjs .tools build
```

Expected result: Hello, World! in the conformed result, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The generated CSS contains correct selector and content. Semantic ambition: CSS generation, not browser display.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://stylus-lang.com/docs/](https://stylus-lang.com/docs/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.styl` | [hello.styl](hello.styl) verified |
