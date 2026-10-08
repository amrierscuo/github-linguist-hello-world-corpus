# 0304 — INI: `.prefs`

Ruolo: Preferenze Eclipse: coppie Java properties senza sezioni INI.

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

- `hello.prefs`: `c45263b5847802c95ebf4ad6f943ab96e49af9dd0f71099580a8338871244ba3`

Fonti primarie:

- https://help.eclipse.org/latest/topic/org.eclipse.platform.doc.isv/reference/api/org/eclipse/core/runtime/preferences/package-summary.html
- https://docs.python.org/3/library/configparser.html
