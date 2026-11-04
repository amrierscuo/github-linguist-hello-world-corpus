# #169 Dogescript

Fill out Dogescript in JavaScript and print Hello, World! with console.loge.

## Toolchain

Node.js v22.20.0; dogescript 2.4.3

## Commands and procedure

npm install; node check.cjs

## Expected result

Filler generates valid JavaScript; execution produces exactly a greeting.

## Status

syntax and behavior verified.

check.cjs chiama il compilatore Dogescript originale, compila il risultato con vm.Script di Node e ne esegue il codice catturando console.log. Il checker non traduce il linguaggio.

Actual verification of 2026-10-08T11:56:12.746770+00:00 on Windows x64: [log](verification/result.json).
Hash of sorgenti/checker, real versions and commands, output codes, stdout/stderr and test limits are in the log.

## Primary sources and format reference

- [https://github.com/dogescript/dogescript](https://github.com/dogescript/dogescript)
- [https://github.com/dogescript/dogescript/blob/master/LANGUAGE.md](https://github.com/dogescript/dogescript/blob/master/LANGUAGE.md)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.djs` | [hello.djs](hello.djs) verified |
