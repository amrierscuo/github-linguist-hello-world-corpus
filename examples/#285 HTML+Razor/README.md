# #285 HTML+Razor

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Renderizzare una view Razor .cshtml con variabile C# audience=World.

Il sorgente usa un blocco Razor @{...} e l’espressione esplicita @(audience). È una view, non un documento HTML già renderizzato. Per eseguirlo serve un host Razor autentico.

## Toolchain e riproduzione

ASP.NET Core Razor con .NET SDK e applicazione host; versioni effettive da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
In un’app ASP.NET Core MVC, salvare il file come Views/Home/Hello.cshtml ed eseguire dotnet build.
```

```text
Renderizzare la view Hello mediante il motore Razor dell’applicazione.
```

## Risultato atteso e stato

HTML contiene <p>Hello, World!</p>.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: È disponibile solo un runtime .NET, senza SDK né host Razor preparato; compiler e renderer non eseguiti.

## Fonti primarie

- https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-10.0

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cshtml` | [hello.cshtml](hello.cshtml) creato, verifiche pendenti |
| `.razor` | [Hello.razor](variants/razor-c914e96c/Hello.razor) creato, verifiche pendenti |
