# #825 nanorc

Load a local nanorc and color the greeting in the test buffer.

## Toolchain

 GNU nano, version 7.2

## Procedure

nano --rcfile hello.nanorc greeting.hello; exit without rescue with Ctrl-X.

## Expected result

Nano accepts nanorc, shows row numbers and color Hello, World! in bright blue.

## Status

syntax and behavior verified.

--rcfile avoids utente/globali. configurations The buffer and highlight rule are original; PTY test must confirm parsing and text color sequence.

Real check 2026-10-08T13:50:49.777443+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://www.nano-editor.org/dist/latest/nanorc.5.html](https://www.nano-editor.org/dist/latest/nanorc.5.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nanorc` | [hello.nanorc](hello.nanorc) verified |
