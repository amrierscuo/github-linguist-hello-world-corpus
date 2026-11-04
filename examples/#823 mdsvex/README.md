# #823 mdsvex

Preprocess mdsvex and render the component with Svelte SSR.

## Toolchain

Node22.20.0; {'mdsvex': '0.12.8', 'svelte': '5.57.2'}

## Procedure

npm install; node verify.cjs <work-output-module-with-node_modules-ancestor>

## Expected result

Hello, World!

## Status

syntax and behavior verified.

The mdsvex preprocessor and Svelte compiler are original; the official renderr server evaluates the variable name and produces h1. JavaScript generated only in work.

Real check 2026-10-08T13:48:59.212109+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://github.com/pngwn/MDsveX](https://github.com/pngwn/MDsveX)
- [https://svelte.dev/docs/svelte/svelte-compiler](https://svelte.dev/docs/svelte/svelte-compiler)
- [https://svelte.dev/docs/svelte/svelte-server](https://svelte.dev/docs/svelte/svelte-server)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.svx` | [hello.svx](hello.svx) verified |
