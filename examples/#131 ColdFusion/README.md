# #131 ColdFusion

Voce canonica: `ColdFusion`, tipo `programming`, `language_id: 64`.

Servire un template ColdFusion .cfm che concatena le parti del saluto dentro cfoutput.

## Toolchain e riproduzione

Required native toolchain unavailable or not configured — versione non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede un motore CFML Adobe ColdFusion o Lucee configurato localmente; registrare la sua versione e URL di prova. I tag cfsetting/cfcontent sono parte del template, non simulati con un renderer HTML.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
Server Lucee/Adobe ColdFusion locale: servire hello.cfm; curl http://localhost:<porta>/hello.cfm
```

Risultato atteso: HTTP 200; risposta text/plain contenente Hello, World!, senza debug output.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

cfcontent reset=true cancella eventuali output precedenti e cfsetting disabilita il debug. Nessun motore è configurato, dunque la pagina non è stata parsata o richiesta realmente.

Requisiti residui:

- No Adobe ColdFusion/Lucee engine is configured to serve the template.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://docs.lucee.org/reference/tags/output.html](https://docs.lucee.org/reference/tags/output.html)
- [https://docs.lucee.org/reference/tags/content.html](https://docs.lucee.org/reference/tags/content.html)
- [https://docs.lucee.org/reference/tags/setting.html](https://docs.lucee.org/reference/tags/setting.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cfm` | [hello.cfm](hello.cfm) creato, verifiche pendenti |
| `.cfml` | [hello.cfml](variants/ext-cfml-2e63666d6c/hello.cfml) creato, verifiche pendenti |
