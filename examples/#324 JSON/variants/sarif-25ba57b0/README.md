# 0324 — JSON: `.sarif`

Ruolo: Fixture SARIF di una nota illustrativa; non pretende che un analizzatore sia stato eseguito.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Python 3.13.9 json standard library. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
python -m json.tool hello.sarif; poi usare il validatore/lettore originale dello schema (il parsing JSON non dimostra lo schema prodotto).
```

Risultato atteso: Documento JSON riconosciuto nello schema specifico; saluto nel campo indicato.

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Parser del linguaggio accettato; schema/loader/semantica applicativa specifici restano non verificati.

SHA-256 dei file della variante:

- `hello.sarif`: `06c031cb2d4c31ddea2cb1412579497999f47d2c0ad56b2e42d185f0624a45ef`

Fonti primarie:

- https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html
- https://www.rfc-editor.org/rfc/rfc8259

Prova aggiuntiva realmente eseguita:

Parsing JSON/JSON Lines reale della sola grammatica canonica; nessuno schema di progetto/configurazione applicativa è stato validato.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 3.13.9
