# #101 CWeb

Extract a C program from the CWEB source, compile it and print Hello, World! followed by LF.

Canonical type: `programming`; `language_id`: `657332628`.

Toolchain provided: CWEB 4.x (ctangle) and C compiler compliant with C11.

From the example folder, depending on the PATH:

```sh
ctangle hello.w
cc -std=c11 -Wall -Wextra hello.c -o hello
./hello
```

Expected result: exact stdout `Hello, World!\n`, 0. output

The ctangle check covers the .w source; C compilation checks the extracted code. Typesetting with cweave/TeX is a separate step.

Recorded status: syntax verified; behavior verified. Tried toolchain: MiKTeX CTANGLE (version banner in log) + GCC 13.3.0 on WSL Ubuntu 24.04. See [log](verification/verification.log).

Primary sources or original references of the project:

- [CWEB — Knuth e Levy](https://www-cs-faculty.stanford.edu/~knuth/cweb.html)
- [Implementazione CWEB](https://github.com/ascherer/cweb)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.w` | [hello.w](hello.w) verified |
