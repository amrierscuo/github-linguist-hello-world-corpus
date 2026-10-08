# #449 Motorola 68K Assembly

Voce canonica: `Motorola 68K Assembly`, tipo `programming`, language_id `477582706`.

Assemblare un programma Motorola 68000 che usa le syscall Linux write ed exit.

## Toolchain e riproduzione

GNU Binutils m68k 2.42; QEMU user 8.2.2 (pacchetti Ubuntu estratti).

GNU Binutils m68k e qemu-m68k. I file .i/.inc sono include GNU as con un driver .s. I suffissi .asm/.x68 usano esplicitamente il dialetto GNU as, non il dialetto di altri assembler.

Comandi dalla directory dell’esempio; `<output>` indica una directory temporanea esterna al corpus.

```text
m68k-linux-gnu-as -m68000 -o <output>/hello.o hello.s; m68k-linux-gnu-ld -o <output>/hello <output>/hello.o
qemu-m68k <output>/hello
```

Risultato atteso: ELF m68k eseguito con exit 0; stdout esattamente Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il vero assembler/linker GNU produce un ELF Motorola 68000; QEMU user esegue le istruzioni e traduce le syscall Linux write/exit. Tutte le varianti .asm, .i, .inc e .x68 sono state assemblate, linkate ed eseguite separatamente; nessun esito viene ereditato solo per uguaglianza dei byte.

Prova reale: [finish.json](verification/finish.json), con UTC, comandi, versioni, exit code, stdout/stderr e SHA-256 dei sorgenti. Le sostituzioni dei percorsi sono documentate nel log. I prodotti di compilazione e le dipendenze rimangono nelle directory di lavoro.

## Fonti primarie

- https://sourceware.org/binutils/docs/as/M68K_002dDependent.html
- https://www.kernel.org/doc/html/latest/arch/m68k/index.html
- https://www.qemu.org/docs/master/user/main.html

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.asm` | [hello.asm](variants/asm-a9c5b6ca/hello.asm) sintassi e semantica verificate |
| `.i` | [hello.i](variants/i-1708f4ae/hello.i) sintassi e semantica verificate |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) sintassi e semantica verificate |
| `.s` | [hello.s](hello.s), [driver.s](variants/i-1708f4ae/driver.s), [driver.s](variants/inc-dd126fb7/driver.s) sintassi e semantica verificate |
| `.x68` | [hello.x68](variants/x68-9c10e087/hello.x68) sintassi e semantica verificate |
