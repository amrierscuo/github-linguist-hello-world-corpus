# 0304 — INI: `.properties`

Ruolo: Java properties: coppia chiave/valore senza intestazione di sezione.

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

- `hello.properties`: `b39cef82a809353ae1a2ab63aedeb0048b348dd4257df8c9733a7d29042ce150`

Fonti primarie:

- https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Properties.html
- https://docs.python.org/3/library/configparser.html
