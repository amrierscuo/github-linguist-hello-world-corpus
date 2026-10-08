# #310 ImageJ Macro

Eseguire una macro ImageJ originale in batch e stampare il saluto.

## Toolchain

ImageJ 1.54g; Microsoft OpenJDK 21.0.12.1

## Comandi e procedura

java -Djava.awt.headless=true -jar ij.jar -batch hello.ijm

## Risultato atteso

Runtime exit 0; stdout Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

La macro usa print, senza operazioni GUI o immagini. ImageJVersion.java consulta il runtime reale per registrare ij.IJ.getVersion(); non implementa l’interprete macro.

Verifica effettiva del 2026-10-08T12:29:58.567762+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://imagej.net/ij/plugins/command-line-macros.html](https://imagej.net/ij/plugins/command-line-macros.html)
- [https://imagej.net/ij/developer/macro/functions.html](https://imagej.net/ij/developer/macro/functions.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ijm` | [hello.ijm](hello.ijm) verificato |
