# #731 TypeSpec

Compilare un modello TypeSpec con string literal del saluto.

## Toolchain

Microsoft TypeSpec 1.17.0; Node.js22.20.0

## Procedura

npm install @typespec/compiler; node verify.cjs

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

Si usa compile/NodeHost del compiler originale e si legge il tipo effettivo della proprietà; il modello descrive un vincolo del contratto.

Verifica reale 2026-10-08T13:30:14.870000+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://typespec.io/docs/language-basics/models/](https://typespec.io/docs/language-basics/models/)
- [https://typespec.io/docs/language-basics/type-literals/](https://typespec.io/docs/language-basics/type-literals/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tsp` | [hello.tsp](hello.tsp) verificato |
