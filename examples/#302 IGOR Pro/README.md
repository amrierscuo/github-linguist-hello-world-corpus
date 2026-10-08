# #302 IGOR Pro

Eseguire HelloWorld in Igor Pro e scrivere il saluto nella History.

## Toolchain

WaveMetrics Igor Pro; versione da registrare

## Comandi e procedura

Caricare hello.ipf nella finestra Procedure; Compile; nel comando Igor: HelloWorld()

## Risultato atteso

History contiene Hello, World!.

## Stato

Sintassi e semantica in attesa.

La funzione originale usa Print; rtGlobals=3 sceglie l’accesso moderno rigoroso alle variabili. Nessuna finestra/grafico è necessaria per il risultato.

Requisiti residui:
- Igor Pro proprietario/licenza non disponibile; compilazione e History pending.

## Fonti primarie

- [https://www.wavemetrics.com/products/igorpro/programming](https://www.wavemetrics.com/products/igorpro/programming)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ipf` | [hello.ipf](hello.ipf) creato, verifiche pendenti |
