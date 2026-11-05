# 0133 Common Lisp: variant `.asd`

## Latest recorded verification

**Syntax and behavior verified** for `.asd`. SBCL natively read and executed the exact Lisp variant; when declared, ASDF loaded the original system definition and companion source. The actual script/load output includes Hello, World!. No editor or historical plugin host is implied. [Recorded evidence](../../verification/native_20261105_batch_2e617364.json).

Role: Description ASDF system with Lisp component that emits greeting.

Version type: **adapted**. Start model: examples/#133 Common Lisp/hello.lisp; adattato/originale content for this suffix.

Original variable adapted to the role of the suffix; the existing main files are not modified. No verification is inherited from the model.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
SBCL: require asdf; asdf:load-asd sul file hello.asd; asdf:load-system "corpus-greeting".
```

Expected result: Hello, World!

## Earlier status and evidence
Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://www.sbcl.org/manual/#Shebang-Scripts](https://www.sbcl.org/manual/#Shebang-Scripts)
- [https://www.lispworks.com/documentation/HyperSpec/Body/f_concat.htm](https://www.lispworks.com/documentation/HyperSpec/Body/f_concat.htm)
- [https://www.lispworks.com/documentation/HyperSpec/Body/22_c.htm](https://www.lispworks.com/documentation/HyperSpec/Body/22_c.htm)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://asdf.common-lisp.dev/asdf/Defining-systems-with-defsystem.html](https://asdf.common-lisp.dev/asdf/Defining-systems-with-defsystem.html)
