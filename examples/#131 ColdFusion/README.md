# #131 ColdFusion

Voce canonica: `ColdFusion`, tipo `programming`, `language_id: 64`.

Serve a ColdFusion .cfm template that concatenates the greeting parts in cfoutput.

## Toolchain and reproduction

Required native toolchain unavailable or not configured, unavailable version / not verified. Test environment: **Windows x64**.

Requires a CFML Adobe ColdFusion or Lucee engine configured locally; record its version and URL test.The cfsetting/cfcontent tags are part of the template, not simulated with a HTML rendering.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
Server Lucee/Adobe ColdFusion locale: servire hello.cfm; curl http://localhost:<porta>/hello.cfm
```

Expected result: HTTP 200; text/plain response containing Hello, World!, without debug output.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

cfcontent reset=true deletes any previous outputs and cfsetting disables the debug. No engine is configured, so the page has not been parsed or actually requested.

Remaining requirements:

- No Adobe ColdFusion/Lucee engine is configured to serve the template.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain versions and SHA-256 values for the artifacts. The `path_normalization` property documents
local route replacements. `<corpus>` identifies the relative files included in
final corpus, which were first verified in the staging directory.
sources remain those identified by checksums. The only offspring of availability
instruments do not attest parsing or execution.
in the work directory and are not included in the corpus.

## Primary sources

- [https://docs.lucee.org/reference/tags/output.html](https://docs.lucee.org/reference/tags/output.html)
- [https://docs.lucee.org/reference/tags/content.html](https://docs.lucee.org/reference/tags/content.html)
- [https://docs.lucee.org/reference/tags/setting.html](https://docs.lucee.org/reference/tags/setting.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cfm` | [hello.cfm](hello.cfm) created; verification pending |
| `.cfml` | [hello.cfml](variants/ext-cfml-2e63666d6c/hello.cfml) created; verification pending |
