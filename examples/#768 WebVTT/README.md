# #768 WebVTT

Voce canonica `WebVTT`, tipo `data`, language_id `658679714`.

Sottotitolo WebVTT originale, identificatore greeting: `Hello, World!` nell’intervallo da 0 a 2 secondi.

## Toolchain e riproduzione

webvtt-py / Python 3.13.9 — 0.5.1. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Python 3.13.9 e webvtt-py 0.5.1 in ambiente isolato.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python verify.py
```

Risultato atteso: Hello, World! e PASS per il cue da 0 a 2 secondi.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il decoder WebVTT esistente legge il cue; il driver controlla i tempi e il testo. La prova riguarda il modello dati della didascalia, senza attestare il rendering di un player.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.w3.org/TR/webvtt1/](https://www.w3.org/TR/webvtt1/)
- [https://github.com/glut23/webvtt-py](https://github.com/glut23/webvtt-py)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.vtt` | [hello.vtt](hello.vtt) verificato |
