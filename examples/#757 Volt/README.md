# #757 Volt

## Verified on November 20, 2026

Volta compiled the unchanged bytes of hello.volt with Watt from a temporary src/main.volt copy. The linked x86-64 Linux executable ran in WSL, printed the exact greeting on stdout and exited 0.

Run `battery config /path/to/Volta /path/to/Watt . && battery -j 4 build && ./corpusGreeting`.

[Commands, toolchain, output and SHA-256](verification/native_20261120_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill out a Volt program with the watt.io module and print your greeting.

Canonical type `programming`, language_id `390`.

Suggested toolchain: Volt Volta compiler and Watt standard library.

From the example directory:

```sh
volta hello.volt -o hello
./hello
```

Expected result: stdout Hello, World! and newline.

Volt is the D-like language of the VoltLang project, distinguished by V and Phalcon Volt templates.

Initial state: created; syntax and behavioral verification pending. Volta compiler and Watt library not available.

Sources:

- [Volt language](https://volt-lang.org/)
- [Volta source](https://github.com/VoltLang/Volta)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.volt` | [hello.volt](hello.volt) Syntax and behavior verified |

</details>
