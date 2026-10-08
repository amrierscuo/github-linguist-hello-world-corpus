# #488 Oberon

Eseguire un modulo Oberon-2 che usa Out.

## Toolchain

Compilatore Oberon-2 e modulo standard Out

## Procedura

Compilare Hello.ob2 e invocare il modulo Hello con il runtime Oberon-2 scelto; registrare il comando effettivo.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

Il file usa il sottoinsieme MODULE/IMPORT/BEGIN comune a Oberon-2; Out è una dipendenza reale del runtime scelto.

Requisiti residui:
- Compilatore Oberon-2 e libreria Out non disponibili; comando/versione devono essere registrati nel futuro test.

## Fonti primarie

- [https://www.inf.ethz.ch/personal/wirth/Oberon/Oberon07.Report.pdf](https://www.inf.ethz.ch/personal/wirth/Oberon/Oberon07.Report.pdf)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ob2` | [Hello.ob2](Hello.ob2) creato, verifiche pendenti |
