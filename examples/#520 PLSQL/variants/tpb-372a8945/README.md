# 0520 — PLSQL: `.tpb`

Ruolo: Corpo object type PL/SQL con metodo greeting.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Oracle Database e SQL*Plus. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Oracle schema isolato: @spec.sql; @hello.tpb; SELECT corpus_greeting('World').greeting() FROM dual
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.tpb`: `5db31c9025f7b67703917765657beb9a3bdcb0026b7914b1f5bc0abc2714881d`
- `spec.sql`: `46d2c6fc2d3679f20679adba899888e35f962b6b096af4014e456c64f3d2430f`

Fonti primarie:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/overview-of-pl-sql-object-types.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
