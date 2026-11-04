# 0020 Ada: variant `.ads`

Role: Specification of Ada package with public constant, consumed by the companion program.

Type: **adapted**. Starting model: examples/#020 Ada/hello.adb; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
gnatmake consumer.adb -D <output>; <output>/consumer
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

- [https://gcc.gnu.org/onlinedocs/gnat_ugn/Running-a-Simple-Ada-Program.html](https://gcc.gnu.org/onlinedocs/gnat_ugn/Running-a-Simple-Ada-Program.html)
- [https://learn.adacore.com/courses/intro-to-ada/chapters/imperative_language.html](https://learn.adacore.com/courses/intro-to-ada/chapters/imperative_language.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.adacore.com/live/wave/arm05/html/arm05/RM-7-1.html](https://docs.adacore.com/live/wave/arm05/html/arm05/RM-7-1.html)
