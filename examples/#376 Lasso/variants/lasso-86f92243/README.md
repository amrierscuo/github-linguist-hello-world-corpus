# 0376 — Lasso: `.lasso`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#376 Lasso/hello.lasso9.

Toolchain richiesta: Lasso9 originale; versione da registrare. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.lasso; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: stdout Hello, World! seguito da newline.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.lasso`: `d14bbe0b20f4b5e8c8691bf03a8dadc548be880e3067d1bf83ae4f90f2c12764`

Fonti primarie:

- https://lassoguide.com/operations/command-line-tools.html
- https://lassoguide.com/language/variables.html
