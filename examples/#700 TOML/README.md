# #700 TOML

Voce canonica `TOML`, tipo `data`, language_id `365`.

Decodificare una configurazione TOML originale con message e language.

## Toolchain e riproduzione

Python standard-library TOML parser — 3.13.9. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python3.13.9 tomllib nativo.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il parser vero ricostruisce una mappa typed esatta; il campo message produce il saluto.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://toml.io/en/v1.0.0](https://toml.io/en/v1.0.0)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.toml` | [hello.toml](hello.toml) verificato |
| `.toml.example` | [hello.toml.example](variants/toml-example-35fdb380/hello.toml.example) creato, verifiche pendenti |
