# 0178 EJS: variant `.ect`

Ruolo: Template ECT: interpolazione CoffeeScript del membro @greeting, non espressione JavaScript EJS.

Type: **adapted**. Starting model: examples/#178 EJS/hello.ejs; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Node ECT originale: renderizzare hello.ect con greeting="Hello, World!" e confrontare h1.
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

- [https://ejs.co/#docs](https://ejs.co/#docs)
- [https://github.com/mde/ejs](https://github.com/mde/ejs)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://github.com/baryshev/ect](https://github.com/baryshev/ect)
