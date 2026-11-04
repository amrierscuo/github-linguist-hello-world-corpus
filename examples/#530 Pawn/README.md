# #530 Pawn

Voce canonica `Pawn`, tipo `programming`, language_id `271`.

Print your greeting through the host console of the original Pawn distribution.

## Toolchain and reproduction

Required genuine compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires CompuPhase Pawn, console.inc and the host runner with the native consoles recorded.

Comando/procedura from the directory of the example, unless explicit indications:

```text
pawncc hello.pwn -obuild/hello.amx; pawnrun build/hello.amx
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Original program according to the language guide; compiler/host not configured.

Remaining requirements:

- Required pawncc compiler/interpreter and matching host libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://compuphase.com/pawn/pawn.htm](https://compuphase.com/pawn/pawn.htm)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.pwn` | [hello.pwn](hello.pwn), [driver.pwn](variants/inc-dd126fb7/driver.pwn) created; verification pending |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) created; verification pending |
| `.sma` | [hello.sma](variants/sma-3aced296/hello.sma) created; verification pending |
