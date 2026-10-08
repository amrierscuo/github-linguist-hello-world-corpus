# 0387 — Linker Script: `.lds`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#387 Linker Script/hello.ld.

Toolchain richiesta: GNU ld (GNU Binutils for Ubuntu) 2.42; GCC 13.3.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.lds; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Sezione .greeting contiene il testo; boundary symbols racchiudono 14 byte; runtime stampa il saluto.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.lds`: `875d299c757ca4e4a919954f4dc92b066675884ee38f9b7d74ddcc7dd47d8328`
- `main.c`: `31d41a950b832df6e7397dc331bb032117b0eaa03571bc833af6cf63267c8e8b`

Fonti primarie:

- https://sourceware.org/binutils/docs/ld/SECTIONS.html
- https://sourceware.org/binutils/docs/ld/Miscellaneous-Commands.html
