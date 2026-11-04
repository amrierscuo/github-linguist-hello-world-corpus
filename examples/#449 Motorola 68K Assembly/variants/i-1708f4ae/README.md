# #449 Motorola 68K Assembly .i

Includes GNU as with .s. driver The original variant of the corpus keeps the bytes identified by checksum.

## Toolchain and verification

GNU Binutils m68k 2.42 and QEMU user 8.2.2. Run from the directory of the variant; <output> indicates an external working directory.

```text
m68k-linux-gnu-as -m68000 -o <output>/hello.o driver.s; m68k-linux-gnu-ld -o <output>/hello <output>/hello.o; qemu-m68k <output>/hello
```

Artifact **created**; syntax **verified**; behavior **verified**.

The original toolchain has controlled this specific variant.The BitBake task or the executable m68k produces Hello, World! and ends with exit 0. Exit does not come only from equality with the main sample.

Try: [finish_variants.json](../../verification/finish_variants.json), with commands, UTC, versions, exit code, output and hash.

## Verified Sources

- [hello.i](hello.i) SHA-256 `07db4e9cdf3ea13526449c3b91b3454d73faf65cf860ad15213894d176bc44ed`.
- [driver.s](driver.s) SHA-256 `fe4b583f432de82420684d0df94692bee5ee5f6fbfc447c34d8a16ac79ee9b20`.

## Primary sources

- https://sourceware.org/binutils/docs/as/M68K_002dDependent.html
- https://www.kernel.org/doc/html/latest/arch/m68k/index.html
