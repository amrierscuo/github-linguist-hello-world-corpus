# #821 mIRC Script

Caricare un alias mIRC che scrive il saluto nella finestra locale.

## Toolchain

mIRC Script runtime

## Procedura

In mIRC caricare hello.mrc con /load -rs; invocare /hello.

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica in attesa.

echo -a produce output locale; il campione non invia messaggi o avvia connessioni.

Requisiti residui:
- mIRC runtime non disponibile.

## Fonti primarie

- [https://www.mirc.com/help/html/aliases.html](https://www.mirc.com/help/html/aliases.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mrc` | [hello.mrc](hello.mrc) creato, verifiche pendenti |
