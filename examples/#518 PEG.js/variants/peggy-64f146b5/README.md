# 0518 — PEG.js: `.peggy`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#518 PEG.js/hello.pegjs.

Toolchain richiesta: Node.js 22.20.0 + Peggy. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.peggy; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: saluto riconosciuto, input errato rifiutato.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.peggy`: `3636735c9bbd19ff288579658e3b66fdab1bf82ecc3be189c7557b5217e60397`
- `verify.cjs`: `be801a915083bf6331a0cae3578224abb89d2c063801eb69f18c64ba0900f890`

Fonti primarie:

- https://peggyjs.org/documentation.html
