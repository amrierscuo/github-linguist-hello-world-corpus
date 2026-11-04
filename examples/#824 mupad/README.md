# #824 mupad

Evaluate a legacy MuPAD program.

## Toolchain

MuPAD symbolic runtime

## Procedure

Caricare/eseguire hello.mu in MuPAD and record string representation.

## Expected result

MuPAD print shows the Hello, World! string value, possibly bound by quotes.

## Status

Syntax and behavioral verification pending.



Remaining requirements:
- MuPAD legacy runtime unavailable; compatibility of the version to record.

## Primary sources

- [https://www.mathworks.com/help/symbolic/mupad.html](https://www.mathworks.com/help/symbolic/mupad.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mu` | [hello.mu](hello.mu) created; verification pending |
