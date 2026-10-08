# #385 Limbo

Compilare un modulo Limbo per Inferno che usa Sys->print.

## Toolchain

Inferno/Limbo; versione da registrare

## Comandi e procedura

Nel runtime Inferno: limbo -o hello.dis hello.b; ./hello.dis

## Risultato atteso

Modulo carica Sys e scrive Hello, World! più newline.

## Stato

Sintassi e semantica in attesa.

init espone l’interfaccia della shell Inferno e carica il modulo Sys autentico. Sys/Draw interfaces provengono dal runtime; non sono stub inclusi nel corpus.

Requisiti residui:
- Compilatore Limbo e VM Dis Inferno non disponibili; import Sys/Draw e runtime pending.

## Fonti primarie

- [https://www.vitanuova.com/inferno/limbo.html](https://www.vitanuova.com/inferno/limbo.html)
- [https://www.vitanuova.com/inferno/papers/limbo.html](https://www.vitanuova.com/inferno/papers/limbo.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.b` | [hello.b](hello.b), [hello.b](variants/m-f7140aa0/hello.b) creato, verifiche pendenti |
| `.m` | [hello.m](variants/m-f7140aa0/hello.m) creato, verifiche pendenti |
