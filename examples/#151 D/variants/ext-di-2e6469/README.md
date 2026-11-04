# 0151 D: variant `.di`

Ruolo: Interface file D di con dichiarazione pubblica, implementazione e consumer separati.

Type: **adapted**. Starting model: examples/#151 D/hello.d; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
ldc2 -betterC consumer.d greeting.d -of=<output>/hello; <output>/hello
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

- [https://dlang.org/spec/betterc.html](https://dlang.org/spec/betterc.html)
- [https://github.com/ldc-developers/ldc/releases/tag/v1.43.0](https://github.com/ldc-developers/ldc/releases/tag/v1.43.0)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://dlang.org/spec/d_interface.html](https://dlang.org/spec/d_interface.html)
