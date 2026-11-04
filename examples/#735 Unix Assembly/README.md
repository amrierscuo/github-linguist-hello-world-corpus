# #735 Unix Assembly

Assemble syntax GNU AT &T and issue greeting via Linux syscall.

## Toolchain

GNU assembler (GNU Binutils for Ubuntu) 2.42

## Procedure

as -o build/hello.o hello.s; ld -o build/hello build/hello.o; build/hello

## Expected result

Hello, World!

## Status

syntax and behavior verified.



Real check 2026-10-08T13:30:06.052119+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://sourceware.org/binutils/docs/as/](https://sourceware.org/binutils/docs/as/)
- [https://man7.org/linux/man-pages/man2/write.2.html](https://man7.org/linux/man-pages/man2/write.2.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.s` | [hello.s](hello.s) verified |
| `.ms` | [hello.ms](variants/ms-5138d9ae/hello.ms) created; verification pending |
