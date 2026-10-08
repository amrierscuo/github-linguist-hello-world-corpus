# 0290 — Handlebars: `.handlebars`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#290 Handlebars/hello.hbs.

Toolchain richiesta: Handlebars4.7.8, Node.js22.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.handlebars; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: stdout <p>Hello, World!</p> seguito da newline; exit 0.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.handlebars`: `c8a5cdec3b03ec742a9a6f1062f1ca729d8d0883a2fcf37c5758b5fb743d4c2c`
- `render.js`: `a9b1ebd90c02522e9c4f49bab5cb016aaa1f8c2c4779586e6932e5bdb7852fdf`

Fonti primarie:

- https://handlebarsjs.com/guide/
