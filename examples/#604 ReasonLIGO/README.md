# #604 ReasonLIGO

Voce canonica `ReasonLIGO`, tipo `programming`, language_id `319002153`.

Definire e valutare una funzione stringa nel dialetto storico ReasonLIGO.

## Toolchain e riproduzione

Required genuine ligo compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede una release LIGO che supporti ancora ReasonLIGO; le release moderne possono aver rimosso il frontend.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
ligo interpret result --init-file hello.religo --syntax reasonligo
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Funzione originale con parametro World; compiler storico non disponibile. Nessuna catena, wallet o deployment necessario.

Requisiti residui:

- Required ligo compiler/runtime and matching host resources are not available/configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://gitlab.com/ligolang/ligo/-/tree/dev/src/test/contracts](https://gitlab.com/ligolang/ligo/-/tree/dev/src/test/contracts)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.religo` | [hello.religo](hello.religo) creato, verifiche pendenti |
