# 0401 — Lua: `.rbxs`

Ruolo: Script Roblox Luau testuale con print; non un modello binario Roblox.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Lua 5.4.8 native Linux build from original sources. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Roblox Studio: importare il testo come Script e leggere Output in progetto locale
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.rbxs`: `07219cd9561b41ce1f39209958076c471b17855679c968b42767b0122423c782`

Fonti primarie:

- https://create.roblox.com/docs/luau
- https://www.lua.org/manual/5.4/
