# #575 QMake

## Latest recorded verification

**Syntax and behavior verified** on November 4, 2026.

The original qmake project was generated and compiled by Qt; its console-only program printed the exact greeting. No GUI was used.

[Native commands, versions, outputs and SHA-256](verification/native_20261104_followup_main.json).

## Extension results

- `.pro`: syntax and behavior verified. [Evidence](verification/native_20261104_followup_2e70726f.json).
- `.pri`: syntax and behavior verified. [Evidence](verification/native_20261104_followup_2e70726f.json).

<details>
<summary>Original instructions and earlier status</summary>

Generate and compile a qmake Qt Core project.

## Toolchain

qmake; Qt Core; C++

## Procedure

qmake hello.pro; make; ./hello

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- qmake e Qt Core development libraries non predisposti.

## Primary sources

- [https://doc.qt.io/qt-6/qmake-project-files.html](https://doc.qt.io/qt-6/qmake-project-files.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pro` | [hello.pro](hello.pro), [main.pro](variants/pri-e5eeb81c/main.pro) syntax and behavior verified |
| `.pri` | [hello.pri](variants/pri-e5eeb81c/hello.pri) syntax and behavior verified |

</details>
