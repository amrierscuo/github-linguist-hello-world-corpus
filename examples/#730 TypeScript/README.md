# #730 TypeScript

Check the TypeScript types and run the completed JavaScript.

## Toolchain

Version 7.0.2; Node.js22.20.0

## Procedure

tsc hello.ts --strict --target ES2022 --outDir build; node build/hello.js

## Expected result

Hello, World!

## Status

syntax and behavior verified.



Real check 2026-10-08T13:30:07.173282+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://www.typescriptlang.org/docs/handbook/2/everyday-types.html](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ts` | [hello.ts](hello.ts) verified |
| `.cts` | [hello.cts](variants/cts-4d16cc26/hello.cts) syntax and behavior verified |
| `.mts` | [hello.mts](variants/mts-51a93bd5/hello.mts) syntax and behavior verified |

## Additional extension verification

- `.cts`: verified on November 4, 2026. [Evidence](verification/native_20261104_730_variants_result.json).
- `.mts`: verified on November 4, 2026. [Evidence](verification/native_20261104_730_variants_result.json).
