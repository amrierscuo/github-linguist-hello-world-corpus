# #795 Xtend

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill in Xtend and print Hello, World!.

Programma Xtend originale con val e println. Un compilatore Java applicato direttamente al file non verifica Xtend.

## Toolchain and reproduction

Eclipse Xtend compiler/Xbase, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
Eclipse Xtend: compilare Hello.xtend nel progetto Java di prova e avviare Hello.main
```

## Expected result and status

Hello, World! su stdout.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Impedimenti: Compiler Xtend/Xbase non predisposto; generazione Java ed esecuzione pendenti.

## Primary sources

- https://eclipse.dev/xtend/documentation/102_basics.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.xtend` | [Hello.xtend](Hello.xtend) created; verification pending |
