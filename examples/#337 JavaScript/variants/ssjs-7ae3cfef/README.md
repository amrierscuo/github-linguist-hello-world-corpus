# 0337 — JavaScript: `.ssjs`

Ruolo: Marketing Cloud SSJS con funzione host Write.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Node.js 22.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Marketing Cloud SSJS: eseguire hello.ssjs in contenuto di test
```

Risultato atteso: Hello, World! nel log/valore/risposta o geometria secondo il ruolo; PAC restituisce DIRECT senza rete.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.ssjs`: `5f6705ea8cd589e45b1d91b4fdca9f63dc9d48b0a9c2b5135f978d818fbe0454`

Fonti primarie:

- https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/ssjs_utilitiesWrite.html
- https://nodejs.org/api/console.html#consolelogdata-args
