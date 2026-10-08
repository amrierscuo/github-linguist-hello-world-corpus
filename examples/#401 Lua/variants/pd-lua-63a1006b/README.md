# 0401 — Lua: `.pd_lua`

Ruolo: Classe Pd-Lua pdlua con metodo di bang e outlet simbolico, non print Lua standalone.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Lua 5.4.8 native Linux build from original sources. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Pure Data con pdlua: creare [hello], inviare bang e leggere outlet con [print]
```

Risultato atteso: Simbolo Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.pd_lua`: `1889785b2e68c5d26445d1a5fd3b7790a8999a87be2124fb91b245677a8af75f`

Fonti primarie:

- https://github.com/agraef/pd-lua
- https://www.lua.org/manual/5.4/
