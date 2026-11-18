# #621 Roc

## Verified on November 18, 2026

The published Roc nightly ran the sample with the verified CLI platform and executed its greeting action and emitted the greeting.

Run `roc hello.roc`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

[Earlier evidence](verification/toolchain.json).

[Prior attempt](verification/native_20261118_wave736_prior_attempt.json).

<details>
<summary>Earlier instructions and evidence</summary>

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Eseguire Roc e stampare Hello, World!.

main! uses the syntax of the new compiler described in the official tutorial. The alpha4-rolling release obtained contains the historical compiler, which requires a header and does not verify this source.

## Toolchain and reproduction

Roc new compiler with Echo platform builtin; tried tool: nightly d73ea109 of 09/09/2025

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
roc hello.roc
```

## Expected result and status

Hello, World! su stdout.

Artifact created: yes. syntax verified: no. behavior verified: no.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

Commitments: There is a new compiler track compatible with the tutorial; incompatible real attempt recorded.

## Primary sources

- https://raw.githubusercontent.com/roc-lang/roc/main/docs/mini-tutorial-new-compiler.md

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.roc` | [hello.roc](hello.roc) Syntax and behavior verified |

</details>
