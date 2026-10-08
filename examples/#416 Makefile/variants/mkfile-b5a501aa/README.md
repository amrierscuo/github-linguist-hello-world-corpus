# 0416 — Makefile: `.mkfile`

Ruolo: Plan 9 mk: attributo V del target virtuale; sintassi distinta da GNU make.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: GNU Make on Ubuntu 24.04. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
mk -f hello.mkfile all
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.mkfile`: `f671b0ee425f33991f4f8343c6920dd18a62a301bd77e518e37a2f686d7f0c98`

Fonti primarie:

- https://9p.io/sys/doc/mk.html
- https://www.gnu.org/software/make/manual/html_node/Recipes.html
