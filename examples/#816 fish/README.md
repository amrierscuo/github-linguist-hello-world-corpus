# #816 fish

Play fish and expand the wave variable.

## Toolchain

fish, version 3.7.0

## Procedure

fish --no-config --no-execute hello.fish; fish --no-config hello.fish

## Expected result

Hello, World!

## Status

syntax and behavior verified.



Real check 2026-10-08T13:38:35.831384+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://fishshell.com/docs/current/language.html](https://fishshell.com/docs/current/language.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.fish` | [hello.fish](hello.fish) verified |
