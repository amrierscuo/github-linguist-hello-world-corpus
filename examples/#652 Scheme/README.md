# #652 Scheme

Perform a Scheme program with display/newline.

## Toolchain

Welcome to Racket v8.18 [cs].; Scheme display/newline subset in racket/base

## Procedure

racket -I racket/base -f hello.scm

## Expected result

Hello, World!

## Status

syntax and behavior verified.



Real check 2026-10-08T13:23:04.371132+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://docs.racket-lang.org/r5rs/](https://docs.racket-lang.org/r5rs/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.scm` | [hello.scm](hello.scm) verified |
| `.sch` | [hello.sch](variants/sch-5766dac2/hello.sch) created; verification pending |
| `.sld` | [hello.sld](variants/sld-4358f718/hello.sld) created; verification pending |
| `.sls` | [hello.sls](variants/sls-1d513f43/hello.sls) created; verification pending |
| `.sps` | [hello.sps](variants/sps-36bdbd67/hello.sps) created; verification pending |
| `.ss` | [hello.ss](variants/ss-33325a3d/hello.ss) created; verification pending |
