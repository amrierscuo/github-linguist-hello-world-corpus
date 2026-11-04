# #249 Git Revision List

Ignore with git blame a real cosmetic review that adds space in Hello, World!.

## Toolchain

git version 2.51.0.windows.1

## Commands and procedure

python verify.py 249 /percorso/nuovo-repo-temporaneo git

## Expected result

Without ignore: line attributed to the commit formatting; with the list: attributed to the previous commit; final text Hello, World!.

## Status

syntax and behavior verified.

The list contains the real ID object of the second repeatable fix commit; not a invented hash. verify.py recreates commits with identità/date deterministic and compares the recorded value. ID relates to this temporary repository and not the future history of the public corpus.

Actual verification of 2026-10-08T12:15:32.429631+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---ignore-revs-fileltfilegt](https://git-scm.com/docs/git-blame#Documentation/git-blame.txt---ignore-revs-fileltfilegt)
