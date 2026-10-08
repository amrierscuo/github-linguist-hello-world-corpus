# #275 HAProxy

Voce canonica `HAProxy`, tipo `data`, language_id `366607477`.

Servire il saluto come risposta HTTP locale costruita da HAProxy senza backend.

## Toolchain e riproduzione

HAProxy native configuration parser and HTTP engine — HAProxy version 2.8.16-0ubuntu0.24.04.3 2026/06/19 - https://haproxy.org/. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

HAProxy 2.8.16 dal pacchetto Ubuntu estratto localmente, con liblua5.4. verify.py richiede il prefix con usr/sbin/haproxy e librerie. L’unico bind è 127.0.0.1:18881; se la porta è occupata la prova fallisce.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
haproxy -c -f haproxy.cfg; python3 verify.py <prefix-pacchetti-haproxy> haproxy.cfg
```

Risultato atteso: HTTP 200; body Hello, World!; PASS; processo terminato.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La prova prima usa il parser -c, poi avvia un processo privato in foreground, effettua una richiesta locale e lo termina in finally. Verifica HTTP 200, Content-Type text/plain e body esatto.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.haproxy.org/download/2.8/doc/configuration.txt](https://www.haproxy.org/download/2.8/doc/configuration.txt)
- [https://www.haproxy.org/](https://www.haproxy.org/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cfg` | [haproxy.cfg](haproxy.cfg) verificato |
