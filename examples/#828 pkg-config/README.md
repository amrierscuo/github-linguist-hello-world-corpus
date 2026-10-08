# #828 pkg-config

Leggere metadata pkg-config e la variabile del saluto.

## Toolchain

pkg-config 1.8.1

## Procedura

PKG_CONFIG_PATH=<cartella-assoluta> pkg-config --validate hello; pkg-config --variable=greeting hello

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

La libreria è illustrativa: Libs/Cflags vuoti. pkg-config controlla il file e risolve davvero la variabile greeting; non si cerca una libreria inventata.

Verifica reale 2026-10-08T13:48:50.733718+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://people.freedesktop.org/~dbn/pkg-config-guide.html](https://people.freedesktop.org/~dbn/pkg-config-guide.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pc` | [hello.pc](hello.pc) verificato |
| `.pc.in` | [hello.pc.in](variants/pc-in-477d8206/hello.pc.in) creato, verifiche pendenti |
