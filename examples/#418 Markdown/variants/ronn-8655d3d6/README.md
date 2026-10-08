# 0418 — Markdown: `.ronn`

Ruolo: Documento Ronn con intestazione name(section) e sezioni man.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Python 3.13.9 + markdown-it-py 4.2.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
ronn --roff hello.ronn
```

Risultato atteso: Manpage con Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.ronn`: `6106b50a78d01bc5c119d6d5531f5e981057352825fc561600b1ab42698332b1`

Fonti primarie:

- https://github.com/rtomayko/ronn
- https://spec.commonmark.org/0.31.2/
- https://github.com/executablebooks/markdown-it-py
