# 0017 ASP.NET — variante `.axd`

Ruolo: Fixture risorsa testuale AXD servita da un IHttpHandler ASP.NET registrato esplicitamente in Web.config. Il file AXD contiene il payload effettivo dell’endpoint; questo contesto non definisce un sorgente ASP.NET standard. Il companion C# viene compilato da App_Code.

Tipo variante: **adapted**. Modello di partenza: examples/#017 ASP.NET/hello.aspx; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Copiare tutti i file della variante in un sito temporaneo ASP.NET Framework 4.x; IISExpress.exe /path:<copia-assoluta> /port:18717 /clr:v4.0; da altro terminale Invoke-WebRequest http://127.0.0.1:18717/hello.axd -UseBasicParsing; confrontare Content con Hello, World! più LF.
```

Risultato atteso: GET /hello.axd risponde 200 text/plain UTF-8 con il contenuto della fixture Hello, World! seguito da LF.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://learn.microsoft.com/en-us/aspnet/web-forms/what-is-web-forms](https://learn.microsoft.com/en-us/aspnet/web-forms/what-is-web-forms)
- [https://learn.microsoft.com/en-us/aspnet/web-forms/overview/moving-to-aspnet-20/configuration-and-instrumentation](https://learn.microsoft.com/en-us/aspnet/web-forms/overview/moving-to-aspnet-20/configuration-and-instrumentation)
- [https://learn.microsoft.com/en-us/dotnet/api/system.web.hosting.applicationhost?view=netframework-4.8.1](https://learn.microsoft.com/en-us/dotnet/api/system.web.hosting.applicationhost?view=netframework-4.8.1)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://learn.microsoft.com/en-us/troubleshoot/developer/webapps/aspnet/development/http-modules-handlers](https://learn.microsoft.com/en-us/troubleshoot/developer/webapps/aspnet/development/http-modules-handlers)
- [https://learn.microsoft.com/en-us/iis/configuration/system.webserver/handlers/add](https://learn.microsoft.com/en-us/iis/configuration/system.webserver/handlers/add)
- [https://learn.microsoft.com/en-us/iis/extensions/using-iis-express/running-iis-express-from-the-command-line](https://learn.microsoft.com/en-us/iis/extensions/using-iis-express/running-iis-express-from-the-command-line)
