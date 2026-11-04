# #127 Clue

Voce canonica: `Clue`, tipo `programming`, `language_id: 163763508`.

Fill out the source Clue in Lua and perform it in the official embedded interpreter to print greetings.

## Toolchain and reproduction

Official Clue native compiler and embedded Lua interpreter, clue 3.4.7. Test environment: **Windows x64**.

Official portable distribution Clue 3.4.7 Windows x64 from the ClueLang/Clue. --dontsave repository prevents creating the Lua generated in the example folder; --execute uses the embedded feature interpreter.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
clue --dontsave --execute hello.clue
```

Exit 0; compiler banner plus a Hello, World! line.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Questo è Clue di ClueLang, con concatenamento Lua .. e sintassi C/Rust; local e print sono compilati veramente. Il log mostra compilazione ed esecuzione e registra SHA-256 del binario ufficiale.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain versions and SHA-256 values for the artifacts. The `path_normalization` property documents
local route replacements. `<corpus>` identifies the relative files included in
final corpus, which were first verified in the staging directory.
sources remain those identified by checksums. The only offspring of availability
instruments do not attest parsing or execution.
in the work directory and are not included in the corpus.

## Primary sources

- [https://github.com/ClueLang/Clue](https://github.com/ClueLang/Clue)
- [https://github.com/ClueLang/Clue/wiki](https://github.com/ClueLang/Clue/wiki)
- [https://github.com/ClueLang/Clue/releases/tag/v3.4.7](https://github.com/ClueLang/Clue/releases/tag/v3.4.7)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.clue` | [hello.clue](hello.clue) verified |
