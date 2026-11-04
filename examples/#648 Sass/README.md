# #648 Sass

Fill Sass indented in CSS with greeting in the generated content.

## Toolchain

Dart Sass 1.105.1; Node.js22.20.0; Chrome154.0.8037.98

## Procedure

npm install sass; node verify.cjs build/hello.css; copy verify.html in build and open it with Chrome; date-pass must be true

## Expected result

CSS generated contains #greeting::before and content: "Hello, World!".

## Status

syntax and behavior verified.

Original Dart Sass compiler and verification of the content generated in the true CSS Chromium engine; CSS/profilo browser remain in work.

Real check 2026-10-08T13:24:10.648526+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://sass-lang.com/documentation/syntax/](https://sass-lang.com/documentation/syntax/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sass` | [hello.sass](hello.sass) verified |
