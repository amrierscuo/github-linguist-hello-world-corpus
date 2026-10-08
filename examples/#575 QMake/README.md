# #575 QMake

Generare e compilare un progetto qmake Qt Core.

## Toolchain

qmake; Qt Core; C++

## Procedura

qmake hello.pro; make; ./hello

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.



Requisiti residui:
- qmake e Qt Core development libraries non predisposti.

## Fonti primarie

- [https://doc.qt.io/qt-6/qmake-project-files.html](https://doc.qt.io/qt-6/qmake-project-files.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pro` | [hello.pro](hello.pro), [main.pro](variants/pri-e5eeb81c/main.pro) creato, verifiche pendenti |
| `.pri` | [hello.pri](variants/pri-e5eeb81c/hello.pri) creato, verifiche pendenti |
