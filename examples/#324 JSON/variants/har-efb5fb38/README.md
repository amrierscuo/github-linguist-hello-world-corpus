# 0324 — JSON: `.har`

Ruolo: Fixture HTTP Archive 1.2 con corpo risposta del saluto; data e URL illustrativi, nessuna richiesta effettuata.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Python 3.13.9 json standard library. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Validatore HAR 1.2 e lettura log.entries[0].response.content.text
```

Risultato atteso: Hello, World! nel corpo rappresentato

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Parser del linguaggio accettato; schema/loader/semantica applicativa specifici restano non verificati.

SHA-256 dei file della variante:

- `hello.har`: `dd45b3f0696a090659966c56890432a14f75d5bb6d600e647ddaf12668f98f78`

Fonti primarie:

- https://w3c.github.io/web-performance/specs/HAR/Overview.html
- https://www.rfc-editor.org/rfc/rfc8259

Prova aggiuntiva realmente eseguita:

Parsing JSON/JSON Lines reale della sola grammatica canonica; nessuno schema di progetto/configurazione applicativa è stato validato.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 3.13.9
