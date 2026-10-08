# #386 Linear Programming

Risolvere un LP originale il cui ottimo codifica Hello, World! in ASCII.

## Toolchain

GLPSOL--GLPK LP/MIP Solver 5.0; Python stdlib result reader

## Comandi e procedura

glpsol --lp hello.lp --write build/solution.txt --output build/report.txt; python verify.py build/solution.txt

## Risultato atteso

Status OPTIMAL; 13 variabili assumono i codici ASCII inferiori e decodificano Hello, World!.

## Stato

Sintassi e semantica verificate.

L’obiettivo minimizza la somma di 13 variabili, ognuna in un intervallo [ASCII, ASCII+1]. Il vincolo complete mantiene la somma almeno al valore dei caratteri. GLPK analizza il formato LP e risolve realmente il problema; verify.py legge la soluzione nativa, controlla ottimalità/interezza e decodifica i valori.

Verifica effettiva del 2026-10-08T12:48:20.311924+00:00 su WSL GLPK + Windows Python: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://www.gnu.org/software/glpk/](https://www.gnu.org/software/glpk/)
- [https://www.gnu.org/software/glpk/glpk.html](https://www.gnu.org/software/glpk/glpk.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lp` | [hello.lp](hello.lp) verificato |
