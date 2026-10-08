# 0325 — JSON with Comments: `.sublime-completions`

Ruolo: Completamento del saluto.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Node.js 22.20.0 + jsonc-parser 3.3.1. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Aprire/interpretare con VS Code o Sublime Text secondo il ruolo; il file è solo un fixture e non viene installato nelle preferenze utente.
```

Risultato atteso: Configurazione riconosciuta; inserimento/nome del saluto secondo il ruolo. Per il tema: regola colore, nessuna emissione del saluto.

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Parser del linguaggio accettato; schema/loader/semantica applicativa specifici restano non verificati.

SHA-256 dei file della variante:

- `hello.sublime-completions`: `2b25c1ff624b368c7e02235d006b59e1f7e2f9e05b81cbaf71b7b62910eb4acb`

Fonti primarie:

- https://www.sublimetext.com/docs/completions.html
- https://github.com/microsoft/node-jsonc-parser

Prova aggiuntiva realmente eseguita:

Parsing JSONC reale con Microsoft jsonc-parser; strutture applicative VS Code/Sublime non caricate.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 3.3.1
