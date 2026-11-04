# #733 Unified Parallel C

Fill Unified Parallel C and print from one thread.

## Toolchain

UPC compiler/runtime

## Procedure

upcc -o build/hello hello.upc; upcrun -n 2 build/hello

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- UPC compiler e runtime shared-memory non predisposti.

## Primary sources

- [https://upc.lbl.gov/docs/](https://upc.lbl.gov/docs/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.upc` | [hello.upc](hello.upc) created; verification pending |
