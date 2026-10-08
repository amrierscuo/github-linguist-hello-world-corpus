# 0408 — MAXScript: `.mcr`

Ruolo: MacroScript MAXScript registrabile, stampa in Listener solo on execute.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Autodesk 3ds Max MAXScript runtime. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
3ds Max: valutare hello.mcr; eseguire la macro CorpusGreeting in ambiente di test
```

Risultato atteso: Hello, World! nel Listener

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.mcr`: `65a32b61750d64c68133288fc281c3f15a852d8fc444334545b45abebeb3df04`

Fonti primarie:

- https://help.autodesk.com/view/MAXDEV/2024/ENU/?guid=GUID-6E21C768-7256-4500-AB1F-B144F492F055
- https://help.autodesk.com/view/MAXDEV/2026/ENU/
