# 0520 — PLSQL: `.plsql`

Ruolo: Blocco anonimo PL/SQL senza direttive client SET; stesso linguaggio SQL procedurale.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Oracle Database e SQL*Plus. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
SQL*Plus di test: SET SERVEROUTPUT ON; @hello.plsql
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.plsql`: `964f21462fc46b2baa6d32ce9273cfee5c17434b080cdf0be23fd1fdfd402459`

Fonti primarie:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/overview.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
