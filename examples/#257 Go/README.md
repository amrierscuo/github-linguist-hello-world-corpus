# #257 Go

Fill out a Go program that prints Hello, World!.

## Toolchain

go version go1.27.1 windows/amd64

## Commands and procedure

go version; go build -o build/hello.exe hello.go; build/hello.exe

## Expected result

Build and runtime exit 0; stdout greeting more newline.

## Status

syntax and behavior verified.

Official go is downloaded as portable archive and SHA-256 is verified vs go.dev.

Actual verification of 2026-10-08T12:16:15.084445+00:00 on Windows x64: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://go.dev/doc/tutorial/getting-started](https://go.dev/doc/tutorial/getting-started)
- [https://pkg.go.dev/fmt#Println](https://pkg.go.dev/fmt#Println)
- [https://go.dev/dl/](https://go.dev/dl/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.go` | [hello.go](hello.go) verified |
