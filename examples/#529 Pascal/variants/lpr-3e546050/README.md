# 0529 — Pascal: `.lpr`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#529 Pascal/hello.pas.

Toolchain richiesta: Genuine Free Pascal compiler — 3.2.2. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.lpr; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.lpr`: `61390bec262f49020edd581463d7747ae45794775aeab6fad686b6241c28f082`

Fonti primarie:

- https://www.freepascal.org/docs.html
