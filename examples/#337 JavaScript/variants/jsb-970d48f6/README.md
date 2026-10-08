# 0337 — JavaScript: `.jsb`

Ruolo: Sorgente JavaScript testuale del linguaggio canonico; integrazione del loader/framework e qualsiasi schema build proprietario non verificati.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#337 JavaScript/hello.js.

Toolchain richiesta: Node.js 22.20.0. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
node --check < hello.jsb; node < hello.jsb
```

Risultato atteso: stdout Hello, World! e LF, uscita 0.

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `true`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Prova limitata a Node via stdin: loader/framework proprietario del suffisso non verificato.
- La prova eventualmente effettuata via stdin riguarda JavaScript; nessuna compatibilità del loader .bones/.jsb o schema di build applicativo viene affermata.

SHA-256 dei file della variante:

- `hello.jsb`: `dcc62e4a18325773332e645365de256e46ae08fd1609ff72edd1d7367ed4b632`

Fonti primarie:

- https://nodejs.org/api/cli.html
- https://github.com/github-linguist/linguist/tree/main/samples/JavaScript
- https://nodejs.org/api/console.html#consolelogdata-args

Prova aggiuntiva realmente eseguita:

JavaScript originale analizzato ed eseguito da Node via stdin; stdout esatto Hello, World! e LF. Non verifica loader proprietari del suffisso.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: v22.20.0
