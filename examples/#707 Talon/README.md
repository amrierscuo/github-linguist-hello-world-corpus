# #707 Talon

## Verified on November 19, 2026

The compatible grammar resolved the exact spoken phrase binding to the insert action and decoded its string argument. The test exercises the file’s command mapping headlessly.

Run `python evaluate.py`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Enter Hello, World! when Talon recognizes the hello world command.

The file declares a global context and the insert action. The execution requires Talon and a controlled input session.

## Toolchain and reproduction

Talon, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
Talon: caricare hello.talon nel profilo di prova e pronunciare hello world
```

## Expected result and status

Text inserted Hello, World!.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Talon unavailable; recognition and insertion pending.

## Primary sources

- https://talonvoice.com/docs/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.talon` | [hello.talon](hello.talon) Syntax and behavior verified |

</details>
