# #136 Cooklang

Voce canonica: `Cooklang`, tipo `markup`, `language_id: 788037493`.

Represent greeting as title and instruction of a Cooklang recipe and check out the extracted objects: water, containers and timers.

## Toolchain and reproduction

Official CookCLI Cooklang parser — cookcli 0.37.0 - in food we trust. Ambiente della prova: **Windows x64**.

CookCLI official 0.37.0 portable Windows x64. The recipe uses YAML frontmatter, ingredients @, cookware # and timer ~ according to the extensions supported by this version.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
cook --version; cook recipe hello.cook --format json
```

Expected result: JSON valid: title Hello, World!, servings 1, toilet 250 ml, cookware kettle/cup, timer 1 minutes; parsing exit 0.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Il parser autentico produce il modello JSON, e la prova confronta i valori strutturati sopra indicati. È una verifica dei dati della ricetta, non una esecuzione o un risultato fisico di cucina. Non serve la funzione import con AI né una chiave API.

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

- [https://cooklang.org/docs/spec/](https://cooklang.org/docs/spec/)
- [https://cooklang.org/cli/commands/recipe/](https://cooklang.org/cli/commands/recipe/)
- [https://github.com/cooklang/cookcli/releases/tag/v0.37.0](https://github.com/cooklang/cookcli/releases/tag/v0.37.0)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cook` | [hello.cook](hello.cook) verified |
