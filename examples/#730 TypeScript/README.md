# #730 TypeScript

Controllare i tipi TypeScript ed eseguire il JavaScript compilato.

## Toolchain

Version 7.0.2; Node.js22.20.0

## Procedura

tsc hello.ts --strict --target ES2022 --outDir build; node build/hello.js

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.



Verifica reale 2026-10-08T13:30:07.173282+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://www.typescriptlang.org/docs/handbook/2/everyday-types.html](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ts` | [hello.ts](hello.ts) verificato |
| `.cts` | [hello.cts](variants/cts-4d16cc26/hello.cts) creato, verifiche pendenti |
| `.mts` | [hello.mts](variants/mts-51a93bd5/hello.mts) creato, verifiche pendenti |
