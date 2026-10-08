# 0530 — Pawn: `.sma`

Ruolo: Plugin AMX Mod X Pawn: include amxmodx e callback plugin_init, non console main.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Required genuine compiler/runtime — non disponibile / non verificata. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
AMX Mod X compiler: amxxpc hello.sma; caricare solo in server di test locale
```

Risultato atteso: Hello, World! nel server log

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.sma`: `838dc2e7cd55213665d125ecbc0f9af8d2d0892d576a57651c53db6f8d405016`

Fonti primarie:

- https://www.amxmodx.org/doc/
- https://compuphase.com/pawn/pawn.htm
