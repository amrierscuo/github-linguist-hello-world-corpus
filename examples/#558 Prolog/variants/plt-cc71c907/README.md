# 0558 — Prolog: `.plt`

Ruolo: Unit test Prolog plunit con verifica del saluto, distinto da main.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: SWI-Prolog9.0.4 ufficiale Ubuntu. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
swipl -q -g run_tests -t halt hello.plt
```

Risultato atteso: Test plunit PASS

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.plt`: `7dfb71c8bc69e695d125e6ae16a614c01807dcddb1a0c7062fb5679a41d5a7f1`

Fonti primarie:

- https://www.swi-prolog.org/pldoc/doc_for?object=section(%27packages/plunit.html%27)
- https://www.swi-prolog.org/pldoc/doc_for?object=atomic_list_concat/2
- https://www.swi-prolog.org/pldoc/doc_for?object=initialization/2
