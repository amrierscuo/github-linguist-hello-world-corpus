# #653 Scilab

Eseguire un file Scilab.

## Toolchain

Scilab CLI

## Procedura

scilab-cli -nb -f hello.sce

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.



Requisiti residui:
- Scilab runtime non disponibile.

## Fonti primarie

- [https://help.scilab.org/docs/2025.1.0/en_US/mprintf.html](https://help.scilab.org/docs/2025.1.0/en_US/mprintf.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sci` | [hello.sci](variants/sci-27617630/hello.sci) creato, verifiche pendenti |
| `.sce` | [hello.sce](hello.sce), [main.sce](variants/sci-27617630/main.sce) creato, verifiche pendenti |
| `.tst` | [hello.tst](variants/tst-04f6df08/hello.tst) creato, verifiche pendenti |
