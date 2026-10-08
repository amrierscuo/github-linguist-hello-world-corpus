# #763 Wavefront Object

Voce canonica `Wavefront Object`, tipo `data`, language_id `393`.

Oggetto Wavefront OBJ originale: un triangolo planare con tre vertici e una faccia, associato al materiale denominato `Hello, World!`.

## Toolchain e riproduzione

trimesh / Python 3.13.9 — 5.1.1. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python 3.13.9, trimesh 5.1.1 e NumPy. Installare le librerie in ambiente isolato; la prova usa il loader MTL/OBJ del progetto trimesh.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py
```

Risultato atteso: Hello, World!, seguito da PASS; nome, colore o geometria corrispondono al modello originale.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il parser esistente legge il file nativo. Le asserzioni originali controllano il nome e il modello dati: colore per MTL; geometria, bounds e riferimento al materiale per OBJ. L’obiettivo dichiarato è il modello caricato, non un rendering 3D.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://trimesh.org/trimesh.exchange.obj.html](https://trimesh.org/trimesh.exchange.obj.html)
- [https://paulbourke.net/dataformats/obj/](https://paulbourke.net/dataformats/obj/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.obj` | [hello.obj](hello.obj) verificato |
