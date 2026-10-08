# 0472 — Nim: `.nims`

Ruolo: NimScript con istruzione top-level echo, separato da codice C generato Nim.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Nim1.6.14 Ubuntu, backend C/GCC. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
nim e hello.nims
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.nims`: `cf4de8709c40d3e7cc30fb5e859b52358f9f0f6c9241551d49f3c09c4ce5bdb6`

Fonti primarie:

- https://nim-lang.org/docs/nims.html
- https://nim-lang.org/docs/tut1.html
