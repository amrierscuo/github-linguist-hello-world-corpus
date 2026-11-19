# #726 Turing

## Verified on November 19, 2026

The compatible publisher compiler accepted the unchanged Turing program and its generated native executable emitted the exact greeting.

Run `tpc -o greeting hello.t && ./greeting`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Run a Turing program.

## Toolchain

Holt Turing/Open Turing runtime

## Procedure

Open hello.t in Turing and choose Run; record version and output.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- Turing compiler/runtime non predisposto.

## Primary sources

- [https://compsci.ca/holtsoft/doc/](https://compsci.ca/holtsoft/doc/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.t` | [hello.t](hello.t) Syntax and behavior verified |
| `.tu` | [hello.tu](variants/tu-b8fdb221/hello.tu) created; verification pending |

</details>
