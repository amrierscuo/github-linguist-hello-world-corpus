# #308 Ignore List

Apply an Ignore List Git, excluding builds and generated files but retaining the greeting file.

## Toolchain

git version 2.51.0.windows.1

## Commands and procedure

python verify.py /percorso/nuovo-repo-temporaneo git

## Expected result

build/disposable.txt and other.generated.txt ignored; hello.generated.txt preserved and contains Hello, World!.

## Status

syntax and behavior verified.

The fixture creates a real separate repository, .gitignore law and also test the exception with!. No global configuration or corpus repository is modified.

Actual verification of 2026-10-08T12:29:57.452856+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://git-scm.com/docs/gitignore](https://git-scm.com/docs/gitignore)
- [https://git-scm.com/docs/git-check-ignore](https://git-scm.com/docs/git-check-ignore)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gitignore` | [.gitignore](.gitignore) verified |
