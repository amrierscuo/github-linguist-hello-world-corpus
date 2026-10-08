# 0395 — LiveScript: `._ls`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#395 LiveScript/hello.ls.

Toolchain richiesta: livescript 1.6.0; Node 22.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello._ls; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Exit 0; Hello, World! più newline.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello._ls`: `88f3edde83d49c7e1e3c49a41948d6e87205f4d29613b7c46eda7eaa0898b3b2`
- `package.json`: `d70b4a612ae3e0e484b2836702588994e003fb7e126add48512094e03b518222`

Fonti primarie:

- https://livescript.net/
- https://github.com/gkz/LiveScript
