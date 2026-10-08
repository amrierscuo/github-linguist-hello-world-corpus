# 0376 — Lasso: `.lasso8`

Ruolo: Template Lasso 8 bracket syntax con espressione di stringa; distinta dal template Lasso 9.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Lasso9 originale; versione da registrare. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Lasso 8: servire il template hello.lasso8 da host di test
```

Risultato atteso: Hello, World! nel rendering

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.lasso8`: `0431588ad84fbfc41ca0c7e1341ab5d0586ec5a47237fc88be6b8f095c75821a`

Fonti primarie:

- https://www.lassosoft.com/Lasso-8-Documentation
- https://lassoguide.com/operations/command-line-tools.html
- https://lassoguide.com/language/variables.html
