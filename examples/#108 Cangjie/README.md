# #108 Cangjie

## Verified on November 18, 2026

The published compiler built the unchanged Cangjie program and the resulting console application printed the exact greeting.

Run `source envsetup.sh; cjc hello.cj -o hello; ./hello`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_wave736_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Fill out a Cangjie program that prints Hello, World! followed by newline.

Canonical type: `programming`; `language_id`: `581895317`.

Suggested toolchain: Cangjie SDK 1.0.0 or compatible, cjc compiler.

From the example folder, depending on the PATH:

```sh
cjc hello.cj -o hello
./hello
```

Expected result: stdout `Hello, World!` followed by newline, 0. output

On Windows produce hello.exe and start it with.\ hello.exe. The main signature and println follow the compiler guide.

Initial state: artifact created, syntax and behavioral verification pending. Specific toolchain not yet performed on this example; syntax and behavior remain to be checked.

Primary sources or original references of the project:

- [Cangjie — primo programma](https://docs.cangjie-lang.cn/en/docs/1.0.0/user_manual/source_en/first_understanding/hello_world.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cj` | [hello.cj](hello.cj) Syntax and behavior verified |

</details>
