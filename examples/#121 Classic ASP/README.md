# #121 Classic ASP

Voce canonica: `Classic ASP`, tipo `programming`, `language_id: 8`.

Serve a Classic ASP page in VBScript and write Hello, World! in the response body HTTP text/plain.

## Toolchain and reproduction

Required native toolchain unavailable or not configured, unavailable version / not verified. Test environment: **Windows x64**.

It requires IIS with the Classic ASP feature and the VBScript engine. Use a dedicated local site. cscript.exe exists, but does not provide the ASP Response object and does not demonstrate the validity of the page.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
IIS locale con ASP abilitato: pubblicare hello.asp nel sito di prova; curl http://localhost:<porta>/hello.asp
```

Expected result: HTTP 200; body containing exactly the Hello, World! greeting, with possible newline of end of page.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Language=VBScript, Option Explicit, ContentType and string concatenation are original ASP source. The test records availability of the VBScript host; a real IIS request is missing, so both flags remain false.

Remaining requirements:

- Classic ASP requires IIS ASP request context; cscript/WScript VBScript alone does not provide Response.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain versions and SHA-256 values for the artifacts. The `path_normalization` property documents
local route replacements. `<corpus>` identifies the relative files included in
final corpus, which were first verified in the staging directory.
sources remain those identified by checksums. The only offspring of availability
instruments do not attest parsing or execution.
in the work directory and are not included in the corpus.

## Primary sources

- [https://learn.microsoft.com/en-us/previous-versions/iis/6.0-sdk/ms524741(v=vs.90)](https://learn.microsoft.com/en-us/previous-versions/iis/6.0-sdk/ms524741(v=vs.90))
- [https://learn.microsoft.com/en-us/previous-versions/iis/6.0-sdk/ms525585(v=vs.90)](https://learn.microsoft.com/en-us/previous-versions/iis/6.0-sdk/ms525585(v=vs.90))
- [https://learn.microsoft.com/en-us/iis/configuration/system.webserver/asp/](https://learn.microsoft.com/en-us/iis/configuration/system.webserver/asp/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.asp` | [hello.asp](hello.asp) created; verification pending |
