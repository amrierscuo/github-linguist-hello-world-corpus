# 0337 — JavaScript: `.jsx`

Ruolo: Script Adobe ExtendScript .jsx: JavaScript senza JSX React, dialogo del saluto.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Node.js 22.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Host Adobe ExtendScript compatibile: eseguire hello.jsx
```

Risultato atteso: Hello, World! nel log/valore/risposta o geometria secondo il ruolo; PAC restituisce DIRECT senza rete.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.jsx`: `4cedb4294e19952cef51dfd2e310dfa71e0acd702ed27c5ad73dc2544afcc6c2`

Fonti primarie:

- https://extendscript.docsforadobe.dev/
- https://nodejs.org/api/console.html#consolelogdata-args
