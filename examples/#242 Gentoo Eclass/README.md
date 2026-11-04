# #242 Gentoo Eclass

Export src_install from an eclass EAPI 8 and install the hello-world script in its ebuild consumer.

## Toolchain

GNU bash, version 5.2.21(1)-release (x86_64-pc-linux-gnu)

## Commands and procedure

bash -n hello-world.eclass; bash -n hello-world-1.0.ebuild; insert the eclass in eclass/ of a temporary overlay; ebuild hello-world-1.0.ebuild install

## Expected result

Portage solves inherit hello-world and EXPORT_FUNCTIONS; image contains hello-world printing greeting.

## Status

syntax verified; behavioral verification pending.

The original eclass handles EAPI 8 and exports hello-world_src_install. Consumer is included to make future verification concrete. Bash -n verifies host language; inheritance, metadata and newbin require real portage and remain to be tried.

Actual verification of 2026-10-08T12:15:43.041537+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

Remaining requirements:
- Gentoo Portage package environment not available: native install/inherit phases pending.

## Primary sources

- [https://devmanual.gentoo.org/eclass-writing/index.html](https://devmanual.gentoo.org/eclass-writing/index.html)
- [https://projects.gentoo.org/pms/latest/pms.html](https://projects.gentoo.org/pms/latest/pms.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.eclass` | [hello-world.eclass](hello-world.eclass) syntax verified |
