# #824 mupad

## Verified on November 19, 2026

The compatible Giac runtime executed the unchanged MuPAD program bytes after selecting its MuPAD compatibility mode, and the print call emitted the exact greeting.

Run `{ printf "xcas_mode(2);\n"; cat hello.mu; } | icas`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave756_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

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
| `.mu` | [hello.mu](hello.mu) Syntax and behavior verified |

</details>
