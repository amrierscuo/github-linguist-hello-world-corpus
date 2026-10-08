# 0304 — INI: `.container`

Ruolo: Descriptor Podman Quadlet; immagine illustrativa locale non presente.

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

- `hello.container`: `03275b3a551029e24addf823b458ab3a4d7bc3ca840ac6a7751d9be7b9c25d4b`

Fonti primarie:

- https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html
- https://docs.python.org/3/library/configparser.html
