# #285 HTML+Razor

The ASP.NET Core MVC view engine rendered the original view, and Blazor HtmlRenderer rendered the original component. Each produced <p>Hello, World!</p> in memory.

Canonical type: `markup`. Linguist language ID: `479039817`.

## Recorded verification

**Syntax and behavior verified** on November 4, 2026 with .NET SDK 8.0.318 and ASP.NET Core 8.0.21.

[Recorded commands, outputs and hashes](verification/native_20261104_html_razor_result.json).

## Reproduce the check

Copy `verification/razor/` to a scratch directory, then copy `hello.cshtml` to `Views/Home/Hello.cshtml` and `variants/razor-c914e96c/Hello.razor` to `Hello.razor` there. With the .NET 8 SDK and ASP.NET Core installed, run:

```sh
dotnet build --disable-build-servers -c Release -p:RestoreConfigFile=NuGet.Config
dotnet bin/Release/net8.0/RazorHarness.dll
```

The fixture renders in memory with ephemeral keys and does not start a web server.

## Primary sources

- https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-10.0

## Extension coverage

| Extension | Files | Status |
| --- | --- | --- |
| `.cshtml` | [hello.cshtml](hello.cshtml) | Syntax and behavior verified |
| `.razor` | [Hello.razor](variants/razor-c914e96c/Hello.razor) | Syntax and behavior verified |
