# #498 Opal

## Verified on November 19, 2026

For the Ruby-to-JavaScript dialect used by the referenced Linguist sample, Opal compiled the corpus source to JavaScript. The compiled code called the browser alert bridge with the exact greeting, which the headless host captured as text.

Run `opal -I . -r browser_bridge --compile hello.opal > greeting.js; node check.js`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Show greeting with alert in the .opal dialect of the baseline.

## Toolchain

Runtime Opal compatibile con StoneCypher/DeepakChopra_Opal

## Procedure

Charge hello.opal in the runtime compatible with the upstream sample; record compiler and actual procedure.

## Expected result

Finestra alert con Hello, World!.

## Status

Syntax and behavioral verification pending.

The choice of alerts and comments -- follows the Linguist/upstream sample; it is not replaced with the Ruby Opal language or with the distinct OPAL algebric.

Remaining requirements:
- The runtime/compilatore historical dialect .opal has not been identified and prepared.

## Primary sources

- [https://github.com/StoneCypher/DeepakChopra_Opal](https://github.com/StoneCypher/DeepakChopra_Opal)
- [https://github.com/github-linguist/linguist/blob/main/samples/Opal/DeepakChopra.opal](https://github.com/github-linguist/linguist/blob/main/samples/Opal/DeepakChopra.opal)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.opal` | [hello.opal](hello.opal) Syntax and behavior verified |

</details>
