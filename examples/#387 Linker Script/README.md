# #387 Linker Script

Place the Hello, World! string in a ELF section via an original script linker.

## Toolchain

GNU ld (GNU Binutils for Ubuntu) 2.42; GCC 13.3.0

## Commands and procedure

gcc main.c -Wl,-T,hello.ld -o build/hello; readelf -p .greeting build/hello; build/hello

## Expected result

Section .greeting contains the text; boundary symbols enclose 14 byte; runtime print greeting.

## Status

syntax and behavior verified.

INSERT AFTER .rodata integrates the script into the standard ELF layout. KEEP retains the section and the program really uses __greeting_start; it does not print a second independent string from the linker. No ELF delivered.

Actual verification of 2026-10-08T12:48:20.800152+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://sourceware.org/binutils/docs/ld/SECTIONS.html](https://sourceware.org/binutils/docs/ld/SECTIONS.html)
- [https://sourceware.org/binutils/docs/ld/Miscellaneous-Commands.html](https://sourceware.org/binutils/docs/ld/Miscellaneous-Commands.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ld` | [hello.ld](hello.ld) verified |
| `.lds` | [hello.lds](variants/lds-ad88c9e8/hello.lds) created; verification pending |
| `.x` | [hello.x](variants/x-bb42e4c6/hello.x) created; verification pending |
