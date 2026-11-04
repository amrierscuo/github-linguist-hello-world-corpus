# #720 Textile

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Render Textile and read Hello, World! from markup HTML.

The authentic Textile maker evaluates the paragraph and the bold. HTMLParser reads the text from the result; it does not replace the Textile parser.

## Toolchain and reproduction

Python Textile4.0.4 originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

HTML <p>Hello, <strong>World</strong>!</p>, testo Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://github.com/textile/python-textile

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.textile` | [hello.textile](hello.textile) verified |
