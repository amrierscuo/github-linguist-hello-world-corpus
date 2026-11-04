# #041 Assembly

Voce canonica: `Assembly`, tipo `programming`, `language_id: 24`.

Print exactly Hello, World! with syscall Linux x86_64 write, then finish with 0. status

## Toolchain and reproduction

GNU GAS and ld, Linux x86_64 syscall ABI, GNU assembler ( GNU Binutils for Ubuntu) 2.42. Test environment: **Ubuntu 24.04 WSL2/Linux x86_64**.

Run in Linux x86_64 with GNU Binutils. In Windows use Ubuntu WSL2; this source uses GAS in syntax Intel and ABI Linux, not the PE Windows format.

Comando/procedura from the example directory:

```text
as --64 -o hello.o hello.s; ld -o hello hello.o; ./hello
```

Exit 0; stdout exactly Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The check assembles the original bytes, links an ELF binary in an isolated directory and runs that binary. It does not require libc.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain and SHA-256 of artifacts. `path_normalization` describes the replacements of artifacts.
machine paths; source bytes remain those identified by checksums.
If the log only records the availability of the tools, no parsing or runtime is attested.
Tools, dependencies and verification products remain in the work directory.

## Primary sources

- [https://sourceware.org/binutils/docs/as/i386_002dSyntax.html](https://sourceware.org/binutils/docs/as/i386_002dSyntax.html)
- [https://sourceware.org/binutils/docs/as/i386_002dOptions.html](https://sourceware.org/binutils/docs/as/i386_002dOptions.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.asm` | [hello.asm](variants/ext-asm-2e61736d/hello.asm) created; verification pending |
| `.a51` | [hello.a51](variants/ext-a51-2e613531/hello.a51) created; verification pending |
| `.i` | [hello.i](variants/ext-i-2e69/hello.i) created; verification pending |
| `.inc` | [hello.inc](variants/ext-inc-2e696e63/hello.inc) created; verification pending |
| `.nas` | [hello.nas](variants/ext-nas-2e6e6173/hello.nas) created; verification pending |
| `.nasm` | [hello.nasm](variants/ext-nasm-2e6e61736d/hello.nasm) created; verification pending |
| `.s` | [hello.s](hello.s), [consumer.s](variants/ext-inc-2e696e63/consumer.s) created; verification pending |
