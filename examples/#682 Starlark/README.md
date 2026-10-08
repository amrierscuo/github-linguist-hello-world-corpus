# #682 Starlark

Voce canonica `Starlark`, tipo `programming`, language_id `960266174`.

Valutare una funzione Starlark parametrica e controllare print e Reader.

## Toolchain e riproduzione

Authentic Google Starlark Go evaluator — go.starlark.net v0.0.0-20261005163335-bcb1a1a55bf9; go version go1.27.1 windows/amd64. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Google Starlark Go implementation originale, versione esatta nel go.mod/go.sum; Go 1.27.1 ufficiale.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
go run verify.go hello.star
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

ExecFile compila/esegue il file reale; starlark.Call invoca greet con Reader e verifica il valore. Cache/build sono in work.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/google/starlark-go](https://github.com/google/starlark-go)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bzl` | [hello.bzl](variants/bzl-54e0179a/hello.bzl) creato, verifiche pendenti |
| `.star` | [hello.star](hello.star) verificato |
