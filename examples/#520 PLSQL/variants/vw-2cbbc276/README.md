# 0520 — PLSQL: `.vw`

Ruolo: View SQL Oracle: proiezione del saluto, non blocco anonimo.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Oracle Database e SQL*Plus. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Oracle schema temporaneo: @hello.vw; SELECT message FROM corpus_greeting
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.vw`: `a065b7b395c301f6d8081a3738feb91b8be2a94cd1fa311b440a34c1c87545bf`

Fonti primarie:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/CREATE-VIEW.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
