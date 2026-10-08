# 0423 — Max: `.mxt`

Ruolo: Patcher Max legacy testuale max v2/#N/#P, con lista dei 13 codici ASCII del saluto -> itoa -> print. Non è il formato binario maxb; la message numerica non usa separatori virgola.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Cycling ’74 Max 8+. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Max originale compatibile: aprire hello.mxt come patcher testuale (o importare dal clipboard) e leggere la console; verificare il reader legacy e il collegamento loadbang/message/itoa/print.
```

Risultato atteso: Console con simbolo Hello, World! (prefisso print corpus consentito).

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.
- Reader Max legacy non eseguito; saluto espresso come codici ASCII e convertito da itoa, evitando ambiguità della serializzazione del comma.

SHA-256 dei file della variante:

- `hello.mxt`: `9f2eb2ebe46c91b32617235c1be7329ec11fce04663c86b9ee979bfad7c9f26f`

Fonti primarie:

- https://docs.cycling74.com/userguide/filetypes/
- https://docs.cycling74.com/reference/itoa/
- https://github.com/github-linguist/linguist/blob/main/samples/Max/Hello.mxt
- https://docs.cycling74.com/reference/message/
- https://docs.cycling74.com/reference/print/
