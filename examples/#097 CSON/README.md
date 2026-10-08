# #097 CSON

Decodificare il file CSON in un oggetto che contiene soltanto greeting=Hello, World!.

## Toolchain

Node.js v22.20.0; cson-parser 4.0.9

## Comandi e procedura

Da questa cartella:

```sh
npm install
node check.cjs
```

package.json fissa la versione del parser; check.cjs confronta l'intero
oggetto restituito, inclusa l'assenza di campi aggiuntivi.

## Risultato atteso

Parser restituisce esattamente {greeting: "Hello, World!"}; exit 0 e saluto su stdout.

## Stato

Sintassi e semantica verificate.

CSON usa la rappresentazione dati CoffeeScript. Il checker chiama cson-parser e confronta l'oggetto reale; non usa regex per leggere i valori.

Verifica effettiva del 2026-10-08T11:33:44.249893+00:00 su Windows x64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://github.com/groupon/cson-parser](https://github.com/groupon/cson-parser)
- [https://github.com/bevry/cson](https://github.com/bevry/cson)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cson` | [hello.cson](hello.cson) verificato |
