# 0203 FPP: variant `.fppi`

Role: Fragment FPP included within a module.

Type: **adapted**. Starting model: examples/#203 FPP/hello.fpp; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
fpp-check consumer.fpp; fpp-to-xml -d <output> consumer.fpp; controllare constant Greeting.
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

- [https://nasa.github.io/fpp/fpp-spec.html](https://nasa.github.io/fpp/fpp-spec.html)
- [https://nasa.github.io/fpp/fpp-users-guide.html](https://nasa.github.io/fpp/fpp-users-guide.html)
- [https://github.com/nasa/fpp](https://github.com/nasa/fpp)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://nasa.github.io/fpp/fpp-user-guide.html](https://nasa.github.io/fpp/fpp-user-guide.html)
