# #491 ObjectScript

Compilare una classe InterSystems e invocarne Greet.

## Toolchain

InterSystems IRIS ObjectScript

## Procedura

Nel namespace di prova: do $SYSTEM.OBJ.Load("Hello.cls","ck") poi do ##class(Corpus.Hello).Greet()

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.



Requisiti residui:
- InterSystems IRIS compiler/namespace non disponibile.

## Fonti primarie

- [https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=GCOS](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=GCOS)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cls` | [Hello.cls](Hello.cls) creato, verifiche pendenti |
