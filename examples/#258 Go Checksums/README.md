# #258 Go Checksums

Usare un go.sum autentico per risolvere la dipendenza x/text e generare Hello, World! con case conversion.

## Toolchain

go version go1.27.1 windows/amd64

## Comandi e procedura

go mod tidy; go mod verify; go mod download -json golang.org/x/text@v0.31.0; go run .

## Risultato atteso

go.sum generato dai tool; checksum verificati; programma stampa Hello, World! più newline.

## Stato

Sintassi e semantica verificate.

I valori h1 sono prodotti da Go per il modulo originale e il suo go.mod; non sono hash scritti manualmente. go mod verify controlla il contenuto del module cache. main.go usa davvero cases.Title, e go.mod fornisce il contesto del formato checksum.

Verifica effettiva del 2026-10-08T12:16:15.315614+00:00 su Windows x64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://go.dev/ref/mod#go-sum-files](https://go.dev/ref/mod#go-sum-files)
- [https://go.dev/ref/mod#authenticating](https://go.dev/ref/mod#authenticating)
- [https://pkg.go.dev/golang.org/x/text/cases](https://pkg.go.dev/golang.org/x/text/cases)
