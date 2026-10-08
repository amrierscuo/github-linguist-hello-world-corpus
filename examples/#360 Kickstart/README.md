# #360 Kickstart

Voce canonica `Kickstart`, tipo `data`, language_id `692635484`.

Analizzare comandi Kickstart e preservare una sezione post con il saluto come dato di configurazione.

## Toolchain e riproduzione

Original Pykickstart Kickstart parser — 3.68; Fedora F42 handler. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Pykickstart originale 3.68, handler Fedora F42. Il helper chiama KickstartParser.readKickstart e controlla lingua, timezone, numero di script e inChroot=False.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python -m pip install pykickstart==3.68; python verify.py hello.ks
```

Risultato atteso: Comandi accettati; post-script printf del saluto preservato esattamente; PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La prova usa esclusivamente il parser: non avvia Anaconda, non installa/partiziona un sistema e non esegue lo script post. La semantica dichiarata riguarda il modello di configurazione e il contenuto dello script preservato.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://pykickstart.readthedocs.io/en/latest/pykickstart.html](https://pykickstart.readthedocs.io/en/latest/pykickstart.html)
- [https://pykickstart.readthedocs.io/en/latest/sections.html](https://pykickstart.readthedocs.io/en/latest/sections.html)
- [https://github.com/pykickstart/pykickstart](https://github.com/pykickstart/pykickstart)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ks` | [hello.ks](hello.ks) verificato |
