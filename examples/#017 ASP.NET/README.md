# #017 ASP.NET

`hello.aspx` is a **ASP.NET Web Forms** page with a C# expression performed
on the server, which produces `Hello World` as `text/plain` content.

Toolchain verified: Windows x64, .NET Framework **4.8**, `aspnet_compiler`
**4.8.9221.0**, CLR **4.0.30319.42000**, assembly `System.Web` **4.0.0.0**.
From the example directory:

```powershell
powershell -NoProfile -File .\verify.ps1 -BuildDirectory C:\temp\aspnet-check
```

The build folder must be new. The script copies the page there, fill in
`VerifyHost.cs` support and use the ASP.NET compiler of the Framework:

```powershell
aspnet_compiler -v / -p C:\temp\aspnet-check\site C:\temp\aspnet-check\precompiled
```

Then `VerifyHost.exe` creates a domain ASP.NET by `ApplicationHost`, send
a request to `hello.aspx` using `HttpRuntime` and compares the complete answer
(took the iniziali/finali spaces) with `Hello World`. Expected result:

```text
Rendered: Hello World
PASS: ASP.NET compiled and executed hello.aspx
```

syntax and behavior verified: **sì**, vedere `verification.log`.
The verification exercises the Web Forms runtime without opening network ports.
To reproduce it you need .NET Framework for Windows with ASP.NET components;
the only runtime/SDK ASP.NET Core does not support these pages.

Riferimenti primari: [Web Forms, Microsoft](https://learn.microsoft.com/en-us/aspnet/web-forms/what-is-web-forms),
[compilatore ASP.NET](https://learn.microsoft.com/en-us/aspnet/web-forms/overview/moving-to-aspnet-20/configuration-and-instrumentation)
e [ApplicationHost](https://learn.microsoft.com/en-us/dotnet/api/system.web.hosting.applicationhost?view=netframework-4.8.1).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.asax` | [Global.asax](variants/ext-asax-2e61736178/Global.asax) created; verification pending |
| `.ascx` | [hello.ascx](variants/ext-ascx-2e61736378/hello.ascx) created; verification pending |
| `.ashx` | [hello.ashx](variants/ext-ashx-2e61736878/hello.ashx) created; verification pending |
| `.asmx` | [hello.asmx](variants/ext-asmx-2e61736d78/hello.asmx) created; verification pending |
| `.aspx` | [hello.aspx](hello.aspx), [host.aspx](variants/ext-ascx-2e61736378/host.aspx) created; verification pending |
| `.axd` | [hello.axd](variants/ext-axd-2e617864/hello.axd) created; verification pending |
