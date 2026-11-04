# #791 XSLT

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Applicare XSLT1.0 a XML e produrre Hello, World!.

The XSLT processor compiles the sheet and evaluates concat on the content /audience of the original fixture.

## Toolchain and reproduction

lxml6.1.3 con libxslt originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

Hello, World! as a textual result of transformation.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.w3.org/TR/1999/REC-xslt-19991116

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.xslt` | [hello.xslt](variants/xslt-6c8e89da/hello.xslt) created; verification pending |
| `.xsl` | [hello.xsl](hello.xsl) verified |
