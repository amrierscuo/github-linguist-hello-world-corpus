# 0017 ASP.NET: variant `.axd`

Role: Fixture text resource AXD served by an IHttpHandler ASP.NET explicitly recorded in Web.config. The AXD file contains the actual payload of the endpoint; this context does not define a standard ASP.NET source.

Type: **adapted**. Starting model: examples/#017 ASP.NET / hello.aspx; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Copiare tutti i file della variante in un sito temporaneo ASP.NET Framework 4.x; IISExpress.exe /path:<copia-assoluta> /port:18717 /clr:v4.0; da altro terminale Invoke-WebRequest http://127.0.0.1:18717/hello.axd -UseBasicParsing; confrontare Content con Hello, World! più LF.
```

Expected result: GET / hello.axd answers 200 text/plain UTF - 8 with the content of Hello, World! fixtures followed by LF.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://learn.microsoft.com/en-us/aspnet/web-forms/what-is-web-forms](https://learn.microsoft.com/en-us/aspnet/web-forms/what-is-web-forms)
- [https://learn.microsoft.com/en-us/aspnet/web-forms/overview/moving-to-aspnet-20/configuration-and-instrumentation](https://learn.microsoft.com/en-us/aspnet/web-forms/overview/moving-to-aspnet-20/configuration-and-instrumentation)
- [https://learn.microsoft.com/en-us/dotnet/api/system.web.hosting.applicationhost?view=netframework-4.8.1](https://learn.microsoft.com/en-us/dotnet/api/system.web.hosting.applicationhost?view=netframework-4.8.1)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://learn.microsoft.com/en-us/troubleshoot/developer/webapps/aspnet/development/http-modules-handlers](https://learn.microsoft.com/en-us/troubleshoot/developer/webapps/aspnet/development/http-modules-handlers)
- [https://learn.microsoft.com/en-us/iis/configuration/system.webserver/handlers/add](https://learn.microsoft.com/en-us/iis/configuration/system.webserver/handlers/add)
- [https://learn.microsoft.com/en-us/iis/extensions/using-iis-express/running-iis-express-from-the-command-line](https://learn.microsoft.com/en-us/iis/extensions/using-iis-express/running-iis-express-from-the-command-line)
