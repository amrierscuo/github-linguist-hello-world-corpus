# #693 Sweave

Voce canonica `Sweave`, tipo `prose`, language_id `558779190`.

Eseguire il chunk R di un documento Sweave e produrre il saluto nel LaTeX generato.

## Toolchain e riproduzione

Original R Sweave document engine — R version 4.3.3 (2024-02-29) -- "Angel Food Cake". Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

GNU R4.3.3 e Sweave originali. Il log registra R_HOME e librerie della distribuzione relocata.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
R --vanilla --slave -e 'utils::Sweave("hello.rnw",output="build/hello.tex")'
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

R esegue cat nel chunk results=tex; il documento generato contiene il saluto esatto. Ambito: Sweave e LaTeX generato, senza compilazione/impaginazione TeX.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://stat.ethz.ch/R-manual/R-devel/library/utils/html/Sweave.html](https://stat.ethz.ch/R-manual/R-devel/library/utils/html/Sweave.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rnw` | [hello.rnw](hello.rnw) verificato |
