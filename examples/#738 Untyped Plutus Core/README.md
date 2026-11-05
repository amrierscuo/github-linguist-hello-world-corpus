# #738 Untyped Plutus Core

## Latest recorded verification

**Syntax and behavior verified** on November 5, 2026.

The maintained Aiken native UPLC parser and CEK evaluator loaded the exact original program and evaluated it to (con string "Hello, World!") with recorded positive CPU/memory budget usage. This verifies the pure UPLC constant only; no blockchain, wallet, deployment or transaction was involved.

[Native commands, versions, outputs and SHA-256](verification/native_20261105_target546_main.json).

Current native command or procedure: `aiken uplc eval hello.uplc`.

## Extension results

- `.uplc`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Analyze and evaluate a constant string Untyped Plutus Core.

## Toolchain

UPLC parser/CEK evaluator

## Procedure

Use the official parser/evaluatore UPLC of the compatible version to evaluate hello.uplc.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

The program is a constant, no transactions or deployment.

Remaining requirements:
- Toolchain UPLC/CEK non predisposta; valutazione pending.

## Primary sources

- [https://plutus.cardano.intersectmbo.org/docs/](https://plutus.cardano.intersectmbo.org/docs/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.uplc` | [hello.uplc](hello.uplc) syntax and behavior verified |

</details>
