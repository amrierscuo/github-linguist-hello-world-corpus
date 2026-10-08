# #309 ImHex Pattern Language

Mappare 13 byte ASCII di Hello, World! con un pattern ImHex.

## Toolchain

ImHex / PatternLanguage ufficiale; versione da registrare

## Comandi e procedura

In ImHex aprire hello.txt come dati, caricare hello.hexpat e Evaluate; ispezionare greeting

## Risultato atteso

Pattern char greeting[13] all’indirizzo 0 contiene esattamente Hello, World!.

## Stato

Sintassi e semantica in attesa.

hello.txt è una fixture ASCII senza newline, lunga 13 byte. Il pattern originale descrive una vista sui dati e non stampa. Solo l’evaluator ufficiale potrà validare sintassi e mapping.

Requisiti residui:
- ImHex/PatternLanguage evaluator non disponibile; nessun parser personalizzato viene contato come verifica.

## Fonti primarie

- [https://github.com/WerWolv/PatternLanguage](https://github.com/WerWolv/PatternLanguage)
- [https://imhex.werwolv.net/](https://imhex.werwolv.net/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.hexpat` | [hello.hexpat](hello.hexpat) creato, verifiche pendenti |
