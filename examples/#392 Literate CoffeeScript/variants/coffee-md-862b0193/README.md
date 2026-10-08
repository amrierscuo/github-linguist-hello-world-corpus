# 0392 — Literate CoffeeScript: `.coffee.md`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#392 Literate CoffeeScript/hello.litcoffee.

Toolchain richiesta: coffeescript 2.7.0; Node 22.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.coffee.md; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Prosa ignorata, codice indentato compilato; stdout Hello, World! più newline.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.coffee.md`: `47a98ff081bd84d8e6256f4931fd20d4e684fa704b1042f6e75b25b01a62a084`
- `package.json`: `f4996b9974b12a80f0c6b5a867c49809c02a052f28a0b98bb1b68dc023e5bfeb`

Fonti primarie:

- https://coffeescript.org/#literate
- https://github.com/jashkenas/coffeescript
