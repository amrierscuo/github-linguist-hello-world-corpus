# #349 Just

Voce canonica `Just`, tipo `programming`, language_id `128447695`.

Analizzare un justfile ed eseguire la ricetta hello con una shell Windows esplicitamente dichiarata.

## Toolchain e riproduzione

Official Just recipe parser and runner — just 1.58.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Just ufficiale 1.58.0 portable Windows x64. justfile configura windows-shell con powershell.exe -NoLogo -NoProfile -Command. La ricetta non modifica file o sistema.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
just --list; just hello
```

Risultato atteso: Ricetta elencata; exit 0; saluto esatto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il vero parser elenca hello e il runner esegue la ricetta originale. echo nella shell indicata produce stdout confrontato esattamente.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://just.systems/man/en/](https://just.systems/man/en/)
- [https://github.com/casey/just](https://github.com/casey/just)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.just` | [hello.just](variants/just-45047af7/hello.just) creato, verifiche pendenti |
