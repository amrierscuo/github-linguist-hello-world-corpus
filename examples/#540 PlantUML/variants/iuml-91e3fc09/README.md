# 0540 — PlantUML: `.iuml`

Ruolo: Include PlantUML con definizione di variabile del saluto, driver diagramma separato.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Official PlantUML MIT Light sequence-diagram parser/renderer — PlantUML version 1.2026.8 / 149874a [2026-09-05 15:59:17 UTC]. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
java -jar plantuml.jar -tsvg driver.puml
```

Risultato atteso: Label Hello, World! nello SVG

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `driver.puml`: `25772e482c8bcabb40472dc44ba271903534187c0b00fd9039deb5caff5abee1`
- `hello.iuml`: `bf5a6ae4fb7487d784bf3f88a4f78024a4167a0cc68aa9ec84ff883b1decaeea`

Fonti primarie:

- https://plantuml.com/preprocessing
- https://plantuml.com/sequence-diagram
