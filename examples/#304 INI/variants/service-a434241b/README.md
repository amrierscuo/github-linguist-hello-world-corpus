# 0304 — INI: `.service`

Ruolo: Servizio oneshot systemd illustrativo; non viene installato né avviato.

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

- `corpus-hello.service`: `a52e66871d797ebbc81c19637251e6f67219ae426c0bc25bf792be594bc145f8`

Fonti primarie:

- https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html
- https://docs.python.org/3/library/configparser.html
