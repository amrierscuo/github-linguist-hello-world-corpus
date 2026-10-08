# 0324 — JSON: `.4DProject`

Ruolo: Descriptor di progetto 4D con commento riconosciuto; nessuna base dati binaria.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Python 3.13.9 json standard library. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
python -m json.tool hello.4DProject; poi usare il validatore/lettore originale dello schema (il parsing JSON non dimostra lo schema prodotto).
```

Risultato atteso: Documento JSON riconosciuto nello schema specifico; saluto nel campo indicato.

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Parser del linguaggio accettato; schema/loader/semantica applicativa specifici restano non verificati.

SHA-256 dei file della variante:

- `hello.4DProject`: `6019c386a0188b4ed9fc7420eb82d7484d3c5dfa48a24827371d743ae4b5f653`

Fonti primarie:

- https://developer.4d.com/docs/18/Project/architecture
- https://github.com/github-linguist/linguist/blob/main/samples/JSON/4DPopGit.4DProject
- https://www.rfc-editor.org/rfc/rfc8259

Prova aggiuntiva realmente eseguita:

Parsing JSON/JSON Lines reale della sola grammatica canonica; nessuno schema di progetto/configurazione applicativa è stato validato.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 3.13.9
