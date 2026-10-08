# 0520 — PLSQL: `.pck`

Ruolo: Script package completo con specifica e corpo, distinto dai singoli file spec/body.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Oracle Database e SQL*Plus. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
SQL*Plus di test: @hello.pck; SELECT corpus_greeting.greeting FROM dual
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.pck`: `45a13a5f73eaa6f1bae49ee8151b5577934a9ab08d762e3d0efb4293438e76ff`

Fonti primarie:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-packages.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
