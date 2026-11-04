# #574 QML

Qt Quick loaded the original QML and rendered a 320 by 120 frame. The native text item and the visible frame both show Hello, World!

Canonical type: `programming`. Linguist language ID: `305`.

## Recorded verification

**Syntax and behavior verified** on November 4, 2026 with PySide6 6.9.2 and Qt 6.9.2 software Qt Quick.

[Recorded commands, outputs and hashes](verification/native_20261104_qml_result.json).
[Rendered frame](verification/native_20261104_frame.png).

## Reproduce the check

To view the example with Qt Quick installed, run `qml hello.qml` from the example directory. The recorded check used QQmlApplicationEngine with the offscreen platform and software Qt Quick, then checked the text item and grabbed the frame. The Qbs project has its own pending check.

## Primary sources

- https://doc.qt.io/qt-6/qml-qtquick-text.html

## Extension coverage

| Extension | Files | Status |
| --- | --- | --- |
| `.qml` | [hello.qml](hello.qml) | Syntax and behavior verified |
| `.qbs` | [hello.qbs](variants/qbs-7cd27494/hello.qbs) | Verification pending |
