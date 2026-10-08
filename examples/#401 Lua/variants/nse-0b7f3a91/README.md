# 0401 — Lua: `.nse`

Ruolo: Nmap NSE con prerule e action del saluto; non effettua scansioni.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Lua 5.4.8 native Linux build from original sources. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
nmap --script-help hello.nse (offline, carica descriptor; action da verificare in harness originale senza target)
```

Risultato atteso: NSE registra il descriptor; action restituisce Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.nse`: `ca521774b0b7c7a373901a1487b54c48f3170d491bc793e48427094f182b87a6`

Fonti primarie:

- https://nmap.org/book/nse-script-format.html
- https://www.lua.org/manual/5.4/
