# #259 Go Module

Define an original Go module that requires x/text and performs the conversion as a greeting.

## Toolchain

go version go1.27.1 windows/amd64

## Commands and procedure

go mod tidy; go mod verify; go run .

## Expected result

Graph module solved without errors; authenticated dependence; Hello, World! result.

## Status

syntax and behavior verified.

La direttiva module usa example.invalid, un namespace illustrativo. La versione di x/text è fissata; go.mod e go.sum finali sono quelli dei comandi reali. Nessun modulo viene pubblicato.

Actual verification of 2026-10-08T12:16:15.324157+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://go.dev/ref/mod#go-mod-file](https://go.dev/ref/mod#go-mod-file)
- [https://go.dev/ref/mod#go-mod-tidy](https://go.dev/ref/mod#go-mod-tidy)
- [https://pkg.go.dev/golang.org/x/text/cases](https://pkg.go.dev/golang.org/x/text/cases)
