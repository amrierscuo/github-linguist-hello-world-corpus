# #414 MUF

## Verified on November 19, 2026

Fuzzball loaded the original MUF source through its editor, compiled it, dispatched it as an action and delivered the exact native notification to the test player.

Run `python3 execute_muf.py <fbmuck> <minimal.db> hello.muf in an isolated network namespace`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave756_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Send a Hello, World! message to the local user in a MUCK test environment.

Canonical type `programming`, language_id `219`.

Suggested toolchain: Fuzzball MUCK with compilatore/interprete MUF.

From the example directory:

```sh
Compilare hello.muf come programma nel server MUCK locale di prova e invocarlo.
```

Expected result: compiled program; the user who performs it receives Hello, World!.

No public server connection: behavior requires a local MUCK runtime with the recipient me.

Initial state: created; syntax and behavioral verification pending. Local runtime MUCK/MUF unavailable.

Sources:

- [Fuzzball — MUF Reference Manual](https://www.fuzzball.org/docs/mufman.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.muf` | [hello.muf](hello.muf) Syntax and behavior verified |
| `.m` | [hello.m](variants/m-f7140aa0/hello.m) created; verification pending |

</details>
