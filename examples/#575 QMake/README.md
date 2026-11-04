# #575 QMake

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
| `.pro` | [hello.pro](hello.pro), [main.pro](variants/pri-e5eeb81c/main.pro) created; verification pending |
| `.pri` | [hello.pri](variants/pri-e5eeb81c/hello.pri) created; verification pending |
