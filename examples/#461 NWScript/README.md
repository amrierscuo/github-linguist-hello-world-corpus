# #461 NWScript

## Verified on November 19, 2026

The bundled official compiler compiled the original NWScript. The compatible VM executed the resulting bytecode and dispatched the computed greeting to the registered PrintString host callback.

Run `python run_nwscript.py hello.nss <upstream nwscript.nss>`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave756_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Eseguire main NWScript e inviare Hello, World! al log tramite PrintString.

main concatenate a string and call PrintString. Requires builtin statements and VM of the game; GCC is not a NWScript compiler.

## Toolchain and reproduction

Compiler e VM Neverwinter Nights/NWScript originali; versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
Compilare hello.nss nel toolset NWN ed eseguirlo in un modulo locale.
```

## Expected result and status

Runtime log contains Hello, World!.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Impedimenti: Toolset/compiler/VM NWScript non preparati; verifiche pendenti.

## Primary sources

- https://forums.beamdog.com/uploads/editor/w4/7kqf0pqj21mb.pdf
- https://nwn.beamdog.net/docs/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nss` | [hello.nss](hello.nss) Syntax and behavior verified |

</details>
