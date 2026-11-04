# #395 LiveScript

Fill out LiveScript in JavaScript and run console.log.

## Toolchain

livescript 1.6.0; Node 22.20.0

## Commands and procedure

npm install; npx lsc hello.ls

## Expected result

Exit 0; Hello, World! more newline.

## Status

syntax and behavior verified.

You use the original LiveScript compiler and the Node runtime. .ls is kept in the specific folder, separated from the LoomScript file with the same extension.

Actual verification of 2026-10-08T12:48:18.107237+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://livescript.net/](https://livescript.net/)
- [https://github.com/gkz/LiveScript](https://github.com/gkz/LiveScript)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ls` | [hello.ls](hello.ls) verified |
| `._ls` | [hello._ls](variants/ls-4f7bfbd4/hello._ls) created; verification pending |
