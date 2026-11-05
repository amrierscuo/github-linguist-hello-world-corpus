# #316 Ioke

## Latest recorded verification

**Syntax and behavior verified** on November 5, 2026.

The official Ioke JVM implementation parsed and executed the unchanged Ioke message-send source and printed exactly Hello, World! with LF. No Io substitution, CLR backend or GUI was used.

[Native commands, versions, outputs and SHA-256](verification/native_20261105_target546_main.json).

Current native command or procedure: `java -jar ioke.jar hello.ik (use the native JVM build and classpath recorded in the receipt)`.

## Extension results

- `.ik`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Invoke println on the greeting text in the Ioke runtime.

## Toolchain

Ioke JVM/CLR; versione da registrare

## Commands and procedure

ioke hello.ik

## Expected result

Hello, World! more newline.

## Status

Syntax and behavioral verification pending.

Ioke is the language to messages of the original project, distinct from Io. The .ik file is a concrete example; compatibility with Java/CLR and runtime are still tested.

Remaining requirements:
- Runtime Ioke historical unavailable; no verification with Io generico.

## Primary sources

- [https://github.com/olabini/ioke](https://github.com/olabini/ioke)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ik` | [hello.ik](hello.ik) syntax and behavior verified |

</details>
