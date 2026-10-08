# #298 Hurl

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Eseguire un file Hurl che asserisce HTTP200 e body Hello, World! su un server loopback.

hello.hurl contiene richiesta GET, status atteso e asserzione body. La fixture originale avvia un HTTPServer soltanto su127.0.0.1 con porta effimera; invoca il vero Hurl con --test e --variable port, disattiva proxy e conclude server, socket e thread in finally.

## Toolchain e riproduzione

Hurl8.0.1 Windows x64, libcurl8.17.0-DEV; CPython3.13.9

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

1 file/request riuscito, body esatto Hello, World!, seguito da CLEANUP; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://hurl.dev/docs/asserting-response.html
- https://hurl.dev/docs/running-tests.html
- https://github.com/Orange-OpenSource/hurl/releases/tag/8.0.1

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.hurl` | [hello.hurl](hello.hurl) verificato |
