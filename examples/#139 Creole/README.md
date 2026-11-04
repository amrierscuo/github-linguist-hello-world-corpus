# #139 Creole

Voce canonica: `Creole`, tipo `prose`, `language_id: 71`.

Rendering a document Creole 1.0 with heading, Greeting in bold and a phrase in italics.

## Toolchain and reproduction

Existing creoleparser Creole 1.0 renderr with Genshi, 0.7.5; 0.7.11. Test environment: **Windows x64**.

Python 3.13.9, creoleparser 0.7.5 and Genshi 0.7.11. Insulated dependencies in work; to reproduce use a venv. The returnr returns byte UTF - 8, which verify.py decodes before the assertions.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
python -m pip install creoleparser==0.7.5; python verify.py hello.creole
```

Expected result: HTML with <h1>Greeting</h1>, <strong> Hello, World! </strong> and control <em>A small Creole document.</em>; PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

It is the parser/renderer Creole 1.0 existing, which is permissive for generic text. The test concerns the acceptance and rendering of the three declared structures, not a universal strict validator for all wiki extensions.

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

- [https://github.com/wikiotics/creoleparser](https://github.com/wikiotics/creoleparser)
- [https://creoleparser.readthedocs.io/en/latest/](https://creoleparser.readthedocs.io/en/latest/)
- [https://www.wikicreole.org/wiki/Creole1.0](https://www.wikicreole.org/wiki/Creole1.0)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.creole` | [hello.creole](hello.creole) verified |
