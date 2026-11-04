# #449 Motorola 68K Assembly

Voce canonica: `Motorola 68K Assembly`, tipo `programming`, language_id `477582706`.

Assemble a Motorola 68000 program that uses Linux write and exit syscalls.

## Toolchain and reproduction

GNU Binutils m68k 2.42; QEMU user 8.2.2 (pacchetti Ubuntu estratti).

GNU Binutils m68k and qemu-m68k. .i / .inc files are included GNU as with a .s. driver .asm suffix / .x68 explicitly use the GNU dialect as, not other assemblies

Commands from the directory of the example; `<output>` indicates a temporary directory external to the corpus.

```text
m68k-linux-gnu-as -m68000 -o <output>/hello.o hello.s; m68k-linux-gnu-ld -o <output>/hello <output>/hello.o
qemu-m68k <output>/hello
```

Expected result: ELF m68k executed with exit 0; stdout exactly Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Il vero assembler/linker GNU produce un ELF Motorola 68000; QEMU user esegue le istruzioni e traduce le syscall Linux write/exit. Tutte le varianti .asm, .i, .inc e .x68 sono state assemblate, linkate ed eseguite separatamente; nessun esito viene ereditato solo per uguaglianza dei byte.

Real test: [finish.json](verification/finish.json), with UTC, commands, versions, exit code, stdout/stderr and SHA-256 of sources.

## Primary sources

- https://sourceware.org/binutils/docs/as/M68K_002dDependent.html
- https://www.kernel.org/doc/html/latest/arch/m68k/index.html
- https://www.qemu.org/docs/master/user/main.html

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.asm` | [hello.asm](variants/asm-a9c5b6ca/hello.asm) syntax and behavior verified |
| `.i` | [hello.i](variants/i-1708f4ae/hello.i) syntax and behavior verified |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) syntax and behavior verified |
| `.s` | [hello.s](hello.s), [driver.s](variants/i-1708f4ae/driver.s), [driver.s](variants/inc-dd126fb7/driver.s) syntax and behavior verified |
| `.x68` | [hello.x68](variants/x68-9c10e087/hello.x68) syntax and behavior verified |
