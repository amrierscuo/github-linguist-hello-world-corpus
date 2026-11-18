# #599 Rascal

## Verified on November 18, 2026

The official Rascal interpreter executed the original program unchanged in a minimal project and emitted the expected greeting.

Run `java -Drascal.path=src -jar rascal-0.43.0.jar Hello`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Perform an entry point Rascal calling IO.println.

Canonical type `programming`, language_id `173616037`.

Suggested toolchain: Rascal interpreter JVM.

From the example directory:

```sh
java -jar rascal-shell.jar Hello.rsc
```

Expected result: stdout Hello, World! and newline.

The name of the module corresponds to the name of the file; it requires the Rascal engine.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Rascal IO](https://www.rascal-mpl.org/docs/Library/IO/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rsc` | [Hello.rsc](Hello.rsc) Syntax and behavior verified |

</details>
