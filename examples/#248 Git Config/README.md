# #248 Git Config

Read with Git a corpus.greeting configuration that contains Hello, World!.

## Toolchain

git version 2.51.0.windows.1

## Commands and procedure

python verify.py 248 /percorso/nuovo-repo-temporaneo git

## Expected result

git config --file .gitconfig --get corpus.greeting returns the most newline greeting.

## Status

syntax and behavior verified.

The corpus section is an illustrative metadata read by the original Git parser. The --file flag selects the file included; no overall configuration is changed.

Actual verification of 2026-10-08T12:15:30.771284+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://git-scm.com/docs/git-config](https://git-scm.com/docs/git-config)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gitconfig` | [.gitconfig](.gitconfig) verified |
