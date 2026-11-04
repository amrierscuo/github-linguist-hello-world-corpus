# 0122 Clean: variant `.dcl`

Ruolo: Modulo di definizione Clean .dcl, con implementazione .icl e programma consumer.

Type: **adapted**. Starting model: examples/#122 Clean/Hello.icl; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Clean clm: compilare Consumer con Greeting.dcl/Greeting.icl nel module path; eseguire il programma esterno.
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

- [https://clean.cs.ru.nl/Download_Clean](https://clean.cs.ru.nl/Download_Clean)
- [https://clean.cs.ru.nl/*NIX_Instructions](https://clean.cs.ru.nl/*NIX_Instructions)
- [https://clean.cs.ru.nl/Clean_language_report](https://clean.cs.ru.nl/Clean_language_report)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://clean.cs.ru.nl/Language_Report](https://clean.cs.ru.nl/Language_Report)
