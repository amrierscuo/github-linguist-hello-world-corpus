# #580 QuickBASIC

Compilare ed eseguire QuickBASIC console.

## Toolchain

Microsoft QuickBASIC 4.5; DOS emulator

## Procedura

Nel runtime DOS: BC HELLO.BAS; LINK HELLO.OBJ; HELLO.EXE (registrare opzioni/versioni effettive).

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

Sorgente originale nel sottoinsieme PRINT/END; una prova con altro BASIC non viene contata come verifica QuickBASIC.

Requisiti residui:
- Compiler Microsoft QuickBASIC e runtime DOS non disponibili.

## Fonti primarie

- [https://archive.org/details/ms-quickbasic-4.5](https://archive.org/details/ms-quickbasic-4.5)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bas` | [hello.bas](hello.bas), [main.bas](variants/bi-5b4ad4e3/main.bas) creato, verifiche pendenti |
| `.bi` | [hello.bi](variants/bi-5b4ad4e3/hello.bi) creato, verifiche pendenti |
