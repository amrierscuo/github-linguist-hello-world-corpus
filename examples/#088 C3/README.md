# #088 C3

Stampare esattamente Hello, World! seguito da newline con std::io in C3.

## Toolchain

C3 0.8.4 / LLVM 22.1.8 (Windows)

## Commands and procedure

With official C3 0.8.4 distribution, from the example folder:

```text
c3c --version
c3c compile hello.c3 -o hello
hello.exe
```

On Linux/macOS the last command is `./hello`. To keep separate derivatives,
the test compiled a copy of the source in a work folder and has
recorded the hash of the original source delivered.

## Expected result

Filler and linker exit 0; executable exit 0 and stdout Hello, World! more newline.

## Status

syntax and behavior verified.

Compilation, linking and execution really performed with the official compiler C3 portable Windows.

Actual verification of 2026-10-08T11:34:07.737503+00:00 on Windows x64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://c3-lang.org/getting-started/hello-world/](https://c3-lang.org/getting-started/hello-world/)
- [https://github.com/c3lang/c3c/releases/tag/v0.8.4](https://github.com/c3lang/c3c/releases/tag/v0.8.4)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.c3` | [hello.c3](hello.c3) verified |
