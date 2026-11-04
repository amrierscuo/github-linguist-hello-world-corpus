# #532 Perl

Voce canonica `Perl`, tipo `programming`, language_id `282`.

Run a Perl program with World parameter interpolation.

## Toolchain and reproduction

Authentic Perl interpreter, This is perl 5, version 38, subversion 2 ( v5.38.2 ) built for x86_64-linux-gnu-thread-multi. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Genuine perl available in Ubuntu WSL, version in the log.

Comando/procedura from the directory of the example, unless explicit indications:

```text
perl -c hello.pl; perl hello.pl
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Syntax check e runtime reali, stdout esatto.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://perldoc.perl.org/perlintro](https://perldoc.perl.org/perlintro)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pl` | [hello.pl](hello.pl), [driver.pl](variants/ph-d462b572/driver.pl), [driver.pl](variants/pm-c810ce30/driver.pl) created; verification pending |
| `.al` | [greeting.al](variants/al-ceb20bd5/greeting.al) syntax verified |
| `.cgi` | [hello.cgi](variants/cgi-89feb572/hello.cgi) verified |
| `.fcgi` | [hello.fcgi](variants/fcgi-209194e4/hello.fcgi) created; verification pending |
| `.perl` | [hello.perl](variants/perl-ffad7d6b/hello.perl) verified |
| `.ph` | [hello.ph](variants/ph-d462b572/hello.ph) verified |
| `.plx` | [hello.plx](variants/plx-e52b193c/hello.plx) verified |
| `.pm` | [Greeting.pm](variants/pm-c810ce30/Corpus/Greeting.pm) verified |
| `.psgi` | [hello.psgi](variants/psgi-c2b00512/hello.psgi) created; verification pending |
| `.t` | [hello.t](variants/t-3c247edb/hello.t) verified |
