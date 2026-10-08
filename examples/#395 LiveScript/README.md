# #395 LiveScript

Compilare LiveScript in JavaScript ed eseguire console.log.

## Toolchain

livescript 1.6.0; Node 22.20.0

## Comandi e procedura

npm install; npx lsc hello.ls

## Risultato atteso

Exit 0; Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

Si usa il compilatore LiveScript originale e il runtime Node. .ls viene tenuto nella cartella specifica, separato dal file LoomScript con la stessa estensione.

Verifica effettiva del 2026-10-08T12:48:18.107237+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://livescript.net/](https://livescript.net/)
- [https://github.com/gkz/LiveScript](https://github.com/gkz/LiveScript)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ls` | [hello.ls](hello.ls) verificato |
| `._ls` | [hello._ls](variants/ls-4f7bfbd4/hello._ls) creato, verifiche pendenti |
