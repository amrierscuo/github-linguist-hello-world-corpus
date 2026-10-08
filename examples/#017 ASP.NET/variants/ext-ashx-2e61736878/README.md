# 0017 ASP.NET — variante `.ashx`

Ruolo: HTTP handler ASP.NET con ProcessRequest.

Tipo variante: **adapted**. Modello di partenza: examples/#017 ASP.NET/hello.aspx; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Host ASP.NET Framework isolato: servire hello.ashx e invocare la pagina/handler con una richiesta HTTP locale.
```

Risultato atteso: Hello, World!

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
- [https://learn.microsoft.com/en-us/previous-versions/aspnet/ms972975(v=msdn.10)](https://learn.microsoft.com/en-us/previous-versions/aspnet/ms972975(v=msdn.10))
