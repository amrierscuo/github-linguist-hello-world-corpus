# #121 Classic ASP

Voce canonica: `Classic ASP`, tipo `programming`, `language_id: 8`.

Servire una pagina Classic ASP in VBScript e scrivere Hello, World! nel corpo della risposta HTTP text/plain.

## Toolchain e riproduzione

Required native toolchain unavailable or not configured — versione non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede IIS con la feature Classic ASP e il motore VBScript. Usare un sito locale dedicato. cscript.exe esiste, ma non fornisce l’oggetto ASP Response e non dimostra la validità della pagina.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
IIS locale con ASP abilitato: pubblicare hello.asp nel sito di prova; curl http://localhost:<porta>/hello.asp
```

Risultato atteso: HTTP 200; corpo contenente esattamente il saluto Hello, World!, con eventuale newline di fine pagina.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Direttiva Language=VBScript, Option Explicit, ContentType e concatenazione di stringhe sono sorgente ASP originale. La prova registra disponibilità dell’host VBScript; manca una vera richiesta IIS, quindi entrambi i flag restano false.

Requisiti residui:

- Classic ASP requires IIS ASP request context; cscript/WScript VBScript alone does not provide Response.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://learn.microsoft.com/en-us/previous-versions/iis/6.0-sdk/ms524741(v=vs.90)](https://learn.microsoft.com/en-us/previous-versions/iis/6.0-sdk/ms524741(v=vs.90))
- [https://learn.microsoft.com/en-us/previous-versions/iis/6.0-sdk/ms525585(v=vs.90)](https://learn.microsoft.com/en-us/previous-versions/iis/6.0-sdk/ms525585(v=vs.90))
- [https://learn.microsoft.com/en-us/iis/configuration/system.webserver/asp/](https://learn.microsoft.com/en-us/iis/configuration/system.webserver/asp/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.asp` | [hello.asp](hello.asp) creato, verifiche pendenti |
