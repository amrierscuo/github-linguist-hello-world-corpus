# #515 Oz

## Verified on November 18, 2026

Mozart evaluated the exact expression in a headless harness. The harness sent Browse’s actual argument to the standard console reporter and observed the greeting.

Run `ozc -x check.oz -o hello-oz; ozengine hello-oz`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Show greeting in Mozart Oz's browser.

Canonical type `programming`, language_id `270`.

Provided Toolchain: Mozart Oz runtime and Browser.

From the example directory:

```sh
ozengine hello.oz
```

Expected result: Browser shows the Hello, World! string.

Browse is a view in the runtime, not a guaranteed stdout print.

Initial state: created; syntax and behavioral verification pending. Mozart runtime unavailable.

Sources:

- [Mozart Oz tutorial](https://mozart.github.io/mozart-v1/doc-1.4.0/tutorial/index.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.oz` | [hello.oz](hello.oz) Syntax and behavior verified |

</details>
