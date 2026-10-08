# 0301 — IDL: `.dlm`

Ruolo: Descriptor IDL Dynamically Loadable Module: nome, versione e dichiarazione della routine; non codice .pro.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: NV5 Geospatial IDL proprietario; versione da registrare. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
IDL con SDK: compilare una libreria che esporta IDL_Load e CORPUS_HELLO; impostare !DLM_PATH e DLM_LOAD, "corpus_hello"
```

Risultato atteso: IDL registra il modulo descritto; una futura routine nativa stampa Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.
- La libreria condivisa e l’SDK IDL proprietario non sono disponibili; il solo descriptor non implementa la routine.

SHA-256 dei file della variante:

- `hello.dlm`: `e9f8b8157912ff4e4ebd03da09de88c3663d463d6cf61aad64bf48cd06ffd680`

Fonti primarie:

- https://www.nv5geospatialsoftware.com/docs/DLM.html
- https://www.nv5geospatialsoftware.com/docs/PRINT.html
- https://www.nv5geospatialsoftware.com/docs/Defining_Procedures.html
