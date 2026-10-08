# 0418 — Markdown: `.scd`

Ruolo: Manuale scdoc: header obbligatorio name(section), non Markdown generico.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Python 3.13.9 + markdown-it-py 4.2.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
scdoc < hello.scd > hello.1
```

Risultato atteso: Manpage con Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.scd`: `a9a70bfda1895c46f18bfb44e63289c3e5b8df63109bff49482c0ad21a22f28b`

Fonti primarie:

- https://git.sr.ht/~sircmpwn/scdoc/tree/master/item/scdoc.5.scd
- https://spec.commonmark.org/0.31.2/
- https://github.com/executablebooks/markdown-it-py
