# 0530 — Pawn: `.inc`

Ruolo: Header Pawn con stock function per non imporre main nel file incluso.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Required genuine compiler/runtime — non disponibile / non verificata. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
pawncc driver.pwn; runtime AMX con binding console originale
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `driver.pwn`: `f20e4f1d693a36f6c37493b85b0c67c7a4e4f7add5ede167262d0518cc7efb4b`
- `hello.inc`: `c24e2ab2a428839585147ac9efb96dbfdf5dc76d6dfa755cc1d6c040653cd54f`

Fonti primarie:

- https://github.com/compuphase/pawn
- https://compuphase.com/pawn/pawn.htm
