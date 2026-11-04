# #132 ColdFusion CFC

Voce canonica: `ColdFusion CFC`, tipo `programming`, `language_id: 65`.

Define the CFML Greeting component and call hello() from the control template, also checking a different recipient.

## Toolchain and reproduction

Required native toolchain unavailable or not configured, unavailable version / not verified. Test environment: **Windows x64**.

Requires a CFML engine with syntax script component/function. The CFC file defines a public method with string and default argument; check.cfm uses new Greeting and launches an exception for unexpected results.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
Server Lucee/Adobe ColdFusion locale: servire check.cfm con Greeting.cfc nella stessa directory; curl http://localhost:<porta>/check.cfm
```

Expected result: Component loaded; hello() returns Hello, World!; hello( "Reader" ) returns Hello, Reader!; HTTP answer with greeting.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

La voce canonica CFC è separata dal template ColdFusion. Il saluto è il risultato effettivo di un metodo, e il controllo usa un secondo argomento. Nessuna invocazione del componente è attestata finché il motore manca.

Remaining requirements:

- No Adobe ColdFusion/Lucee engine is configured to load and invoke the component.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain versions and SHA-256 values for the artifacts. The `path_normalization` property documents
local route replacements. `<corpus>` identifies the relative files included in
final corpus, which were first verified in the staging directory.
sources remain those identified by checksums. The only offspring of availability
instruments do not attest parsing or execution.
in the work directory and are not included in the corpus.

## Primary sources

- [https://docs.lucee.org/reference/tags/component.html](https://docs.lucee.org/reference/tags/component.html)
- [https://docs.lucee.org/reference/tags/function.html](https://docs.lucee.org/reference/tags/function.html)
- [https://docs.lucee.org/guides/cookbooks/component.html](https://docs.lucee.org/guides/cookbooks/component.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cfc` | [Greeting.cfc](Greeting.cfc) created; verification pending |
