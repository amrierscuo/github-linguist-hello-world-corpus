# #164 DenizenScript

## Verified on November 19, 2026

The genuine Denizen core loaded the original task and the upstream command used its TO_CONSOLE branch. A Bukkit console adapter captured the greeting verbatim.

Run `Load the original hello.dsc in Probe against the released Denizen core and Bukkit libraries`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Run a DenizenScript task that announces Hello, World! in the server console.

## Toolchain

Denizen plugin su server Minecraft/Paper compatibile; versioni effettive da registrare

## Commands and procedure

Copiare hello.dsc in plugins/Denizen/scripts; eseguire /ex reload e /ex run hello_world

## Expected result

Reload without errors; hello_world task writes Hello, World! in the console.

## Status

Syntax and behavioral verification pending.

The structure is a real Denizen task; a YAML parser alone would not wait for the plugin commands.

Remaining requirements:
- Minecraft/Paper and compatible Denizen plugins not available; reloading and unrun task.

## Primary sources and format reference

- [https://guide.denizenscript.com/guides/first-steps/task-script.html](https://guide.denizenscript.com/guides/first-steps/task-script.html)
- [https://meta.denizenscript.com/Docs/Commands/Announce](https://meta.denizenscript.com/Docs/Commands/Announce)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.dsc` | [hello.dsc](hello.dsc) Syntax and behavior verified |

</details>
