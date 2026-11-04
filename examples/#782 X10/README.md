# #782 X10

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill in X10 and print Hello, World!.

X10 program with main(Rail[String]) and x10.io.Console; the ordinary Java toolchain does not replace X10.

## Toolchain and reproduction

Compilatore/runtime X10, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
x10c Hello.x10; x10 Hello
```

## Expected result and status

Hello, World! su stdout.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Filler X10 unavailable; parser and hanging execution.

## Primary sources

- https://x10-lang.org/articles/11.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.x10` | [Hello.x10](Hello.x10) created; verification pending |
