# #576 Qt Script

## Latest recorded verification

**Syntax and behavior verified** on November 5, 2026.

The unchanged C++ QCoreApplication consumer loaded the exact hello.qs into the native Qt5 QScriptEngine and printed its final value, Hello, World!, with exit0 and no exceptions. No display variables were supplied, and no QtGui/QtWidgets libraries or GUI processes were used.

[Native commands, versions, outputs and SHA-256](verification/native_20261105_batch_main.json).

## Extension results

- `.qs`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Evaluate ECMAScript in the real QScriptEngine.

## Toolchain

Qt 5 QtScript; C++

## Procedure

Fill in main.cpp by connecting Qt5Core and Qt5Script; run in the hello.qs folder.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

The script returns a string as a final value; the consumer C++ uses evaluate and controls native exceptions.

Remaining requirements:
- Qt5Script/Qt Core compiler e librerie non predisposti.

## Primary sources

- [https://doc.qt.io/archives/qt-5.15/qtscript-index.html](https://doc.qt.io/archives/qt-5.15/qtscript-index.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.qs` | [hello.qs](hello.qs) syntax and behavior verified |

</details>
