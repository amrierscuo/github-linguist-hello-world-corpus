# #389 Liquid

Interpretare un template Liquid con default, interpolazione e HTML escaping.

## Toolchain

liquidjs 10.30.0; Node 22.20.0

## Comandi e procedura

npm install; node verify.cjs

## Risultato atteso

World e nome assente danno Hello, World!; <World> viene escapato.

## Stato

Sintassi e semantica verificate.

LiquidJS è un’implementazione community autentica di Liquid; il checker chiama engine.parse/render e prova default/escape. La prova non è un’esecuzione su un negozio Shopify.

Verifica effettiva del 2026-10-08T12:49:20.783420+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://shopify.github.io/liquid/](https://shopify.github.io/liquid/)
- [https://liquidjs.com/tutorials/intro-to-liquid.html](https://liquidjs.com/tutorials/intro-to-liquid.html)
- [https://github.com/harttle/liquidjs](https://github.com/harttle/liquidjs)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.liquid` | [hello.liquid](hello.liquid) verificato |
