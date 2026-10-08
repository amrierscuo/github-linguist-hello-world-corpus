# 0423 — Max: `.maxhelp`

Ruolo: Patch di aiuto Max: stesso documento patcher JSON del sorgente principale; la message box resta collegata a print.

Provenienza: adattamento del patcher originale del corpus; il contenuto della message box protegge la virgola con backslash per inviare un solo messaggio.

Toolchain richiesta: Cycling ’74 Max 8+. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.maxhelp; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: patch accettato; console contiene greeting: Hello, World!.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.maxhelp`: `0891aa513d9e3cedeb7b8d09e835264e3e52aa063c028c4627230767117e8540`

Fonti primarie:

- https://docs.cycling74.com/reference/message/
- https://docs.cycling74.com/reference/print/

Fonte sul separatore virgola: https://docs.cycling74.com/reference/message/
