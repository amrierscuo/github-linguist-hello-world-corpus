# 0304 — INI: `.frm`

Ruolo: Variante con ruolo/formato distinto dal sorgente principale.

Provenienza: Solo documentazione del blocco; nessun artefatto con estensione richiesta è stato fabbricato.

Toolchain richiesta: Python 3.13.9 stdlib configparser. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Disponibilità del tool originale necessaria; consultare gli impedimenti.
```

Risultato atteso: Da verificare con il formato nativo dopo la risoluzione del blocco.

Stato individuale: artefatto creato `false`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- L’estensione include descriptor MySQL di vista legacy e file tabella binari. Senza esportazione genuina da una versione compatibile del server non si inventano metadati interni come timestamp, checksum o SQL-mode.

Fonti primarie:

- https://dev.mysql.com/doc/refman/5.7/en/innodb-multi-versioning.html
- https://github.com/github-linguist/linguist/blob/main/samples/INI/metrics.frm
- https://docs.python.org/3/library/configparser.html
