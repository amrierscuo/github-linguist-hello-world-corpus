# #033 ApacheConf

`httpd.conf` configura un server limitato a `127.0.0.1:18033` e rende accessibile `www/hello.txt`. La configurazione richiede i moduli DSO event MPM, unixd e authz_core e un utente/gruppo locale `apache`.

Prima di eseguire i comandi, impostare `CORPUS_ROOT` al percorso assoluto di questa cartella, `CORPUS_RUN` a una cartella temporanea scrivibile già creata e `APACHE_MODULE_DIR` alla directory dei moduli della stessa build di Apache. Se la distribuzione usa nomi diversi per utente e gruppo, adattarli e ripetere le prove; gli esiti registrati si riferiscono ai byte qui consegnati.

Esempio per Alpine, avviato dalla cartella dell'esempio con utente root **nel solo rootfs isolato**:

```sh
export CORPUS_ROOT="$PWD"
export CORPUS_RUN=/scratch/apache
export APACHE_MODULE_DIR=/usr/lib/apache2
mkdir -p "$CORPUS_RUN"
httpd -t -f "$CORPUS_ROOT/httpd.conf"
httpd -f "$CORPUS_ROOT/httpd.conf" -k start
curl --fail --silent --show-error http://127.0.0.1:18033/hello.txt
httpd -f "$CORPUS_ROOT/httpd.conf" -k stop
```

Il risultato previsto è `Syntax OK` e un corpo HTTP di esattamente `Hello, World!` con newline. Nel controllo locale il corpo viene scritto nella cartella temporanea e confrontato byte per byte con `www/hello.txt`; il server viene arrestato al termine.

Toolchain: **Apache HTTP Server 2.4.69 in Alpine Linux 3.23.6 x86_64; curl; mod_mpm_event, mod_unixd, mod_authz_core**.

Stato: **Sintassi e semantica verificate.**

Evidenza: [log dei comandi e SHA-256 dei sorgenti](verification/toolchain.json). Il log conserva exit code, stdout e stderr; i percorsi della macchina sono normalizzati.

Dettaglio del controllo: il parser Apache, la richiesta HTTP riuscita e il confronto esatto del corpo sono passati. Il wrapper esterno ha poi terminato con exit 32 perché il bind mount temporaneo `/dev` risultava ancora occupato al momento dello smontaggio. Questo errore di pulizia è conservato nel log ed è distinto dalle prove funzionali concluse; l'arresto Apache era già stato richiesto dal trap del controllo.

Pulizia finale verificata con exit 0: non rimangono processi Apache appartenenti a questo rootfs/configurazione e il bind mount temporaneo `/dev` non è più attivo. Il controllo ha verificato percorsi e processi del solo rootfs del corpus, senza toccare servizi o mount estranei.

Fonti primarie:

- [Documentazione / sorgente ufficiale 1](https://httpd.apache.org/docs/2.4/programs/httpd.html)
- [Documentazione / sorgente ufficiale 2](https://httpd.apache.org/docs/2.4/mod/core.html)
- [Documentazione / sorgente ufficiale 3](https://httpd.apache.org/docs/2.4/mod/mod_authz_core.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.apacheconf` | [hello.apacheconf](variants/ext-apacheconf-2e617061636865636f6e66/hello.apacheconf) creato, verifiche pendenti |
| `.vhost` | [hello.vhost](variants/ext-vhost-2e76686f7374/hello.vhost) creato, verifiche pendenti |
