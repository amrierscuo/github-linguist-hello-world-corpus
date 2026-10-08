# 0324 — JSON: `.JSON-tmLanguage`

Ruolo: Grammatica TextMate JSON con pattern di evidenziazione del saluto.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Python 3.13.9 json standard library. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
python -m json.tool hello.JSON-tmLanguage; poi usare il validatore/lettore originale dello schema (il parsing JSON non dimostra lo schema prodotto).
```

Risultato atteso: Documento JSON riconosciuto nello schema specifico; saluto nel campo indicato.

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Parser del linguaggio accettato; schema/loader/semantica applicativa specifici restano non verificati.

SHA-256 dei file della variante:

- `hello.JSON-tmLanguage`: `2024999f8d5afffa1d07fb59fbdd0abc1c66dc4a5cda1b1902a542c07bef00a4`

Fonti primarie:

- https://macromates.com/manual/en/language_grammars
- https://www.rfc-editor.org/rfc/rfc8259

Prova aggiuntiva realmente eseguita:

Parsing JSON/JSON Lines reale della sola grammatica canonica; nessuno schema di progetto/configurazione applicativa è stato validato.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 3.13.9
