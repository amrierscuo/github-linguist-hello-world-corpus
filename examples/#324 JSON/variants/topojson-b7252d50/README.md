# 0324 — JSON: `.topojson`

Ruolo: Topology TopoJSON con un Point, senza archi perché non necessari.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Python 3.13.9 json standard library. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
python -m json.tool hello.topojson; poi usare il validatore/lettore originale dello schema (il parsing JSON non dimostra lo schema prodotto).
```

Risultato atteso: Documento JSON riconosciuto nello schema specifico; saluto nel campo indicato.

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Parser del linguaggio accettato; schema/loader/semantica applicativa specifici restano non verificati.

SHA-256 dei file della variante:

- `hello.topojson`: `f7b6ed49bbff3cf751f08c0398187d960f1d61665ed0f44d1ca4a0df8eac3b7b`

Fonti primarie:

- https://github.com/topojson/topojson-specification
- https://www.rfc-editor.org/rfc/rfc8259

Prova aggiuntiva realmente eseguita:

Parsing JSON/JSON Lines reale della sola grammatica canonica; nessuno schema di progetto/configurazione applicativa è stato validato.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 3.13.9
