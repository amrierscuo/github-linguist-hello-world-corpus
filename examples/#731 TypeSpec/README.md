# #731 TypeSpec

Fill out a TypeSpec model with literal string of greeting.

## Toolchain

Microsoft TypeSpec 1.17.0; Node.js22.20.0

## Procedure

npm install @typespec/compiler; node verify.cjs

## Expected result

Hello, World!

## Status

syntax and behavior verified.

It is used compile/NodeHost of the original compiler and reads the actual type of property; the model describes a constraint of the contract.

Real check 2026-10-08T13:30:14.870000+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://typespec.io/docs/language-basics/models/](https://typespec.io/docs/language-basics/models/)
- [https://typespec.io/docs/language-basics/type-literals/](https://typespec.io/docs/language-basics/type-literals/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.tsp` | [hello.tsp](hello.tsp) verified |
