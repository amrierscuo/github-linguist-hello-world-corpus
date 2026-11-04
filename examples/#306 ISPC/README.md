# #306 ISPC

Fill out an exported ISPC function that prints greeting and invoke it from a C++ harness.

## Toolchain

Intel(r) Implicit SPMD Program Compiler (Intel(r) ISPC), 1.31.0 (build commit c6adb4f86f5678ce @ 20260625, LLVM 23.0.0); g++ (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0

## Commands and procedure

ispc hello.ispc --pic --target=sse2-i32x4 -h build/hello_ispc.h -o build/hello.o; g++ -I build main.cpp build/hello.o -o build/hello; build/hello

## Expected result

Exit 0 and a Hello, World! line.

## Status

syntax and behavior verified.

ISPC print is an original output operation; the constant greeting is issued once per gang. main.cpp is only the caller of the generated API. --pic allows the linking PIE of the Ubuntu compiler.

Actual verification of 2026-10-08T12:31:12.168007+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://ispc.github.io/ispc.html](https://ispc.github.io/ispc.html)
- [https://github.com/ispc/ispc/releases/tag/v1.31.0](https://github.com/ispc/ispc/releases/tag/v1.31.0)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ispc` | [hello.ispc](hello.ispc) verified |
