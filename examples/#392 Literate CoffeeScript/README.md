# #392 Literate CoffeeScript

Fill in indented code in a Literate CoffeeScript document and print your greeting.

## Toolchain

coffeescript 2.7.0; Node 22.20.0

## Commands and procedure

npm install; npx coffee hello.litcoffee

## Expected result

Excess ignored, indented code compiled; stdout Hello, World! plus newline.

## Status

syntax and behavior verified.

Il formato .litcoffee viene riconosciuto dal compilatore ufficiale; l’esecuzione sul runtime Node è reale. Non si estrae manualmente il blocco per contare la verifica.

Actual verification of 2026-10-08T12:48:17.110423+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://coffeescript.org/#literate](https://coffeescript.org/#literate)
- [https://github.com/jashkenas/coffeescript](https://github.com/jashkenas/coffeescript)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.litcoffee` | [hello.litcoffee](hello.litcoffee) verified |
| `.coffee.md` | [hello.coffee.md](variants/coffee-md-862b0193/hello.coffee.md) created; verification pending |
