# #319 J

Write Hello, World! through the native I/O file of the language J.

## Toolchain

Official Jsoftware j9.6.3/j64/windows/commercial/www.jsoftware.com/2026-02-02T04:38:37/clang-19-1-5/SLEEF=1

## Commands and procedure

Jsoftware jconsole -jprofile version.ijs; Jsoftware jconsole -jprofile hello.ijs

## Expected result

Version engine observed; console Hello, World! plus newline; exit 0.

## Status

syntax and behavior verified.

La primitive 1!:2 con file numero 2 scrive alla console; 2!:55 termina la sessione con codice 0. -jprofile sceglie direttamente questo script senza bootstrap della libreria standard. Si usa il Jsoftware jconsole originale.

Actual verification of 2026-10-08T12:32:59.299767+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://www.jsoftware.com/help/dictionary/dx001.htm](https://www.jsoftware.com/help/dictionary/dx001.htm)
- [https://www.jsoftware.com/help/dictionary/dx002.htm](https://www.jsoftware.com/help/dictionary/dx002.htm)
- [https://www.jsoftware.com/help/dictionary/dx009.htm](https://www.jsoftware.com/help/dictionary/dx009.htm)
- [https://github.com/jsoftware/jsource/releases/tag/build96](https://github.com/jsoftware/jsource/releases/tag/build96)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ijs` | [hello.ijs](hello.ijs), [version.ijs](version.ijs) verified |
