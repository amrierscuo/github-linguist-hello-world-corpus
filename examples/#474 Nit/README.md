# #474 Nit

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Interpret or fill out Nit and print Hello, World!.

The var audience is interpolated in the Nit string with {audience}; print is greeting.

## Toolchain and reproduction

Nit/nitc originali; versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
nit hello.nit
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Compiler/interprete Nit not prepared.

## Primary sources

- https://nitlanguage.org/tools/nit.html
- https://nitlanguage.org/doc/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nit` | [hello.nit](hello.nit) created; verification pending |
