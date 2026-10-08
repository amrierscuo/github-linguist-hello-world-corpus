# 0401 — Lua: `.wlua`

Ruolo: Sorgente Lua windowed per host Windows; stessa sintassi Lua, stdout potrebbe non avere una console.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#401 Lua/hello.lua.

Toolchain richiesta: Lua 5.4.8 native Linux build from original sources. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.wlua; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Il programma richiede un host con stdout o console catturata per osservare Hello, World!.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.wlua`: `07219cd9561b41ce1f39209958076c471b17855679c968b42767b0122423c782`

Fonti primarie:

- https://www.lua.org/manual/5.4/
