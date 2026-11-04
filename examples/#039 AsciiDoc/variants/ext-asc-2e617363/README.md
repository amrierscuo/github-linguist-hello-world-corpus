# 0039 AsciiDoc: variant `.asc`

## Recorded verification

**Syntax and behavior verified** on November 4, 2026. Load each source with Asciidoctor.js and assert document title, the exact paragraph, rendered HTML and no diagnostics. [Evidence](../../verification/native_20261104_039_variants_result.json).

Role: Textual Alias of the same format and of the same programma/dataset of the original model.

Tipo variante: **alias**. Copia byte-identica di examples/#039 AsciiDoc/hello.adoc

Byte-identical copy of the stated model: byte equality is not equivalent to a new toolchain test on the new suffix.

## Verification command or procedure

From the directory of the variant, except for explicit references to the model. `<output>`
indicates an external temporary directory; dependencies and compiled products do not
part of the deliverable.

```text
asciidoctor hello.asc -o <output>/hello.html
```

Expected result: Title Greeting, exactly a paragraph Hello, World!, HTML contains <p> Hello, World! </p>, zero diagnostics and exit 0.

## Earlier status
Artefatto: **created**.
syntax: **not verified**. behavior: **not verified**.
No positive flag is inherited from the main sample or another suffix.
Checking only the bytes or metadata does not establish parsing or execution.

Remaining requirements:
- The variant has not yet been checked with the native toolchain indicated.

## Primary sources

- [https://docs.asciidoctor.org/asciidoc/latest/](https://docs.asciidoctor.org/asciidoc/latest/)
- [https://docs.asciidoctor.org/asciidoctor.js/latest/setup/migration-guide/](https://docs.asciidoctor.org/asciidoctor.js/latest/setup/migration-guide/)
- [https://docs.asciidoctor.org/asciidoctor.js/3.0/processor/logging-api/](https://docs.asciidoctor.org/asciidoctor.js/3.0/processor/logging-api/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
