# 0260 Go Template: variant `.html.tmpl`

## Recorded verification

**Syntax and behavior verified** on November 4, 2026. Parse and execute original templates with Go html/template; assert the greeting and HTML escaping. [Evidence](../../verification/native_20261104_260_variants_result.json).

Role: Template Go with define/template and interpolation; conventional suffix of the view, no template engine of other languages.

Tipo variante: **alias**. Copia byte-identica di examples/#260 Go Template/hello.gotmpl

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
Go html/template: ParseFiles("hello.html.tmpl"); Execute con Recipient="World"; confrontare Hello, World!.
```

Expected result: World produces Hello, World! more newline; <world> produces Hello, &lt;world&gt;! more newline.

## Earlier status
Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://pkg.go.dev/html/template](https://pkg.go.dev/html/template)
- [https://pkg.go.dev/text/template#hdr-Actions](https://pkg.go.dev/text/template#hdr-Actions)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
