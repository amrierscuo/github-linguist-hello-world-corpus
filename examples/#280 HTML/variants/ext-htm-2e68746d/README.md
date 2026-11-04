# 0280 HTML: variant `.htm`

Role: Page in subset HTML common; .html.hl remains HTML/Hoplon format, not source ClojureScript .cljs.hl.

Tipo variante: **alias**. Copia byte-identica di examples/#280 HTML/hello.html

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Reader HTML del modello: caricare hello.htm e controllare il DOM h1; per .html.hl usare inoltre il frontend HTML/Hoplon dedicato.
```

Expected result: Zero errors parser; heading Hello, World!; PASS.

## Status

Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://html.spec.whatwg.org/multipage/](https://html.spec.whatwg.org/multipage/)
- [https://html5lib.readthedocs.io/en/latest/](https://html5lib.readthedocs.io/en/latest/)
- [https://github.com/html5lib/html5lib-python](https://github.com/html5lib/html5lib-python)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
