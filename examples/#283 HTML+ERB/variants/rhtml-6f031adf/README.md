# 0283 — HTML+ERB: `.rhtml`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#283 HTML+ERB/hello.erb.

Toolchain richiesta: Ruby3.2.3, ERB della libreria standard. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.rhtml; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: stdout <p>Hello, World!</p> seguito da newline; exit 0.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.rhtml`: `be111e0cf6656631175533dad2c49ae5667c01ea09c2589089e5f7247bb6c962`
- `render.rb`: `0ded8de25e33e448a6ceeb16159f7dffb20ed85079ff9b8c526b0bfbdec566c7`

Fonti primarie:

- https://docs.ruby-lang.org/en/3.2/ERB.html
