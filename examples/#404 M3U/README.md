# #404 M3U

Analizzare una playlist Extended M3U UTF-8 con titolo di segmento Hello, World!.

Tipo canonico `data`, language_id `89638692`.

Toolchain prevista: Python 3.13 e m3u8 parser.

Dalla cartella dell’esempio:

```sh
python verify.py
```

Risultato atteso: un segmento di 1s con titolo e URI attesi; stdout saluto e LF.

example.invalid è un URI illustrativo: non viene scaricato né riprodotto. La semantica verificata è la struttura e i metadata della playlist.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Python 3.13.9 + m3u8 6.0.0. [Log](verification/result.json). 

Fonti:

- [RFC 8216 — playlist HLS/M3U](https://www.rfc-editor.org/rfc/rfc8216)
- [m3u8 — implementazione](https://github.com/globocom/m3u8)

Preparazione delle dipendenze in una cartella dedicata:

```sh
python -m pip install m3u8==6.0.0
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.m3u` | [hello.m3u](variants/m3u-333e8b48/hello.m3u) creato, verifiche pendenti |
| `.m3u8` | [hello.m3u8](hello.m3u8) verificato |
