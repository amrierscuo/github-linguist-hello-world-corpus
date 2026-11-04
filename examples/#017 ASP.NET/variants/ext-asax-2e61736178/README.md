# 0017 ASP.NET: variant `.asax`

Role: Global.asax: application event that writes greeting for a request HTTP.

Type: **adapted**. Starting model: examples/#017 ASP.NET / hello.aspx; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Collocare Global.asax nella radice di un host ASP.NET Framework isolato; GET / da un client HTTP locale.
```

Expected result: Hello, World!

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
- [https://learn.microsoft.com/en-us/previous-versions/aspnet/ms178473(v=vs.100)](https://learn.microsoft.com/en-us/previous-versions/aspnet/ms178473(v=vs.100))
