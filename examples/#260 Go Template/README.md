# #260 Go Template

Run a Go Template that interpolates Recipient and produces Hello, World!, controlling HTML escaping.

## Toolchain

go version go1.27.1 windows/amd64

## Commands and procedure

go version; go run render.go

## Expected result

World produces Hello, World! more newline; <world> produces Hello, &lt;world&gt;! more newline.

## Status

syntax and behavior verified.

render.go uses html/template.ParseFiles and Execute of the Go runtime, without hand-translating the actions. The named template greeting and its invocation are evaluated; the additional input controls escaping. The checker is support, hello.gotmpl is the canonical sample.

Actual verification of 2026-10-08T12:16:16.831119+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://pkg.go.dev/html/template](https://pkg.go.dev/html/template)
- [https://pkg.go.dev/text/template#hdr-Actions](https://pkg.go.dev/text/template#hdr-Actions)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gohtml` | [hello.gohtml](variants/ext-gohtml-2e676f68746d6c/hello.gohtml) syntax and behavior verified |
| `.gotmpl` | [hello.gotmpl](hello.gotmpl) verified |
| `.html.tmpl` | [hello.html.tmpl](variants/ext-html-tmpl-2e68746d6c2e746d706c/hello.html.tmpl) syntax and behavior verified |
| `.tmpl` | [hello.tmpl](variants/ext-tmpl-2e746d706c/hello.tmpl) syntax and behavior verified |
| `.tpl` | [hello.tpl](variants/ext-tpl-2e74706c/hello.tpl) syntax and behavior verified |

## Additional extension verification

- `.gohtml`: verified on November 4, 2026. [Evidence](verification/native_20261104_260_variants_result.json).
- `.html.tmpl`: verified on November 4, 2026. [Evidence](verification/native_20261104_260_variants_result.json).
- `.tmpl`: verified on November 4, 2026. [Evidence](verification/native_20261104_260_variants_result.json).
- `.tpl`: verified on November 4, 2026. [Evidence](verification/native_20261104_260_variants_result.json).
