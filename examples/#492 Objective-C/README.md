# #492 Objective-C

Fill in a class and send an Objective-C message.

## Toolchain

gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0; GNU libobjc4 14.2.0

## Procedure

gcc hello.m -lobjc -o build/hello; build/hello

## Expected result

Hello, World!

## Status

syntax and behavior verified.

The class uses object of the GNU runtime and a class method; Objective-C++ actually uses std:: string/std::cout. No Foundation library needed.

Real check 2026-10-08T13:11:32.225683+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://gcc.gnu.org/onlinedocs/gcc/Objective-C.html](https://gcc.gnu.org/onlinedocs/gcc/Objective-C.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.m` | [hello.m](hello.m), [greeting.m](variants/h-ff25ca0d/greeting.m) created; verification pending |
| `.h` | [hello.h](variants/h-ff25ca0d/hello.h) created; verification pending |
