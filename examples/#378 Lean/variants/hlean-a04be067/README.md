# 0378 — Lean: `.hlean`

Ruolo: Definizione Lean 2 HoTT di una stringa del saluto; eval riduce il termine. Non usa IO/main Lean 3.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Lean3.51.1 community ufficiale Windows. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Lean 2 originale con libreria HoTT sul LEAN_PATH: lean hello.hlean
```

Risultato atteso: Elaborazione del termine greeting:string e output di eval con la stringa Hello, World! (la formattazione del pretty-printer può includere virgolette).

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.
- Lean 2 e libreria HoTT compatibili non predisposti. Lean 3 e Lean 4 non validano questo dialetto storico.

SHA-256 dei file della variante:

- `hello.hlean`: `bd1f6961b5ef47fc720b2455279d2f8ba0c87eb479f12e3bfd0389549e9d0ba1`

Fonti primarie:

- https://raw.githubusercontent.com/leanprover/tutorial/master/05_Interacting_with_Lean.org
- https://raw.githubusercontent.com/leanprover/lean2/master/hott/init/datatypes.hlean
- https://github.com/leanprover/lean2
- https://github.com/leanprover-community/lean/releases/tag/v3.51.1
- https://leanprover-community.github.io/lean3/
