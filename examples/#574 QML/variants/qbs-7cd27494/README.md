# 0574 — QML — `.qbs`

Progetto Qbs con una regola JavaScript che produce il saluto; distinto da QtQuick.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.qbs`.

Controllo previsto, dalla cartella della variante:

```text
qbs build -f hello.qbs --build-directory work/qbs
```

Risultato atteso: greeting.txt contiene Hello, World! e LF.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://doc.qt.io/qbs/qml-qbsmodules-qbs.html](https://doc.qt.io/qbs/qml-qbsmodules-qbs.html)
- [https://doc.qt.io/qbs/jsextension-textfile.html](https://doc.qt.io/qbs/jsextension-textfile.html)
