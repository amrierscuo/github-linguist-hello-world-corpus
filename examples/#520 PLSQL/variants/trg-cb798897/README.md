# 0520 — PLSQL: `.trg`

Ruolo: Trigger PL/SQL di test su una tabella dedicata; nessun DB reale viene modificato in preparazione.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Oracle Database e SQL*Plus. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Oracle schema temporaneo: creare corpus_events(message VARCHAR2(30)); @hello.trg; INSERT con valore null; SELECT message
```

Risultato atteso: Riga contenente Hello, World! dopo trigger

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.trg`: `6cc616bc64aa4c04d9d3929b1a4145fe2ee63ec18908bb661cebb081e26f9ee8`

Fonti primarie:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-triggers.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
