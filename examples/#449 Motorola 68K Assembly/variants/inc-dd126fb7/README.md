# 0449 — Motorola 68K Assembly: `.inc`

Ruolo: Include GNU as per m68k: routine e stringa, distinto dall’entry point _start.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Genuine GNU Binutils Motorola 68000 cross assembler/linker — GNU assembler (GNU Binutils for Ubuntu) 2.42. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
m68k-linux-gnu-as -o hello.o driver.s; m68k-linux-gnu-ld -o hello hello.o; qemu-m68k ./hello
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `driver.s`: `1a19af04d9d583b4706f1eebb64ebf1e2124968c76c9c14997fbe710695c3b2b`
- `hello.inc`: `07db4e9cdf3ea13526449c3b91b3454d73faf65cf860ad15213894d176bc44ed`

Fonti primarie:

- https://sourceware.org/binutils/docs/as/M68K_002dDependent.html
- https://www.kernel.org/doc/html/latest/arch/m68k/index.html
