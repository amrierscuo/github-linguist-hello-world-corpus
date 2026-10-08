# #656 Shell

Eseguire uno script POSIX Shell.

## Toolchain

Ubuntu dash 0.5.12 POSIX sh

## Procedura

sh -n hello.sh; sh hello.sh

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.



Verifica reale 2026-10-08T13:23:04.448187+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sh.html](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sh.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sh` | [hello.sh](hello.sh) verificato |
| `.bash` | [hello.bash](variants/bash-8a9862b8/hello.bash) creato, verifiche pendenti |
| `.bats` | [hello.bats](variants/bats-7875b11c/hello.bats) creato, verifiche pendenti |
| `.cgi` | [hello.cgi](variants/cgi-89feb572/hello.cgi) creato, verifiche pendenti |
| `.command` | [hello.command](variants/command-05dd8b8d/hello.command) creato, verifiche pendenti |
| `.fcgi` | [hello.fcgi](variants/fcgi-209194e4/hello.fcgi) creato, verifiche pendenti |
| `.ksh` | [hello.ksh](variants/ksh-56d287e3/hello.ksh) creato, verifiche pendenti |
| `.pacscript` | [hello.pacscript](variants/pacscript-d2beaef5/hello.pacscript) creato, verifiche pendenti |
| `.sbatch` | [hello.sbatch](variants/sbatch-e5f39033/hello.sbatch) creato, verifiche pendenti |
| `.sh.in` | [hello.sh.in](variants/sh-in-8a555af8/hello.sh.in) creato, verifiche pendenti |
| `.slurm` | [hello.slurm](variants/slurm-94175ad5/hello.slurm) creato, verifiche pendenti |
| `.tmux` | [hello.tmux](variants/tmux-026ac176/hello.tmux) creato, verifiche pendenti |
| `.tool` | [hello.tool](variants/tool-f27eb9a7/hello.tool) creato, verifiche pendenti |
| `.trigger` | [hello.trigger](variants/trigger-9c81aa55/hello.trigger) creato, verifiche pendenti |
| `.zsh` | [hello.zsh](variants/zsh-55a30bf3/hello.zsh) creato, verifiche pendenti |
| `.zsh-theme` | [hello.zsh-theme](variants/zsh-theme-a4cc3efd/hello.zsh-theme) creato, verifiche pendenti |
