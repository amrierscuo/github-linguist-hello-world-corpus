# #175 EBNF

Define a EBNF grammar that recognizes Hello, World! and rejects Hello, Moon!.

## Toolchain

Node.js v22.20.0; ebnf 1.9.1

## Commands and procedure

npm install; node check.cjs

## Expected result

Completed Grammar; AST Greeting with exact text; different input refused.

## Status

syntax and behavior verified.

The chosen dialect is W3C EBNF, with:= and concatenation of literals; it is not ISO EBNF. The authentic grammarian compiler ebnf generates the parser and applies the productions to the text.

Actual verification of 2026-10-08T11:56:13.607325+00:00 on Windows x64: [log](verification/result.json).
Hash of sorgenti/checker, real versions and commands, output codes, stdout/stderr and test limits are in the log.

## Primary sources and format reference

- [https://www.w3.org/TR/xquery-31/#EBNFNotation](https://www.w3.org/TR/xquery-31/#EBNFNotation)
- [https://github.com/lys-lang/node-ebnf](https://github.com/lys-lang/node-ebnf)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ebnf` | [hello.ebnf](hello.ebnf) verified |
