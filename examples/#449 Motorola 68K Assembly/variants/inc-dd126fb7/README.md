# #449 Motorola 68K Assembly .inc

Include GNU as con driver .s. La variante originale del corpus conserva i byte identificati dai checksum.

## Toolchain e verifica

GNU Binutils m68k 2.42 e QEMU user 8.2.2. Eseguire dalla directory della variante; <output> indica una directory di lavoro esterna.

```text
m68k-linux-gnu-as -m68000 -o <output>/hello.o driver.s; m68k-linux-gnu-ld -o <output>/hello <output>/hello.o; qemu-m68k <output>/hello
```

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La toolchain originale ha controllato questa specifica variante. Il task BitBake o l’eseguibile m68k produce Hello, World! e termina con exit 0. Gli esiti non derivano solo dall’uguaglianza con il campione principale.

Prova: [finish_variants.json](../../verification/finish_variants.json), con comandi, UTC, versioni, exit code, output e hash. Il log registra ogni variante separatamente.

## Sorgenti verificati

- [hello.inc](hello.inc) SHA-256 `07db4e9cdf3ea13526449c3b91b3454d73faf65cf860ad15213894d176bc44ed`.
- [driver.s](driver.s) SHA-256 `1a19af04d9d583b4706f1eebb64ebf1e2124968c76c9c14997fbe710695c3b2b`.

## Fonti primarie

- https://sourceware.org/binutils/docs/as/M68K_002dDependent.html
- https://www.kernel.org/doc/html/latest/arch/m68k/index.html
