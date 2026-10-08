# #103 Caddyfile

Servire una risposta HTTP locale 200 il cui corpo è esattamente Hello, World!.

Tipo canonico: `data`; `language_id`: `615465151`.

Toolchain prevista: Caddy 2.x. La versione effettivamente provata, quando disponibile, è nel log.

Dalla cartella dell'esempio, con le dipendenze nel PATH:

```sh
caddy validate --config Caddyfile --adapter caddyfile
caddy run --config Caddyfile --adapter caddyfile
```

Risultato atteso: GET http://127.0.0.1:18763/ restituisce stato 200 e i 13 byte `Hello, World!`.

L’indirizzo è solo loopback e HTTP; non richiede DNS né certificati. Arrestare il processo con Ctrl+C dopo la richiesta; la verifica automatica avvia e termina il proprio processo.

Stato registrato: sintassi verificata; semantica verificata. Toolchain provata: Caddy 2.11.7 windows/amd64. Vedere [log](verification/verification.log). 

Fonti primarie o riferimenti originali del progetto:

- [Caddy — direttiva respond](https://caddyserver.com/docs/caddyfile/directives/respond)
- [Caddy — riga di comando](https://caddyserver.com/docs/command-line)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.caddyfile` | [hello.caddyfile](variants/ext-caddyfile-2e636164647966696c65/hello.caddyfile) creato, verifiche pendenti |
