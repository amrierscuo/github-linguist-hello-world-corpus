# #812 desktop

Validare una desktop entry originale del saluto.

## Toolchain

desktop-file-utils0.27 native validator

## Procedura

desktop-file-validate hello.desktop; controllare Name nel reader del desktop di prova.

## Risultato atteso

Validatore senza errori; Name=Hello, World! e Exec riconosciuti.

## Stato

Sintassi verificata; semantica in attesa.

La prova valida il formato offline; applicazione e terminale non vengono lanciati.

Verifica reale 2026-10-08T13:38:35.207016+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

Requisiti residui:
- Desktop shell UI/launcher consumer pending.

## Fonti primarie

- [https://specifications.freedesktop.org/desktop-entry/latest/](https://specifications.freedesktop.org/desktop-entry/latest/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.desktop` | [hello.desktop](hello.desktop) sintassi verificata |
| `.desktop.in` | [hello.desktop.in](variants/desktop-in-8bdb31d7/hello.desktop.in) creato, verifiche pendenti |
