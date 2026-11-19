# #626 RouterOS Script

## Verified on November 19, 2026

The vendor RouterOS console parsed and executed the exact script bytes transported as an escaped serial command. Its actual console output contained the greeting. The VM ran with no network interfaces and a disposable disk snapshot.

Run `python3 -I serial_replay.py <qemu-system-x86_64> <firmware> <chr.img> hello.rsc`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Run a RouterOS script that prints Hello, World!.

Script with local variable, concatenation and:put; requires a test RouterOS environment.

## Toolchain and reproduction

RouterOS Script, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
RouterOS: import hello.rsc
```

## Expected result and status

Hello, World! in the RouterOS console.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Runtime RouterOS unavailable; execution and hanging parser.

## Primary sources

- https://help.mikrotik.com/docs/spaces/ROS/pages/47579229/Scripting

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rsc` | [hello.rsc](hello.rsc) Syntax and behavior verified |

</details>
