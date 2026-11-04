# 0575: QMake: `.pri`

## Latest recorded verification

**Syntax and behavior verified** for `.pri`. The primary .pro previously built and ran the console greeting in the same batch. The exact auxiliary .pro then included hello.pri, emitted Project MESSAGE: Hello, World!, and generated its Makefile. Both .pro files and the .pri are covered by the two linked test phases. [Recorded evidence](../../verification/native_20261104_followup_2e70726f.json).

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
