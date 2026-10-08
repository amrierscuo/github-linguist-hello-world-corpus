# #257 Go

Compilare un programma Go che stampa Hello, World!.

## Toolchain

go version go1.27.1 windows/amd64

## Comandi e procedura

go version; go build -o build/hello.exe hello.go; build/hello.exe

## Risultato atteso

Build e runtime exit 0; stdout saluto più newline.

## Stato

Sintassi e semantica verificate.

Go ufficiale è scaricato come archivio portable e il SHA-256 è verificato contro go.dev. Compilazione ed esecuzione native effettive; eseguibile e cache confinati in work.

Verifica effettiva del 2026-10-08T12:16:15.084445+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://go.dev/doc/tutorial/getting-started](https://go.dev/doc/tutorial/getting-started)
- [https://pkg.go.dev/fmt#Println](https://pkg.go.dev/fmt#Println)
- [https://go.dev/dl/](https://go.dev/dl/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.go` | [hello.go](hello.go) verificato |
