# #313 Ink

Fill out an Ink story that emits Hello, World! and reaches END.

## Toolchain

Official inklecate v1.2.1 Windows release; generated inkVersion 21

## Commands and procedure

inklecate -o build/hello.json hello.ink; inklecate -p hello.ink

## Expected result

JSON of the story valid for Ink runtime; Play issues greeting and ends, exit 0.

## Status

syntax and behavior verified.

Both phases use the original inklecate tool; the compiler and runtime of Play are real. JSON compiled only in work.

Actual verification of 2026-10-08T12:29:57.976554+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://github.com/inkle/ink](https://github.com/inkle/ink)
- [https://github.com/inkle/ink/releases/tag/v1.2.1](https://github.com/inkle/ink/releases/tag/v1.2.1)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ink` | [hello.ink](hello.ink) verified |
