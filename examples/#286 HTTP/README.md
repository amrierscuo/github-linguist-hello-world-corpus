# #286 HTTP

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Analizzare una risposta HTTP/1.1 reale e trasferire Hello, World! tramite una connessione loopback.

hello.http è una risposta wire con header CRLF, linea vuota e 13 byte di corpo. Una fixture la invia intatta via socket su 127.0.0.1; h11 analizza richiesta e risposta e il controllo confronta il body. Il listener usa una porta effimera, il socket viene chiuso e il thread viene atteso.

## Toolchain e riproduzione

h11 0.16.0 e CPython3.13.9

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

h11 accetta HTTP200, Content-Length13 e body Hello, World!; fixture conclusa con CLEANUP.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.rfc-editor.org/rfc/rfc9112.html
- https://h11.readthedocs.io/en/stable/basic-usage.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.http` | [hello.http](hello.http) verificato |
