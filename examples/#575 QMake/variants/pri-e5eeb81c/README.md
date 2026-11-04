# 0575: QMake: `.pri`

Includes qmake with variable and message, consumed by a companion project.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.pri`.

Control provided, from the folder of the variant:

```text
qmake main.pro -o work/Makefile
```

Expected result: qmake signals Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://doc.qt.io/qt-6/qmake-project-files.html](https://doc.qt.io/qt-6/qmake-project-files.html)
