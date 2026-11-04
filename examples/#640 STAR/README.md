# #640 STAR

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Analyze a STAR block and read the Hello, World! data.

This example STAR uses only the subset scalar compatible with CIF. Gemmi reads the block and decodes the string; it does not declare verification of all STAR constructs.

## Toolchain and reproduction

Gemmi0.7.5 originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

The _greeting value is Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.iucr.org/__data/iucr/cif/standard/cifstd4.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.star` | [hello.star](hello.star) verified |
