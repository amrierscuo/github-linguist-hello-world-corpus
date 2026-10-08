# #045 AutoHotkey

Voce canonica: `AutoHotkey`, tipo `programming`, `language_id: 26`.

Inviare Hello, World! e LF allo stream stdout e terminare AutoHotkey v2.

## Toolchain e riproduzione

Official AutoHotkey 64-bit portable interpreter v2 — 2.0.27. Ambiente della prova: **Windows x64**.

Estrarre il pacchetto ufficiale AutoHotkey 2.0.27 e usare AutoHotkey64.exe. Il codice richiede v2.0; non è sintassi AutoHotkey v1.

Comando/procedura dalla directory dell’esempio:

```text
AutoHotkey64.exe /ErrorStdOut hello.ahk
```

Risultato atteso: Exit 0; stdout catturato esattamente Hello, World! seguito da LF.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

FileAppend con destinazione * scrive su stdout. Un launcher GUI Windows può non mostrarlo direttamente nel prompt: acquisire o reindirizzare stdout, come nella prova registrata. Nessuna finestra/hotkey viene creata.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://github.com/AutoHotkey/AutoHotkeyDocs/blob/v2/docs/lib/FileAppend.htm](https://github.com/AutoHotkey/AutoHotkeyDocs/blob/v2/docs/lib/FileAppend.htm)
- [https://www.autohotkey.com/download/2.0/](https://www.autohotkey.com/download/2.0/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ahk` | [hello.ahk](hello.ahk) verificato |
| `.ah1` | [hello.ah1](variants/ext-ah1-2e616831/hello.ah1) creato, verifiche pendenti |
| `.ah2` | [hello.ah2](variants/ext-ah2-2e616832/hello.ah2) creato, verifiche pendenti |
| `.ahkl` | [hello.ahkl](variants/ext-ahkl-2e61686b6c/hello.ahkl) creato, verifiche pendenti |
