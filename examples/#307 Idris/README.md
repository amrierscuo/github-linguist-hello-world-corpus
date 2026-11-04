# #307 Idris

Type and run a main Idris that uses putStrLn.

## Toolchain

Idris; scegliere/registrare a version compatible with .idr

## Commands and procedure

idris --check hello.idr; idris hello.idr -o build/hello; build/hello

## Expected result

Main type: IO (); Hello, World! press program more newline.

## Status

Syntax and behavioral verification pending.

The Main module and the IO type make the goal concrete.This simple sample is documented according to Idris 1; a possible migration Idris 2 will have to record actual tool/backend.

Remaining requirements:
- Compilatore/backend Idris not available in this tranche; type check and runtime pending.

## Primary sources

- [https://docs.idris-lang.org/en/latest/tutorial/introduction.html](https://docs.idris-lang.org/en/latest/tutorial/introduction.html)
- [https://docs.idris-lang.org/en/latest/tutorial/starting.html](https://docs.idris-lang.org/en/latest/tutorial/starting.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.idr` | [hello.idr](hello.idr) created; verification pending |
| `.lidr` | [hello.lidr](variants/lidr-f41f21bf/hello.lidr) created; verification pending |
