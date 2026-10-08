# #696 TI Program

Voce canonica `TI Program`, tipo `programming`, language_id `422`.

Mostrare il saluto con Disp in un programma TI-BASIC esportato come testo.

## Toolchain e riproduzione

Required genuine TI-Connect compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede tool TI che supporti il formato testuale esportato e il runtime della calcolatrice.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
Importare hello.8xp.txt con uno strumento TI compatibile, tokenizzare nel formato .8xp e avviare HELLO su TI-83/84 o emulatore autentico.
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Il file canonico .8xp.txt contiene sorgente originale con header PROGRAM e istruzione Disp, non un falso pacchetto binario .8xp. Toolchain/calcolatrice assenti.

Requisiti residui:

- Required TI-Connect toolchain and matching execution/format resources are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://education.ti.com/en/guidebook/details/en/BF077B5A987B41878D5FA83B6EADFBE5/84pceb](https://education.ti.com/en/guidebook/details/en/BF077B5A987B41878D5FA83B6EADFBE5/84pceb)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.8xp` | [hello.8xp](variants/8xp-e496e607/hello.8xp) sintassi verificata |
| `.8xp.txt` | [hello.8xp.txt](hello.8xp.txt) creato, verifiche pendenti |
