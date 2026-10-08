# #807 Zig

Compilare Zig e scrivere il saluto sullo stream debug.

## Toolchain

Zig 0.15.2

## Procedura

zig build-exe hello.zig -femit-bin=build/hello.exe; build/hello.exe

## Risultato atteso

Hello, World!

## Stato

Sintassi e semantica verificate.

std.debug.print scrive su stderr: il checker confronta quello stream, non inventa stdout.

Verifica reale 2026-10-08T13:38:42.134007+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://ziglang.org/documentation/0.15.2/](https://ziglang.org/documentation/0.15.2/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.zig` | [hello.zig](hello.zig), [hello.zig](variants/zig-zon-af1980a8/hello.zig), [build.zig](variants/zig-zon-af1980a8/build.zig) creato, verifiche pendenti |
| `.zig.zon` | [build.zig.zon](variants/zig-zon-af1980a8/build.zig.zon) verificato |
