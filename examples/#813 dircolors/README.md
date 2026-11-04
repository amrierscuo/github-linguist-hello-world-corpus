# #813 dircolors

Apply dircolors and color the name of the fixture of the greeting.

## Toolchain

dircolors (GNU coreutils) 9.4

## Procedure

TERM=xterm; eval "$(dircolors -b hello.dircolors)"; ls --color=always -- "Hello, World!.hello"

## Expected result

The name Hello, World! .hello is preceded by the code ANSI bold-blue 01; 34.

## Status

syntax and behavior verified.

dircolors really generates LS_COLORS and ls consumes code for .hello. EXEC 00 disables the color of executables to make reproducible the test also on Windows filesystems mounted in WSL.

Real check 2026-10-08T13:39:24.271672+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html](https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.dircolors` | [hello.dircolors](hello.dircolors) verified |
