# #391 Literate Agda

## Verified on November 18, 2026

Agda selected the literate code block, typechecked the original source against the standard IO library and compiled it with the native GHC backend. The executable printed the greeting.

Run `agda --guardedness -i /usr/share/agda-stdlib --compile Hello.lagda; ./Hello`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill out a literary Agda program that uses IO.Main to print your greeting.

## Toolchain

Agda e agda-stdlib compatibili; versione da registrare

## Commands and procedure

agda -i <agda-stdlib/src> --compile Hello.lagda; run the main compiled by toolchain Agda/GHC

## Expected result

Selected code blocks; type Main accepted; runtime press Hello, World!.

## Status

Syntax and behavioral verification pending.

File LaTeX letterato originale con blocco code; la libreria standard fornisce run/putStrLn e Main. Non basta un compilatore LaTeX per verificare Agda.

Remaining requirements:
- Agda/stdlib/backend GHC not available; type check and IO pending.

## Primary sources

- [https://agda.readthedocs.io/en/latest/tools/literate-programming.html](https://agda.readthedocs.io/en/latest/tools/literate-programming.html)
- [https://agda.github.io/agda-stdlib/v2.0/IO.html](https://agda.github.io/agda-stdlib/v2.0/IO.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lagda` | [Hello.lagda](Hello.lagda) Syntax and behavior verified |

</details>
