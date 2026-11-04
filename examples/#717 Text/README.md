# #717 Text

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Read the greeting as UTF8 text.

The text canonical entry is prose: the verification consists of decoding UTF8 and comparing the content, without declaring a compiler.

## Toolchain and reproduction

Codec UTF8 and original file reader of the standard Python library

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

Hello, World! con LF finale.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://docs.python.org/3/library/pathlib.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.txt` | [hello.txt](hello.txt) verified |
| `.fr` | [hello.fr](variants/fr-859c52c1/hello.fr) created; verification pending |
| `.nb` | [hello.nb](variants/nb-af372417/hello.nb) created; verification pending |
| `.ncl` | [hello.ncl](variants/ncl-381c21d0/hello.ncl) created; verification pending |
| `.no` | [hello.no](variants/no-0f00f447/hello.no) created; verification pending |
