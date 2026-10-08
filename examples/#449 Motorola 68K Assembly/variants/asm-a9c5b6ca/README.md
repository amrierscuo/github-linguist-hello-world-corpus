# #449 Motorola 68K Assembly .asm

Sorgente Motorola 68000 nel dialetto GNU as Linux. La variante originale del corpus conserva i byte identificati dai checksum.

## Toolchain e verifica

GNU Binutils m68k 2.42 e QEMU user 8.2.2. Eseguire dalla directory della variante; <output> indica una directory di lavoro esterna.

```text
m68k-linux-gnu-as -m68000 -o <output>/hello.o hello.asm; m68k-linux-gnu-ld -o <output>/hello <output>/hello.o; qemu-m68k <output>/hello
```

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La toolchain originale ha controllato questa specifica variante. Il task BitBake o l’eseguibile m68k produce Hello, World! e termina con exit 0. Gli esiti non derivano solo dall’uguaglianza con il campione principale.

Prova: [finish_variants.json](../../verification/finish_variants.json), con comandi, UTC, versioni, exit code, output e hash. Il log registra ogni variante separatamente.

## Sorgenti verificati

- [hello.asm](hello.asm) SHA-256 `a2b40cbf257839c9302d478550cf7d3de7141e85350979c4ed03846991aae150`.

## Fonti primarie

- https://sourceware.org/binutils/docs/as/M68K_002dDependent.html
- https://www.kernel.org/doc/html/latest/arch/m68k/index.html
