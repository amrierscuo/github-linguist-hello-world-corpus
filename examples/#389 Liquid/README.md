# #389 Liquid

Interpret a Liquid template with default, interpolation and HTML escaping.

## Toolchain

liquidjs 10.30.0; Node 22.20.0

## Commands and procedure

npm install; node verify.cjs

## Expected result

World e nome assente danno Hello, World!; <World> viene escapato.

## Status

syntax and behavior verified.

LiquidJS is an authentic implementation community of Liquid; the checker calls engine.parse /render and default/escape. test is not an execution on a Shopify store.

Actual verification of 2026-10-08T12:49:20.783420+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://shopify.github.io/liquid/](https://shopify.github.io/liquid/)
- [https://liquidjs.com/tutorials/intro-to-liquid.html](https://liquidjs.com/tutorials/intro-to-liquid.html)
- [https://github.com/harttle/liquidjs](https://github.com/harttle/liquidjs)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.liquid` | [hello.liquid](hello.liquid) verified |
