# 0449 — Motorola 68K Assembly: `.x68`

Ruolo: Sorgente Motorola 68000 in dialetto GNU as Linux; il suffisso non implica sintassi di altri assembler.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#449 Motorola 68K Assembly/hello.s.

Toolchain richiesta: Genuine GNU Binutils Motorola 68000 cross assembler/linker — GNU assembler (GNU Binutils for Ubuntu) 2.42. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
m68k-linux-gnu-as -o hello.o hello.x68; m68k-linux-gnu-ld -o hello hello.o; qemu-m68k ./hello
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.x68`: `a2b40cbf257839c9302d478550cf7d3de7141e85350979c4ed03846991aae150`

Fonti primarie:

- https://sourceware.org/binutils/docs/as/M68K_002dDependent.html
- https://www.kernel.org/doc/html/latest/arch/m68k/index.html
