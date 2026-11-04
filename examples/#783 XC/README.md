# #783 XC

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill out xC for a XMOS target and print Hello, World!.

Original xC source with entry point and IO stdio. It is necessary a toolchain/target XMOS; filling as C with GCC would not verify xC.

## Toolchain and reproduction

XMOS XTC/xcc con target appropriato, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
xcc -target=<target-XMOS-di-prova> hello.xc -o hello.xe; xsim hello.xe
```

## Expected result and status

Hello, World! in simulatore/target. terminal

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: XTC/xcc and target/simulatore XMOS not available; verification pending.

## Primary sources

- https://www.xmos.com/download/XMOS-Programming-Guide-%28documentation%29%28F%29.pdf

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.xc` | [hello.xc](hello.xc) created; verification pending |
