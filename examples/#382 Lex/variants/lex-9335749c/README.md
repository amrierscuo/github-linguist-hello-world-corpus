# 0382 — Lex: `.lex`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#382 Lex/hello.l.

Toolchain richiesta: flex 2.6.4; GCC 13.3.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.lex; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Scanner exit 0; una riga Hello, World!.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.lex`: `4ab326b779b681bd4737c8cd30b9bd6cc36af946eb36e6d82fb0b138a904c067`
- `input.txt`: `5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03`

Fonti primarie:

- https://westes.github.io/flex/manual/
- https://westes.github.io/flex/manual/Simple-Examples.html
