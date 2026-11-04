# #658 ShellSession

Record an authentic transcript of greeting shell session.

## Toolchain

Ubuntu dash 0.5.12 POSIX sh

## Procedure

sh replay.sh; compare output with hello.sh-session transcript

## Expected result

Hello, World!

## Status

syntax and behavior verified.

The transcript contains the conventional prompts and the actual output of the equivalent script; the prompts are not interpreted as commands.

Real check 2026-10-08T13:23:04.712051+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sh.html](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sh.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sh-session` | [hello.sh-session](hello.sh-session) verified |
