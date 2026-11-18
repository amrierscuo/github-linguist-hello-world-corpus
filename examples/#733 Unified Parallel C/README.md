# #733 Unified Parallel C

## Verified on November 18, 2026

The native Berkeley UPC implementation ran the original over two local threads, completed its barrier and emitted the exact greeting once.

Run `upcc -network=smp -T 2 -o hello hello.upc; upcrun -n 2 ./hello`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

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
| `.upc` | [hello.upc](hello.upc) Syntax and behavior verified |

</details>
