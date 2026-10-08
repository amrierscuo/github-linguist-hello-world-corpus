# 0401 — Lua: `.p8`

Ruolo: Cartuccia PICO-8 testuale con header/version e sezione __lua__; il saluto è disegnato in _draw.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Lua 5.4.8 native Linux build from original sources. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
PICO-8: load hello.p8; run
```

Risultato atteso: Hello, World! a schermo

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.p8`: `69b1187af68e835a7a5f603b681ff580c07aa1ba9f81af74401b930dd71f3952`

Fonti primarie:

- https://www.lexaloffle.com/dl/docs/pico-8_manual.html
- https://www.lua.org/manual/5.4/
