# 0325 — JSON with Comments: `.sublime_session`

Ruolo: Dati JSONC del linguaggio canonico; non una serializzazione di stato/sessione Sublime originale.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Node.js 22.20.0 + jsonc-parser 3.3.1. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Parser JSONC originale sul file hello.sublime_session
```

Risultato atteso: Dato greeting Hello, World!; schema applicativo Sublime non verificato.

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Parser del linguaggio accettato; schema/loader/semantica applicativa specifici restano non verificati.
- Lo schema/versione dello stato editor è ignoto; questo fixture non va importato come sessione o cache dell’editor.

SHA-256 dei file della variante:

- `hello.sublime_session`: `a6b0590ded57cdec36711b0e2419126863803a761388ceccacb1dcadcb650ac0`

Fonti primarie:

- https://github.com/microsoft/node-jsonc-parser
- https://www.sublimetext.com/docs/projects.html

Prova aggiuntiva realmente eseguita:

Parsing JSONC reale con Microsoft jsonc-parser; strutture applicative VS Code/Sublime non caricate.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 3.3.1
