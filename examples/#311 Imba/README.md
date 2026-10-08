# #311 Imba

Compilare ed eseguire Imba per scrivere il saluto sulla console Node.

## Toolchain

Imba 2.0.0-alpha.253; Node.js 22.20.0

## Comandi e procedura

npm install; npx imba hello.imba

## Risultato atteso

CLI exit 0; console.log emette Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

Il CLI originale compila il file .imba e lo esegue realmente. package.json fissa la versione provata; bundle/cache restano in work. Nessun browser è necessario.

Verifica effettiva del 2026-10-08T12:30:00.143794+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://github.com/imba/imba](https://github.com/imba/imba)
- [https://imba.io/](https://imba.io/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.imba` | [hello.imba](hello.imba) verificato |
