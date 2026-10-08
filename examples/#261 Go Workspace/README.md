# #261 Go Workspace

Voce canonica `Go Workspace`, tipo `data`, language_id `934546256`.

Definire un workspace Go con due moduli locali: app importa greeting e ne stampa il risultato.

## Toolchain e riproduzione

Official Go toolchain workspace loader and compiler — go version go1.27.1 windows/amd64. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Go 1.27.1 portable Windows x64. go.work elenca app e greeting; app richiede example.org/corpus/greeting v0.0.0. Il workspace risolve quella dipendenza alla directory locale. La prova usa GOPROXY=off, GOSUMDB=off, GOTOOLCHAIN=local e cache sotto work.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
go work edit -json; go run ./app
```

Risultato atteso: Workspace con due Use; programma exit 0 e stdout esatto Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il vero loader Go analizza go.work e il compilatore costruisce entrambi i moduli prima dell’esecuzione. Nessun replace o modulo scaricato è necessario. Cache e binari non entrano nel corpus.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://go.dev/doc/tutorial/workspaces](https://go.dev/doc/tutorial/workspaces)
- [https://go.dev/ref/mod#workspaces](https://go.dev/ref/mod#workspaces)
