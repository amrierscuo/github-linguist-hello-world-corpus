# #656 Shell

Run a POSIX Shell script.

## Toolchain

Ubuntu dash 0.5.12 POSIX sh

## Procedure

sh -n hello.sh; sh hello.sh

## Expected result

Hello, World!

## Status

syntax and behavior verified.



Real check 2026-10-08T13:23:04.448187+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sh.html](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sh.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sh` | [hello.sh](hello.sh) verified |
| `.bash` | [hello.bash](variants/bash-8a9862b8/hello.bash) created; verification pending |
| `.bats` | [hello.bats](variants/bats-7875b11c/hello.bats) created; verification pending |
| `.cgi` | [hello.cgi](variants/cgi-89feb572/hello.cgi) created; verification pending |
| `.command` | [hello.command](variants/command-05dd8b8d/hello.command) created; verification pending |
| `.fcgi` | [hello.fcgi](variants/fcgi-209194e4/hello.fcgi) created; verification pending |
| `.ksh` | [hello.ksh](variants/ksh-56d287e3/hello.ksh) created; verification pending |
| `.pacscript` | [hello.pacscript](variants/pacscript-d2beaef5/hello.pacscript) created; verification pending |
| `.sbatch` | [hello.sbatch](variants/sbatch-e5f39033/hello.sbatch) created; verification pending |
| `.sh.in` | [hello.sh.in](variants/sh-in-8a555af8/hello.sh.in) created; verification pending |
| `.slurm` | [hello.slurm](variants/slurm-94175ad5/hello.slurm) created; verification pending |
| `.tmux` | [hello.tmux](variants/tmux-026ac176/hello.tmux) created; verification pending |
| `.tool` | [hello.tool](variants/tool-f27eb9a7/hello.tool) created; verification pending |
| `.trigger` | [hello.trigger](variants/trigger-9c81aa55/hello.trigger) created; verification pending |
| `.zsh` | [hello.zsh](variants/zsh-55a30bf3/hello.zsh) created; verification pending |
| `.zsh-theme` | [hello.zsh-theme](variants/zsh-theme-a4cc3efd/hello.zsh-theme) created; verification pending |
