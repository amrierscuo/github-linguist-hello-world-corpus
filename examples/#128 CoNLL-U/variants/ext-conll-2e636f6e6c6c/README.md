# 0128 CoNLL-U: variant `.conll`

Role: CoNLL-X table to 10 columns ( HEAD/DEPREL/PHEAD/PDEPREL ), distinct from the columns DEPS/MISC CoNLL-U.

Type: **adapted**. Starting model: examples/#128 CoNLL-U/hello.conllu; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Parser CoNLL-X: leggere hello.conll, verificare quattro token e dependency tree; ricomporre Hello, World!.
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

- [https://universaldependencies.org/format.html](https://universaldependencies.org/format.html)
- [https://github.com/UniversalDependencies/tools/tree/master/udtools](https://github.com/UniversalDependencies/tools/tree/master/udtools)
- [https://universaldependencies.org/u/dep/vocative.html](https://universaldependencies.org/u/dep/vocative.html)
- [https://github.com/EmilStenstrom/conllu](https://github.com/EmilStenstrom/conllu)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://ilk.uvt.nl/conll/](https://ilk.uvt.nl/conll/)
