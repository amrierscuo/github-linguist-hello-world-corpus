# #804 Zeek

Run zeek_init without network capture.

## Toolchain

Zeek runtime

## Procedure

zeek hello.zeek

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

Only start of the local script, no capture interface or network.

Remaining requirements:
- Zeek parser/runtime unavailable.

## Primary sources

- [https://docs.zeek.org/en/current/scripting/basics.html](https://docs.zeek.org/en/current/scripting/basics.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.zeek` | [hello.zeek](hello.zeek) created; verification pending |
| `.bro` | [hello.bro](variants/bro-c936c4b3/hello.bro) created; verification pending |
