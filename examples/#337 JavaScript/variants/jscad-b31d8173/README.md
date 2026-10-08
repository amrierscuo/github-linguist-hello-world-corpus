# 0337 — JavaScript: `.jscad`

Ruolo: OpenJSCAD: segmenti delle lettere convertiti in geometrie path2.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Node.js 22.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
OpenJSCAD/modeling: caricare hello.jscad e chiamare main
```

Risultato atteso: Hello, World! nel log/valore/risposta o geometria secondo il ruolo; PAC restituisce DIRECT senza rete.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.jscad`: `4f65f03e95787496ce4454f3b553e4c642e3863d5374d0814f73e148e41daa6d`

Fonti primarie:

- https://openjscad.xyz/docs/module-modeling_text.html
- https://nodejs.org/api/console.html#consolelogdata-args
