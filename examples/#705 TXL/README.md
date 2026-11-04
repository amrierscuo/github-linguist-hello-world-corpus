# #705 TXL

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Turn a token sequence into a TXL greeting string.

Grammatic program as repeat token and main rewriting function; the stringlit output represents greeting.

## Toolchain and reproduction

TXL, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
txl input.txt hello.txl
```

## Expected result and status

Token stringlit "Hello, World!" in output.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Interpreting TXL unavailable; hanging parser and transformation.

## Primary sources

- https://www.txl.ca/plow2014.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.txl` | [hello.txl](hello.txl) created; verification pending |
