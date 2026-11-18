# #104 Cadence

## Verified on November 18, 2026

The official Cadence VM ran the exact original script. The returned Cadence String was the expected greeting.

Run `go run -mod=mod . with the recorded local runtime harness`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Evaluate a Cadence 1.0 script and get the Hello, World! string.

Canonical type: `programming`; `language_id`: `270184138`.

Suggested toolchain: Play standalone Cadence of the project onflow/cadence, Go; Cadence 1.x. The version actually tried, when available, is in the log.

From the example folder, depending on the PATH:

```sh
cadence hello.cdc
```

Expected result: the value returned from main is the `Hello, World!` string.

It is a pure script, without contracts, accounts, keys or transactions on the network. syntax access(all) belongs to Cadence 1.x.

Initial state: artifact created, syntax and behavioral verification pending. Specific toolchain not yet performed on this example; syntax and behavior remain to be checked.

Primary sources or original references of the project:

- [Cadence — funzioni](https://cadence-lang.org/docs/language/functions)
- [Cadence — interprete standalone originale](https://github.com/onflow/cadence/tree/master/cmd/main)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cdc` | [hello.cdc](hello.cdc) Syntax and behavior verified |

</details>
