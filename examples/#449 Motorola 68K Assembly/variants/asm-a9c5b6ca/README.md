# #449 Motorola 68K Assembly .asm

Motorola 68000 source in the GNU dialect as Linux. The original corpus variant retains the bytes identified by the checksum.

## Toolchain and verification

GNU Binutils m68k 2.42 and QEMU user 8.2.2. Run from the directory of the variant; <output> indicates an external working directory.

```text
m68k-linux-gnu-as -m68000 -o <output>/hello.o hello.asm; m68k-linux-gnu-ld -o <output>/hello <output>/hello.o; qemu-m68k <output>/hello
```

Artifact **created**; syntax **verified**; behavior **verified**.

The original toolchain has controlled this specific variant.The BitBake task or the executable m68k produces Hello, World! and ends with exit 0. Exit does not come only from equality with the main sample.

Try: [finish_variants.json](../../verification/finish_variants.json), with commands, UTC, versions, exit code, output and hash.

## Verified Sources

- [hello.asm](hello.asm) SHA-256 `a2b40cbf257839c9302d478550cf7d3de7141e85350979c4ed03846991aae150`.

## Primary sources

- https://sourceware.org/binutils/docs/as/M68K_002dDependent.html
- https://www.kernel.org/doc/html/latest/arch/m68k/index.html
