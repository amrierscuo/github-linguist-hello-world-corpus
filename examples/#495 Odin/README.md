# #495 Odin

Fill in and execute Odin with fmt.println.

## Toolchain

<workspace>/work/tools_481_500/odin/odin-linux-amd64-nightly+2026-10-06/odin version dev-2026-10-nightly:84bc3fc; GCC linker

## Procedure

odin check hello.odin -file; odin build hello.odin -file -build-mode:obj -out:build/hello.o; gcc build/hello-*.o -lm -lpthread -o build/hello; build/hello

## Expected result

Hello, World!

## Status

syntax and behavior verified.



Real check 2026-10-08T13:12:09.149453+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://odin-lang.org/docs/overview/](https://odin-lang.org/docs/overview/)
- [https://github.com/odin-lang/Odin/releases/tag/dev-2026-10](https://github.com/odin-lang/Odin/releases/tag/dev-2026-10)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.odin` | [hello.odin](hello.odin) verified |
