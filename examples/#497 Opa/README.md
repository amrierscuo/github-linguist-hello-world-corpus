# #497 Opa

Servire una pagina Opa che contiene il saluto.

## Toolchain

Opa web compiler, sintassi JS-like

## Procedura

opa --parser js-like hello.opa --; leggere la pagina HTTP locale della porta effettiva

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

Server.start e sintassi page:function sono conformi al campione canonico; verificare l’opzione del compilatore scelto prima del test.

Requisiti residui:
- Compilatore Opa web storico e runtime Node richiesto non predisposti.

## Fonti primarie

- [https://github.com/MLstate/opalang](https://github.com/MLstate/opalang)
- [https://github.com/github-linguist/linguist/blob/main/samples/Opa/hello_syntax2.opa](https://github.com/github-linguist/linguist/blob/main/samples/Opa/hello_syntax2.opa)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.opa` | [hello.opa](hello.opa) creato, verifiche pendenti |
