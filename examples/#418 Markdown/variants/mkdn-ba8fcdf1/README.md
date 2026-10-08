# 0418 — Markdown: `.mkdn`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#418 Markdown/hello.md.

Toolchain richiesta: Python 3.13.9 + markdown-it-py 4.2.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.mkdn; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: HTML <h1>Hello, World!</h1> e LF; stdout saluto e LF.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.mkdn`: `0b4fdcfa10c709d9ab7d679fed4eb63742b2f51d8b073ec9016e5c5165d148ae`
- `verify.py`: `74f9fb2fa2e3e3eca61a3c83e458b9c7a459217f7caf3d41d121cf9ae13598d2`

Fonti primarie:

- https://spec.commonmark.org/0.31.2/
- https://github.com/executablebooks/markdown-it-py
