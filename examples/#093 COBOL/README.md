# #093 COBOL

Print exactly Hello, World! followed by newline from a COBOL program in free format.

## Toolchain

cobc (GnuCOBOL) 3.1.2.0

## Commands and procedure

Con GnuCOBOL e la propria libreria libcob disponibili:

```sh
mkdir -p build
cobc --version
cobc -x -free -o build/hello hello.cob
./build/hello
```

In the test the packages were extracted in a work folder and invoked with
COB_CONFIG_DIR, COB_COPY_DIR, LD_LIBRARY_PATH e percorsi include/library
local. In a normal installation these paths are already configured.

## Expected result

Filling and linking exit 0; exit program 0, stdout Hello, World! plus newline.

## Status

syntax and behavior verified.

Toolchain GnuCOBOL obtained from locally extracted Ubuntu packages; no global installation. The C backend compiler issued a _FORTIFY_SOURCE redefinition warning, kept in the log; successfully executed program.

Actual verification of 2026-10-08T11:33:57.576818+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

## Primary sources

- [https://gnucobol.sourceforge.io/doc/gnucobol.html](https://gnucobol.sourceforge.io/doc/gnucobol.html)
- [https://gnucobol.sourceforge.io/HTML/gnucobpg.html](https://gnucobol.sourceforge.io/HTML/gnucobpg.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cob` | [hello.cob](hello.cob), [consumer.cob](variants/ext-cpy-2e637079/consumer.cob) created; verification pending |
| `.cbl` | [hello.cbl](variants/ext-cbl-2e63626c/hello.cbl) created; verification pending |
| `.ccp` | [hello.ccp](variants/ext-ccp-2e636370/hello.ccp) created; verification pending |
| `.cobol` | [hello.cobol](variants/ext-cobol-2e636f626f6c/hello.cobol) created; verification pending |
| `.cpy` | [hello.cpy](variants/ext-cpy-2e637079/hello.cpy) created; verification pending |
