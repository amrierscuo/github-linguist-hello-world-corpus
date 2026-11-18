# #462 Nasal

## Verified on November 18, 2026

The original Nasal print expression ran in its upstream VM and concatenated the parts into the exact greeting.

Run `nasal-bin hello.nas`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Play Nasal in the runtime FlightGear and print Hello, World!.

The audience variable passed to print as a distinct subject; the builtin FlightGear concatenates the arguments and writes a line.

## Toolchain and reproduction

Original Nasal with print function of the FlightGear context; version to record

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
Caricare hello.nas nel contesto Nasal FlightGear.
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Impedimenti: Nasal/FlightGear non preparati; runtime pendente.

## Primary sources

- https://wiki.flightgear.org/Creating_new_Nasal_scripts
- https://wiki.flightgear.org/Nasal_library

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nas` | [hello.nas](hello.nas) Syntax and behavior verified |

</details>
