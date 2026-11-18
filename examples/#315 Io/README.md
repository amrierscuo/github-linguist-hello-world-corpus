# #315 Io

## Verified on November 18, 2026

The native Io runtime sent println to the string object in the unchanged source and emitted the greeting.

Run `io hello.io`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Send println to a string in the runtime I.

## Toolchain

IoLanguage Io; versione da registrare

## Commands and procedure

io hello.io

## Expected result

Hello, World! more newline; exit 0.

## Status

Syntax and behavioral verification pending.

The program uses the dispatch to messages of Io and the println method of the string. No translation to other languages is used to count verification.

Remaining requirements:
- Interprete Io nativo non preparato; parsing/evaluation pending.

## Primary sources

- [https://iolanguage.org/docs/Tutorial/index.html](https://iolanguage.org/docs/Tutorial/index.html)
- [https://github.com/IoLanguage/io](https://github.com/IoLanguage/io)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.io` | [hello.io](hello.io) Syntax and behavior verified |

</details>
