# #699 TMDL

Voce canonica `TMDL`, tipo `data`, language_id `769162295`.

Descrivere un modello tabulare TMDL con una misura DAX originale che restituisce il saluto.

## Toolchain e riproduzione

Required genuine Microsoft.AnalysisServices.Tabular TmdlSerializer compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede Microsoft.AnalysisServices.Tabular TOM/TmdlSerializer e engine tabulare per DAX.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
TmdlSerializer.DeserializeModelFromFolder(directory); in un motore tabulare compatibile valutare la misura Greeting[Hello].
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Modello e tabella sorgenti originali; parser/engine non disponibili. Nessun servizio Power BI o account remoto necessario per una futura verifica locale.

Requisiti residui:

- Required Microsoft.AnalysisServices.Tabular TmdlSerializer toolchain and matching execution/format resources are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://learn.microsoft.com/en-us/analysis-services/tmdl/tmdl-overview?view=asallproducts-allversions](https://learn.microsoft.com/en-us/analysis-services/tmdl/tmdl-overview?view=asallproducts-allversions)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tmdl` | [model.tmdl](model.tmdl), [Greeting.tmdl](tables/Greeting.tmdl) creato, verifiche pendenti |
