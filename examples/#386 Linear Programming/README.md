# #386 Linear Programming

Solve an original LP whose excellent Hello, World! encoding in ASCII.

## Toolchain

GLPSOL--GLPK LP/MIP Solver 5.0; Python stdlib result reader

## Commands and procedure

glpsol --lp hello.lp --write build/solution.txt --output build/report.txt; python verify.py build/solution.txt

## Expected result

Status OPTIMAL; 13 variabili assumono i codici ASCII inferiori e decodificano Hello, World!.

## Status

syntax and behavior verified.

L’obiettivo minimizza la somma di 13 variabili, ognuna in un intervallo [ASCII, ASCII+1]. Il vincolo complete mantiene la somma almeno al valore dei caratteri. GLPK analizza il formato LP e risolve realmente il problema; verify.py legge la soluzione nativa, controlla ottimalità/interezza e decodifica i valori.

Actual verification of 2026-10-08T12:48:20.311924+00:00 on WSL GLPK + Windows Python: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://www.gnu.org/software/glpk/](https://www.gnu.org/software/glpk/)
- [https://www.gnu.org/software/glpk/glpk.html](https://www.gnu.org/software/glpk/glpk.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.lp` | [hello.lp](hello.lp) verified |
