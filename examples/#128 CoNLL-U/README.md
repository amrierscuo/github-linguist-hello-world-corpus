# #128 CoNLL-U

Voce canonica: `CoNLL-U`, tipo `data`, `language_id: 421026389`.

Represent Hello, World! as four tokens CoNLL-U with a UD tree and rebuild exactly the text using SpaceAfter.

## Toolchain and reproduction

Original Universal Dependencies udtools validator and existing conllu reader, 0.2.8; 6.0.0. Test environment: **Windows x64**.

In a venv: python -m pip install udtools== 0.2.8 conllu== 6.0.0. udvalidate is the entry point of the original UniversalDependencies/tools. package The local test invokes the same udtools.cli.main function from Python isolated under work.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
udvalidate --lang en --level 3 hello.conllu; python verify.py hello.conllu
```

Expected result: Original Validator: * ** PASSED ** *; Hello, World! reconstruction; PASS of the assertions on the World token and on the root.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The original validator tests 3: format, tree and universal annotations. It does not declare complete linguistic validation of the successive levels. verify.py uses the existing parser conllu and controls detokenization, root and vocations; the annotations are a small original didactic example, not an external treebank.

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

- [https://universaldependencies.org/format.html](https://universaldependencies.org/format.html)
- [https://github.com/UniversalDependencies/tools/tree/master/udtools](https://github.com/UniversalDependencies/tools/tree/master/udtools)
- [https://universaldependencies.org/u/dep/vocative.html](https://universaldependencies.org/u/dep/vocative.html)
- [https://github.com/EmilStenstrom/conllu](https://github.com/EmilStenstrom/conllu)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.conllu` | [hello.conllu](hello.conllu) verified |
| `.conll` | [hello.conll](variants/ext-conll-2e636f6e6c6c/hello.conll) created; verification pending |
