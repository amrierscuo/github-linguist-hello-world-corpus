# #083 C

Print exactly Hello, World! followed by newline from a C11 program.

## Toolchain

gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0

## Commands and procedure

Run in Linux/WSL, creating a temporary build folder:

```sh
mkdir -p build
gcc --version
gcc -std=c11 -Wall -Wextra -Werror -o build/hello hello.c
./build/hello
```

The delivered corpus contains the source and the log; the test executable remains
in a workbook outside the artifacts to be published.

## Expected result

Exit 0; exit program 0 and stdout Hello, World! plus newline.

## Status

syntax and behavior verified.

Real compilation and execution with GCC; puts adds the newline character.

Actual verification of 2026-10-08T11:33:31.686254+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://gcc.gnu.org/onlinedocs/gcc/Standards.html](https://gcc.gnu.org/onlinedocs/gcc/Standards.html)
- [https://www.gnu.org/software/libc/manual/html_node/Simple-Output.html](https://www.gnu.org/software/libc/manual/html_node/Simple-Output.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.c` | [hello.c](hello.c), [consumer.c](variants/ext-h-2e68/consumer.c), [consumer.c](variants/ext-h-in-2e682e696e/consumer.c) created; verification pending |
| `.cats` | [hello.cats](variants/ext-cats-2e63617473/hello.cats) created; verification pending |
| `.h` | [hello.h](variants/ext-h-2e68/hello.h) created; verification pending |
| `.h.in` | [hello.h.in](variants/ext-h-in-2e682e696e/hello.h.in) created; verification pending |
| `.idc` | [hello.idc](variants/ext-idc-2e696463/hello.idc) created; verification pending |
