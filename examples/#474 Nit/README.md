# #474 Nit

## Verified on November 19, 2026

The genuine Nit bootstrap generated a standalone compiler. The compiled program ran the interpolation and emitted the greeting.

Run `nitc hello.nit -o hello && ./hello`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Interpret or fill out Nit and print Hello, World!.

The var audience is interpolated in the Nit string with {audience}; print is greeting.

## Toolchain and reproduction

Nit/nitc originali; versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
nit hello.nit
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Compiler/interprete Nit not prepared.

## Primary sources

- https://nitlanguage.org/tools/nit.html
- https://nitlanguage.org/doc/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nit` | [hello.nit](hello.nit) Syntax and behavior verified |

</details>
