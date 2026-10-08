# #393 Literate Haskell

Interpretare un programma Haskell letterato in stile Bird che stampa il saluto.

## Toolchain

Genuine Hugs98 September 2006; Ubuntu package 98.200609.21-6build3 Haskell98 mode

## Comandi e procedura

HUGSDIR=<libreria-hugs> runhugs +98 -P<percorsi-librerie-bundled> hello.lhs

## Risultato atteso

Righe > riconosciute; main : IO (); output Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

L’interprete Hugs98 originale analizza direttamente .lhs e controlla i tipi; non è stato convertito a .hs da un parser personale. Le librerie Haskell98 e base sono quelle del tool. È una verifica sullo standard Haskell98, senza claim GHC moderno.

Verifica effettiva del 2026-10-08T12:51:44.086941+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://www.haskell.org/onlinereport/literate.html](https://www.haskell.org/onlinereport/literate.html)
- [https://www.haskell.org/hugs/](https://www.haskell.org/hugs/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lhs` | [hello.lhs](hello.lhs) verificato |
