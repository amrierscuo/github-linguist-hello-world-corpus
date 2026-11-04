# 0280 HTML: variant `.xht`

Role: Document XHTML 1.0 Strict XML well formed and with namespace, distinct from the parsing HTML5.

Type: **adapted**. Starting model: examples/#280 HTML/hello.html; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Parser XML con DTD XHTML locale: validare hello.xht; renderer XHTML: controllare h1.
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

- [https://html.spec.whatwg.org/multipage/](https://html.spec.whatwg.org/multipage/)
- [https://html5lib.readthedocs.io/en/latest/](https://html5lib.readthedocs.io/en/latest/)
- [https://github.com/html5lib/html5lib-python](https://github.com/html5lib/html5lib-python)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://www.w3.org/TR/xhtml1/](https://www.w3.org/TR/xhtml1/)
