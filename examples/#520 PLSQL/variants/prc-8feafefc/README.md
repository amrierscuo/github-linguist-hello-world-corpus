# 0520 — PLSQL: `.prc`

Ruolo: Procedura stored PL/SQL con DBMS_OUTPUT.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Oracle Database e SQL*Plus. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
SQL*Plus di test: SET SERVEROUTPUT ON; @hello.prc; EXEC corpus_hello
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.prc`: `387a6fe5d402fcf975bcd53afd3f1c41aeb9aaf50bc576690703ba67afa9f8e9`

Fonti primarie:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-subprograms.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
