# #657 ShellCheck Config

Leggere la configurazione .shellcheckrc con ShellCheck e controllare lo script.

## Toolchain

ShellCheck - shell script analysis tool
version: 0.9.0
license: GNU General Public License, version 3
website: https://www.shellcheck.net

## Procedura

shellcheck hello.sh; sh hello.sh

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

Il test verifica che ShellCheck trovi la configurazione locale senza alterare configurazioni globali; lo script viene eseguito realmente.

Verifica reale 2026-10-08T13:23:05.420327+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://github.com/koalaman/shellcheck/wiki/Directive](https://github.com/koalaman/shellcheck/wiki/Directive)
