# #309 ImHex Pattern Language

Mapping 13 byte ASCII Hello, World! with an ImHex pattern.

## Toolchain

ImHex / PatternLanguage ufficiale; versione da registrare

## Commands and procedure

In ImHex open hello.txt as data, upload hello.hexpat and Evaluate; inspect greeting

## Expected result

Pattern greeting[ 13 ] at 0 contains exactly Hello, World!.

## Status

Syntax and behavioral verification pending.

hello.txt is a ASCII fixture without newline, long 13 byte. The original pattern describes a view of data and non-print. Only official evaluator can validate syntax and mapping.

Remaining requirements:
- ImHex/PatternLanguage assessor unavailable; no custom parser is counted as verification.

## Primary sources

- [https://github.com/WerWolv/PatternLanguage](https://github.com/WerWolv/PatternLanguage)
- [https://imhex.werwolv.net/](https://imhex.werwolv.net/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.hexpat` | [hello.hexpat](hello.hexpat) created; verification pending |
