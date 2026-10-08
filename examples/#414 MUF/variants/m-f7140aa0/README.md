# 0414 — MUF: `.m`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#414 MUF/hello.muf.

Toolchain richiesta: Fuzzball MUCK con compilatore/interprete MUF. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.m; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: programma compilato; l’utente che lo esegue riceve Hello, World!.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.m`: `fca9bc311b87a87fd9e8a0733cd22a9603816483aec68f307287a2cb0ec36f2b`

Fonti primarie:

- https://www.fuzzball.org/docs/mufman.html
