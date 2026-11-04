# #807 Zig

Fill Zig and write the greeting on the stream debug.

## Toolchain

Zig 0.15.2

## Procedure

zig build-exe hello.zig -femit-bin=build/hello.exe; build/hello.exe

## Expected result

Hello, World!

## Status

syntax and behavior verified.

std.debug.print writes on stderr: the checker compares that stream, does not invent stdout.

Real check 2026-10-08T13:38:42.134007+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://ziglang.org/documentation/0.15.2/](https://ziglang.org/documentation/0.15.2/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.zig` | [hello.zig](hello.zig), [hello.zig](variants/zig-zon-af1980a8/hello.zig), [build.zig](variants/zig-zon-af1980a8/build.zig) created; verification pending |
| `.zig.zon` | [build.zig.zon](variants/zig-zon-af1980a8/build.zig.zon) verified |
