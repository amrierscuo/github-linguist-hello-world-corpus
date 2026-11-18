# #390 Liquidsoap

## Verified on November 18, 2026

The native Liquidsoap CLI evaluated its original print operation during the check. The script did not start streaming.

Run `liquidsoap --check hello.liq`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Evaluate a Liquidsoap script that prints greeting without configuring streaming.

## Toolchain

Liquidsoap; versione da registrare

## Commands and procedure

liquidsoap --check hello.liq; liquidsoap --check-and-evaluate hello.liq (check availability option in the selected version)

## Expected result

Type of accepted print; evaluation writes Hello, World!.

## Status

Syntax and behavioral verification pending.

The sample is pure text and does not open sources, devices or streams. The evaluation command must be adattato/registrato according to the actual CLI; there is no generic parser OCaml.

Remaining requirements:
- Runtime Liquidsoap non predisposto; parsing/type check e valutazione pending.

## Primary sources

- [https://www.liquidsoap.info/doc-2.2.5/language.html](https://www.liquidsoap.info/doc-2.2.5/language.html)
- [https://www.liquidsoap.info/doc-2.2.5/script_loading.html](https://www.liquidsoap.info/doc-2.2.5/script_loading.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.liq` | [hello.liq](hello.liq) Syntax and behavior verified |

</details>
