# #173 E

Eseguire println in E e stampare Hello, World!.

## Toolchain

E-on-Java ERights, launcher rune e JVM compatibile; versioni da registrare

## Comandi e procedura

rune hello.e

## Risultato atteso

Interprete E exit 0, stdout Hello, World! più newline.

## Stato

Sintassi e semantica in attesa.

La voce è il linguaggio E di ERights. println è una funzione del suo ambiente standard; non si presume che un compilatore con estensione .e di altro linguaggio sia compatibile.

Requisiti residui:
- Runtime E-on-Java/rune compatibile non predisposto; interprete E non eseguito.

## Fonti primarie e riferimento di formato

- [https://www.erights.org/](https://www.erights.org/)
- [https://erights.org/elang/kernel/auditors/index.html](https://erights.org/elang/kernel/auditors/index.html)
- [https://erights.org/download/0-8-14/index.html](https://erights.org/download/0-8-14/index.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.e` | [hello.e](hello.e) creato, verifiche pendenti |
