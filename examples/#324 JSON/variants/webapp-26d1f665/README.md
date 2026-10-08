# 0324 — JSON: `.webapp`

Ruolo: Manifest Open Web App Mozilla storico; saluto nel nome.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Python 3.13.9 json standard library. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
python -m json.tool hello.webapp; poi usare il validatore/lettore originale dello schema (il parsing JSON non dimostra lo schema prodotto).
```

Risultato atteso: Documento JSON riconosciuto nello schema specifico; saluto nel campo indicato.

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Parser del linguaggio accettato; schema/loader/semantica applicativa specifici restano non verificati.

SHA-256 dei file della variante:

- `hello.webapp`: `568067ef9ab02bdeae81f0ebf54c60b50baf4d1930abf7491c2513bd3d44f58b`
- `index.html`: `67867b77f5bc7be02ee8c4788be7d073ef63a75ad317ee1d9b46193a52ee06f3`

Fonti primarie:

- https://firefox-source-docs.mozilla.org/devtools-user/app_manager/index.html
- https://www.rfc-editor.org/rfc/rfc8259

Prova aggiuntiva realmente eseguita:

Parsing JSON/JSON Lines reale della sola grammatica canonica; nessuno schema di progetto/configurazione applicativa è stato validato.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 3.13.9
