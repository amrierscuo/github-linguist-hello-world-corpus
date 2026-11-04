# #790 XS

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Fill out an extension Perl XS and read Hello, World! from function C.

xsubpp really interprets Greeting.xs; GCC generates a shared library then imported with XSLoader. The XS function is called by Perl and its compared value.

## Toolchain and reproduction

Perl5.38.2/xsubpp/ExtUtils::MakeMaker originali, GCC e header libperl-dev isolati

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
perl Makefile.PL; make; perl verify.pl
```

## Expected result and status

Corpus::Greeting::greeting() restituisce Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://perldoc.perl.org/perlxs

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.xs` | [Greeting.xs](Greeting.xs) verified |
