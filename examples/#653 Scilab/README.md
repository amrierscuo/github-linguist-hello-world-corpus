# #653 Scilab

Run a Scilab file.

## Toolchain

Scilab CLI

## Procedure

scilab-cli -nb -f hello.sce

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- Scilab runtime unavailable.

## Primary sources

- [https://help.scilab.org/docs/2025.1.0/en_US/mprintf.html](https://help.scilab.org/docs/2025.1.0/en_US/mprintf.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sci` | [hello.sci](variants/sci-27617630/hello.sci) created; verification pending |
| `.sce` | [hello.sce](hello.sce), [main.sce](variants/sci-27617630/main.sce) created; verification pending |
| `.tst` | [hello.tst](variants/tst-04f6df08/hello.tst) created; verification pending |
