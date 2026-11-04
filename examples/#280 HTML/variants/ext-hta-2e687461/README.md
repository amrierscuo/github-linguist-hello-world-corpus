# 0280 HTML: variant `.hta`

Role: HTML Application Windows with hta:application element and visible text, without script or filesystem operations.

Type: **adapted**. Starting model: examples/#280 HTML/hello.html; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Windows in ambiente di prova: mshta.exe hello.hta; verificare il saluto nell’interfaccia nativa e chiudere la finestra.
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
- [https://learn.microsoft.com/en-us/previous-versions/ms536496(v=vs.85)](https://learn.microsoft.com/en-us/previous-versions/ms536496(v=vs.85))
