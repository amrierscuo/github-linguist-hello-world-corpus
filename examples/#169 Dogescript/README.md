# #169 Dogescript

Compilare Dogescript in JavaScript e stampare Hello, World! con console.loge.

## Toolchain

Node.js v22.20.0; dogescript 2.4.3

## Comandi e procedura

npm install; node check.cjs

## Risultato atteso

Compilatore genera JavaScript valido; esecuzione produce esattamente un saluto.

## Stato

Sintassi e semantica verificate.

check.cjs chiama il compilatore Dogescript originale, compila il risultato con vm.Script di Node e ne esegue il codice catturando console.log. Il checker non traduce il linguaggio.

Verifica effettiva del 2026-10-08T11:56:12.746770+00:00 su Windows x64: [log](verification/result.json).
Hash delle sorgenti/checker, versioni e comandi reali, codici di uscita, stdout/stderr e limiti della prova sono nel log.

## Fonti primarie e riferimento di formato

- [https://github.com/dogescript/dogescript](https://github.com/dogescript/dogescript)
- [https://github.com/dogescript/dogescript/blob/master/LANGUAGE.md](https://github.com/dogescript/dogescript/blob/master/LANGUAGE.md)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.djs` | [hello.djs](hello.djs) verificato |
