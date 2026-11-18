# #241 Gentoo Ebuild

## Verified on November 18, 2026

Portage executed the original ebuild in its disposable package image. The installed executable printed the exact greeting.

Run `ebuild hello-world-1.0.ebuild install (isolated overlay); run its image/usr/bin/hello-world`.

[Commands, toolchain, output and SHA-256](verification/native_20261118_main.json).

[Earlier evidence](verification/result.json).

<details>
<summary>Earlier instructions and evidence</summary>

Install an original hello-world script through the src_install phase of an ebuild EAPI 8.

## Toolchain

GNU bash, version 5.2.21(1)-release (x86_64-pc-linux-gnu)

## Commands and procedure

bash -n hello-world-1.0.ebuild; ebuild hello-world-1.0.ebuild install; eseguire hello-world dall’immagine di installazione temporanea

## Expected result

syntax Bash accepted; Portage installs binary shell that print Hello, World! more newline.

## Status

syntax verified; behavioral verification pending.

La verifica presente è limitata al parser Bash reale e alla fixture shell originale, che stampa il saluto. Le funzioni newbin e le fasi EAPI non sono simulate: l’installazione Portage resta pending. L’URL example.invalid è illustrativo e il pacchetto non scarica sorgenti.

Actual verification of 2026-10-08T12:15:42.652678+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

Remaining requirements:
- Gentoo Portage package environment not available: native install/inherit phases pending.

## Primary sources

- [https://devmanual.gentoo.org/ebuild-writing/file-format/index.html](https://devmanual.gentoo.org/ebuild-writing/file-format/index.html)
- [https://devmanual.gentoo.org/ebuild-writing/functions/src_install/index.html](https://devmanual.gentoo.org/ebuild-writing/functions/src_install/index.html)
- [https://projects.gentoo.org/pms/latest/pms.html](https://projects.gentoo.org/pms/latest/pms.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ebuild` | [hello-world-1.0.ebuild](hello-world-1.0.ebuild) Syntax and behavior verified |

</details>
