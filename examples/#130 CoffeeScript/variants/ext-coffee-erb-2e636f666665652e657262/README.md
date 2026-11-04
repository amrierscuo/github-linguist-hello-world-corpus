# 0130 CoffeeScript: variant `.coffee.erb`

Role: Template ERB Ruby of the CoffeeScript source; first ERB interpolation, then CoffeeScript.

Type: **adapted**. Starting model: examples/#130 CoffeeScript/hello.coffee; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Ruby ERB con name="World": generare hello.coffee; coffee -c hello.coffee; node hello.js
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

- [https://coffeescript.org/#installation](https://coffeescript.org/#installation)
- [https://coffeescript.org/#strings](https://coffeescript.org/#strings)
- [https://github.com/jashkenas/coffeescript](https://github.com/jashkenas/coffeescript)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.ruby-lang.org/en/master/ERB.html](https://docs.ruby-lang.org/en/master/ERB.html)
- [https://coffeescript.org/](https://coffeescript.org/)
