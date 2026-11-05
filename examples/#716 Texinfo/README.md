# #716 Texinfo

## Latest recorded verification

Latest extension checks:
- `.texinfo`: GNU Texinfo parsed and rendered the exact suffix variant as plain text containing Hello, World!, without a viewer or graphical application. [Evidence](verification/native_20261105_batch_2e746578696e666f.json).
- `.txi`: GNU Texinfo parsed and rendered the exact suffix variant as plain text containing Hello, World!, without a viewer or graphical application. [Evidence](verification/native_20261105_batch_2e747869.json).

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Render a Texinfo document with Hello, World!.

Texi2any/makeinfo original analyzes nodes and directives and generates simple text.

## Toolchain and reproduction

GNU Texinfo7.1 originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
makeinfo --plaintext --output=- hello.texi
```

## Expected result and status

Document rendered contains Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.gnu.org/software/texinfo/manual/texinfo/html_node/Short-Sample.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.texinfo` | [hello.texinfo](variants/texinfo-67e352f4/hello.texinfo) syntax and behavior verified |
| `.texi` | [hello.texi](hello.texi) verified |
| `.txi` | [hello.txi](variants/txi-415ac389/hello.txi) syntax and behavior verified |