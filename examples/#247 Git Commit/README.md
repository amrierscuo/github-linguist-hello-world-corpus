# #247 Git Commit

Use an original Git commit message with subject Hello, World! and verify it in the commit created.

## Toolchain

git version 2.51.0.windows.1

## Commands and procedure

python verify.py 247 /percorso/nuovo-repo-temporaneo git

## Expected result

Local comit created; git log returns the subject Hello, World!; cat-file preserves the body of .gitmessage.

## Status

syntax and behavior verified.

verify.py uses commit -F and --cleanup=verbatim in the temporary repository.Identity and dates are deterministic illustrative fixtures, without personal data. No commit comes created in the corpus.

Actual verification of 2026-10-08T12:15:30.149179+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://git-scm.com/docs/git-commit](https://git-scm.com/docs/git-commit)
- [https://git-scm.com/docs/git-log](https://git-scm.com/docs/git-log)
- [https://git-scm.com/docs/git-cat-file](https://git-scm.com/docs/git-cat-file)
