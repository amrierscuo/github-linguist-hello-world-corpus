# #808 Zimpl

## Latest recorded verification

**Syntax and behavior verified** on November 5, 2026.

After explicitly binding the indexed-variable iterator in the three declared sources, native Zimpl generated each LP and GLPK solved it to optimality. The thirteen native solution variables decode to exactly Hello, World!. Each suffix was compiled and solved separately.

[Native commands, versions, outputs and SHA-256](verification/native_20261105_batch_main.json).

The indexed variable declaration was minimally corrected to bind its iterator explicitly. The same correction was compiled and solved separately for every suffix listed below. [Original compiler failure](verification/native_20261105_batch_original_failure.json).

## Extension results

- `.zimpl`: syntax and behavior verified.
- `.zmpl`: syntax and behavior verified.
- `.zpl`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Generate and solve a LP Zimpl whose excellent encodes greeting bytes.

## Toolchain

Zimpl; LP solver

## Procedure

zimpl -o build/hello hello.zpl; glpsol --lp build/hello.lp; read and decode the optimal x[i].

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

Original indexed variables have bounds [ ASCII, ASCII + 1 ]; the minimizing objective must choose the lower codes.

Remaining requirements:
- Zimpl compiler unavailable nei pacchetti isolati; parsing/generazione LP e soluzione pending.

## Primary sources

- [https://zimpl.zib.de/](https://zimpl.zib.de/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.zimpl` | [hello.zimpl](variants/zimpl-c607d319/hello.zimpl) syntax and behavior verified |
| `.zmpl` | [hello.zmpl](variants/zmpl-c5eac23d/hello.zmpl) syntax and behavior verified |
| `.zpl` | [hello.zpl](hello.zpl) syntax and behavior verified |

</details>
