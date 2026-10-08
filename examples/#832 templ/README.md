# #832 templ

Generare Go da templ e renderizzare il componente originale.

## Toolchain

v0.3.1070; go version go1.27.1 windows/amd64

## Procedura

templ generate; go mod tidy; go mod verify; go run .

## Risultato atteso

HTML renderizzato contiene <h1>Hello, World!</h1>.

## Stato

Sintassi e semantica verificate.

CLI/generator e runtime templ originali; nome è passato come parametro. Go generato e binari restano in work, go.sum deriva dalla risoluzione vera.

Verifica reale 2026-10-08T13:49:00.064965+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://templ.guide/quick-start/creating-a-simple-templ-component/](https://templ.guide/quick-start/creating-a-simple-templ-component/)
- [https://github.com/a-h/templ/releases/tag/v0.3.1070](https://github.com/a-h/templ/releases/tag/v0.3.1070)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.templ` | [hello.templ](hello.templ) verificato |
