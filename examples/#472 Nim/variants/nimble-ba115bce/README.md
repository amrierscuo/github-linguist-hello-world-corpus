# 0472 — Nim: `.nimble`

Ruolo: Manifest Nimble in NimScript con metadata e task hello.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Nim1.6.14 Ubuntu, backend C/GCC. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
nimble hello
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.nimble`: `c9cbdcadd41ecac468bfc3894695dc1d6233a260b57cb2183cc9452da33961de`

Fonti primarie:

- https://github.com/nim-lang/nimble#creating-packages
- https://nim-lang.org/docs/tut1.html
