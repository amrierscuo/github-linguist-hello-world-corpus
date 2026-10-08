# 0520 — PLSQL: `.bdy`

Ruolo: Corpo package PL/SQL con implementazione; specifica separata.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Oracle Database e SQL*Plus. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
SQL*Plus di test: @spec.sql; @hello.bdy; SELECT corpus_greeting.greeting FROM dual
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.bdy`: `f6a36a006932ec10430d11941fbe58c44dfe97ad99ceca59d5157e010e2f1e3d`
- `spec.sql`: `9e49e46c4d7bf9942c9bdbe3e271b7d1ca0c148a21a228b2dfce95fd81d05ff1`

Fonti primarie:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-packages.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
