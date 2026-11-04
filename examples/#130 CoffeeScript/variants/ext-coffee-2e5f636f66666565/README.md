# 0130 CoffeeScript: variant `._coffee`

## Latest recorded verification

**Syntax and behavior verified** for `._coffee`. Unchanged suffix variant; main example status unchanged. [Recorded evidence](../../verification/native_20261104_followup_2e5f636f66666565.json).

Role: Common CoffeeScript subset without asynchronous extensions; the suffix selects the appropriate frontend Streamline/Iced.

Tipo variante: **alias**. Copia byte-identica di examples/#130 CoffeeScript/hello.coffee

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
coffee hello._coffee
```

Expected result: Exit 0; runtime exit 0; Hello, World! followed by newline.

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
