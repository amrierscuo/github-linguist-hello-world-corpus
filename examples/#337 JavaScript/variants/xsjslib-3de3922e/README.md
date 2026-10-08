# 0337 — JavaScript: `.xsjslib`

Ruolo: Libreria SAP HANA XS classic esportabile con funzione greeting.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Node.js 22.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
SAP HANA XS classic: importare la libreria e chiamare greeting()
```

Risultato atteso: Hello, World! nel log/valore/risposta o geometria secondo il ruolo; PAC restituisce DIRECT senza rete.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.xsjslib`: `781946f10e485a7dbb8a9b0b8b5d3fe4b610a05e113f1c6e789973eb107a6602`

Fonti primarie:

- https://help.sap.com/docs/PRODUCT_ID/52715f71adba4aaeb480d946c742d1f6/649ff83a7da04762a02e3dad8be01c8b.html
- https://nodejs.org/api/console.html#consolelogdata-args
