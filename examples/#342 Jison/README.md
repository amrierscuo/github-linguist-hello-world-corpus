# #342 Jison

Voce canonica `Jison`, tipo `programming`, language_id `284531423`.

Generate a Jison parser for a small greeting grammar and try it on valid and invalid inputs.

## Toolchain and reproduction

Official Jison grammar compiler/parser generator, jison 0.4.18. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Jison 0.4.18 and Node.js 22.20.0. hello.jison includes scanners, start symbol and behavior action; the generated JavaScript remains in build.

Comando/procedura from the directory of the example, unless explicit indications:

```text
npm install --prefix .tools jison@0.4.18; node verify.cjs .tools build
```

Expected result: Parser generated; accettati/rifiutati input as expected; Hello, World! result.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The authentic generator compiles the grammar and the parser really generated Hello, World! law, a variant with spaces and refuses Reader.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/zaach/jison](https://github.com/zaach/jison)
- [https://gerhobbelt.github.io/jison/docs/](https://gerhobbelt.github.io/jison/docs/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.jison` | [hello.jison](hello.jison) verified |
