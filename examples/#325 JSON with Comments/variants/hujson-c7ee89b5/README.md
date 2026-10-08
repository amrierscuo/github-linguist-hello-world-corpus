# 0325 — JSON with Comments: `.hujson`

Ruolo: HuJSON: superset JSON con commenti; questo fixture usa il sottoinsieme JSONC condiviso.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#325 JSON with Comments/hello.jsonc.

Toolchain richiesta: Node.js 22.20.0 + jsonc-parser 3.3.1. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.hujson; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Hello, World! e LF; nessun errore di parsing.

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Parser del linguaggio accettato; schema/loader/semantica applicativa specifici restano non verificati.

SHA-256 dei file della variante:

- `hello.hujson`: `4284fd1dd5b3626ea52df2ac06daccaef3605d1e510a41cd2969ef03e493aaed`
- `verify.cjs`: `8e0f9decdfa86c6106e75f58312b147912c4e75f81afe3587a63873b5339d35a`

Fonti primarie:

- https://github.com/tailscale/hujson
- https://github.com/microsoft/node-jsonc-parser

Prova aggiuntiva realmente eseguita:

Parsing JSONC reale con Microsoft jsonc-parser; strutture applicative VS Code/Sublime non caricate.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 3.3.1
