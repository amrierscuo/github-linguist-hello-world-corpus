# #319 J

Scrivere Hello, World! tramite il file I/O nativo del linguaggio J.

## Toolchain

Official Jsoftware j9.6.3/j64/windows/commercial/www.jsoftware.com/2026-02-02T04:38:37/clang-19-1-5/SLEEF=1

## Comandi e procedura

Jsoftware jconsole -jprofile version.ijs; Jsoftware jconsole -jprofile hello.ijs

## Risultato atteso

Versione engine osservata; console Hello, World! più newline; exit 0.

## Stato

Sintassi e semantica verificate.

La primitive 1!:2 con file numero 2 scrive alla console; 2!:55 termina la sessione con codice 0. -jprofile sceglie direttamente questo script senza bootstrap della libreria standard. Si usa il Jsoftware jconsole originale.

Verifica effettiva del 2026-10-08T12:32:59.299767+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://www.jsoftware.com/help/dictionary/dx001.htm](https://www.jsoftware.com/help/dictionary/dx001.htm)
- [https://www.jsoftware.com/help/dictionary/dx002.htm](https://www.jsoftware.com/help/dictionary/dx002.htm)
- [https://www.jsoftware.com/help/dictionary/dx009.htm](https://www.jsoftware.com/help/dictionary/dx009.htm)
- [https://github.com/jsoftware/jsource/releases/tag/build96](https://github.com/jsoftware/jsource/releases/tag/build96)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ijs` | [hello.ijs](hello.ijs), [version.ijs](version.ijs) verificato |
