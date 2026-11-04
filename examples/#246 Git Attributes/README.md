# #246 Git Attributes

Apply Git attributes to Hello, World! file: text with newline LF and metadata corpus-greeting=hello-world.

## Toolchain

git version 2.51.0.windows.1

## Commands and procedure

python verify.py 246 /percorso/nuovo-repo-temporaneo git

## Expected result

check-attr returns text=set, eol=lf, corpus-greeting=hello-world; Git index contains Hello, World! with LF.

## Status

syntax and behavior verified.

Il saluto è nel file hello.txt. L’attributo custom ha un valore senza spazi valido per il formato .gitattributes. La fixture crea un repository separato e disabilita lettura/modifica della configurazione globale.

Actual verification of 2026-10-08T12:15:29.811553+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://git-scm.com/docs/gitattributes](https://git-scm.com/docs/gitattributes)
- [https://git-scm.com/docs/git-check-attr](https://git-scm.com/docs/git-check-attr)
