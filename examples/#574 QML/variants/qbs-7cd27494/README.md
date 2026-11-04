# 0574: QML: `.qbs`

Project Qbs with a JavaScript rule that produces greeting; distinct from QtQuick.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.qbs`.

Control provided, from the folder of the variant:

```text
qbs build -f hello.qbs --build-directory work/qbs
```

Expected result: greeting.txt contains Hello, World! and LF.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://doc.qt.io/qbs/qml-qbsmodules-qbs.html](https://doc.qt.io/qbs/qml-qbsmodules-qbs.html)
- [https://doc.qt.io/qbs/jsextension-textfile.html](https://doc.qt.io/qbs/jsextension-textfile.html)
