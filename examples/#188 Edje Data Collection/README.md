# #188 Edje Data Collection

## Verified on November 18, 2026

Edje compiled the original collection. In a private rendering buffer the runtime loaded the collection and exposed the exact text of its genuine label part.

Run `edje_cc hello.edc hello.edj; run verify_edje.c with Edje and Ecore-Evas`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill out a Edje group with a textual part showing Hello, World!.

Canonical type `data`, language_id `342840478`.

Toolchain provided: EFL/Edje with edje_cc and viewer edje_player or Edje application.

From the example directory:

```sh
edje_cc hello.edc hello.edj
edje_player hello.edj -g greeting
```

Expected result: greeting collection compiled; in the label part appears Hello, World!.

The compilation of the collection and the observation of the text in the viewer are distinct controls; it serves a EFL graphic environment with Sans font available.

Initial state: created; syntax and behavioral verification pending. native toolchain not yet performed: syntax and behavior verifications remain pending.

Sources of linguaggio/formato and original implementations:

- [Edje — riferimento EDC originale](https://github.com/Enlightenment/efl/blob/master/doc/edcref.dox)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.edc` | [hello.edc](hello.edc) Syntax and behavior verified |

</details>
