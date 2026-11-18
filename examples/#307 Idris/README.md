# #307 Idris

## Verified on November 18, 2026

The published Idris 2 compiler built the original source against the original Idris standard libraries. The compiled Chez program emitted the exact greeting.

Run `idris2 --cg chez hello.idr -o hi_run; run the generated executable or Chez program`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

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
| `.idr` | [hello.idr](hello.idr) Syntax and behavior verified |
| `.lidr` | [hello.lidr](variants/lidr-f41f21bf/hello.lidr) created; verification pending |

</details>
