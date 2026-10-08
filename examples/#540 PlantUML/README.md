# #540 PlantUML

Voce canonica `PlantUML`, tipo `data`, language_id `833504686`.

Renderizzare un diagramma di sequenza PlantUML con il saluto sul messaggio.

## Toolchain e riproduzione

Official PlantUML MIT Light sequence-diagram parser/renderer — PlantUML version 1.2026.8 / 149874a [2026-09-05 15:59:17 UTC]. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

PlantUML 1.2026.8 MIT Light ufficiale e Java 21; sequenza non richiede Graphviz per il rendering.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
java -jar /path/to/plantuml-1.2026.8.jar -tsvg hello.puml
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il renderer vero produce SVG e la verifica legge il nodo text della freccia, con Hello, World! esatto. SVG compilato resta in work.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://plantuml.com/sequence-diagram](https://plantuml.com/sequence-diagram)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.puml` | [hello.puml](hello.puml), [driver.puml](variants/iuml-91e3fc09/driver.puml) creato, verifiche pendenti |
| `.iuml` | [hello.iuml](variants/iuml-91e3fc09/hello.iuml) creato, verifiche pendenti |
| `.plantuml` | [hello.plantuml](variants/plantuml-b52e863a/hello.plantuml) creato, verifiche pendenti |
