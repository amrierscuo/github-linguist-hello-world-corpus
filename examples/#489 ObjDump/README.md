# #489 ObjDump

Produce an authentic ObjDump list of the greeting C program.

## Toolchain

GNU objdump (GNU Binutils for Ubuntu) 2.42; gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0

## Procedure

gcc hello.c -o build/hello; (cd build && objdump -d -s hello > hello.objdump); build/hello; objcopy --dump-section .rodata=build/rodata.bin build/hello

## Expected result

Hello, World!

## Status

syntax and behavior verified.

hello.objdump is real text output; ELF and binary section remain in work. Greeting is controlled in .rodata section and in program execution.

Real check 2026-10-08T13:10:44.904153+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://sourceware.org/binutils/docs/binutils/objdump.html](https://sourceware.org/binutils/docs/binutils/objdump.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.objdump` | [hello.objdump](hello.objdump) verified |
