# #140 Crystal

Voce canonica: `Crystal`, tipo `programming`, language_id `72`.

Interpolate the recipient in a Crystal string, fill it in a native executable and print it.

## Toolchain and reproduction

Crystal 1.11.2 (2024-04-01), LLVM 17.0.6, target x86_64-pc-linux-gnu.

Crystal 1.11.2 and native GC dependencies, libevent and PCRE1. For the extract package set CRYSTAL_PATH to its usr/lib/crystal/lib and LD_LIBRARY_PATH/LIBRARY_PATH to local prefixes containing libraries.

Commands from the directory of the example; `<output>` indicates a temporary directory external to the corpus.

```text
crystal build hello.cr -o <output>/hello
<output>/hello
```

Expected result: Exit 0; executable exit 0, stdout exactly Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The source with interpolation is compiled by the real Crystal toolchain and executed as binary Linux x86_64. Fixed the dependence of libpcre3-dev link with local Ubuntu package extraction, without global installation.

Real test: [finish.json](verification/finish.json), with UTC, commands, versions, exit code, stdout/stderr and SHA-256 of sources.

## Primary sources

- https://crystal-lang.org/reference/1.11/
- https://crystal-lang.org/reference/1.11/syntax_and_semantics/literals/string.html
- https://crystal-lang.org/reference/1.11/man/crystal/index.html

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.cr` | [hello.cr](hello.cr) syntax and behavior verified |
