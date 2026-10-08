# 0403 — M: `.m`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#403 M/hello.mumps.

Toolchain richiesta: YottaDB o GT.M con routine M abilitata. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.m; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: stdout Hello, World! e LF.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.m`: `a81e922a3255f5fc417d51cccd5a5748f19bc14fdbb4df8440dcee68c9a9ea39`

Fonti primarie:

- https://docs.yottadb.com/ProgrammersGuide/langfeat.html
