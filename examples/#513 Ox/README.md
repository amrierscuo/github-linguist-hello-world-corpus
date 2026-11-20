# #513 Ox

## Verified on November 20, 2026

The published Ox compiler and runtime loaded their packaged standard library, compiled the original hello.ox and ran its main function. The worker emitted the exact greeting and reported exit code 0 in a headless WSL process.

Run `node oxrun_worker_runner.cjs oxrun_assets.json hello.ox with the files and digests recorded in the evidence`.

[Commands, toolchain, output and SHA-256](verification/native_20261120_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Run main Ox and print your greeting.

Canonical type `programming`, language_id `268`.

Suggested toolchain: Ox Console/OxMetrics and oxstd.

From the example directory:

```sh
oxl hello.ox
```

Expected result: stdout Hello, World! followed by newline.

Ox is the econometric language of Jurgen Doornik; it is not replaced with a C compiler.

Initial state: created; syntax and behavioral verification pending. Runtime Ox unavailable.

Sources:

- [Ox documentation](https://www.doornik.com/ox/ox.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ox` | [hello.ox](hello.ox), [hello.ox](variants/oxh-134bfc42/hello.ox) created; verification pending |
| `.oxh` | [hello.oxh](variants/oxh-134bfc42/hello.oxh) created; verification pending |
| `.oxo` | artifact to generate Ox object compiled: requires original compilation of the target version; no binary or .ox source is produced. |

</details>
