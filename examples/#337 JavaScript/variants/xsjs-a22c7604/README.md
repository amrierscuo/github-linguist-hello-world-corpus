# 0337 — JavaScript: `.xsjs`

Ruolo: Endpoint SAP HANA XS classic con risposta del saluto.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Node.js 22.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
SAP HANA XS classic: attivare solo in progetto di test e richiedere endpoint locale
```

Risultato atteso: Hello, World! nel log/valore/risposta o geometria secondo il ruolo; PAC restituisce DIRECT senza rete.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.xsjs`: `934c760c40e8274a936ddad214fafe5f6aba4e3cef87b77ffbef148d61da4f2d`

Fonti primarie:

- https://help.sap.com/doc/3de842783af24336b6305a3c0223a369/2.0.05/en-US/%24.web.Body.html
- https://nodejs.org/api/console.html#consolelogdata-args
