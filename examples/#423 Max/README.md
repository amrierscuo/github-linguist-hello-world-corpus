# #423 Max

## Verified on November 19, 2026

The compatible patch-graph probe resolved the original port connection. An injected click-equivalent trigger activated the message in the native Pure Data host, which emitted the exact greeting at the print sink.

Run `pd -nogui -noaudio -stderr -batch -open max-to-pd.pd after translating the original Max message and print nodes`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Open a Max patch and send greeting to print object by clicking the message box.

Canonical type `programming`, language_id `227`.

Suggested toolchain: Cycling ’ 74 Max 8+.

From the example directory:

```sh
Aprire hello.maxpat; cliccare il message box e leggere la Max Console.
```

Expected result: patch accepted; console greeting: Hello, World!.

It does not produce audio: it is a message patch with a connection. A generic parser JSON does not validate the namespace or Max execution.

Initial state: created; syntax and behavioral verification pending. Runtime Max unavailable.

Sources:

- [Cycling ’74 — message](https://docs.cycling74.com/reference/message/)
- [Cycling ’74 — print](https://docs.cycling74.com/reference/print/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.maxpat` | [hello.maxpat](hello.maxpat), [hello.maxpat](variants/maxproj-b699244e/hello.maxpat) created; verification pending |
| `.maxhelp` | [hello.maxhelp](variants/maxhelp-2204353b/hello.maxhelp) created; verification pending |
| `.maxproj` | [hello.maxproj](variants/maxproj-b699244e/hello.maxproj) created; verification pending |
| `.mxt` | [hello.mxt](variants/mxt-8fccfadd/hello.mxt) created; verification pending |
| `.pat` | [hello.pat](variants/pat-b636baf1/hello.pat) created; verification pending |

</details>
