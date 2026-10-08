# 0547 — PostCSS: `.postcss`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#547 PostCSS/hello.pcss.

Toolchain richiesta: PostCSS8 e postcss-custom-properties originali; versioni effettive nel log. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.postcss; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: CSS trasformato contiene content: "Hello, World!".

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.postcss`: `7da058442245be1726962a0b9b571bf6e9e0f97b017d63380e9787759d71779c`
- `verify.js`: `ed71830e46f5dddcdd00a451ccff75fb5d0de3ca21641cf162a74c339d01a2db`

Fonti primarie:

- https://postcss.org/
- https://github.com/csstools/postcss-plugins/tree/main/plugins/postcss-custom-properties
