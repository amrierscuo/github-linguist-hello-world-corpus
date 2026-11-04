# #312 Inform 7

Fill out a story Inform 7 that greets you on startup and ends.

## Toolchain

inform7 version 10.1.2 'Krypton' (29 August 2022); Inform 6 Inform 6.41 for Linux (22nd July 2022); Frotz 2.54

## Commands and procedure

inform7 -internal <risorse-vendor> -external build/external -transient build/transient -no-index -no-problems -no-census-update -format=Inform6/16 -source hello.ni -o build/hello.inf; inform6 -wSDv8 build/hello.inf build/hello.z8; dfrotz -m build/hello.z8 (stdin: quit più newline)

## Expected result

Transcript contains Hello, World!; quit closes the final menu and runtime ends with exit 0.

## Status

syntax and behavior verified.

The rules in natural language are compiled by Inform 7, translated into the Backend Inform 6 and interpreted by Frotz as true story Z-machine v8. The standard final menu is part of the transcript; no stdout is required composed only by the greeting. Story/Inter/output binaries remain in work.

Actual verification of 2026-10-08T12:34:30.772531+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://github.com/ganelson/inform/releases/tag/v10.1.2](https://github.com/ganelson/inform/releases/tag/v10.1.2)
- [https://ganelson.github.io/inform-website/](https://ganelson.github.io/inform-website/)
- [https://davidgriffith.gitlab.io/frotz/](https://davidgriffith.gitlab.io/frotz/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ni` | [hello.ni](hello.ni), [hello.ni](variants/i7x-25250f70/hello.ni) created; verification pending |
| `.i7x` | [Corpus Greeting.i7x](variants/i7x-25250f70/Corpus%20Greeting.i7x) created; verification pending |
