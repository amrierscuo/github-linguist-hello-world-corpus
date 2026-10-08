# 0443 — Monkey: `.monkey2`

Ruolo: Programma Monkey2 con import std e namespace, distinto dalla sintassi Monkey X.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Required genuine toolchain not available/configured — non disponibile / non verificata. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Monkey2 mx2cc: compilare hello.monkey2 e avviare programma locale
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.monkey2`: `a4d68b1bdf3594af5db37931800ab99c7afaf406775fcce0046cd861fc05b344`

Fonti primarie:

- https://github.com/blitz-research/monkey2
- https://github.com/blitz-research/monkey
