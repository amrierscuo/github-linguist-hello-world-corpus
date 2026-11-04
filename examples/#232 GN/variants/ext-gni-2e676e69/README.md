# 0232 GN: variant `.gni`

Role: Includes GN with statement of build arguments, imported by BUILD.gn.

Type: **adapted**. Starting model: examples/#232 GN/.gn; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
GN nel progetto temporaneo del modello: importare hello.gni, passare corpus_greeting all’azione e usare gn gen + ninja.
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

- [https://gn.googlesource.com/gn/+/main/docs/quick_start.md](https://gn.googlesource.com/gn/+/main/docs/quick_start.md)
- [https://gn.googlesource.com/gn/+/main/docs/reference.md](https://gn.googlesource.com/gn/+/main/docs/reference.md)
- [https://ninja-build.org/manual.html](https://ninja-build.org/manual.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
