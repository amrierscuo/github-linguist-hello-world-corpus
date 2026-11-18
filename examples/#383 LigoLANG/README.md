# #383 LigoLANG

## Verified on November 18, 2026

The official LIGO command executable interpreted the original source in its declared dialect and returned the exact greeting.

Run `ligo run interpret greeting --init-file hello.ligo --syntax pascaligo --deprecated`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Evaluate a constant greeting string in syntax Baseline PascaLIGO .ligo.

## Toolchain

LIGO compatible with PascaLIGO, for example 0.73 series; actual version to be recorded

## Commands and procedure

With a compiler that supports PascaLIGO: ligo run evaluate-expr hello.ligo greeting --syntax pascaligo --deprecated

## Expected result

The value of greeting is the Hello, World! string.

## Status

Syntax and behavioral verification pending.

The .ligo canonical extension identifies historical PascaLIGO. The file is not renamed as JsLIGO: recent compilers require a migration path.

Remaining requirements:
- Compilatore con supporto PascaLIGO unavailable; sintassi/evaluation pending.

## Primary sources

- [https://gitlab.com/ligolang/ligo](https://gitlab.com/ligolang/ligo)
- [https://ligolang.org/docs/next/intro/changelog/](https://ligolang.org/docs/next/intro/changelog/)
- [https://gitlab.com/ligolang/ligo/-/merge_requests/2395](https://gitlab.com/ligolang/ligo/-/merge_requests/2395)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ligo` | [hello.ligo](hello.ligo) Syntax and behavior verified |

</details>
