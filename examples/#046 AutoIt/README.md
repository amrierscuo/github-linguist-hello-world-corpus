# #046 AutoIt

Voce canonica: `AutoIt`, tipo `programming`, `language_id: 27`.

Scrivere il saluto concatenato su stdout AutoIt e terminare con codice 0.

## Toolchain e riproduzione

Official AutoIt x64 and Au3Check portable — 3.3.18.0. Ambiente della prova: **Windows x64**.

Estrarre AutoIt 3.3.18.0 Portable dal sito ufficiale; usare Au3Check.exe e AutoIt3_x64.exe della directory install.

Comando/procedura dalla directory dell’esempio:

```text
Au3Check.exe hello.au3; AutoIt3_x64.exe /ErrorStdOut hello.au3
```

Risultato atteso: Au3Check: 0 errori e 0 warning; runtime exit 0; stdout Hello, World! seguito da CRLF.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

ConsoleWrite produce lo stream stdout; un interprete GUI non garantisce la sua visualizzazione nel prompt senza acquisizione. La prova cattura realmente quello stream e normalizza CRLF tramite text mode.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://www.autoitscript.com/autoit3/docs/functions/ConsoleWrite.htm](https://www.autoitscript.com/autoit3/docs/functions/ConsoleWrite.htm)
- [https://www.autoitscript.com/site/autoit/downloads/](https://www.autoitscript.com/site/autoit/downloads/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.au3` | [hello.au3](hello.au3) verificato |
