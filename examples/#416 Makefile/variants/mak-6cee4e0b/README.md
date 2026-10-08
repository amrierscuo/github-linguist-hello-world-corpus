# 0416 — Makefile: `.mak`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#416 Makefile/Makefile.

Toolchain richiesta: GNU Make on Ubuntu 24.04. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.mak; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: stdout Hello, World! e LF, exit 0.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.mak`: `522f2f7a71537199972884632c2535e8f3e0d2fb4222a5e952528af1c0037c57`

Fonti primarie:

- https://www.gnu.org/software/make/manual/html_node/Recipes.html
