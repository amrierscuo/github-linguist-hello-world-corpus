# #011 AMPL

`hello.ampl` uses AMPL `printf` command to output `Hello, World!` following
does not require a model, a solver or an optimization problem.

## Toolchain and command

The official AMPL interpreter is used. From the example folder, with `ampl` in PATH:

```powershell
ampl hello.ampl
```

Expected result on stdout: one row `Hello, World!`, 0. output code

## Verification performed

syntax and behavior verified su Windows con AMPL Version 20260809, proveniente
from the official package `ampl_module_base-20260809-py3-none-win_amd64.whl`.
The distribution contains a demo license sufficient to execute this command;
a personal license has not been activated. The code has been verified
output, absence of stderr and bytes of stdout: `b'Hello, World!\r\n'` on
Windows. The checker admits only one LF or CRLF; it does not admit
Additional text. See `verification.log`.

To reproduce control with the interpreter installed or extracted locally:

```powershell
python verify.py --ampl /percorso/di/ampl.exe
```

`verify.py` starts the real interpreter and compares the result; does not interpret AMPL.
The track and the license are not part of the corpus. The log records origin and SHA-256
of the distribution used; future availability of licenses follow AMPL.

## Primary sources

- [AMPL: capitolo ufficiale sui comandi di output, sezione printf](https://ampl.com/wp-content/uploads/Chapter-12-Display-Commands-AMPL-Book.pdf)
- [AMPL: integrazione Python e distribuzione moduli](https://dev.ampl.com/ampl/python/index.html)
- [Indice ufficiale del modulo AMPL base](https://pypi.ampl.com/ampl-module-base/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ampl` | [hello.ampl](hello.ampl) verified |
| `.mod` | [hello.mod](variants/ext-mod-2e6d6f64/hello.mod) created; verification pending |
