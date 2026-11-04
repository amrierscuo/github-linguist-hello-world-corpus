# #086 C-ObjDump

Keep an authentic C-ObjDump disassembled from the C program that prints Hello, World!, including the C lines and main instructions.

## Toolchain

gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 / GNU objdump (GNU Binutils for Ubuntu) 2.42

## Commands and procedure

Rigenerazione con toolchain ELF x86_64 Linux/WSL:

```sh
mkdir -p build
gcc -std=c11 -Wall -Wextra -Werror -g -O0 -fno-pie -no-pie -o build/hello hello.c
objdump --version
objdump -d -S build/hello > build/hello.c-objdump
./build/hello
```

The listing delivered is a test produced by the tool.
compiler can change between toolchain; the main source and the
greetings remain recognizable. The pathways of the springs are normalized for
publish a legible artifact without reference to the local machine.

## Expected result

Objdump exit 0; text contains main, instructions and source puts( "Hello, World!")); C program prints greeting, exit 0.

## Status

syntax and behavior verified.

objdump produces hello.c-objdump. Absolute source paths are normalized to <corpus>; the format and instructions are unchanged from the tool output. The listing is a data format. The execution check covers the corresponding C ELF binary, retained only in work.

Actual verification of 2026-10-08T11:33:36.476099+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://sourceware.org/binutils/docs/binutils/objdump.html](https://sourceware.org/binutils/docs/binutils/objdump.html)
- [https://gcc.gnu.org/onlinedocs/gcc/Standards.html](https://gcc.gnu.org/onlinedocs/gcc/Standards.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.c-objdump` | [hello.c-objdump](hello.c-objdump) verified |
