# #823 mdsvex

Preprocessare mdsvex e renderizzare il componente con Svelte SSR.

## Toolchain

Node22.20.0; {'mdsvex': '0.12.8', 'svelte': '5.57.2'}

## Procedura

npm install; node verify.cjs <work-output-module-with-node_modules-ancestor>

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

Il preprocessore mdsvex e compiler Svelte sono originali; il renderer server ufficiale valuta la variabile name e produce h1. JavaScript generato soltanto in work.

Verifica reale 2026-10-08T13:48:59.212109+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://github.com/pngwn/MDsveX](https://github.com/pngwn/MDsveX)
- [https://svelte.dev/docs/svelte/svelte-compiler](https://svelte.dev/docs/svelte/svelte-compiler)
- [https://svelte.dev/docs/svelte/svelte-server](https://svelte.dev/docs/svelte/svelte-server)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.svx` | [hello.svx](hello.svx) verificato |
