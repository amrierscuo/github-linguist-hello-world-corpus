# #166 Diff

Apply a unified patch diff that turns Hello into Hello, World!.

## Toolchain

GNU GNU patch 2.7.6; diff (GNU diffutils) 3.10

## Commands and procedure

diff -u --label a/hello.txt before/hello.txt --label b/hello.txt after/hello.txt; copiare before/hello.txt in build/hello.txt; da build: patch --batch -p1 -i ../hello.diff

## Expected result

diff exit 1 perché esistono differenze; patch exit 0; file risultante uguale a after/hello.txt.

## Status

syntax and behavior verified.

The patch included is compared bytes per bytes with GNU diff. patch applies it in a temporary directory; greeting in the resulting file is verified. Exit 1 da diff is the correct code for different files.

Actual verification of 2026-10-08T11:56:12.780978+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Hash of sorgenti/checker, real versions and commands, output codes, stdout/stderr and test limits are in the log.

## Primary sources and format reference

- [https://www.gnu.org/software/diffutils/manual/html_node/Unified-Format.html](https://www.gnu.org/software/diffutils/manual/html_node/Unified-Format.html)
- [https://www.gnu.org/software/diffutils/manual/html_node/Invoking-patch.html](https://www.gnu.org/software/diffutils/manual/html_node/Invoking-patch.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.diff` | [hello.diff](hello.diff) verified |
| `.patch` | [hello.patch](variants/ext-patch-2e7061746368/hello.patch) created; verification pending |
