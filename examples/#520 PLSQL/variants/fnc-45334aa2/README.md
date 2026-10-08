# 0520 — PLSQL: `.fnc`

Ruolo: Funzione stored PL/SQL del saluto.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Oracle Database e SQL*Plus. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
SQL*Plus di test: @hello.fnc; SELECT corpus_greeting FROM dual
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.fnc`: `cf780ca738d44e7db6b6bf32a3939ad3895579089e5675843c65245eeea9b7c6`

Fonti primarie:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-subprograms.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
