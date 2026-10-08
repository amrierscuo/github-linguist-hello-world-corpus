# 0289 — Haml: `.haml.deface`

Ruolo: Override Deface Haml con commento direttiva, non semplice rinomina di template.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Haml6.3.0, Temple0.10.7, Tilt2.9.0, Thor1.5.0; Ruby3.2.3. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Deface: collocare hello.html.haml.deface sotto app/overrides/posts/show/ e renderizzare il fixture
```

Risultato atteso: Paragrafo Hello, World! aggiunto dopo h1

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `fixture.html.erb`: `9212220934071959eee5b86f08428d18c5f93fdb0b302125e2f217d52c8a5cc3`
- `hello.html.haml.deface`: `c8e77a714bc31ceff49c6d69ac7b5459fe2c065a496487c1b0ba84e71cb25940`

Fonti primarie:

- https://github.com/spree/deface
- https://haml.info/docs/yardoc/file.REFERENCE.html
- https://github.com/haml/haml
- https://rubygems.org/gems/haml/versions/6.3.0
