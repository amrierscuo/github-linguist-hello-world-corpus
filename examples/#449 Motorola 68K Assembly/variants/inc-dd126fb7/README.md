# #449 Motorola 68K Assembly .inc

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

- [hello.inc](hello.inc) SHA-256 `07db4e9cdf3ea13526449c3b91b3454d73faf65cf860ad15213894d176bc44ed`.
- [driver.s](driver.s) SHA-256 `1a19af04d9d583b4706f1eebb64ebf1e2124968c76c9c14997fbe710695c3b2b`.

## Primary sources

- https://sourceware.org/binutils/docs/as/M68K_002dDependent.html
- https://www.kernel.org/doc/html/latest/arch/m68k/index.html
