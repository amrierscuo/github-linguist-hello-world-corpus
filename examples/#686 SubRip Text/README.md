# #686 SubRip Text

Voce canonica `SubRip Text`, tipo `data`, language_id `360`.

Decodificare una sottotitolazione SubRip con saluto e intervallo di due secondi.

## Toolchain e riproduzione

Existing PySRT format parser — 1.1.2. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Parser esistente pysrt 1.1.2.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il decoder reale valida indice, start/end e testo; il goal eÌâ‚¬ il modello dei sottotitoli, senza video-player.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/byroot/pysrt](https://github.com/byroot/pysrt)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.srt` | [hello.srt](hello.srt) verificato |
