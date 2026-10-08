# #175 EBNF

Definire una grammatica EBNF che riconosce Hello, World! e rifiuta Hello, Moon!.

## Toolchain

Node.js v22.20.0; ebnf 1.9.1

## Comandi e procedura

npm install; node check.cjs

## Risultato atteso

Grammatica compilata; AST Greeting con testo esatto; input diverso rifiutato.

## Stato

Sintassi e semantica verificate.

Il dialetto scelto è W3C EBNF, con ::= e concatenazione di letterali; non è ISO EBNF. Il compilatore di grammatiche ebnf autentico genera il parser e applica le produzioni al testo.

Verifica effettiva del 2026-10-08T11:56:13.607325+00:00 su Windows x64: [log](verification/result.json).
Hash delle sorgenti/checker, versioni e comandi reali, codici di uscita, stdout/stderr e limiti della prova sono nel log.

## Fonti primarie e riferimento di formato

- [https://www.w3.org/TR/xquery-31/#EBNFNotation](https://www.w3.org/TR/xquery-31/#EBNFNotation)
- [https://github.com/lys-lang/node-ebnf](https://github.com/lys-lang/node-ebnf)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ebnf` | [hello.ebnf](hello.ebnf) verificato |
