# 0283 — HTML+ERB: `.erb.deface`

Ruolo: Override Deface con direttiva di inserimento e corpo ERB, nella gerarchia app/overrides.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Ruby3.2.3, ERB della libreria standard. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Deface: collocare hello.html.erb.deface sotto app/overrides/posts/show/ e renderizzare il fixture di vista
```

Risultato atteso: Un paragrafo aggiunto dopo h1 contenente Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `fixture.html.erb`: `9212220934071959eee5b86f08428d18c5f93fdb0b302125e2f217d52c8a5cc3`
- `hello.html.erb.deface`: `59fb850d6330c5e58bdb9593ceb94c7eb09542731a00e8679ec3809764e6457d`

Fonti primarie:

- https://github.com/spree/deface
- https://docs.ruby-lang.org/en/3.2/ERB.html
