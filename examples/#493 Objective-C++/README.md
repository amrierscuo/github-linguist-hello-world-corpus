# #493 Objective-C++

Fill out a class and send an Objective-C+ message.

## Toolchain

g++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0; GNU libobjc4 14.2.0

## Procedure

g++ hello.mm -lobjc -o build/hello; build/hello

## Expected result

Hello, World!

## Status

syntax and behavior verified.

The class uses object of the GNU runtime and a class method; Objective-C++ actually uses std:: string/std::cout. No Foundation library needed.

Real check 2026-10-08T13:11:33.760305+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://gcc.gnu.org/onlinedocs/gcc/Objective-C.html](https://gcc.gnu.org/onlinedocs/gcc/Objective-C.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.mm` | [hello.mm](hello.mm) verified |
