# 0575 — QMake — `.pri`

Include qmake con variabile e message, consumato da un progetto companion.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.pri`.

Controllo previsto, dalla cartella della variante:

```text
qmake main.pro -o work/Makefile
```

Risultato atteso: qmake segnala Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://doc.qt.io/qt-6/qmake-project-files.html](https://doc.qt.io/qt-6/qmake-project-files.html)
