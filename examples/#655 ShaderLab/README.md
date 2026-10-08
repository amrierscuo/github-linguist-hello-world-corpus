# #655 ShaderLab

Caricare uno shader ShaderLab con proprieta del saluto nel material inspector.

## Toolchain

Unity ShaderLab compiler/editor

## Procedura

Importare hello.shader in un progetto Unity compatibile con shader fixed-function; creare un materiale e controllare la proprieta.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

Il goal di formato è la proprieta nominata Hello, World! e il pass che ne consuma il colore, non testo visibile nel rendering.

Requisiti residui:
- Unity editor/shader compiler non disponibile; compatibilità fixed-function da provare.

## Fonti primarie

- [https://docs.unity3d.com/Manual/SL-Properties.html](https://docs.unity3d.com/Manual/SL-Properties.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.shader` | [hello.shader](hello.shader) creato, verifiche pendenti |
