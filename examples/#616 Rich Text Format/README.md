# #616 Rich Text Format

Voce canonica `Rich Text Format`, tipo `markup`, language_id `51601661`.

Decodificare un documento Rich Text Format originale nel saluto in plain text.

## Toolchain e riproduzione

Existing striprtf authentic format parser — 0.0.33. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Parser esistente striprtf 0.0.33.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il parser reale interpreta rtf1, font table, f0 e par: confronto del corpo decodificato. Il goal eÌ€ estrazione testuale, non impaginazione grafica.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://learn.microsoft.com/en-us/previous-versions/office/developer/office2007/aa338117(v=office.12)](https://learn.microsoft.com/en-us/previous-versions/office/developer/office2007/aa338117(v=office.12))

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rtf` | [hello.rtf](hello.rtf) verificato |
