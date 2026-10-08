# #723 Tolk

Compilare un get method Tolk che restituisce il saluto.

## Toolchain

@ton/tolk-js 1.4.2; actual Tolk version in stdout; Node.js22.20.0

## Procedura

npm install @ton/tolk-js; node verify.cjs build/compiled.json; invocare il get method greeting nella TVM locale.

## Risultato atteso

Hello, World!

## Stato

Sintassi verificata; semantica in attesa.

Nessuna pubblicazione on-chain; compiler originale e stdlib embedded. La compilazione non attesta il valore del metodo in TVM.

Verifica reale 2026-10-08T13:30:50.636083+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

Requisiti residui:
- Offline TVM evaluation of greeting pending.

## Fonti primarie

- [https://docs.ton.org/tolk/overview](https://docs.ton.org/tolk/overview)
- [https://github.com/ton-blockchain/tolk-js](https://github.com/ton-blockchain/tolk-js)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tolk` | [hello.tolk](hello.tolk) sintassi verificata |
