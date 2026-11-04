# #475 Nix

## Latest recorded verification

**Syntax and behavior verified** on November 4, 2026.

Original Nix evaluator returned exactly the intended string. No derivations, builds, system configuration or network evaluation.

[Native commands, versions, outputs and SHA-256](verification/native_20261104_followup_main.json).

## Extension results

- `.nix`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Evaluate an expression Nix and get Hello, World!.

The pure expression let/in uses ${audience} interpolation. It does not contain derivatives, fetch or system modifications; however, the test requires the evaluator Nix.

## Toolchain and reproduction

Nix evaluator originale; versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
nix-instantiate --eval --strict hello.nix
```

## Expected result and status

Valore stringa "Hello, World!".

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Impedimenti: Nix originale non preparato; evaluator pendente.

## Primary sources

- https://nix.dev/manual/nix/stable/language/string-interpolation.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nix` | [hello.nix](hello.nix) syntax and behavior verified |

</details>
