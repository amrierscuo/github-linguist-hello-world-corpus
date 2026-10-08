# 0017 ASP.NET — variante `.asax`

Ruolo: Global.asax: evento di applicazione che scrive il saluto per una richiesta HTTP.

Tipo variante: **adapted**. Modello di partenza: examples/#017 ASP.NET/hello.aspx; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Collocare Global.asax nella radice di un host ASP.NET Framework isolato; GET / da un client HTTP locale.
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
- [https://learn.microsoft.com/en-us/previous-versions/aspnet/ms178473(v=vs.100)](https://learn.microsoft.com/en-us/previous-versions/aspnet/ms178473(v=vs.100))
