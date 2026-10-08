# #576 Qt Script

Valutare ECMAScript nel vero QScriptEngine.

## Toolchain

Qt 5 QtScript; C++

## Procedura

Compilare main.cpp collegando Qt5Core e Qt5Script; eseguire nella cartella di hello.qs.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

Lo script restituisce una stringa come valore finale; il consumer C++ usa evaluate e controlla le eccezioni native.

Requisiti residui:
- Qt5Script/Qt Core compiler e librerie non predisposti.

## Fonti primarie

- [https://doc.qt.io/archives/qt-5.15/qtscript-index.html](https://doc.qt.io/archives/qt-5.15/qtscript-index.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.qs` | [hello.qs](hello.qs) creato, verifiche pendenti |
