# #797 YANG

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Validate a YANG1.1 model and read the default Hello, World!.

Pyang controls the grammar and constraints of modello/default and the driver reads the validated leaf. The goal is the default value of the model; no dispositivo/NETCONF is configured.

## Toolchain and reproduction

Pyang2.7.1 originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

Modello valido, leaf greeting di tipo string con default Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.rfc-editor.org/rfc/rfc7950.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.yang` | [corpus-greeting.yang](corpus-greeting.yang) verified |
