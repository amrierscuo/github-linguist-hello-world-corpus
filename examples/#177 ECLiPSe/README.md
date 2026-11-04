# #177 ECLiPSe

Load a main preacher in ECLiPSe Prolog and printf of greeting.

## Toolchain

Official ECLiPSe CLP 7.2

## Commands and procedure

eclipse -e "get_flag(version, V), writeln(V)"; eclipse -b hello.ecl -e main

## Expected result

Upload exit 0; main writes Hello, World! more newline, exit 0.

## Status

syntax and behavior verified.

Runtime nativo ufficiale ECLiPSe CLP. La distribuzione portabile usa ECLIPSEDIR per trovare il proprio kernel e le librerie. %n è il controllo formato della newline; niente dipendenza da HPCC.

Actual verification of 2026-10-08T12:01:23.327370+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Hash of sorgenti/checker, real versions and commands, output codes, stdout/stderr and test limits are in the log.

## Primary sources and format reference

- [https://eclipseclp.org/](https://eclipseclp.org/)
- [https://www.eclipseclp.org/doc/bips/kernel/ioterm/printf-2.html](https://www.eclipseclp.org/doc/bips/kernel/ioterm/printf-2.html)
- [https://eclipseclp.org/Distribution/Builds/7.2_13/x86_64_linux/](https://eclipseclp.org/Distribution/Builds/7.2_13/x86_64_linux/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ecl` | [hello.ecl](hello.ecl) verified |
