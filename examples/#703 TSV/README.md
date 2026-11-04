# #703 TSV

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Analyze a TSV table and read the Hello, World! value.

Table with header key and value; csv.DictReader really uses the TAB delimiter.

## Toolchain and reproduction

Python csv original; version in the log

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

A data line, greeting key, Hello, World! value.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://docs.python.org/3/library/csv.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.tsv` | [hello.tsv](hello.tsv) verified |
| `.vcf` | [hello.vcf](variants/vcf-96d2ee95/hello.vcf) created; verification pending |
