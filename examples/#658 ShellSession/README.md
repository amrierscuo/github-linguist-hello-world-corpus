# #658 ShellSession

Registrare un transcript autentico di sessione shell del saluto.

## Toolchain

Ubuntu dash 0.5.12 POSIX sh

## Procedura

sh replay.sh; confrontare output con il transcript hello.sh-session

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

Il transcript contiene i prompt convenzionali e l’output reale dello script equivalente; i prompt non vengono interpretati come comandi.

Verifica reale 2026-10-08T13:23:04.712051+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sh.html](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sh.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sh-session` | [hello.sh-session](hello.sh-session) verificato |
