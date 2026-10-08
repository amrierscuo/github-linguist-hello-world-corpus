# 0540 — PlantUML: `.plantuml`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#540 PlantUML/hello.puml.

Toolchain richiesta: Official PlantUML MIT Light sequence-diagram parser/renderer — PlantUML version 1.2026.8 / 149874a [2026-09-05 15:59:17 UTC]. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.plantuml; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.plantuml`: `2bf9c506da220ed07b52a992b480af135eb7f9852dde165255630713d602f75f`

Fonti primarie:

- https://plantuml.com/sequence-diagram
