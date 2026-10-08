# 0401 — Lua: `.rockspec`

Ruolo: Descriptor LuaRocks: dati Lua con summary e module mapping, non programma print.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Lua 5.4.8 native Linux build from original sources. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
luarocks lint corpus-hello-1.0-1.rockspec; in build locale generare il tar del fixture e luarocks make
```

Risultato atteso: Descriptor registrato; modulo restituisce Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `corpus-hello-1.0-1.rockspec`: `04b95ae9c6ce6c4f2b19987c53644f86e093fb1d94304b2a83c5ff9071f877c1`
- `corpus_hello.lua`: `c6472388da8d915a57c4073b4fd9cabdbf9a3ec35a84fe263cf6b4b839aa7c23`

Fonti primarie:

- https://github.com/luarocks/luarocks/blob/main/docs/rockspec_format.md
- https://www.lua.org/manual/5.4/
