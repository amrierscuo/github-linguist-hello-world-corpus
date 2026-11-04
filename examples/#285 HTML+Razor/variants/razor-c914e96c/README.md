# 0285: HTML+Razor: `.razor`

## Recorded verification

**Syntax and behavior verified** on November 4, 2026. The ASP.NET Core MVC view engine rendered the original view, and Blazor HtmlRenderer rendered the original component. Each produced <p>Hello, World!</p> in memory. [Evidence](../../verification/native_20261104_html_razor_result.json).

Role: Component Razor Blazor with markup and field C#, distinct from page MVC .cshtml.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: ASP.NET Core Razor con .NET SDK e applicazione host; versioni effettive da registrare. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
SDK .NET con Blazor: aggiungere Hello.razor a un progetto e renderizzare il componente
```

Expected result: Element p con Hello, World!

Earlier status (before this check): Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `Hello.razor`: `7e37c225ae71b2b827243c4ace306420be08d7990f782e0d3b8ed74167b9d343`

Primary sources:

- https://learn.microsoft.com/en-us/aspnet/core/blazor/components/
- https://learn.microsoft.com/en-us/aspnet/core/mvc/views/razor?view=aspnetcore-10.0
