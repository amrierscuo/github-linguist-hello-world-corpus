# #564 Pug

Render a Pug page with interpolation and escaping.

## Toolchain

Pug 3.0.4; Node.js v22.20.0

## Procedure

npm install pug; node verify.cjs

## Expected result

Hello, World!

## Status

syntax and behavior verified.

The original Pug compiler produces HTML and the checker controls the greeting node and the excavating of the name.

Real check 2026-10-08T13:16:51.001660+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://pugjs.org/api/getting-started.html](https://pugjs.org/api/getting-started.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.jade` | [hello.jade](variants/jade-6d41832d/hello.jade) created; verification pending |
| `.pug` | [hello.pug](hello.pug) verified |
