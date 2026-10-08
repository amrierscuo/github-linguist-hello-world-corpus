# 0401 — Lua: `.fcgi`

Ruolo: Script Lua FastCGI per binding Lua MSYS documentata: un request su socket FD 0 ereditato, risposta e finish.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Lua 5.4.8 native Linux build from original sources. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Host Lua MSYS FastCGI: socket FD 0 ereditato da un processo di test; una sola richiesta di test e cleanup
```

Risultato atteso: Risposta FastCGI con Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.
- Binding fcgi Lua MSYS originale non predisposta; nessun socket viene creato in questa preparazione.

SHA-256 dei file della variante:

- `hello.fcgi`: `c819d3acb5b468c607b1a0c1e3dbbd7dff54df2d028e54cf1720554f5bdb20ba`

Fonti primarie:

- https://lua.msys.ch/lua-module-reference.html
- https://www.lua.org/manual/5.4/
