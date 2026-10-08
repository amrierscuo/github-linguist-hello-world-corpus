# #058 Batchfile

Voce canonica: `Batchfile`, tipo `programming`, `language_id: 29`.

Stampare Hello, World! tramite il command processor Windows mantenendo il punto esclamativo.

## Toolchain e riproduzione

Windows cmd.exe — Microsoft Windows [Version 10.0.26300.9457]. Ambiente della prova: **Windows x64**.

Usare cmd.exe di Windows. La prova è eseguita su Windows 10.0.26300.9457; /d evita le istruzioni AutoRun del profilo.

Comando/procedura dalla directory dell’esempio:

```text
cmd /d /c hello.cmd
```

Risultato atteso: Exit 0; stdout Hello, World! seguito da CRLF.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

setlocal DisableDelayedExpansion mantiene letterale ! anche se il chiamante usa delayed expansion. Il log acquisisce stdout reale e converte CRLF in LF tramite text mode.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://learn.microsoft.com/windows-server/administration/windows-commands/echo](https://learn.microsoft.com/windows-server/administration/windows-commands/echo)
- [https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bat` | [hello.bat](variants/ext-bat-2e626174/hello.bat) creato, verifiche pendenti |
| `.cmd` | [hello.cmd](hello.cmd) verificato |
