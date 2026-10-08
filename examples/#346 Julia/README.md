# #346 Julia

Voce canonica `Julia`, tipo `programming`, language_id `184`.

Eseguire un sorgente Julia che concatena il saluto tramite gli argomenti di println.

## Toolchain e riproduzione

Official Julia native runtime — julia version 1.13.1. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Julia ufficiale portable 1.13.1 Windows x64. L’archivio è verificato contro SHA-256 del versions.json ufficiale. JULIA_DEPOT_PATH è isolata nella directory di lavoro.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
julia --startup-file=no --history-file=no hello.jl
```

Risultato atteso: Exit 0; saluto esatto seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il runtime nativo legge ed esegue il vero sorgente .jl e stdout viene confrontato esattamente. La voce Julia REPL registra separatamente prompt e visualizzazione interattiva.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://docs.julialang.org/en/v1/manual/command-line-interface/](https://docs.julialang.org/en/v1/manual/command-line-interface/)
- [https://docs.julialang.org/en/v1/manual/strings/](https://docs.julialang.org/en/v1/manual/strings/)
- [https://julialang-s3.julialang.org/bin/versions.json](https://julialang-s3.julialang.org/bin/versions.json)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.jl` | [hello.jl](hello.jl) verificato |
