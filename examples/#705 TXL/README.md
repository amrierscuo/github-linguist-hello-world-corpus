# #705 TXL

## Latest recorded verification

**Syntax and behavior verified** on November 5, 2026.

After the minimal construct-type correction, native OpenTXL parsed the grammar and rewrite function and transformed the original input.txt into exactly the quoted Hello, World! string-literal token. The output is a transformed program token, not an unquoted console print. The original compiler failure is retained.

[Native commands, versions, outputs and SHA-256](verification/native_20261105_target546_main.json).

Current native command or procedure: `txl input.txt hello.txl`.

The rewrite variable is now constructed with the program type required by the replacement. [Original compiler failure](verification/native_20261105_target546_original_failure.json).

## Extension results

- `.txl`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Turn a token sequence into a TXL greeting string.

Grammatic program as repeat token and main rewriting function; the stringlit output represents greeting.

## Toolchain and reproduction

TXL, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
txl input.txt hello.txl
```

## Expected result and status

Token stringlit "Hello, World!" in output.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Interpreting TXL unavailable; hanging parser and transformation.

## Primary sources

- https://www.txl.ca/plow2014.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.txl` | [hello.txl](hello.txl) syntax and behavior verified |

</details>
