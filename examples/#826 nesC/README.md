# #826 nesC

Compilare una configurazione nesC TinyOS e registrare il saluto da Boot.

## Toolchain

nesC; TinyOS; piattaforma/simulatore

## Procedura

Nel contesto TinyOS con MAKERULES/TOSROOT configurati: make <target-di-prova>; avviare e leggere il canale printf.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.



Requisiti residui:
- nesC/TinyOS compiler, componenti e target di prova non disponibili.

## Fonti primarie

- [https://github.com/tinyos/nesc](https://github.com/tinyos/nesc)
- [https://github.com/tinyos/tinyos-main](https://github.com/tinyos/tinyos-main)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.nc` | [HelloAppC.nc](HelloAppC.nc), [HelloC.nc](HelloC.nc) creato, verifiche pendenti |
