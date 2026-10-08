# 0520 — PLSQL: `.plb`

Ruolo: Variante con ruolo/formato distinto dal sorgente principale.

Provenienza: Solo documentazione del blocco; nessun artefatto con estensione richiesta è stato fabbricato.

Toolchain richiesta: Oracle Database e SQL*Plus. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Disponibilità del tool originale necessaria; consultare gli impedimenti.
```

Risultato atteso: Da verificare con il formato nativo dopo la risoluzione del blocco.

Stato individuale: artefatto creato `false`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Output del PL/SQL wrap utility, non sorgente testuale ordinario. Il wrapper Oracle originale non è disponibile: non si fabbrica una sequenza wrapped.

Fonti primarie:

- https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/wrapping-pl-sql-source-text-pl-sql-wrapper-utility.html
- https://docs.oracle.com/en/database/oracle/oracle-database/23/arpls/DBMS_OUTPUT.html
