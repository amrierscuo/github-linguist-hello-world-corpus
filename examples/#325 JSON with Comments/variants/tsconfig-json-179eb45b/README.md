# 0325 — JSON with Comments: `.tsconfig.json`

Ruolo: Config TypeScript con fixture sorgente separato; non JSON generico.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Node.js 22.20.0 + jsonc-parser 3.3.1. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
tsc -p hello.tsconfig.json; node build/hello.js
```

Risultato atteso: Configurazione riconosciuta; inserimento/nome del saluto secondo il ruolo. Per il tema: regola colore, nessuna emissione del saluto.

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Parser del linguaggio accettato; schema/loader/semantica applicativa specifici restano non verificati.

SHA-256 dei file della variante:

- `hello.ts`: `dcc62e4a18325773332e645365de256e46ae08fd1609ff72edd1d7367ed4b632`
- `hello.tsconfig.json`: `1172df4baeffa57b7796a73888b6c7d05dd7ea7699daa1628067f59ef4e06fcc`

Fonti primarie:

- https://www.typescriptlang.org/tsconfig/
- https://github.com/microsoft/node-jsonc-parser

Prova aggiuntiva realmente eseguita:

Parsing JSONC reale con Microsoft jsonc-parser; strutture applicative VS Code/Sublime non caricate.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 3.3.1
