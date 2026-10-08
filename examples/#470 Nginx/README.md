# #470 Nginx

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Caricare una configurazione Nginx e servire Hello, World! via HTTP su loopback.

Il file principale .nginxconf usa return200 nella location/greeting. Il driver invoca nginx-t, avvia solo il processo dedicato su127.0.0.1:18080, confronta il corpo e in finally arresta il processo e verifica la chiusura del listener. File temporanei e log restano nella copia in work.

## Toolchain e riproduzione

Nginx1.24.0 Ubuntu, Python3 della fixture locale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python3 verify.py
```

## Risultato atteso e stato

Configurazione accettata; HTTP200/body esatto Hello, World!; CLEANUP confermato.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://nginx.org/en/docs/http/ngx_http_rewrite_module.html#return
- https://nginx.org/en/docs/switches.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nginx` | [hello.nginx](variants/nginx-50552489/hello.nginx) creato, verifiche pendenti |
| `.nginxconf` | [hello.nginxconf](hello.nginxconf) verificato |
| `.vhost` | [hello.vhost](variants/vhost-a09033b0/hello.vhost) creato, verifiche pendenti |
