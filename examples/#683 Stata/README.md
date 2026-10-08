# #683 Stata

Voce canonica `Stata`, tipo `programming`, language_id `358`.

Eseguire un do-file Stata con macro locale e display.

## Toolchain e riproduzione

Required genuine stata compiler/runtime — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede Stata 18 o compatibile con licenza locale valida.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
stata -b do hello.do
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Programma originale; interpreter proprietario non disponibile.

Requisiti residui:

- Required stata toolchain and matching execution/format resources are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.stata.com/manuals/pdisplay.pdf](https://www.stata.com/manuals/pdisplay.pdf)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.do` | [hello.do](hello.do), [main.do](variants/doh-7967ee57/main.do) creato, verifiche pendenti |
| `.ado` | [hello.ado](variants/ado-34dc7b88/hello.ado) creato, verifiche pendenti |
| `.doh` | [hello.doh](variants/doh-7967ee57/hello.doh) creato, verifiche pendenti |
| `.ihlp` | [hello.ihlp](variants/ihlp-05facafd/hello.ihlp) creato, verifiche pendenti |
| `.mata` | [hello.mata](variants/mata-3f9d2836/hello.mata) creato, verifiche pendenti |
| `.matah` | [hello.matah](variants/matah-70401489/hello.matah) creato, verifiche pendenti |
| `.sthlp` | [hello.sthlp](variants/sthlp-90c77a77/hello.sthlp) creato, verifiche pendenti |
