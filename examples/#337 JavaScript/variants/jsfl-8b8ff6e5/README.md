# 0337 — JavaScript: `.jsfl`

Ruolo: Script Adobe Animate JSFL; log tramite host fl.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Node.js 22.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Adobe Animate: eseguire hello.jsfl come command
```

Risultato atteso: Hello, World! nel log/valore/risposta o geometria secondo il ruolo; PAC restituisce DIRECT senza rete.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.jsfl`: `156978da52aa831d15d70f73aa03ac4d8323ddc148c028bcb6ef95338aef40c3`

Fonti primarie:

- https://help.adobe.com/en_US/flash/cs/extend/flash_cs5_extending.pdf
- https://nodejs.org/api/console.html#consolelogdata-args
