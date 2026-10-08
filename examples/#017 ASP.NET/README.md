# #017 ASP.NET

`hello.aspx` è una pagina **ASP.NET Web Forms** con una espressione C# eseguita
sul server, che produce `Hello World` come contenuto `text/plain`.

Toolchain verificata: Windows x64, .NET Framework **4.8**, `aspnet_compiler`
**4.8.9221.0**, CLR **4.0.30319.42000**, assembly `System.Web` **4.0.0.0**.
Dalla cartella dell'esempio:

```powershell
powershell -NoProfile -File .\verify.ps1 -BuildDirectory C:\temp\aspnet-check
```

La cartella di build deve essere nuova. Lo script copia la pagina lì, compila
il supporto `VerifyHost.cs` e usa il compilatore ASP.NET del Framework:

```powershell
aspnet_compiler -v / -p C:\temp\aspnet-check\site C:\temp\aspnet-check\precompiled
```

Poi `VerifyHost.exe` crea un dominio ASP.NET mediante `ApplicationHost`, invia
una richiesta a `hello.aspx` usando `HttpRuntime` e confronta la risposta completa
(tolti gli spazi iniziali/finali) con `Hello World`. Risultato atteso:

```text
Rendered: Hello World
PASS: ASP.NET compiled and executed hello.aspx
```

Sintassi e semantica verificate: **sì**, vedere `verification.log`.
La verifica esercita il runtime Web Forms senza aprire porte di rete.
Per riprodurla occorre .NET Framework per Windows con i componenti ASP.NET;
il solo runtime/SDK ASP.NET Core non supporta queste pagine.

Riferimenti primari: [Web Forms, Microsoft](https://learn.microsoft.com/en-us/aspnet/web-forms/what-is-web-forms),
[compilatore ASP.NET](https://learn.microsoft.com/en-us/aspnet/web-forms/overview/moving-to-aspnet-20/configuration-and-instrumentation)
e [ApplicationHost](https://learn.microsoft.com/en-us/dotnet/api/system.web.hosting.applicationhost?view=netframework-4.8.1).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.asax` | [Global.asax](variants/ext-asax-2e61736178/Global.asax) creato, verifiche pendenti |
| `.ascx` | [hello.ascx](variants/ext-ascx-2e61736378/hello.ascx) creato, verifiche pendenti |
| `.ashx` | [hello.ashx](variants/ext-ashx-2e61736878/hello.ashx) creato, verifiche pendenti |
| `.asmx` | [hello.asmx](variants/ext-asmx-2e61736d78/hello.asmx) creato, verifiche pendenti |
| `.aspx` | [hello.aspx](hello.aspx), [host.aspx](variants/ext-ascx-2e61736378/host.aspx) creato, verifiche pendenti |
| `.axd` | [hello.axd](variants/ext-axd-2e617864/hello.axd) creato, verifiche pendenti |
