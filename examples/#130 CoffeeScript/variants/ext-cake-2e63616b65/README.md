# 0130 CoffeeScript: variant `.cake`

## Latest recorded verification

**Syntax and behavior verified** for `.cake`. Original .cake copied byte-identically as Cakefile. Official Cake task executed; main example unchanged. [Recorded evidence](../../verification/native_20261104_followup_2e63616b65.json).

Role: Cake task CoffeeScript, distinguished from .cake C# file of the 84. voice

Type: **adapted**. Starting model: examples/#130 CoffeeScript/hello.coffee; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
CoffeeScript cake: nel progetto temporaneo caricare hello.cake come Cakefile ed eseguire cake hello.
```

Expected result: Hello, World!

## Earlier status and evidence
Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://coffeescript.org/#installation](https://coffeescript.org/#installation)
- [https://coffeescript.org/#strings](https://coffeescript.org/#strings)
- [https://github.com/jashkenas/coffeescript](https://github.com/jashkenas/coffeescript)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://coffeescript.org/#cake](https://coffeescript.org/#cake)
