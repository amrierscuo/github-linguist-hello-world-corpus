# #490 Object Data Instance Notation

## Verified on November 18, 2026

Archie’s ODIN parser converted the exact original document. The resulting object contains the exact greeting value.

Run `java -cp <Archie dependencies> ReadOdin.java`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Decode the greeting ODIN attribute of openEHR.

## Toolchain

Parser ODIN openEHR conforme

## Procedure

Upload hello.odin with a parser ODIN openEHR and read greeting; record API/versione/risultato.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

ODIN is Object Data Instance Notation of openEHR; the primitive string value is enclosed in < >. It does not contain patient data.

Remaining requirements:
- Parser ODIN openEHR not predisposed.

## Primary sources

- [https://specifications.openehr.org/releases/BASE/latest/odin.html](https://specifications.openehr.org/releases/BASE/latest/odin.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.odin` | [hello.odin](hello.odin) Syntax and behavior verified |

</details>
