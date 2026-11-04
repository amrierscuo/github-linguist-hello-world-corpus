# #397 Logos

Expand %ctor Logos and define an Objective-C constructor that uses NSLog.

## Toolchain

Theos Logos master snapshot; This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi

## Commands and procedure

perl logos.pl -c generator=internal -c warnings=error hello.xm; fill out the Objective-C result in the Apple test target and start the manufacturer

## Expected result

Preprocessore senza errori genera constructor; NSLog del target contiene Hello, World!.

## Status

syntax verified; behavioral verification pending.

The original Perl pre-processor expands the directive and keeps NSLog; hashs of all files of the snapshot tool are recorded. This test only applies to the syntax Logos/preprocessing. Foundation and Apple runtimes have not been simulated or executed.

Actual verification of 2026-10-08T12:48:20.545080+00:00 on WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

Remaining requirements:
- Apple Foundation Objective-C compile/runtime unavailable; NSLog execution pending.

## Primary sources

- [https://theos.dev/docs/logos](https://theos.dev/docs/logos)
- [https://theos.dev/docs/logos-syntax](https://theos.dev/docs/logos-syntax)
- [https://github.com/theos/logos](https://github.com/theos/logos)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.xm` | [hello.xm](hello.xm) syntax verified |
| `.x` | [hello.x](variants/x-bb42e4c6/hello.x) created; verification pending |
| `.xi` | [hello.xi](variants/xi-347cda4a/hello.xi) created; verification pending |
