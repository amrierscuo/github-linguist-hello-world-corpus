# #477 Nu

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Interpretare Nu e stampare Hello, World!.

The puts form is the builtin of the Nu language. The .nu file is kept distinct from Nushell, which shares the extension.

## Toolchain and reproduction

Nu/nush originale con runtime Objective-C/Foundation; versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
nush hello.nu
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Impedimenti: Nu/Objective-C Foundation non preparati; runtime pendente.

## Primary sources

- https://github.com/programming-nu/nu

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nu` | [hello.nu](hello.nu) created; verification pending |
