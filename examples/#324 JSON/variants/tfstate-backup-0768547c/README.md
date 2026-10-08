# 0324 — JSON: `.tfstate.backup`

Ruolo: Fixture testuale di stato Terraform schema v4 con output stringa, scritto come dato illustrativo; non dichiara apply o snapshot reali.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Python 3.13.9 json standard library. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
terraform show -json hello.tfstate.backup
```

Risultato atteso: Output greeting con valore Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Parser del linguaggio accettato; schema/loader/semantica applicativa specifici restano non verificati.

SHA-256 dei file della variante:

- `hello.tfstate.backup`: `c90936cf4ed25df3960ef70914546a75a65f5baf5dc70db2382a4d130d4805a6`

Fonti primarie:

- https://developer.hashicorp.com/terraform/language/state
- https://github.com/hashicorp/terraform/blob/main/internal/states/statefile/version4.go
- https://www.rfc-editor.org/rfc/rfc8259

Prova aggiuntiva realmente eseguita:

Parsing JSON/JSON Lines reale della sola grammatica canonica; nessuno schema di progetto/configurazione applicativa è stato validato.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 3.13.9
