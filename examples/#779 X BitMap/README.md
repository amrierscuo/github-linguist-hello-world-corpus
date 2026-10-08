# #779 X BitMap

Voce canonica `X BitMap`, tipo `data`, language_id `782911107`.

Immagine XBM originale da 104×1 pixel: i bit della riga codificano i 13 byte ASCII di `Hello, World!`, nell’ordine LSB previsto dal formato bitmap X.

## Toolchain e riproduzione

Pillow / Python 3.13.9 — 12.0.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python 3.13.9 e Pillow 12.0.0 in ambiente isolato.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py
```

Risultato atteso: Immagine XBM 104×1 caricata, payload Hello, World! e PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Pillow interpreta realmente XBM e carica l’immagine. Il driver ricompone i byte dai pixel caricati e controlla il payload. L’obiettivo è una codifica binaria nei pixel, non la resa grafica di lettere visibili.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#xbm](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#xbm)
- [https://www.x.org/releases/current/doc/libX11/libX11/libX11.html](https://www.x.org/releases/current/doc/libX11/libX11/libX11.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.xbm` | [hello.xbm](hello.xbm) verificato |
