# 0225 GAP: variant `.tst`

Ruolo: Transcript di test GAP tst con prompt e risultato atteso, non script g rinominato.

Type: **adapted**. Starting model: examples/#225 GAP/hello.g; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
gap -q -c 'Test("hello.tst"); QUIT_GAP(0);'
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

- [https://docs.gap-system.org/doc/tut/manual.pdf](https://docs.gap-system.org/doc/tut/manual.pdf)
- [https://www.gap-system.org/](https://www.gap-system.org/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.gap-system.org/doc/ref/chap7.html](https://docs.gap-system.org/doc/ref/chap7.html)
