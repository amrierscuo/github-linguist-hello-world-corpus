# #698 TLA

Voce canonica `TLA`, tipo `programming`, language_id `364`.

Verificare un modello TLA+ finito con saluto iniziale e invariante esatto.

## Toolchain e riproduzione

Original TLA+ SANY parser and TLC finite-state model checker — TLA+ tools release 1.8.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

TLA+ tools1.8.0 ufficiali, SANY e TLC.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
java -cp /path/to/tla2tools.jar tla2sany.SANY Hello.tla; java -cp /path/to/tla2tools.jar tlc2.TLC -cleanup -metadir build/states -config Hello.cfg Hello.tla
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

SANY accetta il modulo; TLC stampa PrintT del valore e completa il model checking con 1 stato distinto e invariante senza violazioni.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://lamport.azurewebsites.net/tla/tools.html](https://lamport.azurewebsites.net/tla/tools.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tla` | [Hello.tla](Hello.tla) verificato |
