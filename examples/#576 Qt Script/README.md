# #576 Qt Script

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
| `.qs` | [hello.qs](hello.qs) created; verification pending |
