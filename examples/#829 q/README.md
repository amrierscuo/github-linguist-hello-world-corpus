# #829 q

## Verified on November 18, 2026

The published PeachQ implementation executed the unchanged q script. Its console printed the exact greeting.

Run `q hello.q (then close STDIN)`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Run a q file that writes greeting.

## Toolchain

KX q runtime

## Procedure

q hello.q; record output and exit from the test runtime.

## Expected result

Hello, World!

## Status

Syntax and behavioral verification pending.

- 1 is the handle console text; the sample uses the q canon language KX.

Remaining requirements:
- KX q runtime unavailable.

## Primary sources

- [https://code.kx.com/q/ref/file-text/](https://code.kx.com/q/ref/file-text/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.q` | [hello.q](hello.q) Syntax and behavior verified |

</details>
