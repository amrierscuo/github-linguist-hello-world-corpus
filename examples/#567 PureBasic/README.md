# #567 PureBasic

## Verified on November 18, 2026

The official compiler built the unmodified example. Its native executable printed the exact greeting after resolving missing bundled allocator linkage aliases.

Run `pbcompiler hello.pb --console --executable hello; ./hello`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill out a PureBasic console program.

## Toolchain

PureBasic compiler

## Procedure

Fill hello.pb as a console application with pbcompiler and start the result.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- PureBasic compiler proprietario unavailable.

## Primary sources

- [https://www.purebasic.com/documentation/console/printn.html](https://www.purebasic.com/documentation/console/printn.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pb` | [hello.pb](hello.pb), [main.pb](variants/pbi-e96dcf89/main.pb) created; verification pending |
| `.pbi` | [hello.pbi](variants/pbi-e96dcf89/hello.pbi) created; verification pending |

</details>
