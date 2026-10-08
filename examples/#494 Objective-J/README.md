# #494 Objective-J

Compilare e invocare un metodo Objective-J originale.

## Toolchain

Node.js 22.20.0; objj-transpiler 1.0.0-10; objj-runtime 0.4.6

## Procedura

npm install objj-transpiler@1.0.0-10 objj-runtime@0.4.6; npx objjc hello.j -o build/hello.js; npx objj hello.j (runtime loader Windows pending)

## Risultato atteso

Hello, World!

## Stato

Sintassi verificata; semantica in attesa.

Classe radice originale senza dipendenza Foundation; il dispatcher Objective-J deve invocare realmente say.

Verifica reale 2026-10-08T13:11:33.888833+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

Requisiti residui:
- Objective-J native runtime execution pending: original objj-runtime 0.4.6 Windows local file resolution fails.

## Fonti primarie

- [https://www.cappuccino.dev/learn/objective-j.html](https://www.cappuccino.dev/learn/objective-j.html)
- [https://github.com/mrcarlberg/objj-runtime](https://github.com/mrcarlberg/objj-runtime)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.j` | [hello.j](hello.j) sintassi verificata |
| `.sj` | artefatto da generare La variante .sj appartiene al toolchain Objective-J storico; non è stata stabilita una forma minima affidabile distinta da sorgente .j né una serializzazione nativa. |
