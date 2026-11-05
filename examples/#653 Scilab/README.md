# #653 Scilab

## Latest recorded verification

**Syntax and behavior verified** on November 5, 2026.

The minimal native Scilab command-line interpreter ran the original .sce script; separately loaded and called the original .sci function through its original companion driver; and executed the .tst assertion. Each emitted the exact greeting. The nwni mode uses GUI/graphics/JVM-disabled libraries, with no display supplied and no GUI library linkage.

[Native commands, versions, outputs and SHA-256](verification/native_20261105_batch_main.json).

## Extension results

- `.sci`: syntax and behavior verified.
- `.sce`: syntax and behavior verified.
- `.tst`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

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
| `.sci` | [hello.sci](variants/sci-27617630/hello.sci) syntax and behavior verified |
| `.sce` | [hello.sce](hello.sce), [main.sce](variants/sci-27617630/main.sce) syntax and behavior verified |
| `.tst` | [hello.tst](variants/tst-04f6df08/hello.tst) syntax and behavior verified |

</details>
