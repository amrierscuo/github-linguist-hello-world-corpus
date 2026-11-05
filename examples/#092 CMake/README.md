# #092 CMake

## Latest recorded verification

Latest extension checks:
- `.cmake`: Native CMake executed the exact configuration script, substituted the original @GREETING@ template, and executed its generated script with the expected greeting. The aggregate .cmake record also ran the original main script and checked its stderr channel. [Evidence](verification/native_20261105_batch_2e636d616b65.json).
- `.cmake.in`: Native CMake executed the exact configuration script, substituted the original @GREETING@ template, and executed its generated script with the expected greeting. The aggregate .cmake record also ran the original main script and checked its stderr channel. [Evidence](verification/native_20261105_batch_2e636d616b652e696e.json).

Perform in CMake script mode a check on the value greeting and write Hello, World! with message.

## Toolchain

cmake version 4.4.4

## Commands and procedure

You do not need a project or C/C++ compiler; use the script mode:

```sh
cmake --version
cmake -P hello.cmake
```

Greeting appears on stderr. An error on the value of the variable would be
reported by FATAL_ERROR and would produce a different command result from zero.

## Expected result

Exit 0; stderr contains exactly Hello, World! plus newline; empty stdout.

## Status

syntax and behavior verified.

message without STATUS mode sends the message to stderr: the correct channel is explicitly verified. if/FATAL_ERROR control is performed by the real CMake.

Actual verification of 2026-10-08T11:33:20.658387+00:00 on Windows x64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://cmake.org/cmake/help/latest/manual/cmake.1.html](https://cmake.org/cmake/help/latest/manual/cmake.1.html)
- [https://cmake.org/cmake/help/latest/command/message.html](https://cmake.org/cmake/help/latest/command/message.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cmake` | [hello.cmake](hello.cmake), [configure.cmake](variants/ext-cmake-in-2e636d616b652e696e/configure.cmake) syntax and behavior verified |
| `.cmake.in` | [hello.cmake.in](variants/ext-cmake-in-2e636d616b652e696e/hello.cmake.in) syntax and behavior verified |