# #039 AsciiDoc

Convert the AsciiDoc document under the title Greeting and a Hello, World! paragraph into HTML while keeping the text of the paragraph.

## File

- `hello.adoc`
- `check.cjs`
- `package.json`

## Toolchain and verification

Node.js v22.20.0; @asciidoctor/core 4.1.1 (Asciidoctor.js).

From the example directory:

```sh
npm install
node check.cjs
```

`package.json` fixes `@asciidoctor/core` to 4.1.1. The checker uses `await`
for parsing and conversion, as required by API v4.
of the document and the HTML result; `MemoryLogger` captures diagnostics.
The HTML is controlled in memory and is not saved as an additional artifact.

## Expected result

Title Greeting, exactly a paragraph Hello, World!, HTML contains <p> Hello, World! </p>, zero diagnostics and exit 0.

## State of the test

syntax verified. behavior verified.

Parsing e conversione HTML realmente eseguiti con API asincrona v4. HTML derivato controllato in memoria; nessun file .build consegnato.

Actual Windows x64 test of 2026-10-08T11:01:56.068379+00:00: [log](verification/result.json).
The log includes hash SHA-256 of the source, observed versions, commands, exit codes, stdout and stderr.

## Primary sources

- [https://docs.asciidoctor.org/asciidoc/latest/](https://docs.asciidoctor.org/asciidoc/latest/)
- [https://docs.asciidoctor.org/asciidoctor.js/latest/setup/migration-guide/](https://docs.asciidoctor.org/asciidoctor.js/latest/setup/migration-guide/)
- [https://docs.asciidoctor.org/asciidoctor.js/3.0/processor/logging-api/](https://docs.asciidoctor.org/asciidoctor.js/3.0/processor/logging-api/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.asciidoc` | [hello.asciidoc](variants/ext-asciidoc-2e6173636969646f63/hello.asciidoc) syntax and behavior verified |
| `.adoc` | [hello.adoc](hello.adoc) verified |
| `.asc` | [hello.asc](variants/ext-asc-2e617363/hello.asc) syntax and behavior verified |

## Additional extension verification

- `.asciidoc`: verified on November 4, 2026. [Evidence](verification/native_20261104_039_variants_result.json).
- `.asc`: verified on November 4, 2026. [Evidence](verification/native_20261104_039_variants_result.json).
