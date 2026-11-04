# #311 Imba

Fill in and execute Imba to write the greeting on the console Node.

## Toolchain

Imba 2.0.0-alpha.253; Node.js 22.20.0

## Commands and procedure

npm install; npx imba hello.imba

## Expected result

CLI exit 0; console.log emitting Hello, World! more newline.

## Status

syntax and behavior verified.

The original CLI compiles the .imba file and actually executes it. package.json fixes the tried version; bundle/cache stays in work. No browser is required.

Actual verification of 2026-10-08T12:30:00.143794+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://github.com/imba/imba](https://github.com/imba/imba)
- [https://imba.io/](https://imba.io/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.imba` | [hello.imba](hello.imba) verified |
