# 0304 — INI: `.socket`

Ruolo: Socket unit systemd; solo descriptor offline, nessuna porta aperta.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Python 3.13.9 stdlib configparser. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Esaminare il file con il lettore originale del prodotto. Per unità systemd: systemd-analyze verify FILE (solo offline; non installare/avviare).
```

Risultato atteso: Configurazione riconosciuta; il saluto è nel valore/descrizione indicato, non una prova di runtime.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `corpus-hello.socket`: `272b551c62a1b165d53b5cc27aaa756dfe1f17934d9e84b53c395d630e03afbe`

Fonti primarie:

- https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html
- https://docs.python.org/3/library/configparser.html
