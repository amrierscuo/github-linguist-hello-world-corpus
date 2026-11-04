# #343 Jison Lex

Voce canonica `Jison Lex`, tipo `programming`, language_id `406395330`.

Generate a Jison Lex scanner and check tokens and lexeme of greeting.

## Toolchain and reproduction

Official Jison Lex lexer generator, jison-lex 0.3.4. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

official jison-lex 0.3.4 and Node.js 22.20.0. hello.jisonlex is a specific autonomous scanner, without parser grammar.

Comando/procedura from the directory of the example, unless explicit indications:

```text
npm install --prefix .tools jison-lex@0.3.4; node verify.cjs .tools
```

Expected result: correct Token/lexeme and PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The true scanner generates HELLO, COMMA, WORLD, BANG with the expected textual values; the reconstruction makes Hello, World!. A character produces INVALID. The distinct voice Jison also contains grammar.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/zaach/jison-lex](https://github.com/zaach/jison-lex)
- [https://github.com/zaach/jison](https://github.com/zaach/jison)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.jisonlex` | [hello.jisonlex](hello.jisonlex) verified |
