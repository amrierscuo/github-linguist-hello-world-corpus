# #227 GDB

Voice and canonical order of the `reference/languages.yml` of the corpus.Sources and fixtures are original.

## Goal

Run a script of GDB commands that print Hello, World!.

The printf command belongs to the GDB command language. -nx avoids user initialization file and -batch only runs the script; no external process is connected or analyzed.

## Toolchain and reproduction

GNU GDB 15.1, Ubuntu 15.1-1ubuntu1~24.04.1

Commands in the example folder with the tools available in PATH. Use a temporary copy for build and output; test dependencies are isolated in work.

```text
gdb -q -nx -batch -x hello.gdb
```

## Expected result and status

stdout esattamente Hello, World! seguito da newline; exit 0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records provenance and versions, SHA-256 of sources, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.gnu.org/software/gdb/documentation/
- https://sourceware.org/gdb/current/onlinedocs/gdb.html/Output.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gdb` | [hello.gdb](hello.gdb) verified |
| `.gdbinit` | [hello.gdbinit](variants/ext-gdbinit-2e676462696e6974/hello.gdbinit) created; verification pending |
