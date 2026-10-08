# #400 LoomScript

Avviare un’applicazione LoomScript originale e tracciare il saluto da run.

## Toolchain

LoomSDK storico; versione da registrare

## Comandi e procedura

Inserire HelloWorld.ls come classe principale del progetto Loom; loom build; loom run

## Risultato atteso

run invoca base initialization e trace emette Hello, World!.

## Stato

Sintassi e semantica in attesa.

È il linguaggio LoomScript del Loom Native SDK per applicazioni/giochi. La classe estende loom.Application e mantiene super.run come indicato dal codice vendor. Non è un SDK blockchain omonimo.

Requisiti residui:
- Loom compiler/runtime storico non predisposto; build/avvio applicazione pending.

## Fonti primarie

- [https://github.com/LoomSDK/LoomSDK](https://github.com/LoomSDK/LoomSDK)
- [https://github.com/LoomSDK/LoomSDK/blob/master/sdk/src/loom/Application.ls](https://github.com/LoomSDK/LoomSDK/blob/master/sdk/src/loom/Application.ls)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ls` | [HelloWorld.ls](HelloWorld.ls) creato, verifiche pendenti |
