# #051 B4X

Voce canonica: `B4X`, tipo `programming`, `language_id: 96642275`.

Stampare Hello, World! nel log di una applicazione console non-UI B4J, variante della famiglia B4X.

## Toolchain e riproduzione

B4J.exe — non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede B4J e JDK compatibile. Main.bas è il modulo sorgente da inserire in un nuovo progetto non-UI: gli attributi e i metadati del progetto sono creati dall’IDE.

Comando/procedura dalla directory dell’esempio:

```text
B4J IDE: File > New > Non-UI Project; sostituire il modulo Main con Main.bas; Run in Release; controllare il log.
```

Risultato atteso: Build riuscita e una riga Hello, World! nel log della applicazione.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Usa AppStart(Args() As String) per B4J console e Log per il saluto. B4J non è presente e il modulo non è stato compilato. Non è dichiarato un progetto B4A/B4i completo.

Requisiti residui:

- B4J.exe toolchain not installed or not available in this isolated verification environment.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://www.b4x.com/guides/B4XGettingStarted.html](https://www.b4x.com/guides/B4XGettingStarted.html)
- [https://www.b4x.com/android/forum/threads/console-application-output-shown-after-command-prompt.167324/](https://www.b4x.com/android/forum/threads/console-application-output-shown-after-command-prompt.167324/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bas` | [Main.bas](Main.bas) creato, verifiche pendenti |
