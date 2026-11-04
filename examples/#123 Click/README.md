# #123 Click

Voce canonica: `Click`, tipo `programming`, `language_id: 61`.

Run a Click Active Script that issues Hello, World! and stops the userlevel driver.

## Toolchain and reproduction

Required native toolchain unavailable or not configured, unavailable version / not verified. Test environment: **Windows x64**.

Richiede il driver userlevel di The Click Modular Router, compilato dal repository kohler/click con l’elemento standard Script. Nessuna scheda di rete, pacchetto reale o modulo kernel è necessario.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
click hello.click
```

Expected result: Accepted Click configuration; a Hello, World! line in the Click diagnostic stream; finished driver.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The .click entry is the configuration language of the modular router. The file contains a Script element with TYPE ACTIVE, print and stop. The driver is not available: no parser/runtime is attested.

Remaining requirements:

- Click Modular Router userlevel binary is not available; Script configuration has not been parsed/run.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain versions and SHA-256 values for the artifacts. The `path_normalization` property documents
local route replacements. `<corpus>` identifies the relative files included in
final corpus, which were first verified in the staging directory.
sources remain those identified by checksums. The only offspring of availability
instruments do not attest parsing or execution.
in the work directory and are not included in the corpus.

## Primary sources

- [https://github.com/kohler/click](https://github.com/kohler/click)
- [https://github.com/kohler/click/blob/master/elements/standard/script.hh](https://github.com/kohler/click/blob/master/elements/standard/script.hh)
- [https://github.com/kohler/click/blob/master/doc/click.5](https://github.com/kohler/click/blob/master/doc/click.5)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.click` | [hello.click](hello.click) created; verification pending |
