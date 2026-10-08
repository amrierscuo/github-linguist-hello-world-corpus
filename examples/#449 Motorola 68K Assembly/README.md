# #449 Motorola 68K Assembly

Voce canonica `Motorola 68K Assembly`, tipo `programming`, language_id `477582706`.

Assemblare un programma Motorola 68000 che usa le syscall Linux write ed exit.

## Toolchain e riproduzione

Genuine GNU Binutils Motorola 68000 cross assembler/linker — GNU assembler (GNU Binutils for Ubuntu) 2.42. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

GNU Binutils m68k 2.42 estratto in work. Le istruzioni sono per 68000; l’esecuzione richiede Linux m68k o QEMU user mode.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
m68k-linux-gnu-as -m68000 -o build/hello.o hello.s; m68k-linux-gnu-ld -o build/hello build/hello.o; qemu-m68k build/hello
```

Risultato atteso: Hello, World!

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **in attesa**.

Assembler, linker e disassembler reali producono ELF e bytecode; il saluto non è stato eseguito. Hash ELF registrato, semantica pending.

Requisiti residui:

- Native 68000 bytecodes assembled/linked; execution on a Linux m68k runtime/emulator is not performed.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://sourceware.org/binutils/docs/as/M68K_002dDependent.html](https://sourceware.org/binutils/docs/as/M68K_002dDependent.html)
- [https://www.kernel.org/doc/html/latest/arch/m68k/index.html](https://www.kernel.org/doc/html/latest/arch/m68k/index.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.asm` | [hello.asm](variants/asm-a9c5b6ca/hello.asm) creato, verifiche pendenti |
| `.i` | [hello.i](variants/i-1708f4ae/hello.i) creato, verifiche pendenti |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) creato, verifiche pendenti |
| `.s` | [hello.s](hello.s), [driver.s](variants/i-1708f4ae/driver.s), [driver.s](variants/inc-dd126fb7/driver.s) creato, verifiche pendenti |
| `.x68` | [hello.x68](variants/x68-9c10e087/hello.x68) creato, verifiche pendenti |
