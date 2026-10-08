# 0324 — JSON: `.yyp`

Ruolo: Dati JSON del linguaggio canonico, con estensione associata da languages.yml. Schema applicativo non verificato.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Python 3.13.9 json standard library. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
python -m json.tool hello.yyp
```

Risultato atteso: Oggetto JSON con greeting Hello, World!; nessuna promessa di validità per l’applicazione associata.

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Parser del linguaggio accettato; schema/loader/semantica applicativa specifici restano non verificati.
- Lo schema progetto GameMaker non è verificato; il dato non pretende di essere un progetto avviabile.

SHA-256 dei file della variante:

- `hello.yyp`: `ea6a04019de5767c9316a9ae80fd4542ed54fb1a46621d4d70e007299d1000fa`

Fonti primarie:

- https://www.rfc-editor.org/rfc/rfc8259
- https://manual.gamemaker.io/

Prova aggiuntiva realmente eseguita:

Parsing JSON/JSON Lines reale della sola grammatica canonica; nessuno schema di progetto/configurazione applicativa è stato validato.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 3.13.9
