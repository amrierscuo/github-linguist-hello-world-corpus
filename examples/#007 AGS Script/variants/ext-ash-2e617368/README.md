# 0007 AGS Script: variant `.ash`

Role: Header AGS with global function statement implemented in the companion.

Type: **adapted**. Starting model: examples/#007 AGS Script/room1.asc; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
In un progetto AGS di prova: importare hello.ash come script header e greeting.asc come global script; chiamare ShowCorpusGreeting() da un evento.
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

- [https://adventuregamestudio.github.io/ags-manual/Globalfunctions_Message.html](https://adventuregamestudio.github.io/ags-manual/Globalfunctions_Message.html)
- [https://adventuregamestudio.github.io/ags-manual/EventTypes.html](https://adventuregamestudio.github.io/ags-manual/EventTypes.html)
- [https://adventuregamestudio.github.io/ags-manual/DistGame.html](https://adventuregamestudio.github.io/ags-manual/DistGame.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://adventuregamestudio.github.io/ags-manual/ImportingFunctionsAndVariables.html](https://adventuregamestudio.github.io/ags-manual/ImportingFunctionsAndVariables.html)
