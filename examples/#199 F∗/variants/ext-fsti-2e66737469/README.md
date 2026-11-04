# 0199 F*: variant `.fsti`

Role: Sign F* of the main function, with FST implementation of the same name.

Type: **adapted**. Departure model: examples/#199 F variable/ Hello.fst; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
F* originale: typecheck Hello.fsti e Hello.fst; estrarre e invocare Hello.main().
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

- [https://fstar-lang.org/tutorial/book/part1/part1_getting_off_the_ground.html](https://fstar-lang.org/tutorial/book/part1/part1_getting_off_the_ground.html)
- [https://github.com/FStarLang/FStar/blob/master/ulib/FStar.IO.fsti](https://github.com/FStarLang/FStar/blob/master/ulib/FStar.IO.fsti)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://fstar-lang.org/tutorial/book/part1/part1_modules.html](https://fstar-lang.org/tutorial/book/part1/part1_modules.html)
