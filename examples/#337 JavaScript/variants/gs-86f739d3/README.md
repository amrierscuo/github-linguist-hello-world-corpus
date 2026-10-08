# 0337 — JavaScript: `.gs`

Ruolo: Google Apps Script, routine esplicita hello e Logger.log.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Node.js 22.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Eseguire hello nell’editor Apps Script; leggere log locale del progetto
```

Risultato atteso: Hello, World! nel log/valore/risposta o geometria secondo il ruolo; PAC restituisce DIRECT senza rete.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.gs`: `0a0249c44cde6bd323ba20a7e9e04f4950bebea75064fcff5ace476ad3181f92`

Fonti primarie:

- https://developers.google.com/apps-script/reference/base/logger
- https://nodejs.org/api/console.html#consolelogdata-args
